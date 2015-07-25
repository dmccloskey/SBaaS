'''resequencing class'''

from sbaas.analysis.analysis_base import *
from .stage01_resequencing_query import *
from .stage01_resequencing_io import *
#from sbaas.resources.r import r_calculate

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
            data_mutations_list = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutations(experiment_id,sn);
            for data_mutations in data_mutations_list:
                print('Filtering mutations for mutation id ' + str(data_mutations['mutation_id']));
                #query data filtered by evidence-specific criteria
                data_evidence_list = [];
                for pid in data_mutations['parent_ids']:
                    print('Filtering mutations for parent id ' + str(pid));
                    data_evidence_dict = {};
                    data_evidence_dict = self.stage01_resequencing_query.get_evidence_experimentIDAndSampleNameAndParentID_dataStage01ResequencingEvidence(experiment_id,sn,pid);
                    data_evidence_list.append(data_evidence_dict);
                if data_evidence_list[0]: #check that filtered evidence was found
                    data_O.append(data_mutations);
                    #add data to the database table
                    row = None;
                    row = data_stage01_resequencing_mutationsFiltered(data_mutations['experiment_id'],
                        data_mutations['sample_name'],
                        data_mutations['mutation_id'],
                        data_mutations['parent_ids'],
                        data_mutations['mutation_data']);
                        #json.dumps(data_mutations['mutation_data']));
                    self.session.add(row);
        #add data to the database table
        self.session.commit();
    def execute_annotateFilteredMutations(self,experiment_id,sample_names_I=[],
                                                 ref_genome_I='data/U00096.2.gb'):

        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

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
                annotation = self.find_genesFromMutationPosition(mutation['mutation_data']['position'],record);
                data_tmp['mutation_genes'] = annotation['gene']
                data_tmp['mutation_locations'] = annotation['location']
                data_tmp['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                data_tmp['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences('MG1655',bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = self.generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
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
        3. hitch-hiker mutations'''
        #Input:
        #   experiment_id = experiment id
        #   strain_lineage = {"lineage_name":{0:sample_name,1:sample_name,2:sample_name,...,n:sample_name}}
        #                       where n is the end-point strain
        #Output:

        #TODO: drive from analysis table
        #TODO: convert time-point to lineage
        #       lineage = [i for i,tp in enumerate(time_points)];

        print('Executing analyzeLineage_population...')
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
                for end_cnt,end_mutation in enumerate(end_mutations):
                    print('end mutation type/position ' + end_mutation['mutation_data']['type'] + '/' + str(end_mutation['mutation_data']['position']));
                    for inter_cnt,intermediate_mutation in enumerate(intermediate_mutations):
                        print('intermediate mutation type/position ' + intermediate_mutation['mutation_data']['type'] + '/' + str(intermediate_mutation['mutation_data']['position']));
                        if intermediate == 0 and inter_cnt == 0:
                            #copy end_point data (only once per strain lineage)
                            data_tmp = {};
                            data_tmp['experiment_id'] = end_mutation['experiment_id'];
                            data_tmp['sample_name'] = end_mutation['sample_name'];
                            data_tmp['intermediate'] = end_point;
                            frequency = 1.0;
                            if 'frequency' in end_mutation['mutation_data']: frequency = end_mutation['mutation_data']['frequency'];
                            data_tmp['mutation_frequency'] = frequency
                            data_tmp['mutation_position'] = end_mutation['mutation_data']['position']
                            data_tmp['mutation_type'] = end_mutation['mutation_data']['type']
                            data_tmp['lineage_name'] = lineage_name;
                            data_tmp['mutation_data'] = end_mutation['mutation_data'];
                            data_O.append(data_tmp);
                        # find the mutation in the intermediates
                        # filter by mutation type-specific criteria
                        match = {};
                        if end_mutation['mutation_data']['type'] == 'SNP':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['new_seq']==intermediate_mutation['mutation_data']['new_seq']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'SUB':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size'] and \
                                end_mutation['mutation_data']['new_seq']==intermediate_mutation['mutation_data']['new_seq']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'DEL':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'INS':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['new_seq']==intermediate_mutation['mutation_data']['new_seq']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'MOB':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['repeat_name']==intermediate_mutation['mutation_data']['repeat_name'] and \
                                end_mutation['mutation_data']['strand']==intermediate_mutation['mutation_data']['strand'] and \
                                end_mutation['mutation_data']['duplication_size']==intermediate_mutation['mutation_data']['duplication_size']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'AMP':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size'] and \
                                end_mutation['mutation_data']['new_copy_number']==intermediate_mutation['mutation_data']['new_copy_number']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'CON':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size'] and \
                                end_mutation['mutation_data']['region']==intermediate_mutation['mutation_data']['region']:
                                match = intermediate_mutation;
                        elif end_mutation['mutation_data']['type'] == 'INV':
                            if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                                end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                                end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size']:
                                match = intermediate_mutation;
                        else:
                            print('unknown mutation type');
                        if match:
                            data_tmp = {};
                            data_tmp['experiment_id'] = match['experiment_id'];
                            data_tmp['sample_name'] = match['sample_name'];
                            data_tmp['intermediate'] = intermediate;
                            frequency = 1.0;
                            if 'frequency' in match['mutation_data']: frequency = match['mutation_data']['frequency'];
                            data_tmp['mutation_frequency'] = frequency
                            data_tmp['mutation_position'] = match['mutation_data']['position']
                            data_tmp['mutation_type'] = match['mutation_data']['type']
                            data_tmp['lineage_name'] = lineage_name;
                            data_tmp['mutation_data'] = match['mutation_data'];
                            data_O.append(data_tmp);
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
    def execute_analyzeEndpointReplicates_population(self,experiment_id,end_points):
        '''Analyze a endpoint replicates to identify the following:
        1. conserved mutations among replicates
        2. unique mutations among replicates'''
        #Input:
        #   experiment_id = experiment id
        #   end_points = {analysis_id: [sample_name_1,sample_name_2,sample_name_3,...]}
        #Output:

        #TODO: drive from analysis table

        print('Executing analyzeEndpointReplicates_population...')
        data_O = [];
        for analysis_id,strains in end_points.items():
            print('analyzing endpoint ' + analysis_id);
            analyzed_strain1 = []; # strain1s that have been analyzed
            analyzed_mutation_pairs = []; # mutation pairs that have been analyzed
            matched_mutations = {};
            for strain1 in strains:
                # query strain 1 data:
                strain1_mutations = [];
                strain1_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain1);
                analyzed_strain1.append(strain1);
                analyzed_strain1_mutations = []; # mutations from strain 1 that have been analyzed
                analyzed_strain2_mutations_all = []; # all mutations from strain 2 that have been analyzed
                strain2_cnt = 0;
                for strain2 in strains:
                    if strain2 == strain1: continue; # do not compare the same strain to itself
                    print('comparing ' + strain1 + ' to ' + strain2);
                    # query strain 1 data:
                    strain2_mutations = [];
                    strain2_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain2);
                    analyzed_strain2_mutations = []; # mutations from strain 2 that have been analyzed
                    for strain1_mutation_cnt,strain1_mutation in enumerate(strain1_mutations):
                        print('strain1 mutation type/position ' + strain1_mutation['mutation_data']['type'] + '/' + str(strain1_mutation['mutation_data']['position']));
                        if strain2_cnt == 0: # record strain 1 mutations only once for all strain 2 mutations
                            analyzed_strain1_mutations.append((strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position']));
                        for strain2_mutation_cnt,strain2_mutation in enumerate(strain2_mutations):
                            print('strain2 mutation type/position ' + strain2_mutation['mutation_data']['type'] + '/' + str(strain2_mutation['mutation_data']['position']));
                            if strain2_mutation_cnt == 0 and \
                                (strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position']) not in matched_mutations:
                                matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] = 0;
                            # find the mutations that are common to strain1 and strain2
                            # filter by mutation type-specific criteria
                            match = {};
                            if strain1_mutation['mutation_data']['type'] == 'SNP':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['new_seq']==strain2_mutation['mutation_data']['new_seq']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'SUB':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size'] and \
                                    strain1_mutation['mutation_data']['new_seq']==strain2_mutation['mutation_data']['new_seq']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'DEL':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'INS':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['new_seq']==strain2_mutation['mutation_data']['new_seq']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'MOB':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['repeat_name']==strain2_mutation['mutation_data']['repeat_name'] and \
                                    strain1_mutation['mutation_data']['strand']==strain2_mutation['mutation_data']['strand'] and \
                                    strain1_mutation['mutation_data']['duplication_size']==strain2_mutation['mutation_data']['duplication_size']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'AMP':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size'] and \
                                    strain1_mutation['mutation_data']['new_copy_number']==strain2_mutation['mutation_data']['new_copy_number']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'CON':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size'] and \
                                    strain1_mutation['mutation_data']['region']==strain2_mutation['mutation_data']['region']:
                                    match = strain1_mutation;
                            elif strain1_mutation['mutation_data']['type'] == 'INV':
                                if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                                    strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                                    strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size']:
                                    match = strain1_mutation;
                            else:
                                print('unknown mutation type');
                            if match and \
                                 matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] == 0:
                                # check that the mutation combination and pairs of strains have not already been analyzed
                                data_tmp = {};
                                data_tmp['experiment_id'] = match['experiment_id'];
                                data_tmp['sample_name'] = match['sample_name'];
                                frequency = 1.0;
                                if 'frequency' in match['mutation_data']: frequency = match['mutation_data']['frequency'];
                                data_tmp['mutation_frequency'] = frequency
                                data_tmp['mutation_position'] = match['mutation_data']['position']
                                data_tmp['mutation_type'] = match['mutation_data']['type']
                                data_tmp['analysis_id'] = analysis_id;
                                data_tmp['mutation_data'] = match['mutation_data'];
                                data_tmp['isUnique'] = False;
                                data_O.append(data_tmp);
                                matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] += 1;
                            if strain1_mutation_cnt == 0: # record strain 2 mutations only once for all strain 1 mutations
                                analyzed_strain2_mutations.append((strain2_mutation['mutation_data']['type'],strain2_mutation['mutation_data']['position']));
                    analyzed_strain2_mutations_all.append(analyzed_strain2_mutations);
                    strain2_cnt += 1;
                # check for unique mutations and for conserved mutations
                for analyzed_strain1_mutation in analyzed_strain1_mutations:
                    isUnique_bool = True;
                    isConserved_cnt = 0;
                    for analyzed_strain2_mutations_cnt,analyzed_strain2_mutations in enumerate(analyzed_strain2_mutations_all):
                        for analyzed_strain2_mutation in analyzed_strain2_mutations:
                            if analyzed_strain1_mutation == analyzed_strain2_mutation:
                                isUnique_bool = False;
                                isConserved_cnt += 1;
                    if isUnique_bool:
                        for strain1_mutation_cnt,strain1_mutation in enumerate(strain1_mutations):
                            if (strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])==analyzed_strain1_mutation:
                                data_tmp = {};
                                data_tmp['experiment_id'] = strain1_mutation['experiment_id'];
                                data_tmp['sample_name'] = strain1_mutation['sample_name'];
                                frequency = 1.0;
                                if 'frequency' in strain1_mutation['mutation_data']: frequency = strain1_mutation['mutation_data']['frequency'];
                                data_tmp['mutation_frequency'] = frequency
                                data_tmp['mutation_position'] = strain1_mutation['mutation_data']['position']
                                data_tmp['mutation_type'] = strain1_mutation['mutation_data']['type']
                                data_tmp['analysis_id'] = analysis_id;
                                data_tmp['mutation_data'] = strain1_mutation['mutation_data'];
                                data_tmp['isUnique'] = True;
                                data_O.append(data_tmp);


        for d in data_O:
            row = [];
            row = data_stage01_resequencing_endpoints(d['experiment_id'],
                d['analysis_id'],
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
    def execute_annotateMutations_lineage(self,experiment_id,sample_names_I=[],ref_genome_I='data/U00096.2.gb'):
        '''Annotate mutations for date_stage01_resequencing_lineage
        based on position, reference genome, and reference genome biologicalmaterial_id'''

        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

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
                annotation = self.find_genesFromMutationPosition(row['mutation_position'],record);
                row['mutation_genes'] = annotation['gene']
                row['mutation_locations'] = annotation['location']
                row['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                row['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences('MG1655',bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = self.generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                            row['mutation_links'].append(ecogene_link)
                        else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                data_O.append(row);
        # update rows in the database
        io = stage01_resequencing_io();
        io.update_dataStage01ResequencingLineage(data_O);
    def execute_annotateMutations_endpoints(self,experiment_id,sample_names_I=[],ref_genome_I='data/U00096.2.gb'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

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
                annotation = self.find_genesFromMutationPosition(row['mutation_position'],record);
                row['mutation_genes'] = annotation['gene']
                row['mutation_locations'] = annotation['location']
                row['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                row['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences('MG1655',bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = self.generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
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
    def execute_heatmap(self, analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete'):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.stage01_resequencing_query.get_experimentIDAndSampleName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # partition into variables:
        mutation_data_O = [];
        mutation_ids_all = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sample_name_cnt],sample_name);
            for end_cnt,mutation in enumerate(mutations):
                if mutation['mutation_position'] > 4000000: #ignore positions great than 4000000
                    continue;
                if mutation['mutation_frequency']<frequency_threshold:
                    continue;
                # mutation id
                mutation_genes_str = '';
                for gene in mutation['mutation_genes']:
                    mutation_genes_str = mutation_genes_str + gene + '-/-'
                mutation_genes_str = mutation_genes_str[:-3];
                mutation_id = mutation['mutation_type'] + '_' + mutation_genes_str + '_' + str(mutation['mutation_position'])
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids_all.append(mutation_id);
        mutation_ids_all_unique = list(set(mutation_ids_all));
        mutation_ids = [x for x in mutation_ids_all_unique if not x in mutation_id_exclusion_list];
        # generate the frequency matrix data structure (mutation x intermediate)
        data_O = numpy.zeros((len(sample_names),len(mutation_ids)));
        samples=[];
        # order 2: groups each sample by mutation (intermediate x mutation)
        for sample_name_cnt,sample_name in enumerate(sample_names): #all samples for intermediate j / mutation i
            samples.append(sample_name); # corresponding label from hierarchical clustering
            for mutation_cnt,mutation in enumerate(mutation_ids): #all mutations i for intermediate j
                for row in mutation_data_O:
                    if row['mutation_id'] == mutation and row['sample_name'] == sample_name:
                        data_O[sample_name_cnt,mutation_cnt] = row['mutation_frequency'];
        # generate the clustering for the heatmap
        heatmap_O = [];
        dendrogram_col_O = {};
        dendrogram_row_O = {};
        heatmap_O,dendrogram_col_O,dendrogram_row_O = self.calculate.heatmap(data_O,samples,mutation_ids,
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
    #helper functions
    def find_genesFromMutationPosition(self,mutation_position_I,record_I):
        '''find genes at the position or closest to the position given the reference genome'''
        #input:
        # mutation_position_I = mutation position [int]
        # record = genbank record [SeqRecord]
        snp_records = {};
        snp_records['gene'] = []
        snp_records['db_xref'] = []
        snp_records['locus_tag'] = []
        snp_records['EC_number'] = []
        snp_records['product'] = []
        snp_records['location'] = []
        # find features in the coding region of the genome that bracket the mutation position
        for feature_cnt,feature in enumerate(record_I.features):
            if mutation_position_I in feature and feature.type == 'gene':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['db_xref'] = feature.qualifiers.get('db_xref')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
            elif mutation_position_I in feature and feature.type == 'CDS':
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
            elif mutation_position_I in feature and feature.type == 'repeat_region':
                snp_records['location'] = feature.qualifiers.get('note')
            elif mutation_position_I in feature and feature.type == 'mobile_element':
                snp_records['location'] = feature.qualifiers.get('mobile_element_type')
            elif mutation_position_I in feature and feature.type == 'misc_feature':
                snp_records['location'] = feature.qualifiers.get('note')
            elif mutation_position_I in feature and feature.type == 'mat_peptide':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
            elif mutation_position_I in feature and feature.type == 'tRNA':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
            elif mutation_position_I in feature and feature.type == 'rRNA':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['db_xref'] = feature.qualifiers.get('db_xref')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
            elif mutation_position_I in feature and feature.type == 'ncRNA':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['db_xref'] = feature.qualifiers.get('db_xref')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
            elif mutation_position_I in feature and feature.type != 'source':
                print(feature)
        if not snp_records['location']:
            # no features in the coding region were found that bracket the mutation
            # find features before and after the mutation position
            start_prev = 0;
            stop_prev = 0;
            inter1_start = None;
            inter1_stop = None;
            inter2_start = None;
            inter2_stop = None;
            # pass 1: locate the start and stop positions of the features before and after the mutation
            for feature_cnt,feature in enumerate(record_I.features):
                start = feature.location.start.position
                stop = feature.location.end.position
                if mutation_position_I > stop_prev and mutation_position_I < start:
                    inter1_start = start_prev;
                    inter1_stop = stop_prev;
                    inter2_start = start;
                    inter2_stop = stop
                    break;
                start_prev = start;
                stop_prev = stop;
            if not inter1_start:
                # the end of the genome was reached without finding features both before and after the mutation
                # record the last entry
                inter1_start = start_prev;
                inter1_stop = stop_prev;
                inter2_start = start;
                inter2_stop = stop
            # pass 2: record features before and after the mutation
            for feature_cnt,feature in enumerate(record_I.features):
                start = feature.location.start.position
                stop = feature.location.end.position
                if (inter1_start == start and inter1_stop == stop) or (inter2_start == start and inter2_stop == stop):
                    if feature.type == 'gene':
                        snp_records['gene'] += feature.qualifiers.get('gene')
                        snp_records['db_xref'] += feature.qualifiers.get('db_xref')
                        snp_records['locus_tag'] += feature.qualifiers.get('locus_tag')
                    if feature.type == 'CDS':
                        if feature.qualifiers.get('EC_number'):snp_records['EC_number'] += feature.qualifiers.get('EC_number')
                        else:snp_records['EC_number'] += [None]
                        if feature.qualifiers.get('product'):snp_records['product'] += feature.qualifiers.get('product')
                        else:snp_records['product'] += [None]
            for gene in snp_records['gene']:
                snp_records['location'] += ['intergenic']
        return snp_records;
    def generate_httplink2gene_ecogene(self,ecogene_I):
        '''Generate link to ecocyc using the ecogene accession number'''
        ecogene_httplink = 'http://ecocyc.org/ECOLI/NEW-IMAGE?type=GENE&object='+ecogene_I;
        return ecogene_httplink
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
                #reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                #reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
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
    def reset_dataStage01_filtered(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_lineage(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_lineage).filter(data_stage01_resequencing_lineage.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_lineage).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_endpoints(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
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
    def execute_coverageStats_fromGff(self,analysis_id_I):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''
        # get the analysis_info
        analysis_rows = [];

        # get the data
        data_O = [];
        for cnt,analysis in analysis_rows:
            # get the sample_names
            experiment_id = analysis['experiment_id'];
            sn = analysis['sample_name'];
        

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

    def execute_findAmplifications_fromGff(self,
                #analysis_id_I,
                experiment_id_I,
                strand_start, strand_stop,
                sample_names_I = [],
                scale_factor=True, downsample_factor=0,reads_min=1.5,reads_max=5.0, indices_min=200,consecutive_tol=10):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''

        from sequencing_utilities.coverage import extract_strandsFromGff,find_highCoverageRegions

        # get the data
        data_O = [];
        
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
            # extract the strands
            plus,minus=extract_strandsFromGff(filename[0], strand_start, strand_stop, scale=scale_factor, downsample=downsample_factor)
            # find high coverage regions
            plus_high_region_indices,minus_high_region_indices,plus_high_regions, minus_high_regions = find_highCoverageRegions(plus,minus,coverage_min=reads_min,coverage_max=reads_max,points_min=indices_min,consecutive_tol=consecutive_tol)
            # record high coverage regions
            # + strand
            iter = 0;
            for index,reads in plus_high_regions.iteritems():
                if index > plus_high_region_indices[iter]['stop']:
                    iter+=1;
                data_O.append({
                #'analysis_id':analysis_id,
                'experiment_id':experiment_id,
                'sample_name':sn,
                'genome_chromosome':1, #default
                'genome_strand':'+',
                'genome_index':int(index),
                'strand_start':strand_start,
                'strand_stop':strand_stop,
                'reads':float(reads),
                'reads_min':reads_min,
                'reads_max':reads_max,
                'indices_min':indices_min,
                'consecutive_tol':consecutive_tol,
                'scale_factor':scale_factor,
                'downsample_factor':downsample_factor,
                'amplification_start':int(plus_high_region_indices[iter]['start']),
                'amplification_stop':int(plus_high_region_indices[iter]['stop']),
                'used_':True,
                'comment_':None
                    });
            # - strand
            iter = 0;
            for index,reads in minus_high_regions.iteritems():
                if index > minus_high_region_indices[iter]['stop']:
                    iter+=1;
                data_O.append({
                #'analysis_id':analysis_id,
                'experiment_id':experiment_id,
                'sample_name':sn,
                'genome_chromosome':1, #default
                'genome_strand':'-',
                'genome_index':int(index),
                'strand_start':strand_start,
                'strand_stop':strand_stop,
                'reads':float(reads),
                'reads_min':reads_min,
                'reads_max':reads_max,
                'indices_min':indices_min,
                'consecutive_tol':consecutive_tol,
                'scale_factor':scale_factor,
                'downsample_factor':downsample_factor,
                'amplification_start':int(minus_high_region_indices[iter]['start']),
                'amplification_stop':int(minus_high_region_indices[iter]['stop']),
                'used_':True,
                'comment_':None
                    });
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
                        # calculate using R
                        #data_TTest = {};
                        #data_TTest = self.r_calc.calculate_oneSampleTTest(data_reads, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
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

        from sequencing_utilities.coverage import extract_strandsFromGff,find_highCoverageRegions

        # get the data
        data_O = [];
        stats_O = [];
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
            # extract the strands
            plus,minus=extract_strandsFromGff(filename[0], strand_start, strand_stop, scale=scale_factor, downsample=0)
            # record the means for later use
            plus_mean,minus_mean = plus.mean(),minus.mean();
            plus_min,minus_min = plus.min(),minus.min();
            plus_max,minus_max = plus.max(),minus.max();
            # find high coverage regions
            plus_high_region_indices,minus_high_region_indices,plus_high_regions, minus_high_regions = find_highCoverageRegions(plus,minus,coverage_min=reads_min,coverage_max=reads_max,points_min=indices_min,consecutive_tol=consecutive_tol)
            # calculate stats on the high coverage regions
            # + strand
            for row_cnt,row in enumerate(plus_high_region_indices):
                plus_region = plus_high_regions[(plus_high_regions.index>=row['start']) & (plus_high_regions.index<=row['stop'])]
                # calculate using scipy
                data_ave_O, data_var_O, data_lb_O, data_ub_O = None, None, None, None;
                data_ave_O, data_var_O, data_lb_O, data_ub_O = self.calculate.calculate_ave_var(plus_region.values,confidence_I = 0.95);
                # calculate the interquartile range
                min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
                min_O, max_O, median_O, iq_1_O, iq_3_O=self.calculate.calculate_interquartiles(plus_region.values);
                # record data
                stats_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id_I,
                    'sample_name':sn,
                    'genome_chromosome':1,
                    'genome_strand':'plus',
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads_min':min_O,
                    'reads_max':max_O,
                    'reads_lb':data_lb_O,
                    'reads_ub':data_ub_O,
                    'reads_iq1':iq_1_O,
                    'reads_iq3':iq_3_O,
                    'reads_median':median_O,
                    'reads_mean':data_ave_O,
                    'reads_var':data_var_O,
                    'reads_n':len(plus_region.values),
                    'amplification_start':int(row['start']),
                    'amplification_stop':int(row['stop']),
                    'used_':True,
                    'comment_':None
                    })
                # downsample
                collapse_factor = None;
                if downsample_factor > 1:
                    collapse_factor = int((row['stop'] - row['start']) / downsample_factor)
                if collapse_factor and collapse_factor > 1:
                    plus_region = plus_region.groupby(lambda x: x // collapse_factor).mean()
                    plus_region.index *= collapse_factor
                # add mean to index before and after the amplification start and stop, respectively (for visualization)
                if downsample_factor > 1 and row_cnt==0:
                    #plus_region[strand_start]=plus_mean;
                    #plus_region[strand_stop]=plus_mean;
                    data_O.append({
                        #'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':1, #default
                        'genome_strand':'plus_mean',
                        #'genome_index':int(strand_start),
                        'genome_index':int(row['start']-1),
                        'strand_start':strand_start,
                        'strand_stop':strand_stop,
                        'reads':plus_mean,
                        'reads_min':reads_min,
                        'reads_max':reads_max,
                        'indices_min':indices_min,
                        'consecutive_tol':consecutive_tol,
                        'scale_factor':scale_factor,
                        'downsample_factor':downsample_factor,
                        'amplification_start':strand_start,
                        'amplification_stop':strand_stop,
                        'used_':True,
                        'comment_':'mean reads of the plus strand'
                        });
                if downsample_factor > 1 and row_cnt==len(plus_high_region_indices)-1:
                    data_O.append({
                        #'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':1, #default
                        'genome_strand':'plus_mean',
                        #'genome_index':int(strand_stop),
                        'genome_index':int(row['stop']+1),
                        'strand_start':strand_start,
                        'strand_stop':strand_stop,
                        'reads':plus_mean,
                        'reads_min':reads_min,
                        'reads_max':reads_max,
                        'indices_min':indices_min,
                        'consecutive_tol':consecutive_tol,
                        'scale_factor':scale_factor,
                        'downsample_factor':downsample_factor,
                        'amplification_start':strand_start,
                        'amplification_stop':strand_stop,
                        'used_':True,
                        'comment_':'mean reads of the plus strand'
                        });
                ## add zeros to strand start and stop, respectively (for visualization)
                #if downsample_factor > 1:
                #    plus_region[row['start']-1]=plus_mean;
                #    plus_region[row['stop']+1]=plus_mean;
                # record high coverage regions
                for index,reads in plus_region.iteritems():
                    data_O.append({
                        #'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':1, #default
                        'genome_strand':'plus',
                        'genome_index':int(index),
                        'strand_start':strand_start,
                        'strand_stop':strand_stop,
                        'reads':float(reads),
                        'reads_min':reads_min,
                        'reads_max':reads_max,
                        'indices_min':indices_min,
                        'consecutive_tol':consecutive_tol,
                        'scale_factor':scale_factor,
                        'downsample_factor':downsample_factor,
                        'amplification_start':int(row['start']),
                        'amplification_stop':int(row['stop']),
                        'used_':True,
                        'comment_':None
                    });
            # - strand
            for row_cnt,row in enumerate(minus_high_region_indices):
                minus_region = minus_high_regions[(minus_high_regions.index>=row['start']) & (minus_high_regions.index<=row['stop'])]
                # calculate using scipy
                data_ave_O, data_var_O, data_lb_O, data_ub_O = None, None, None, None;
                data_ave_O, data_var_O, data_lb_O, data_ub_O = self.calculate.calculate_ave_var(minus_region.values,confidence_I = 0.95);
                # calculate the interquartile range
                min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
                min_O, max_O, median_O, iq_1_O, iq_3_O=self.calculate.calculate_interquartiles(minus_region.values);
                # record data
                stats_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id_I,
                    'sample_name':sn,
                    'genome_chromosome':1,
                    'genome_strand':'minus',
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads_min':min_O,
                    'reads_max':max_O,
                    'reads_lb':data_lb_O,
                    'reads_ub':data_ub_O,
                    'reads_iq1':iq_1_O,
                    'reads_iq3':iq_3_O,
                    'reads_median':median_O,
                    'reads_mean':data_ave_O,
                    'reads_var':data_var_O,
                    'reads_n':len(minus_region.values),
                    'amplification_start':int(row['start']),
                    'amplification_stop':int(row['stop']),
                    'used_':True,
                    'comment_':None
                    })
                # downsample
                collapse_factor = None;
                if downsample_factor > 1:
                    collapse_factor = int((row['stop'] - row['start']) / downsample_factor)
                if collapse_factor and collapse_factor > 1:
                    minus_region = minus_region.groupby(lambda x: x // collapse_factor).mean()
                    minus_region.index *= collapse_factor
                # add mean to index before and after the amplification start and stop, respectively (for visualization)
                if downsample_factor > 1 and row_cnt==0:
                    #minus_region[strand_start]=minus_mean;
                    #minus_region[strand_stop]=minus_mean;
                    data_O.append({
                        #'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':1, #default
                        'genome_strand':'minus_mean',
                        #'genome_index':int(strand_start),
                        'genome_index':int(row['start']-1),
                        'strand_start':strand_start,
                        'strand_stop':strand_stop,
                        'reads':minus_mean,
                        'reads_min':reads_min,
                        'reads_max':reads_max,
                        'indices_min':indices_min,
                        'consecutive_tol':consecutive_tol,
                        'scale_factor':scale_factor,
                        'downsample_factor':downsample_factor,
                        'amplification_start':strand_start,
                        'amplification_stop':strand_stop,
                        'used_':True,
                        'comment_':'mean reads of the minus strand'
                        });
                if downsample_factor > 1 and row_cnt==len(minus_high_region_indices)-1:
                    data_O.append({
                        #'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':1, #default
                        'genome_strand':'minus_mean',
                        #'genome_index':int(strand_stop),
                        'genome_index':int(row['stop']+1),
                        'strand_start':strand_start,
                        'strand_stop':strand_stop,
                        'reads':minus_mean,
                        'reads_min':reads_min,
                        'reads_max':reads_max,
                        'indices_min':indices_min,
                        'consecutive_tol':consecutive_tol,
                        'scale_factor':scale_factor,
                        'downsample_factor':downsample_factor,
                        'amplification_start':strand_start,
                        'amplification_stop':strand_stop,
                        'used_':True,
                        'comment_':'mean reads of the minus strand'
                        });
                ## add zeros to strand start and stop, respectively (for visualization)
                #if downsample_factor > 1:
                #    minus_region[row['start']-1]=minus_mean;
                #    minus_region[row['stop']+1]=minus_mean;
                # record high coverage regions
                for index,reads in minus_region.iteritems():
                    data_O.append({
                        #'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':1, #default
                        'genome_strand':'minus',
                        'genome_index':int(index),
                        'strand_start':strand_start,
                        'strand_stop':strand_stop,
                        'reads':float(reads),
                        'reads_min':reads_min,
                        'reads_max':reads_max,
                        'indices_min':indices_min,
                        'consecutive_tol':consecutive_tol,
                        'scale_factor':scale_factor,
                        'downsample_factor':downsample_factor,
                        'amplification_start':int(row['start']),
                        'amplification_stop':int(row['stop']),
                        'used_':True,
                        'comment_':None});

        # add data to the DB
        self.stage01_resequencing_io.add_dataStage01ResequencingAmplifications(data_O);
        self.stage01_resequencing_io.add_dataStage01ResequencingAmplificationStats(stats_O);

    def execute_annotateAmplifications(self,experiment_id_I,sample_names_I=[],ref_genome_I='data/U00096.2.gb'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

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
                        annotations = self.find_genesInRegion(start,stops[start_cnt],record)
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
                                    ecogenes = self.stage01_resequencing_query.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences('MG1655',bnumber);
                                    if ecogenes:
                                        ecogene = ecogenes[0];
                                        ecogene_link = self.generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                                        tmp['feature_links'].append(ecogene_link)
                                    else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                            data_O.append(tmp);
        # update rows in the database
        io = stage01_resequencing_io();
        io.add_dataStage01ResequencingAmplificationAnnotations(data_O);
    def find_genesInRegion(self,start_I,stop_I,record_I):
        '''find genes in the start and stop region of the genome'''
        #input:
        # mutation_position_I = mutation position [int]
        # record = genbank record [SeqRecord]
        data_O = [];
        #extract all features within the start and stop region
        features = [f for f in record_I.features if start_I <= f.location.start.position and stop_I <= f.location.end.position]
        for feature_cnt,feature in enumerate(features):
            # NOTE:
            # there are two records for each gene: one of type "gene" and another of type "CDS"
            # sometimes there is also a third of type "mat_peptide" which has a different start/stop position
            # this algorithm will combine the records for types "gene" and "CDS" as a single row
            # and add mat_peptide as a second row (if desired)
            # initialize variables
            if feature_cnt == 0:
                feature_start_pos = feature.location.start.position;
                feature_stop_pos = feature.location.end.position;
                snp_records = {};
                snp_records['gene'] = []
                snp_records['db_xref'] = []
                snp_records['locus_tag'] = []
                snp_records['EC_number'] = []
                snp_records['product'] = []
                snp_records['location'] = []
                snp_records['start'] = None
                snp_records['stop'] = None
                snp_records['type'] = []
            # add complete snp_record to data_O
            if feature_start_pos != feature.location.start.position or feature_stop_pos != feature.location.end.position:
                #snp_records['start'] should be in every record
                data_O.append(snp_records);
                feature_start_pos = feature.location.start.position;
                feature_stop_pos = feature.location.end.position;
                snp_records = {};
                snp_records['gene'] = []
                snp_records['db_xref'] = []
                snp_records['locus_tag'] = []
                snp_records['EC_number'] = []
                snp_records['product'] = []
                snp_records['location'] = []
                snp_records['start'] = None
                snp_records['stop'] = None
                snp_records['type'] = []
            # fill in snp_record (may require multiple passes through features)
            if feature.type == 'gene':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['db_xref'] = feature.qualifiers.get('db_xref')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'CDS': 
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'repeat_region':
                snp_records['location'] = feature.qualifiers.get('note')
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'mobile_element':
                snp_records['location'] = feature.qualifiers.get('mobile_element_type')
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'misc_feature':
                snp_records['location'] = feature.qualifiers.get('note')
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'mat_peptide':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'tRNA':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'rRNA':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['db_xref'] = feature.qualifiers.get('db_xref')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type == 'ncRNA':
                snp_records['gene'] = feature.qualifiers.get('gene')
                snp_records['db_xref'] = feature.qualifiers.get('db_xref')
                snp_records['locus_tag'] = feature.qualifiers.get('locus_tag')
                #snp_records['location'] = feature.qualifiers.get('note')
                if feature.qualifiers.get('EC_number'):snp_records['EC_number'] = feature.qualifiers.get('EC_number')
                else:snp_records['EC_number'] = [None];
                if feature.qualifiers.get('product'):snp_records['product'] = feature.qualifiers.get('product')
                else:snp_records['product'] = [None];
                snp_records['location'] = ['coding'];
                snp_records['start'] = feature.location.start.position;
                snp_records['stop'] = feature.location.end.position;
                snp_records['type'].append(feature.type)
            elif feature.type != 'source':
                print(feature);
            # add the final snp_record to data_O
            if feature_cnt == len(features)-1:
                data_O.append(snp_records);

        return data_O;