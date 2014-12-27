'''resequencing class'''

from analysis.analysis_base import *
from stage01_resequencing_query import *
from stage01_resequencing_io import *

class stage01_resequencing_execute():
    '''class for resequencing analysis'''
    def __init__(self):
        self.session = Session();
        self.stage01_resequencing_query = stage01_resequencing_query();
        self.calculate = base_calculate();
    #analysis
    def execute_filterMutations_population(self,experiment_id,p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1,sample_names_I=None):
        '''Filter mutations that do not meet the desired criteria'''

        print 'Executing filterMutations_population...'
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingMetadata(experiment_id,8);
        for sn in sample_names:
            print 'Filtering mutations for sample_name ' + sn;
            #query mutation data filtered by frequency
            data_mutations_list = [];
            data_mutations_list = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutations(experiment_id,sn);
            for data_mutations in data_mutations_list:
                print 'Filtering mutations for mutation id ' + str(data_mutations['mutation_id']);
                #query data filtered by evidence-specific criteria
                data_evidence_list = [];
                for pid in data_mutations['parent_ids']:
                    print 'Filtering mutations for parent id ' + str(pid);
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
                                                 ref_genome_I='data\\U00096.2.gb'):

        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

        print 'Executing annotation of filtered mutations...'
        genotype_phenotype_O = [];
        # query sample names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingMutationsFiltered(experiment_id);
        for sn in sample_names:
            print 'analyzing sample_name ' + sn;
            # query mutation data:
            mutations = [];
            mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,sn);
            mutation_data_O = [];
            for end_cnt,mutation in enumerate(mutations):
                print 'analyzing mutations'
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
                        else: print 'no ecogene_accession_number found for ordered_locus_location ' + bnumber;
                data_tmp['experiment_id'] = mutation['experiment_id'];
                data_tmp['sample_name'] = mutation['sample_name'];
                frequency = 1.0;
                if mutation['mutation_data'].has_key('frequency'):
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
        #   strain_lineage = {"strain_lineage_name":{0:sample_name,1:sample_name,2:sample_name,...,n:sample_name}}
        #                       where n is the end-point strain
        #Output:

        print 'Executing analyzeLineage_population...'
        data_O = [];
        for lineage_name,strain in strain_lineage.iteritems():
            print 'analyzing lineage ' + lineage_name;
            lineage = strain.keys();
            end_point = max(lineage)
            # query end data:
            end_mutations = [];
            end_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain[end_point]);
            intermediates = [i for i in lineage if i!=end_point];
            intermediate_mutations = [];
            for intermediate in intermediates:
                print 'analyzing intermediate ' + str(intermediate);
                # query intermediate data:
                intermediate_mutations = [];
                intermediate_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain[intermediate]);
                for end_cnt,end_mutation in enumerate(end_mutations):
                    print 'end mutation type/position ' + end_mutation['mutation_data']['type'] + '/' + str(end_mutation['mutation_data']['position']);
                    for inter_cnt,intermediate_mutation in enumerate(intermediate_mutations):
                        print 'intermediate mutation type/position ' + intermediate_mutation['mutation_data']['type'] + '/' + str(intermediate_mutation['mutation_data']['position']);
                        if intermediate == 0 and inter_cnt == 0:
                            #copy end_point data (only once per strain lineage)
                            data_tmp = {};
                            data_tmp['experiment_id'] = end_mutation['experiment_id'];
                            data_tmp['sample_name'] = end_mutation['sample_name'];
                            data_tmp['intermediate'] = end_point;
                            frequency = 1.0;
                            if end_mutation['mutation_data'].has_key('frequency'): frequency = end_mutation['mutation_data']['frequency'];
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
                            print 'unknown mutation type';
                        if match:
                            data_tmp = {};
                            data_tmp['experiment_id'] = match['experiment_id'];
                            data_tmp['sample_name'] = match['sample_name'];
                            data_tmp['intermediate'] = intermediate;
                            frequency = 1.0;
                            if match['mutation_data'].has_key('frequency'): frequency = match['mutation_data']['frequency'];
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
        #   end_points = {endpoint_name: [sample_name_1,sample_name_2,sample_name_3,...]}
        #Output:

        print 'Executing analyzeEndpointReplicates_population...'
        data_O = [];
        for endpoint_name,strains in end_points.iteritems():
            print 'analyzing endpoint ' + endpoint_name;
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
                    print 'comparing ' + strain1 + ' to ' + strain2;
                    # query strain 1 data:
                    strain2_mutations = [];
                    strain2_mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain2);
                    analyzed_strain2_mutations = []; # mutations from strain 2 that have been analyzed
                    for strain1_mutation_cnt,strain1_mutation in enumerate(strain1_mutations):
                        print 'strain1 mutation type/position ' + strain1_mutation['mutation_data']['type'] + '/' + str(strain1_mutation['mutation_data']['position']);
                        if strain2_cnt == 0: # record strain 1 mutations only once for all strain 2 mutations
                            analyzed_strain1_mutations.append((strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position']));
                        for strain2_mutation_cnt,strain2_mutation in enumerate(strain2_mutations):
                            print 'strain2 mutation type/position ' + strain2_mutation['mutation_data']['type'] + '/' + str(strain2_mutation['mutation_data']['position']);
                            if strain2_mutation_cnt == 0 and \
                                not matched_mutations.has_key((strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])):
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
                                print 'unknown mutation type';
                            if match and \
                                 matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] == 0:
                                # check that the mutation combination and pairs of strains have not already been analyzed
                                data_tmp = {};
                                data_tmp['experiment_id'] = match['experiment_id'];
                                data_tmp['sample_name'] = match['sample_name'];
                                frequency = 1.0;
                                if match['mutation_data'].has_key('frequency'): frequency = match['mutation_data']['frequency'];
                                data_tmp['mutation_frequency'] = frequency
                                data_tmp['mutation_position'] = match['mutation_data']['position']
                                data_tmp['mutation_type'] = match['mutation_data']['type']
                                data_tmp['endpoint_name'] = endpoint_name;
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
                                if strain1_mutation['mutation_data'].has_key('frequency'): frequency = strain1_mutation['mutation_data']['frequency'];
                                data_tmp['mutation_frequency'] = frequency
                                data_tmp['mutation_position'] = strain1_mutation['mutation_data']['position']
                                data_tmp['mutation_type'] = strain1_mutation['mutation_data']['type']
                                data_tmp['endpoint_name'] = endpoint_name;
                                data_tmp['mutation_data'] = strain1_mutation['mutation_data'];
                                data_tmp['isUnique'] = True;
                                data_O.append(data_tmp);


        for d in data_O:
            row = [];
            row = data_stage01_resequencing_endpoints(d['experiment_id'],
                d['endpoint_name'],
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
    def execute_annotateMutations_lineage(self,experiment_id,sample_names_I=[],ref_genome_I='data\\U00096.2.gb'):
        '''Annotate mutations for date_stage01_resequencing_lineage
        based on position, reference genome, and reference genome biologicalmaterial_id'''

        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

        print 'Executing annotateMutations_lineage...'
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingLineage(experiment_id);
        for sn in sample_names:
            print 'annotating mutation for sample_name ' + sn;
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
                        else: print 'no ecogene_accession_number found for ordered_locus_location ' + bnumber;
                data_O.append(row);
        # update rows in the database
        io = stage01_resequencing_io();
        io.update_dataStage01ResequencingLineage(data_O);
    def execute_annotateMutations_endpoints(self,experiment_id,sample_names_I=[],ref_genome_I='data\\U00096.2.gb'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        from Bio import SeqIO
        from Bio import Entrez
        record = SeqIO.read(ref_genome_I,'genbank')

        print 'Executing annotateMutations_endpoints...'
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.stage01_resequencing_query.get_sampleNames_experimentID_dataStage01ResequencingEndpoints(experiment_id);
        for sn in sample_names:
            print 'annotating mutation for sample_name ' + sn;
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
                        else: print 'no ecogene_accession_number found for ordered_locus_location ' + bnumber;
                data_O.append(row);
        # update rows in the database
        io = stage01_resequencing_io();
        io.update_dataStage01ResequencingEndpoints(data_O);
    #helper functions
    def find_genesFromMutationPosition(self,mutation_position_I,record_I):
        '''find genes at the position or closes to the position given the reference genome'''
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
                print feature
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
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01(self,experiment_id_I = None):
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
            else:
                reset = self.session.query(data_stage01_resequencing_metadata).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_lineage).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_endpoints).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).delete(synchronize_session=False);
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
    #TODO:
                