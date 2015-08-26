'''resequencing class'''
from copy import copy
from sbaas.analysis.analysis_base import *
from .stage01_resequencing_query import *
from .stage01_resequencing_io import *

# resources
#from calculate_utilities.r import r_calculate

from sequencing_analysis.genome_diff import genome_diff
from sequencing_analysis.genome_annotations import genome_annotations
from sequencing_analysis.mutations_lineage import mutations_lineage
from sequencing_analysis.mutations_endpoints import mutations_endpoints
from sequencing_analysis.mutations_heatmap import mutations_heatmap
from sequencing_analysis.gff_coverage import gff_coverage

class stage01_resequencing_execute():
    '''class for resequencing analysis'''
    def __init__(self,session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage01_resequencing_query = stage01_resequencing_query(self.session);
        self.stage01_resequencing_io = stage01_resequencing_io(self.session);
        self.calculate = base_calculate();
        #self.r_calc = r_calculate();
    #analysis
    def execute_filterMutations_population(self,experiment_id,p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1,sample_names_I=None):
        '''Filter mutations that do not meet the desired criteria'''

        print('Executing filterMutations_population...')
        data_O = [];
        genomediff = genome_diff();
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingMetadata(experiment_id,8);
        for sn in sample_names:
            print('Filtering mutations for sample_name ' + sn);
            #query mutation data filtered by frequency
            data_mutations_list = [];
            data_mutations_list = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutations(experiment_id,sn,frequency_criteria=frequency_criteria);
            #TODO: test passed (but some what trivial since we already filtered the data...);
            data_evidence_list = [];
            data_evidence_list = self.stage01_resequencing_query.get_evidence_experimentIDAndSampleName_dataStage01ResequencingEvidence(experiment_id,sn,
                                                    p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria);
            genomediff.mutations = data_mutations_list;
            genomediff.evidence = data_evidence_list;
            genomediff.filter_mutations_population(p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria)
            data_O.extend(copy(genomediff.mutationsFiltered));
            genomediff.clear_data();
            #for data_mutations in data_mutations_list:
            #    print('Filtering mutations for mutation id ' + str(data_mutations['mutation_id']));
            #    #query data filtered by evidence-specific criteria
            #    data_evidence_list = [];
            #    for pid in data_mutations['parent_ids']:
            #        print('Filtering mutations for parent id ' + str(pid));
            #        data_evidence_dict = {};
            #        data_evidence_dict = self.stage01_resequencing_query.get_evidence_experimentIDAndSampleNameAndParentID_dataStage01ResequencingEvidence(experiment_id,sn,pid,
            #                                        p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria);
            #        data_evidence_list.append(data_evidence_dict);
            #    if data_evidence_list[0]: #check that filtered evidence was found
            #        data_O.append(data_mutations);
            ##        #add data to the database table
            ##        row = None;
            ##        row = data_stage01_resequencing_mutationsFiltered(data_mutations['experiment_id'],
            ##            data_mutations['sample_name'],
            ##            data_mutations['mutation_id'],
            ##            data_mutations['parent_ids'],
            ##            data_mutations['mutation_data']);
            ##            #json.dumps(data_mutations['mutation_data']));
            ##        self.session.add(row);
        #add data to the database table
        self.stage01_resequencing_io.add_dataStage01ResequencingMutationsFiltered(data_O);
        #self.session.commit();
    def execute_annotateFilteredMutations(self,experiment_id,sample_names_I=[],
                                                 ref_genome_I='data/U00096.2.gb',
                                                 ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):

        ref_genome = settings.sbaas + '/sbaas/' + ref_genome_I;
        genomeannotation = genome_annotations(record_I=ref_genome,ref_I=ref_I);

        print('Executing annotation of filtered mutations...')
        genotype_phenotype_O = [];
        # query sample names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingMutationsFiltered(experiment_id);
        for sn in sample_names:
            print('analyzing sample_name ' + sn);
            # query mutation data:
            mutations = [];
            mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,sn);
            mutation_data_O = [];
            for end_cnt,mutation in enumerate(mutations):
                print('analyzing mutations')
                data_tmp = {};
                # annotate each mutation based on the position
                annotation = {};
                annotation = genomeannotation._find_genesFromMutationPosition(mutation['mutation_data']['position']);
                data_tmp['mutation_genes'] = annotation['gene']
                data_tmp['mutation_locations'] = annotation['location']
                data_tmp['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                data_tmp['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                            data_tmp['mutation_links'].append(ecogene_link)
                        else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                data_tmp['experiment_id'] = mutation['experiment_id'];
                data_tmp['sample_name'] = mutation['sample_name'];
                frequency = 1.0;
                if 'frequency' in mutation['mutation_data']:
                    frequency = mutation['mutation_data']['frequency'];
                data_tmp['mutation_frequency'] = frequency
                data_tmp['mutation_position'] = mutation['mutation_data']['position']
                data_tmp['mutation_type'] = mutation['mutation_data']['type']
                data_tmp['mutation_data'] = mutation['mutation_data'];
                mutation_data_O.append(data_tmp);
                # add data to the database
                row = [];
                row = data_stage01_resequencing_mutationsAnnotated(data_tmp['experiment_id'],
                        data_tmp['sample_name'],
                        data_tmp['mutation_frequency'],
                        data_tmp['mutation_type'],
                        data_tmp['mutation_position'],
                        data_tmp['mutation_data'],
                        data_tmp['mutation_annotations'],
                        data_tmp['mutation_genes'],
                        data_tmp['mutation_locations'],
                        data_tmp['mutation_links'],
                        True,
                        None);
                self.session.add(row);
        self.session.commit();
    def execute_analyzeLineage_population(self,experiment_id,strain_lineage):
        '''Analyze a strain lineage to identify the following:
        1. conserved mutations
        2. changes in frequency of mutations
        3. hitch-hiker mutations

        Input:
           experiment_id = experiment id
           strain_lineage = {"lineage_name":{0:sample_name,1:sample_name,2:sample_name,...,n:sample_name}}
                               where n is the end-point strain
        Output:

        TODO: drive from analysis table
        TODO: convert time-point to lineage
               lineage = [i for i,tp in enumerate(time_points)];
        '''

        print('Executing analyzeLineage_population...')
        mutationslineage = mutations_lineage();
        data_O = [];
        for lineage_name,strain in strain_lineage.items():
            print('analyzing lineage ' + lineage_name);
            lineage = list(strain.keys());
            end_point = max(lineage)
            # query end data:
            end_mutations = [];
            end_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain[end_point]);
            intermediates = [i for i in lineage if i!=end_point];
            intermediate_mutations = [];
            for intermediate in intermediates:
                print('analyzing intermediate ' + str(intermediate));
                # query intermediate data:
                intermediate_mutations = [];
                intermediate_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain[intermediate]);
                data_O.extend(mutationslineage._extract_mutationsLineage(lineage_name,end_mutations,intermediate_mutations,intermediate,end_point));
        for d in data_O:
            row = [];
            row = data_stage01_resequencing_lineage(d['experiment_id'],
                d['lineage_name'],
                d['sample_name'],
                d['intermediate'],
                d['mutation_frequency'],
                d['mutation_type'],
                d['mutation_position'],
                d['mutation_data'],
                None,None,None,None,None);
            self.session.add(row);
        self.session.commit();
    def execute_analyzeEndpointReplicates_population(self,analysis_id_I=None,experiment_id=None,end_points=None):
        '''Analyze a endpoint replicates to identify the following:
        1. conserved mutations among replicates
        2. unique mutations among replicates'''
        #Input:
        #   experiment_id = experiment id
        #   end_points = {analysis_id: [sample_name_1,sample_name_2,sample_name_3,...]}
        #Output:

        #TODO: drive from analysis table

        print('Executing analyzeEndpointReplicates_population...')
        mutationsendpoints = mutations_endpoints();

        # get the analysis info
        analysis_info = [];
        analysis_info = self.stage01_resequencing_query.get_rows_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);

        # get the experiments and strains
        analysis_id = analysis_id_I;
        experiment_ids = [];
        strains = [];
        for row in analysis_info:
            experiment_ids.append(row['experiment_id'])
            strains.append(row['sample_name'])

        # get the data
        data_O = [];
        analyzed_strain1 = []; # strain1s that have been analyzed
        analyzed_mutation_pairs = []; # mutation pairs that have been analyzed
        matched_mutations = {};
        for cnt1,strain1 in enumerate(strains):
            # query strain 1 data:
            strain1_mutations = [];
            strain1_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_ids[cnt1],strain1);
            analyzed_strain1.append(strain1);
            analyzed_strain1_mutations = []; # mutations from strain 1 that have been analyzed
            analyzed_strain2_mutations_all = []; # all mutations from strain 2 that have been analyzed
            strain2_cnt = 0;
            for cnt2,strain2 in enumerate(strains):
                if strain2 == strain1: continue; # do not compare the same strain to itself
                print('comparing ' + strain1 + ' to ' + strain2);
                # query strain 1 data:
                strain2_mutations = [];
                strain2_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_ids[cnt2],strain2);
                analyzed_strain2_mutations = []; # mutations from strain 2 that have been analyzed
                # TODO: test passed
                # extract common mutations
                analyzed_strain1_mutations_tmp = [];
                analyzed_strain2_mutations_tmp = [];
                matched_mutations_tmp = {}
                data_tmp = [];
                matched_mutations_tmp,\
                    analyzed_strain1_mutations_tmp,\
                    analyzed_strain2_mutations_tmp,\
                    data_tmp = mutationsendpoints._extract_commonMutations(matched_mutations,\
                        analyzed_strain1_mutations,\
                        analyzed_strain2_mutations,\
                        strain1_mutations,strain2_mutations,
                        strain1,strain2_cnt,analysis_id);
                
                analyzed_strain1_mutations.extend(analyzed_strain1_mutations_tmp)
                analyzed_strain2_mutations.extend(analyzed_strain2_mutations_tmp)
                analyzed_strain2_mutations_all.append(analyzed_strain2_mutations);
                matched_mutations.update(matched_mutations_tmp);
                data_O.extend(data_tmp);
                strain2_cnt += 1;
            # extract unique mutations
            data_tmp = [];
            data_tmp = mutationsendpoints._extract_uniqueMutations(analyzed_strain1_mutations,analyzed_strain2_mutations_all,strain1_mutations,analysis_id);
            data_O.extend(data_tmp);
        #data_O = [];
        #for analysis_id,strains in end_points.items():
        #    print('analyzing endpoint ' + analysis_id);
        #    analyzed_strain1 = []; # strain1s that have been analyzed
        #    analyzed_mutation_pairs = []; # mutation pairs that have been analyzed
        #    matched_mutations = {};
        #    for cnt1,strain1 in enumerate(strains):
        #        # query strain 1 data:
        #        strain1_mutations = [];
        #        strain1_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain1);
        #        analyzed_strain1.append(strain1);
        #        analyzed_strain1_mutations = []; # mutations from strain 1 that have been analyzed
        #        analyzed_strain2_mutations_all = []; # all mutations from strain 2 that have been analyzed
        #        strain2_cnt = 0;
        #        for cnt2,strain2 in enumerate(strains):
        #            if strain2 == strain1: continue; # do not compare the same strain to itself
        #            print('comparing ' + strain1 + ' to ' + strain2);
        #            # query strain 1 data:
        #            strain2_mutations = [];
        #            strain2_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain2);
        #            analyzed_strain2_mutations = []; # mutations from strain 2 that have been analyzed
        #            # TODO: test passed
        #            # extract common mutations
        #            analyzed_strain1_mutations_tmp = [];
        #            analyzed_strain2_mutations_tmp = [];
        #            matched_mutations_tmp = {}
        #            data_tmp = [];
        #            matched_mutations_tmp,\
        #                analyzed_strain1_mutations_tmp,\
        #                analyzed_strain2_mutations_tmp,\
        #                data_tmp = mutationsendpoints._extract_commonMutations(matched_mutations,\
        #                    analyzed_strain1_mutations,\
        #                    analyzed_strain2_mutations,\
        #                    strain1_mutations,strain2_mutations,
        #                    strain1,strain2_cnt,analysis_id);
                
        #            analyzed_strain1_mutations.extend(analyzed_strain1_mutations_tmp)
        #            analyzed_strain2_mutations.extend(analyzed_strain2_mutations_tmp)
        #            analyzed_strain2_mutations_all.append(analyzed_strain2_mutations);
        #            matched_mutations.update(matched_mutations_tmp);
        #            data_O.extend(data_tmp);
        #            strain2_cnt += 1;
        #        # extract unique mutations
        #        data_tmp = [];
        #        data_tmp = mutationsendpoints._extract_uniqueMutations(analyzed_strain1_mutations,analyzed_strain2_mutations_all,strain1_mutations,analysis_id);
        #        data_O.extend(data_tmp);
        for d in data_O:
            row = [];
            row = data_stage01_resequencing_endpoints(d['experiment_id'],
                #TODO: test
                d['endpoint_name'], #=analysis_id
                #d['analysis_id'],
                d['sample_name'],
                d['mutation_frequency'],
                d['mutation_type'],
                d['mutation_position'],
                d['mutation_data'],
                #json.dumps(d['mutation_data'],
                d['isUnique'],
                None,None,None,None,None);
            self.session.add(row);
        self.session.commit();
    def execute_annotateMutations_lineage(self,experiment_id,sample_names_I=[],
                                                 ref_genome_I='data/U00096.2.gb',
                                                 ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):
        '''Annotate mutations for date_stage01_resequencing_lineage
        based on position, reference genome, and reference genome biologicalmaterial_id'''

        genomeannotation = genome_annotations(record_I=ref_genome_I,ref_I=ref_I);

        print('Executing annotateMutations_lineage...')
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingLineage(experiment_id);
        for sn in sample_names:
            print('annotating mutation for sample_name ' + sn);
            # query rows that match the sample name
            rows = [];
            rows = self.stage01_resequencing_query.get_row_experimentIDAndSampleName_dataStage01ResequencingLineage(experiment_id,sn);
            for row in rows:
                # annotate each mutation based on the position
                annotation = {};
                annotation = genomeannotation._find_genesFromMutationPosition(mutation['mutation_data']['position']);
                row['mutation_genes'] = annotation['gene']
                row['mutation_locations'] = annotation['location']
                row['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                row['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                            row['mutation_links'].append(ecogene_link)
                        else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                data_O.append(row);
        # update rows in the database
        io = stage01_resequencing_io();
        io.update_dataStage01ResequencingLineage(data_O);
    def execute_annotateMutations_endpoints(self,experiment_id,sample_names_I=[],
                                                 ref_genome_I='data/U00096.2.gb',
                                                 ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        genomeannotation = genome_annotations(record_I=ref_genome_I,ref_I=ref_I);

        print('Executing annotateMutations_endpoints...')
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingEndpoints(experiment_id);
        for sn in sample_names:
            print('annotating mutation for sample_name ' + sn);
            # query rows that match the sample name
            rows = [];
            rows = self.stage01_resequencing_query.get_row_experimentIDAndSampleName_dataStage01ResequencingEndpoints(experiment_id,sn);
            for row in rows:
                # annotate each mutation based on the position
                annotation = {};
                annotation = genomeannotation._find_genesFromMutationPosition(mutation['mutation_data']['position']);
                row['mutation_genes'] = annotation['gene']
                row['mutation_locations'] = annotation['location']
                row['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                row['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                            row['mutation_links'].append(ecogene_link)
                        else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                data_O.append(row);
        # update rows in the database
        io = stage01_resequencing_io();
        io.update_dataStage01ResequencingEndpoints(data_O);
    def execute_heatmap_lineage(self, analysis_id_I,
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete',
                                                 mutation_id_exclusion_list = []):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');
        # get the analysis information
        experiment_ids,lineage_names = [],[];
        experiment_ids,lineage_names = self.stage01_resequencing_query.get_experimentIDAndLineageName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # partition into variables:
        intermediates_lineage = [];
        mutation_data_lineage_all = [];
        rows_lineage = [];
        n_lineages = len(lineage_names)
        cnt_sample_names = 0;
        for lineage_name_cnt,lineage_name in enumerate(lineage_names):
            # get ALL intermediates by experiment_id and lineage name
            intermediates = [];
            intermediates = self.stage01_resequencing_query.get_intermediates_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_ids[lineage_name_cnt],lineage_name);
            intermediates_lineage.append(intermediates);
            cnt_sample_names += len(intermediates)
            # get ALL mutation data by experiment_id and lineage name
            mutation_data = [];
            mutation_data = self.stage01_resequencing_query.get_mutationData_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_ids[lineage_name_cnt],lineage_name);
            mutation_data_lineage_all.extend(mutation_data);
            # get ALL mutation frequencies by experiment_id and lineage name
            rows = [];
            rows = self.stage01_resequencing_query.get_row_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_ids[lineage_name_cnt],lineage_name)
            rows_lineage.extend(rows);
        mutation_data_lineage_unique = list(set(mutation_data_lineage_all));
        mutation_data_lineage = [x for x in mutation_data_lineage_unique if not x in mutation_id_exclusion_list];
        min_inter = min(intermediates_lineage)
        max_inter = max(intermediates_lineage);
        # generate the frequency matrix data structure (mutation x intermediate)
        data_O = numpy.zeros((cnt_sample_names,len(mutation_data_lineage)));
        labels_O = {};
        lineages=[];
        col_cnt = 0;
        # order 2: groups each lineage by mutation (intermediate x mutation)
        for lineage_name_cnt,lineage_name in enumerate(lineage_names): #all lineages for intermediate j / mutation i
            for intermediate_cnt,intermediate in enumerate(intermediates_lineage[lineage_name_cnt]):
                if intermediate_cnt == min(intermediates_lineage[lineage_name_cnt]):
                    lineages.append(lineage_name+": "+"start"); # corresponding label from hierarchical clustering (in this case, arbitrary)
                elif intermediate_cnt == max(intermediates_lineage[lineage_name_cnt]):
                    lineages.append(lineage_name+": "+"end"); # corresponding label from hierarchical clustering (in this case, arbitrary)
                else:
                    lineages.append(lineage_name+": "+str(intermediate)); # corresponding label from hierarchical clustering (in this case, arbitrary)
                for mutation_cnt,mutation in enumerate(mutation_data_lineage): #all mutations i for intermediate j
                    for row in rows_lineage:
                        if row['mutation_id'] == mutation and row['intermediate'] == intermediate and row['lineage_name'] == lineage_name:
                            data_O[col_cnt,mutation_cnt] = row['mutation_frequency'];
                            #print col_cnt,mutation_cnt
                col_cnt+=1;
        # generate the clustering for the heatmap
        heatmap_O = [];
        dendrogram_col_O = {};
        dendrogram_row_O = {};
        heatmap_O,dendrogram_col_O,dendrogram_row_O = self.calculate.heatmap(data_O,lineages,mutation_data_lineage,
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I);
        # add data to to the database for the heatmap
        for d in heatmap_O:
            row = None;
            row = data_stage01_resequencing_heatmap(
                analysis_id_I,
                d['col_index'],
                d['row_index'],
                d['value'],
                d['col_leaves'],
                d['row_leaves'],
                d['col_label'],
                d['row_label'],
                d['col_pdist_metric'],
                d['row_pdist_metric'],
                d['col_linkage_method'],
                d['row_linkage_method'],
                'frequency',True, None);
            self.session.add(row);
        # add data to the database for the dendrograms
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_col_O['leaves'],
            dendrogram_col_O['icoord'],
            dendrogram_col_O['dcoord'],
            dendrogram_col_O['ivl'],
            dendrogram_col_O['colors'],
            dendrogram_col_O['pdist_metric'],
            dendrogram_col_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_row_O['leaves'],
            dendrogram_row_O['icoord'],
            dendrogram_row_O['dcoord'],
            dendrogram_row_O['ivl'],
            dendrogram_row_O['colors'],
            dendrogram_row_O['pdist_metric'],
            dendrogram_row_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        self.session.commit();
    def execute_heatmap(self, analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,max_position=4000000,
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete'):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');
        mutationsheatmap =  mutations_heatmap();
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.stage01_resequencing_query.get_experimentIDAndSampleName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        mutations_all = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sample_name_cnt],sample_name);
            mutations_all.extend(mutations);
        mutationsheatmap.mutations = mutations_all;
        mutationsheatmap.sample_names = sample_names;
        mutationsheatmap.make_heatmap(mutation_id_exclusion_list=mutation_id_exclusion_list,max_position=max_position,
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I)
        heatmap_O = mutationsheatmap.heatmap;
        dendrogram_col_O = mutationsheatmap.dendrogram_col;
        dendrogram_row_O = mutationsheatmap.dendrogram_row;
        # add data to to the database for the heatmap
        for d in heatmap_O:
            row = None;
            row = data_stage01_resequencing_heatmap(
                analysis_id_I,
                d['col_index'],
                d['row_index'],
                d['value'],
                d['col_leaves'],
                d['row_leaves'],
                d['col_label'],
                d['row_label'],
                d['col_pdist_metric'],
                d['row_pdist_metric'],
                d['col_linkage_method'],
                d['row_linkage_method'],
                'frequency',True, None);
            self.session.add(row);
        # add data to the database for the dendrograms
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_col_O['leaves'],
            dendrogram_col_O['icoord'],
            dendrogram_col_O['dcoord'],
            dendrogram_col_O['ivl'],
            dendrogram_col_O['colors'],
            dendrogram_col_O['pdist_metric'],
            dendrogram_col_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_row_O['leaves'],
            dendrogram_row_O['icoord'],
            dendrogram_row_O['dcoord'],
            dendrogram_row_O['ivl'],
            dendrogram_row_O['colors'],
            dendrogram_row_O['pdist_metric'],
            dendrogram_row_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        self.session.commit();
    def execute_findAmplifications_fromGff(self,
                #analysis_id_I,
                experiment_id_I,
                strand_start, strand_stop,
                sample_names_I = [],
                scale_factor=True, downsample_factor=0,reads_min=1.5,reads_max=5.0, indices_min=200,consecutive_tol=10):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''

        #from sequencing_utilities.coverage import extract_strandsFromGff,find_highCoverageRegions

        # get the data
        data_O = [];
        # TODO: test
        gffcoverage = gff_coverage();

        # get the sample_names
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingCoverage(experiment_id_I);
        #for cnt,analysis in analysis_rows:
        #    # get the sample_names and experiment_ids
        #    experiment_id = analysis['experiment_id'];
        #    sn = analysis['sample_name'];
        #    filename = analysis['data_dir']
        for cnt,sn in enumerate(sample_names):
            # get the data_dir
            filename = [];
            filename = self.stage01_resequencing_query.get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(experiment_id_I,sn);
            #TODO: test
            gffcoverage.find_amplifications_fromGff(filename[0],strand_start, strand_stop, experiment_id, sn, scale=scale_factor, downsample=downsample_factor)
            data_O.extend(copy(gffcoverage.amplifications))
            gffcoverage.clear_data();
            ## extract the strands
            #plus,minus=extract_strandsFromGff(filename[0], strand_start, strand_stop, scale=scale_factor, downsample=downsample_factor)
            ## find high coverage regions
            #plus_high_region_indices,minus_high_region_indices,plus_high_regions, minus_high_regions = find_highCoverageRegions(plus,minus,coverage_min=reads_min,coverage_max=reads_max,points_min=indices_min,consecutive_tol=consecutive_tol)
            ## record high coverage regions
            ## + strand
            #iter = 0;
            #for index,reads in plus_high_regions.iteritems():
            #    if index > plus_high_region_indices[iter]['stop']:
            #        iter+=1;
            #    data_O.append({
            #    #'analysis_id':analysis_id,
            #    'experiment_id':experiment_id,
            #    'sample_name':sn,
            #    'genome_chromosome':1, #default
            #    'genome_strand':'+',
            #    'genome_index':int(index),
            #    'strand_start':strand_start,
            #    'strand_stop':strand_stop,
            #    'reads':float(reads),
            #    'reads_min':reads_min,
            #    'reads_max':reads_max,
            #    'indices_min':indices_min,
            #    'consecutive_tol':consecutive_tol,
            #    'scale_factor':scale_factor,
            #    'downsample_factor':downsample_factor,
            #    'amplification_start':int(plus_high_region_indices[iter]['start']),
            #    'amplification_stop':int(plus_high_region_indices[iter]['stop']),
            #    'used_':True,
            #    'comment_':None
            #        });
            ## - strand
            #iter = 0;
            #for index,reads in minus_high_regions.iteritems():
            #    if index > minus_high_region_indices[iter]['stop']:
            #        iter+=1;
            #    data_O.append({
            #    #'analysis_id':analysis_id,
            #    'experiment_id':experiment_id,
            #    'sample_name':sn,
            #    'genome_chromosome':1, #default
            #    'genome_strand':'-',
            #    'genome_index':int(index),
            #    'strand_start':strand_start,
            #    'strand_stop':strand_stop,
            #    'reads':float(reads),
            #    'reads_min':reads_min,
            #    'reads_max':reads_max,
            #    'indices_min':indices_min,
            #    'consecutive_tol':consecutive_tol,
            #    'scale_factor':scale_factor,
            #    'downsample_factor':downsample_factor,
            #    'amplification_start':int(minus_high_region_indices[iter]['start']),
            #    'amplification_stop':int(minus_high_region_indices[iter]['stop']),
            #    'used_':True,
            #    'comment_':None
            #        });
        # add data to the DB
        self.stage01_resequencing_io.add_dataStage01ResequencingAmplifications(data_O);
    def execute_amplificationStats_fromTable(self,
                #analysis_id_I,
                experiment_id_I,
                sample_names_I=[]):
        '''Calculate coverage statistics'''

        # get the data
        data_O = [];

        ## get the analysis_info
        #analysis_rows = [];
        ## query information from amplification table

        #for cnt,analysis in analysis_rows:
        #    # get the sample_names
        #    experiment_id = analysis['experiment_id'];
        #    sn = analysis['sample_name'];

        # get the sample_names
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingAmplifications(experiment_id_I);
        for cnt,sn in enumerate(sample_names):
            # get chromosomes
            chromosomes = [];
            chromosomes = self.stage01_resequencing_query.get_chromosomes_experimentIDAndSampleName_dataStage01ResequencingAmplifications(experiment_id_I,sn);
            for chromosome in chromosomes:
                # get strands
                strands = []
                strands = self.stage01_resequencing_query.get_strands_experimentIDAndSampleNameAndChromosome_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome);
                # remove visualization regions
                strands = [s for s in strands if not 'mean' in s];
                for strand in strands:
                    # get the start and stop of the indices
                    genomic_starts,genomic_stops = [],[]
                    genomic_starts,genomic_stops = self.stage01_resequencing_query.get_startAndStops_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    # get the start and stop regions
                    starts,stops = [],[]
                    starts,stops = self.stage01_resequencing_query.get_amplificationRegions_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    # get the indices/reads and other information
                    for start_cnt,start in enumerate(starts):
                        data_indices,data_reads = [],[];
                        data_indices,data_reads = self.stage01_resequencing_query.get_genomeIndexAndReads_experimentIDAndSampleNameAndChromosomeAndStrandAndAmplificationRegions_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand,start,stops[start_cnt]);
                        # calculate using scipy
                        data_ave_O, data_var_O, data_lb_O, data_ub_O = self.calculate.calculate_ave_var(data_reads,confidence_I = 0.95);
                        # calculate the interquartile range
                        min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
                        min_O, max_O, median_O, iq_1_O, iq_3_O=self.calculate.calculate_interquartiles(data_reads);
                        # record data for
                        data_O.append({
                            #'analysis_id':analysis_id,
                            'experiment_id':experiment_id_I,
                            'sample_name':sn,
                            'genome_chromosome':chromosome,
                            'genome_strand':strand,
                            'strand_start':genomic_starts[0],
                            'strand_stop':genomic_stops[0],
                            'reads_min':min_O,
                            'reads_max':max_O,
                            #'reads_lb':data_TTest['ci_lb'],
                            #'reads_ub':data_TTest['ci_ub'],
                            'reads_lb':data_lb_O,
                            'reads_ub':data_ub_O,
                            'reads_iq1':iq_1_O,
                            'reads_iq3':iq_3_O,
                            'reads_median':median_O,
                            #'reads_mean':data_TTest['mean'],
                            #'reads_var':data_TTest['var'],
                            'reads_mean':data_ave_O,
                            'reads_var':data_var_O,
                            'reads_n':len(data_reads),
                            'amplification_start':start,
                            'amplification_stop':stops[start_cnt],
                            'used_':True,
                            'comment_':None
                            })
        # add data to the DB
        self.stage01_resequencing_io.add_dataStage01ResequencingAmplificationStats(data_O);
    def execute_findAmplificationsAndCalculateStats_fromGff(self,
                #analysis_id_I,
                experiment_id_I,
                strand_start, strand_stop,
                sample_names_I = [],
                scale_factor=True, downsample_factor=2000,reads_min=1.5,reads_max=5.0, indices_min=200,consecutive_tol=10):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''

        # get the data
        data_O = [];
        stats_O = [];
        gffcoverage = gff_coverage();

        ## get the analysis_info
        #analysis_rows = [];
        # query information from coverage table

        # get the sample_names
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingCoverage(experiment_id_I);
        #for cnt,analysis in analysis_rows:
        #    # get the sample_names and experiment_ids
        #    experiment_id = analysis['experiment_id'];
        #    sn = analysis['sample_name'];
        #    filename = analysis['data_dir']
        for cnt,sn in enumerate(sample_names):
            # get the data_dir
            filename = [];
            filename = self.stage01_resequencing_query.get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(experiment_id_I,sn);
            # find amplifications and calculate stats
            gffcoverage.findAndCalculate_amplificationStats_fromGff(filename[0],strand_start, strand_stop, experiment_id_I=experiment_id, sample_name_I=sn, indices_min = indices_min, consecutive_tol = consecutive_tol, scale_factor=scale_factor, downsample_factor=downsample_factor)
            data_O.extend(copy(gffcoverage.amplifications));
            stats_O.extend(copy(gffcoverage.amplificationStats));
            gffcoverage.clear_data();
        # add data to the DB
        self.stage01_resequencing_io.add_dataStage01ResequencingAmplifications(data_O);
        self.stage01_resequencing_io.add_dataStage01ResequencingAmplificationStats(stats_O);
    def execute_annotateAmplifications(self,experiment_id_I,sample_names_I=[],ref_genome_I='data/U00096.2.gb',ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        genomeannotation = genome_annotations(record_I=ref_genome_I,ref_I=ref_I);

        print('Executing annotateAmplifications...')
        data_O = [];
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingAmplifications(experiment_id);
        for cnt,sn in enumerate(sample_names):
            print('annotating amplifications for sample_name ' + sn);
            # get chromosomes
            chromosomes = [];
            chromosomes = self.stage01_resequencing_query.get_chromosomes_experimentIDAndSampleName_dataStage01ResequencingAmplifications(experiment_id_I,sn);
            for chromosome in chromosomes:
                # get strands
                strands = []
                strands = self.stage01_resequencing_query.get_strands_experimentIDAndSampleNameAndChromosome_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome);
                # remove visualization regions
                strands = [s for s in strands if not 'mean' in s];
                for strand in strands:
                    # get the start and stop of the indices
                    genomic_starts,genomic_stops = [],[]
                    genomic_starts,genomic_stops = self.stage01_resequencing_query.get_startAndStops_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    # get the start and stop regions
                    starts,stops = [],[]
                    starts,stops = self.stage01_resequencing_query.get_amplificationRegions_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    for start_cnt,start in enumerate(starts):
                        # annotate each mutation based on the position
                        annotations = [];
                        annotations = genomeannotation._find_genesInRegion(start,stops[start_cnt])
                        for annotation in annotations:
                            # record the data
                            tmp = {
                                'experiment_id':experiment_id,
                                'sample_name':sn,
                                'genome_chromosome':chromosome,
                                'genome_strand':strand,
                                'strand_start':genomic_starts[0],
                                'strand_stop':genomic_stops[0],
                                'amplification_start':start,
                                'amplification_stop':stops[start_cnt],
                                'used_':True,
                                'comment_':None};
                            tmp['feature_genes'] = annotation['gene']
                            tmp['feature_locations'] = annotation['location']
                            tmp['feature_annotations'] = annotation['product']
                            tmp['feature_start'] = annotation['start'];
                            tmp['feature_stop'] = annotation['stop'];
                            tmp['feature_types'] = annotation['type']
                            # generate a link to ecogene for the genes
                            tmp['feature_links'] = [];
                            for bnumber in annotation['locus_tag']:
                                if bnumber:
                                    ecogenes = [];
                                    ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                                    if ecogenes:
                                        ecogene = ecogenes[0];
                                        ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                                        tmp['feature_links'].append(ecogene_link)
                                    else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                            data_O.append(tmp);
        # update rows in the database
        io = stage01_resequencing_io();
        io.add_dataStage01ResequencingAmplificationAnnotations(data_O);
    #table initializations:
    def drop_dataStage01(self):
        try:
            data_stage01_resequencing_evidence.__table__.drop(engine,True);
            data_stage01_resequencing_mutations.__table__.drop(engine,True);
            data_stage01_resequencing_metadata.__table__.drop(engine,True);
            data_stage01_resequencing_validation.__table__.drop(engine,True);
            data_stage01_resequencing_mutationsFiltered.__table__.drop(engine,True);
            data_stage01_resequencing_lineage.__table__.drop(engine,True);
            data_stage01_resequencing_endpoints.__table__.drop(engine,True);
            data_stage01_resequencing_mutationsAnnotated.__table__.drop(engine,True);
            data_stage01_resequencing_analysis.__table__.drop(engine,True);
            data_stage01_resequencing_heatmap.__table__.drop(engine,True);
            data_stage01_resequencing_dendrogram.__table__.drop(engine,True);
            data_stage01_resequencing_coverage.__table__.drop(engine,True);
            data_stage01_resequencing_coverageStats.__table__.drop(engine,True);
            data_stage01_resequencing_amplifications.__table__.drop(engine,True);
            data_stage01_resequencing_amplificationStats.__table__.drop(engine,True);
            data_stage01_resequencing_amplificationAnnotations.__table__.drop(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01(self,experiment_id_I = None,analysis_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_metadata).filter(data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).filter(data_stage01_resequencing_mutations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).filter(data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).filter(data_stage01_resequencing_validation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_lineage).filter(data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            elif analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_analysis).filter(data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_metadata).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_lineage).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_endpoints).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_analysis).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01(self):
        try:
            data_stage01_resequencing_metadata.__table__.create(engine,True);
            data_stage01_resequencing_mutations.__table__.create(engine,True);
            data_stage01_resequencing_evidence.__table__.create(engine,True);
            data_stage01_resequencing_validation.__table__.create(engine,True);
            data_stage01_resequencing_mutationsFiltered.__table__.create(engine,True);
            data_stage01_resequencing_lineage.__table__.create(engine,True);
            data_stage01_resequencing_endpoints.__table__.create(engine,True);
            data_stage01_resequencing_mutationsAnnotated.__table__.create(engine,True);
            data_stage01_resequencing_analysis.__table__.create(engine,True);
            data_stage01_resequencing_heatmap.__table__.create(engine,True);
            data_stage01_resequencing_dendrogram.__table__.create(engine,True);
            data_stage01_resequencing_coverage.__table__.create(engine,True);
            data_stage01_resequencing_coverageStats.__table__.create(engine,True);
            data_stage01_resequencing_amplifications.__table__.create(engine,True);
            data_stage01_resequencing_amplificationStats.__table__.create(engine,True);
            data_stage01_resequencing_amplificationAnnotations.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_mutationsAnnotated(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_heatmap(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_heatmap).filter(data_stage01_resequencing_heatmap.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_heatmap).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_dendrogram(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_dendrogram).filter(data_stage01_resequencing_dendrogram.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_dendrogram).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_metadataAndmutationsAndEvidenceAndValidation(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_metadata).filter(data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).filter(data_stage01_resequencing_mutations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).filter(data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).filter(data_stage01_resequencing_validation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_metadata).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_filtered(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_lineage(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_lineage).filter(data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_lineage).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_endpoints(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_endpoints).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_coverage(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_resequencing_coverage).filter(
                        data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_coverage.sample_name.like(sn)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_resequencing_coverageStats).filter(
                        data_stage01_resequencing_coverageStats.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_coverageStats.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_coverage).filter(data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_coverageStats).filter(data_stage01_resequencing_coverageStats.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_coverage).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_coverageStats).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_amplifications(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_resequencing_amplifications).filter(
                        data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplifications.sample_name.like(sn)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_resequencing_amplificationStats).filter(
                        data_stage01_resequencing_amplificationStats.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplificationStats.sample_name.like(sn)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(
                        data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplificationAnnotations.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_amplifications).filter(data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationStats).filter(data_stage01_resequencing_amplificationStats.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_amplifications).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationStats).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_amplificationAnnotations(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(
                        data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplificationAnnotations.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    #TODO:
    def execute_coverageStats_fromGff(self,
                    #analysis_id_I,
                    experiment_id_I,
                    strand_start,strand_stop,scale_factor=True,downsample_factor=0,
                    sample_names_I=[]):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''
        
        #TODO: test
        gffcoverage=gff_coverage();

        ## get the analysis_info
        #analysis_rows = [];
        #analysis_rows = self.stage01_resequencing_query.get_rows_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);

        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingCoverage(experiment_id_I);
        # get the data
        data_O = [];
        for sn in sample_names:
            # get the filename
            filename = None;
            filename = self.stage01_resequencing_query.get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(experiment_id_I,sn);
            # calculate the coverage statistics
            gffcoverage.calculate_coverageStats_fromGff(filename[0], 
                strand_start,strand_stop,scale_factor=scale_factor,downsample_factor=downsample_factor,
                experiment_id_I=experiment_id_I, sample_name_I=sn);
            data_O.extend(copy(gffcoverage.coverageStats));
            gffcoverage.clear_data();
        #add data to the database
        self.stage01_resequencing_io.add_dataStage01ResequencingCoverageStats(data_O); 
        

    #todo: template for amplification stats
    def execute_coverageStats_fromTable(self,analysis_id_I):
        '''Calculate coverage statistics'''
        # get the analysis_info
        analysis_rows = [];

        # get the data
        data_O = [];
        for cnt,analysis in analysis_rows:
            # get the sample_names
            experiment_id = analysis['experiment_id'];
            sn = analysis['sample_name'];
            # get chromosomes
            chromosomes = [];

            for chromosome in chromosomes:
                # get strands
                strands = []

                for strand in strands:
                    # get the indices/reads and other information
                    start,stop = None,None;
                    
                    data_indices,data_reads = [],[];

                    # calculate the descriptive statistics
                    data_TTest = {};
                    data_TTest = self.r_calc.calculate_oneSampleTTest(data_reads, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                    # calculate the interquartile range
                    min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
                    min_O, max_O, median_O, iq_1_O, iq_3_O=self.calculate.calculate_interquartiles(data_reads);
                    # record data for
                    data_O.append({
                        'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':chromosome,
                        'genome_strand':strand,
                        'strand_start':start,
                        'strand_stop':stop,
                        'reads_min':min_O,
                        'reads_max':max_O,
                        'reads_lb':data_TTest['ci_lb'],
                        'reads_ub':data_TTest['ci_ub'],
                        'reads_iq1':iq_1_O,
                        'reads_iq3':iq_3_O,
                        'reads_median':median_O,
                        'reads_mean':data_TTest['mean'],
                        'reads_var':data_TTest['var'],
                        'reads_n':len(data_reads)
                        })
        self.stage01_resequencing_io.add_dataStage01ResequencingCoverageStats(data_O);
