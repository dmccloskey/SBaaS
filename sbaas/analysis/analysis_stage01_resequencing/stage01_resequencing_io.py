from sbaas.analysis.analysis_base import *
from .stage01_resequencing_query import stage01_resequencing_query
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sbaas.analysis.analysis_stage01_resequencing import gdparse
import json
#TODO:test
#from sequencing_analysis.genome_diff import genome_diff

class stage01_resequencing_io(base_analysis):
    '''class for resequencing analysis'''
    def __init__(self,session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage01_resequencing_query = stage01_resequencing_query(self.session);
        self.calculate = base_calculate();
    
    def import_resequencingData_add(self, filename, experiment_id, sample_name):
        '''table adds'''

        #TODO: test
        #genomediff = genome_diff();
        #genomediff.import_gd(filename, experiment_id, sample_name)

        gd = gdparse.GDParser(file_handle=open(filename, 'rb'))
        # extract out ids
        mutation_ids = [];
        mutation_ids = list(gd.data['mutation'].keys())
        parent_ids = [];
        for mid in mutation_ids:
            parents = [];
            parents = gd.data['mutation'][mid]['parent_ids'];
            parent_ids.extend(parents);
        # split into seperate data structures based on the destined table add
        metadata = [];
        mutation_data = [];
        evidence_data = [];
        validation_data = [];
        if gd.metadata:
            metadata.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'genome_diff':gd.metadata['GENOME_DIFF'],
                                 'refseq':gd.metadata['REFSEQ'],
                                 'readseq':gd.metadata['READSEQ'],
                                 'author':gd.metadata['AUTHOR']});
        if gd.data['mutation']:
            for mid in mutation_ids:
                mutation_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'mutation_id':mid,
                                 'parent_ids':gd.data['mutation'][mid]['parent_ids'],
                                 'mutation_data':gd.data['mutation'][mid]});
                                 #'mutation_data':json.dumps(gd.data['mutation'][mid])});
        if gd.data['evidence']:
            for pid in parent_ids:
                evidence_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'parent_id':pid,
                                 'evidence_data':gd.data['evidence'][pid]});
                                 #'evidence_data':json.dumps(gd.data['evidence'][pid])});
        if gd.data['validation']:
            for mid in mutation_ids:
                validation_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'validation_id':mid,
                                 'validation_data':gd.data['validation'][mid]});
                                 #'validation_data':json.dumps(gd.data['validation'][mid])});
        # add data to the database:
        #TODO: test
        #self.add_dataStage01ResequencingMetadata(genomediff.metadata);
        #self.add_dataStage01ResequencingMutations(genomediff.mutations);
        #self.add_dataStage01ResequencingEvidence(genomediff.evidence);
        #self.add_dataStage01ResequencingValidation(genomediff.validation);
        self.add_dataStage01ResequencingMetadata(metadata);
        self.add_dataStage01ResequencingMutations(mutation_data);
        self.add_dataStage01ResequencingEvidence(evidence_data);
        self.add_dataStage01ResequencingValidation(validation_data);

    def add_dataStage01ResequencingMutations(self, data_I):
        '''add rows of data_stage01_resequencing_mutations'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_mutations(d['experiment_id'],
                                    d['sample_name'],
                                    d['mutation_id'],
                                    d['parent_ids'],
                                    d['mutation_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage01ResequencingMetadata(self, data_I):
        '''add rows of data_stage01_resequencing_metadata'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_metadata(d['experiment_id'],
                            d['sample_name'],
                            d['genome_diff'],
                            d['refseq'],
                            d['readseq'],
                            d['author']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage01ResequencingEvidence(self, data_I):
        '''add rows of data_stage01_resequencing_evidence'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_evidence(d['experiment_id'],
                        d['sample_name'],
                        d['parent_id'],
                        d['evidence_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage01ResequencingValidation(self, data_I):
        '''add rows of data_stage01_resequencing_validation'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_validation(d['experiment_id'],
                        d['sample_name'],
                        d['validation_id'],
                        d['validation_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01ResequencingLineage_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingLineage(data.data);
        data.clear_data();

    def add_dataStage01ResequencingLineage(self, data_I):
        '''add rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_lineage(d['experiment_id'],
                                d['lineage_name'],
                                d['sample_name'],
                                d['intermediate'],
                                d['mutation_frequency'],
                                d['mutation_type'],
                                d['mutation_position'],
                                d['mutation_data'],
                                d['mutation_annotations'],
                                d['mutation_genes'],
                                d['mutation_locations'],
                                d['mutation_links'],
                                d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01ResequencingLineage_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingLineage(data.data);
        data.clear_data();

    def update_dataStage01ResequencingLineage(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    #if d['mutation_genes']:
                    #    d['mutation_genes']=d['mutation_genes'].split();
                    #if d['mutation_location']:
                    #    d['mutation_location']=d['mutation_location'].split();
                    data_update = self.session.query(data_stage01_resequencing_lineage).filter(
                           data_stage01_resequencing_lineage.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                                'lineage_name':d['lineage_name'],
                                'sample_name':d['sample_name'],
                                'intermediate':d['intermediate'],
                                'mutation_frequency':d['mutation_frequency'],
                                'mutation_type':d['mutation_type'],
                                'mutation_position':d['mutation_position'],
                                'mutation_data':d['mutation_data'],
                                'mutation_annotations':d['mutation_annotations'],
                                'mutation_genes':d['mutation_genes'],
                                'mutation_locations':d['mutation_locations'],
                                'mutation_links':d['mutation_links'],
                                'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01ResequencingEndpoints_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingEndpoints(data.data);
        data.clear_data();

    def add_dataStage01ResequencingEndpoints(self, data_I):
        '''add rows of data_stage01_resequencing_endpoints'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_endpoints(d['experiment_id'],
                            d['analysis_id'],
                            d['sample_name'],
                            d['mutation_frequency'],
                            d['mutation_type'],
                            d['mutation_position'],
                            d['mutation_data'],
                            d['isUnique'],
                            d['mutation_annotations'],
                            d['mutation_genes'],
                            d['mutation_locations'],
                            d['mutation_links'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01ResequencingEndpoints_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingEndpoints(data.data);
        data.clear_data();

    def update_dataStage01ResequencingEndpoints(self,data_I):
        '''update rows of data_stage01_resequencing_endpoints'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_endpoints).filter(
                           data_stage01_resequencing_endpoints.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'analysis_id':d['analysis_id'],
                            'sample_name':d['sample_name'],
                            'mutation_frequency':d['mutation_frequency'],
                            'mutation_type':d['mutation_type'],
                            'mutation_position':d['mutation_position'],
                            'mutation_data':d['mutation_data'],
                            'isUnique':d['isUnique'],
                            'mutation_annotations':d['mutation_annotations'],
                            'mutation_genes':d['mutation_genes'],
                            'mutation_locations':d['mutation_locations'],
                            'mutation_links':d['mutation_links'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01ResequencingAnalysis_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingAnalysis(data.data);
        data.clear_data();

    def add_dataStage01ResequencingAnalysis(self, data_I):
        '''add rows of data_stage01_resequencing_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_analysis(d['analysis_id'],
                            d['experiment_id'],
                            d['lineage_name'],
                            d['sample_name'],
                            d['time_point'],
                            d['analysis_type'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01ResequencingAnalysis_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingAnalysis(data.data);
        data.clear_data();

    def update_dataStage01ResequencingAnalysis(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    #if d['mutation_genes']:
                    #    d['mutation_genes']=d['mutation_genes'].split();
                    #if d['mutation_location']:
                    #    d['mutation_location']=d['mutation_location'].split();
                    data_update = self.session.query(data_stage01_resequencing_analysis).filter(
                           data_stage01_resequencing_analysis.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'time_point':d['time_point'],
                            'analysis_type':d['analysis_type'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    
    def import_resequencingCoverageData_add(self, filename, 
                                            #analysis_id,
                                            experiment_id, sample_name,strand_start,strand_stop,scale_factor=True,downsample_factor=2000):
        '''table adds
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''

        #from sequencing_utilities.makegff import write_samfile_to_gff
        from sequencing_utilities.coverage import extract_strandsFromGff

        if '.bam' in filename:
            #TODO convert .bam to .gff using makegff.py from sequencing_utilities
            print('conversion of .bam to .gff not yet supported');
            exit(2);
            #filename_bam = filename;
            #filename = filename.replace('.bam','.gff');
            #extract_strandsFromGff(filename_bam,filename,separate_strand=False);
        # convert strings to float and int
        strand_start, strand_stop, scale_factor, downsample_factor = int(strand_start), int(strand_stop), bool(scale_factor), float(downsample_factor);        
        # parse the gff file into pandas dataframes
        plus,minus=extract_strandsFromGff(filename, strand_start, strand_stop, scale=scale_factor, downsample=downsample_factor)
        # split into seperate data structures based on the destined table add
        coverage_data = [];
        if not plus.empty:
            for index,reads in plus.iteritems():
                coverage_data.append({
                                #'analysis_id':analysis_id,
                                'experiment_id':experiment_id,
                                'sample_name':sample_name,
                                'data_dir':filename,
                                'genome_chromosome':1, #default
                                'genome_strand':'plus',
                                'genome_index':int(index),
                                'strand_start':strand_start,
                                'strand_stop':strand_stop,
                                'reads':float(reads),
                                'scale_factor':scale_factor,
                                'downsample_factor':downsample_factor,
                                'used_':True,
                                'comment_':None});
        if not minus.empty:
            for index,reads in minus.iteritems():
                coverage_data.append({
                                #'analysis_id':analysis_id,
                                'experiment_id':experiment_id,
                                'sample_name':sample_name,
                                'data_dir':filename,
                                'genome_chromosome':1, #default
                                'genome_strand':'minus',
                                'genome_index':int(index),
                                'strand_start':strand_start,
                                'strand_stop':strand_stop,
                                'reads':float(reads),
                                'scale_factor':scale_factor,
                                'downsample_factor':downsample_factor,
                                'used_':True,
                                'comment_':None});
        # add data to the database:
        self.add_dataStage01ResequencingCoverage(coverage_data);

    def add_dataStage01ResequencingCoverage(self, data_I):
        '''add rows of data_stage01_resequencing_coverage'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_coverage(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['data_dir'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['genome_index'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['reads'],
                    d['scale_factor'],
                    d['downsample_factor'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingCoverageStats(self, data_I):
        '''add rows of data_stage01_resequencing_coverageStats'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_coverageStats(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['reads_min'],
                    d['reads_max'],
                    d['reads_lb'],
                    d['reads_ub'],
                    d['reads_iq1'],
                    d['reads_iq3'],
                    d['reads_median'],
                    d['reads_mean'],
                    d['reads_var'],
                    d['reads_n'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingAmplifications(self, data_I):
        '''add rows of data_stage01_resequencing_amplifications'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_amplifications(
                        #d['analysis_id'],
                        d['experiment_id'],
                        d['sample_name'],
                        d['genome_chromosome'],
                        d['genome_strand'],
                        d['genome_index'],
                        d['strand_start'],
                        d['strand_stop'],
                        d['reads'],
                        d['reads_min'],
                        d['reads_max'],
                        d['indices_min'],
                        d['consecutive_tol'],
                        d['scale_factor'],
                        d['downsample_factor'],
                        d['amplification_start'],
                        d['amplification_stop'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingAmplificationStats(self, data_I):
        '''add rows of data_stage01_resequencing_amplificationStats'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_amplificationStats(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['reads_min'],
                    d['reads_max'],
                    d['reads_lb'],
                    d['reads_ub'],
                    d['reads_iq1'],
                    d['reads_iq3'],
                    d['reads_median'],
                    d['reads_mean'],
                    d['reads_var'],
                    d['reads_n'],
                    d['amplification_start'],
                    d['amplification_stop'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingAmplificationAnnotations(self, data_I):
        '''add rows of data_stage01_resequencing_amplificationAnnotations'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_amplificationAnnotations(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['feature_annotations'],
                    d['feature_genes'],
                    d['feature_locations'],
                    d['feature_links'],
                    d['feature_start'],
                    d['feature_stop'],
                    d['feature_types'],
                    d['amplification_start'],
                    d['amplification_stop'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingCoverage(self,data_I):
        '''update rows of data_stage01_resequencing_coverage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_coverage).filter(
                           data_stage01_resequencing_coverage.id==d['id']).update(
                            {
                                #'analysis_id':d['analysis_id'],
                             'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'data_dir':d['data_dir'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'genome_index':d['genome_index'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads':d['reads'],
                            'scale_factor':d['scale_factor'],
                            'downsample_factor':d['downsample_factor'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingCoverageStats(self,data_I):
        '''update rows of data_stage01_resequencing_coverageStats'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_coverageStats).filter(
                           data_stage01_resequencing_coverageStats.id==d['id']).update(
                            {
                                #'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads_min':d['reads_min'],
                            'reads_max':d['reads_max'],
                            'reads_lb':d['reads_lb'],
                            'reads_ub':d['reads_ub'],
                            'reads_iq1':d['reads_iq1'],
                            'reads_iq3':d['reads_iq3'],
                            'reads_median':d['reads_median'],
                            'reads_mean':d['reads_mean'],
                            'reads_var':d['reads_var'],
                            'reads_n':d['reads_n'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingAmplifications(self,data_I):
        '''update rows of data_stage01_resequencing_amplifications'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_amplifications).filter(
                           data_stage01_resequencing_amplifications.id==d['id']).update(
                            {
                            #'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'genome_index':d['genome_index'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads':d['reads'],
                            'reads_min':d['reads_min'],
                            'reads_max':d['reads_max'],
                            'indices_min':d['indices_min'],
                            'consecutive_tol':d['consecutive_tol'],
                            'scale_factor':d['scale_factor'],
                            'downsample_factor':d['downsample_factor'],
                            'amplification_start':d['amplification_start'],
                            'amplification_stop':d['amplification_stop'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingAmplificationStats(self,data_I):
        '''update rows of data_stage01_resequencing_amplificationStats'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_amplificationStats).filter(
                           data_stage01_resequencing_amplificationStats.id==d['id']).update(
                            {
                            #'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads_min':d['reads_min'],
                            'reads_max':d['reads_max'],
                            'reads_lb':d['reads_lb'],
                            'reads_ub':d['reads_ub'],
                            'reads_iq1':d['reads_iq1'],
                            'reads_iq3':d['reads_iq3'],
                            'reads_median':d['reads_median'],
                            'reads_mean':d['reads_mean'],
                            'reads_var':d['reads_var'],
                            'reads_n':d['reads_n'],
                            'amplification_start':d['amplification_start'],
                            'amplification_stop':d['amplification_stop'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingFpkmTracking_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01RNASequencingFpkmTracking(data.data);
        data.clear_data();

    def add_dataStage01RNASequencingFpkmTracking(self, data_I):
        '''add rows of data_stage01_rnasequencing_fpkmTracking'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_rnasequencing_fpkmTracking(d['experiment_id'],
                            d['sample_name'],
                            d['tracking_id'],
                            d['class_code'],
                            d['nearest_ref_id'],
                            d['gene_id'],
                            d['gene_short_name'],
                            d['tss_id'],
                            d['locus'],
                            d['length'],
                            d['coverage'],
                            d['FPKM'],
                            d['FPKM_conf_lo'],
                            d['FPKM_conf_hi'],
                            d['FPKM_status'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingFpkmTracking_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingFpkmTracking(data.data);
        data.clear_data();

    def update_dataStage01RNASequencingFpkmTracking(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_fpkmTracking).filter(
                           data_stage01_rnasequencing_fpkmTracking.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'tracking_id':d['tracking_id'],
                            'class_code':d['class_code'],
                            'nearest_ref_id':d['nearest_ref_id'],
                            'gene_id':d['gene_id'],
                            'gene_short_name':d['gene_short_name'],
                            'tss_id':d['tss_id'],
                            'locus':d['locus'],
                            'length':d['length'],
                            'coverage':d['coverage'],
                            'FPKM':d['FPKM'],
                            'FPKM_conf_lo':d['FPKM_conf_lo'],
                            'FPKM_conf_hi':d['FPKM_conf_hi'],
                            'FPKM_status':d['FPKM_status'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingGeneExpDiff_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01RNASequencingGeneExpDiff(data.data);
        data.clear_data();

    def add_dataStage01RNASequencingGeneExpDiff(self, data_I):
        '''add rows of data_stage01_rnasequencing_geneExpDiff'''
        if data_I:
            for d in data_I:
                try:
                    if d.has_key('log2(fold_change)'):
                        d['fold_change_log2']=d['log2(fold_change)'];
                    data_add = data_stage01_rnasequencing_geneExpDiff(
                            d['analysis_id'],
                            d['experiment_id'],
                            d['sample_name_1'],
                            d['sample_name_2'],
                            d['test_id'],
                            d['gene_id'],
                            d['gene'],
                            d['sample_1'],
                            d['sample_2'],
                            d['status'],
                            d['value_1'],
                            d['value_2'],
                            d['fold_change_log2'],
                            d['test_stat'],
                            d['p_value'],
                            d['q_value'],
                            d['significant'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingGeneExpDiff_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingGeneExpDiff(data.data);
        data.clear_data();

    def update_dataStage01RNASequencingGeneExpDiff(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    if d.has_key('log2(fold_change)'):
                        d['fold_change_log2']=d['log2(fold_change)'];
                    data_update = self.session.query(data_stage01_rnasequencing_geneExpDiff).filter(
                           data_stage01_rnasequencing_geneExpDiff.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name_1':d['sample_name_1'],
                            'sample_name_2':d['sample_name_2'],
                            'test_id':d['test_id'],
                            'gene_id':d['gene_id'],
                            'gene':d['gene'],
                            'sample_1':d['sample_1'],
                            'sample_2':d['sample_2'],
                            'status':d['status'],
                            'value_1':d['value_1'],
                            'value_2':d['value_2'],
                            'fold_change_log2':d['fold_change_log2'],
                            'test_stat':d['test_stat'],
                            'p_value':d['p_value'],
                            'q_value':d['q_value'],
                            'significant':d['significant'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def export_dataStage01ResequencingMutationsAnnotatedLineage_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,data_dir_I="tmp"):
        '''export data_stage01_resequencing_mutationsAnnotated to js file'''
        
        print('exportingdataStage01ResequencingMutationsAnnotated...')
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        mutation_data_O = [];
        mutation_ids = [];
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
                mutation_id = mutation_genes_str + '_' + mutation['mutation_type'] + '_' + str(mutation['mutation_position'])
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids.append(mutation_id);
        # screen out mutations
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in mutation_data_O:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    #tmp['mutation_id']=mutation['mutation_id']
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=mutation['mutation_genes'];
                    #tmp['mutation_position']=mutation['mutation_position'];
                    #tmp['mutation_annotations']=mutation['mutation_annotations'];
                    #tmp['mutation_locations']=mutation['mutation_locations'];
                    #tmp['mutation_links']=mutation['mutation_links'];
                    #tmp['mutation_type']=mutation['mutation_type'];
                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];
                    tmp['mutation_type']=mutation['mutation_type'];
                    tmp['used_']=mutation['used_'];
                    tmp['comment_']=mutation['comment_'];
                    mutation_ids_uniqueInfo.append(tmp);          
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['time_point']=time_points[sample_name_cnt]
                tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in mutation_data_O:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        break;
                data_O.append(tmp);
        # dump chart parameters to a js files
        data1_keys = [
                    #'experiment_id',
                    #'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    #'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Population mutation frequency", "chart1x1axislabel":"jump_time_point","chart1y1axislabel":"frequency"}
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"jump_time_point","svgy1axislabel":"frequency",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,1],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_mutationsAnnotated' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
    
    def export_dataStage01ResequencingHeatmap_js(self,analysis_id_I,data_dir_I="tmp"):
        """export heatmap to js file"""

        #get the heatmap data for the analysis
        data_O = self.stage01_resequencing_query.get_rows_analysisID_dataStage01ResequencingHeatmap(analysis_id_I);
        # dump chart parameters to a js files
        data1_keys = [
            'analysis_id',
                      'row_label','col_label','row_index','col_index','row_leaves','col_leaves',
                'col_pdist_metric','row_pdist_metric','col_linkage_method','row_linkage_method',
                'value_units']
        data1_nestkeys = ['analysis_id'];
        data1_keymap = {'xdata':'row_leaves','ydata':'col_leaves','zdata':'value',
                'rowslabel':'row_label','columnslabel':'col_label',
                'rowsindex':'row_index','columnsindex':'col_index',
                'rowsleaves':'row_leaves','columnsleaves':'col_leaves'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        svgparameters_O = {"svgtype":'heatmap2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                             'svgcellsize':18,'svgmargin':{ 'top': 200, 'right': 50, 'bottom': 100, 'left': 200 },
                            'svgcolorscale':'quantile',
                            'svgcolorcategory':'heatmap10',
                            'svgcolordomain':[0,1],
                            'svgcolordatalabel':'value',
                            'svgdatalisttileid':'tile1'};
        svgtileparameters_O = {'tileheader':'heatmap','tiletype':'svg','tileid':"tile2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_O.update(svgparameters_O);
        formtileparameters_O = {'tileheader':'filter menu','tiletype':'html','tileid':"tile1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"
            
            };
        formparameters_O = {'htmlid':'datalist1','htmltype':'datalist_01','datalist': [{'value':'hclust','text':'by cluster'},
                            {'value':'probecontrast','text':'by row and column'},
                            {'value':'probe','text':'by row'},
                            {'value':'contrast','text':'by column'},
                            {'value':'custom','text':'by value'}]}
        formtileparameters_O.update(formparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O];
        tile2datamap_O = {"tile1":[0],"tile2":[0]};
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_heatmap' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    def export_dataStage01ResequencingLineage_js(self,analysis_id_I,mutation_id_exclusion_list=[],data_dir_I="tmp"):
        '''export data_stage01_resequencing_lineage to js file'''

        #(self,analysis_id_I,mutation_id_exclusion_list=[],data_dir_I="tmp")
        
        print('exportingdataStage01ResequencingLineage...')
        # get the analysis information
        #analysis_info = {};
        #analysis_info = self.stage01_resequencing_query.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names,lineage_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        # get the lineage information
        lineage_data = [];
        lineage_data = self.stage01_resequencing_query.get_rowsIO_lineageName_dataStage01ResequencingLineage(lineage_names[0]);
        #for lineage in lineage_names:
        #    lineage_data_tmp = [];
        #    lineage_data_tmp = self.stage01_resequencing_query.get_rowsIO_lineageName_dataStage01ResequencingLineage(lineage);
        #    lineage_data.extend(lineage_data_tmp);
        mutation_ids = [x['mutation_id'] for x in lineage_data];
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in lineage_data:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    #tmp['mutation_id']=mutation['mutation_id']
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=mutation['mutation_genes'];
                    #tmp['mutation_position']=mutation['mutation_position'];
                    #tmp['mutation_annotations']=mutation['mutation_annotations'];
                    #tmp['mutation_locations']=mutation['mutation_locations'];
                    #tmp['mutation_links']=mutation['mutation_links'];
                    #tmp['mutation_type']=mutation['mutation_type'];
                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];
                    tmp['mutation_type']=mutation['mutation_type'];
                    tmp['used_']=True;
                    tmp['comment_']=None;
                    mutation_ids_uniqueInfo.append(tmp);          
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in lineage_data:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        break;
                data_O.append(tmp);
        # dump chart parameters to a js files
        data1_keys = [
                    #'experiment_id',
                    #'lineage_name',
                    'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    #'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"intermediate","svgy1axislabel":"frequency",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,1],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_lineage' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
        
    def export_dataStage01ResequencingMutationsAnnotated_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,data_dir_I="tmp"):
        '''export data_stage01_resequencing_mutationsAnnotated to js file'''
        
        print('exportingdataStage01ResequencingMutationsAnnotated...')
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        mutation_data_O = [];
        mutation_ids = [];
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
                mutation_id = mutation_genes_str + '_' + mutation['mutation_type'] + '_' + str(mutation['mutation_position'])
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids.append(mutation_id);
        # screen out mutations
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in mutation_data_O:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    #tmp['mutation_id']=mutation['mutation_id'].replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=str(mutation['mutation_genes']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_position']=str(mutation['mutation_position']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_annotations']=str(mutation['mutation_annotations']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_locations']=str(mutation['mutation_locations']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_links']=str(mutation['mutation_links']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_type']=str(mutation['mutation_type']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');

                    #tmp['mutation_id']=mutation['mutation_id'];
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=mutation['mutation_genes'];
                    #tmp['mutation_position']=mutation['mutation_position'];
                    #tmp['mutation_annotations']=mutation['mutation_annotations'];
                    #tmp['mutation_locations']=mutation['mutation_locations'];
                    #tmp['mutation_links']=mutation['mutation_links'];
                    #tmp['mutation_type']=mutation['mutation_type'];

                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];
                    tmp['mutation_type']=mutation['mutation_type'];
                    tmp['used_']=mutation['used_'];
                    tmp['comment_']=mutation['comment_'];
                    mutation_ids_uniqueInfo.append(tmp);     
                    break;    
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['time_point']=time_points[sample_name_cnt]
                tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in mutation_data_O:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        data_O.append(tmp);
                        break;
        # dump chart parameters to a js files
        data1_keys = [
                    #'experiment_id',
                    'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Population mutation frequency", "chart1x1axislabel":"jump_time_point","chart1y1axislabel":"frequency"}
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'table','tileid':"tile2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_mutationsAnnotated' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    def export_dataStage01ResequencingHeatmap_v1_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,data_dir_I="tmp"):
        """export heatmap to js file"""

        #get the heatmap data for the analysis
        data1_O = self.stage01_resequencing_query.get_rows_analysisID_dataStage01ResequencingHeatmap(analysis_id_I);
        # dump chart parameters to a js files
        data1_keys = [
            'analysis_id',
                      'row_label','col_label','row_index','col_index','row_leaves','col_leaves',
                'col_pdist_metric','row_pdist_metric','col_linkage_method','row_linkage_method',
                'value_units']
        data1_nestkeys = ['analysis_id'];
        data1_keymap = {'xdata':'row_leaves','ydata':'col_leaves','zdata':'value',
                'rowslabel':'row_label','columnslabel':'col_label',
                'rowsindex':'row_index','columnsindex':'col_index',
                'rowsleaves':'row_leaves','columnsleaves':'col_leaves'};
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        mutation_data_O = [];
        mutation_ids = [];
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
                mutation_id = mutation_genes_str + '_' + mutation['mutation_type'] + '_' + str(mutation['mutation_position'])
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids.append(mutation_id);
        # screen out mutations
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in mutation_data_O:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];
                    tmp['mutation_type']=mutation['mutation_type'];
                    tmp['used_']=mutation['used_'];
                    tmp['comment_']=mutation['comment_'];
                    mutation_ids_uniqueInfo.append(tmp);         
        data2_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['time_point']=time_points[sample_name_cnt]
                tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in mutation_data_O:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        break;
                data2_O.append(tmp);
        # dump chart parameters to a js files
        data2_keys = [
                    #'experiment_id',
                    'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data2_nestkeys = ['mutation_id'];
        data2_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        # make the data object
        dataobject_O = [{"data":data1_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data2_O,"datakeys":data2_keys,"datanestkeys":data2_nestkeys}];
        # make the tile parameter objects
        svgparameters_O = {"svgtype":'heatmap2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                             'svgcellsize':18,'svgmargin':{ 'top': 200, 'right': 50, 'bottom': 100, 'left': 200 },
                            'svgcolorscale':'quantile',
                            'svgcolorcategory':'heatmap10',
                            'svgcolordomain':[0,1],
                            'svgcolordatalabel':'value',
                            'svgdatalisttileid':'tile1'};
        svgtileparameters_O = {'tileheader':'heatmap','tiletype':'svg','tileid':"tile2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_O.update(svgparameters_O);
        datalisttileparameters_O = {'tileheader':'filter menu','tiletype':'html','tileid':"tile1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"
            
            };
        datalistparameters_O = {'htmlid':'datalist1','htmltype':'datalist_01','datalist': [{'value':'hclust','text':'by cluster'},
                            {'value':'probecontrast','text':'by row and column'},
                            {'value':'probe','text':'by row'},
                            {'value':'contrast','text':'by column'},
                            {'value':'custom','text':'by value'}]}
        datalisttileparameters_O.update(datalistparameters_O);
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'table','tileid':"tile4",'rowid':"row4",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [datalisttileparameters_O,svgtileparameters_O,formtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"tile1":[0],"tile2":[0],"filtermenu1":[1],"tile4":[1]};
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_heatmap' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    def export_dataStage01ResequencingAmplifications_v1_js(self,analysis_id_I,data_dir_I="tmp"):
        """export amplifications and statistics to js file"""

        # get the analysis info
        #analysis_info = {};
        #analysis_info = self.stage01_resequencing_query.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names,lineage_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        #get the data for the analysis
        data1_O = [];
        data2_O = [];
        data3_O = [];
        for sn_cnt,sn in enumerate(sample_names):
            data1_tmp = [];
            data1_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplifications_visualization(experiment_ids[sn_cnt],sn);
            data1_O.extend(data1_tmp);
            data2_tmp = [];
            data2_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationStats(experiment_ids[sn_cnt],sn);
            data2_O.extend(data2_tmp);
            data3_tmp = [];
            data3_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationAnnotations(experiment_ids[sn_cnt],sn);
            data3_O.extend(data3_tmp);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'sample_name',
                    'genome_chromosome',
                    'genome_strand',
                    'amplification_start',
                    'amplification_stop',
                    'sample_name_strand',
                    ]
        data1_nestkeys = [
                        #'sample_name',
                        'genome_strand'
                        ];
        data1_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'sample_name_strand',#custom for vis
                        #'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        data2_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                'strand_start',
                'strand_stop',
                'reads_min',
                'reads_max',
                'reads_lb',
                'reads_ub',
                'reads_iq1',
                'reads_iq3',
                'reads_median',
                'reads_mean',
                'reads_var',
                'reads_n',
                'amplification_start',
                'amplification_stop',
                'used_',
                'comment_'
                    ]
        data2_nestkeys = ['sample_name'];
        data2_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        data3_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                'strand_start',
                'strand_stop',
                'feature_annotations',
                'feature_genes',
                'feature_locations',
                'feature_links',
                'feature_start',
                'feature_stop',
                'feature_types',
                'amplification_start',
                'amplification_stop',
                'used_',
                'comment_'
                    ]
        data3_nestkeys = ['sample_name'];
        data3_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        # make the data object
        dataobject_O = [{"data":data1_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data2_O,"datakeys":data2_keys,"datanestkeys":data2_nestkeys},
                        {"data":data3_O,"datakeys":data3_keys,"datanestkeys":data3_nestkeys}
                        ];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"index","svgy1axislabel":"reads",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1',
                            "svgx1axistickformat":".2e",
                            "svgx1axisticktextattr":{"transform":"matrix(0,1,-1,0,16,6)",
                                                     #"transform":'rotate(90)',"transform":'translate(0,10)'
                                                     },
                            "svgx1axisticktextstyle":{"text-anchor":"start"}
                            };
        svgtileparameters_O = {'tileheader':'Amplifications','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Amplification statistics','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        tableparameters2_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters2_O = {'tileheader':'Amplification annotations','tiletype':'table','tileid':"tile4",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters2_O.update(tableparameters2_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O,tabletileparameters2_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,0],"tile3":[1],"tile4":[2]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_lineage' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    def export_dataStage01ResequencingAmplifications_js(self,analysis_id_I,data_dir_I="tmp"):
        """export amplifications and statistics to js file"""

        # get the analysis info
        #analysis_info = {};
        #analysis_info = self.stage01_resequencing_query.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names,lineage_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        #get the data for the analysis
        data1_O = [];
        data2_O = [];
        data3_O = [];
        for sn_cnt,sn in enumerate(sample_names):
            data1_tmp = [];
            data1_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplifications_visualization(experiment_ids[sn_cnt],sn);
            data1_O.extend(data1_tmp);
            data2_tmp = [];
            data2_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationStats(experiment_ids[sn_cnt],sn);
            data2_O.extend(data2_tmp);
            data3_tmp = [];
            data3_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationAnnotations(experiment_ids[sn_cnt],sn);
            data3_O.extend(data3_tmp);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'sample_name',
                    'genome_chromosome',
                    'genome_strand',
                    'amplification_start',
                    'amplification_stop',
                    'sample_name_strand',
                    ]
        data1_nestkeys = [
                        #'sample_name',
                        'genome_strand'
                        ];
        data1_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'sample_name_strand',#custom for vis
                        #'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        data2_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                #'reads_min',
                #'reads_max',
                #'reads_lb',
                #'reads_ub',
                #'reads_iq1',
                #'reads_iq3',
                #'reads_median',
                #'reads_mean',
                #'reads_var',
                #'reads_n',
                'amplification_start',
                'amplification_stop',
                    ]
        data2_nestkeys = ['sample_name'];
        data2_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        data3_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                'feature_annotations',
                'feature_genes',
                'feature_locations',
                'feature_links',
                'feature_start',
                'feature_stop',
                'feature_types',
                'amplification_start',
                'amplification_stop',
                    ]
        data3_nestkeys = ['sample_name'];
        data3_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        # make the data object
        dataobject_O = [{"data":data1_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data2_O,"datakeys":data2_keys,"datanestkeys":data2_nestkeys},
                        {"data":data3_O,"datakeys":data3_keys,"datanestkeys":data3_nestkeys}
                        ];
        # make the tile parameter objects
        # linked set #1
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"index","svgy1axislabel":"reads",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1',
                            "svgx1axistickformat":".2e",
                            "svgx1axisticktextattr":{"transform":"matrix(0,1,-1,0,16,6)",
                                                     #"transform":'rotate(90)',"transform":'translate(0,10)'
                                                     },
                            "svgx1axisticktextstyle":{"text-anchor":"start"}
                            };
        svgtileparameters_O = {'tileheader':'Amplifications','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        # linked set #2
        formtileparameters2_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters2_O = {'htmlid':'filtermenuform2',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit2','text':'submit'},"formresetbuttonidtext":{'id':'reset2','text':'reset'},"formupdatebuttonidtext":{'id':'update2','text':'update'}};
        formtileparameters2_O.update(formparameters2_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu2','tableresetbuttonid':'reset2','tablesubmitbuttonid':'submit2'};
        tabletileparameters_O = {'tileheader':'Amplification statistics','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        # linked set #3
        formtileparameters3_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu3",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters3_O = {'htmlid':'filtermenuform3',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit3','text':'submit'},"formresetbuttonidtext":{'id':'reset3','text':'reset'},"formupdatebuttonidtext":{'id':'update3','text':'update'}};
        formtileparameters3_O.update(formparameters3_O);
        tableparameters2_O = {"tabletype":'responsivetable_01',
                    'tableid':'table2',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu3','tableresetbuttonid':'reset3','tablesubmitbuttonid':'submit3'};
        tabletileparameters2_O = {'tileheader':'Amplification annotations','tiletype':'table','tileid':"tile4",'rowid':"row3",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters2_O.update(tableparameters2_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,formtileparameters2_O,tabletileparameters_O,formtileparameters3_O,tabletileparameters2_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,0],"tile3":[1],"tile4":[2],"filtermenu2":[1],"filtermenu3":[2]};
        filtermenuobject_O = [{"filtermenuid":"filtermenu1","filtermenuhtmlid":"filtermenuform1",
                "filtermenusubmitbuttonid":"submit1","filtermenuresetbuttonid":"reset1",
                "filtermenuupdatebuttonid":"update1"},{"filtermenuid":"filtermenu2","filtermenuhtmlid":"filtermenuform2",
                "filtermenusubmitbuttonid":"submit2","filtermenuresetbuttonid":"reset2",
                "filtermenuupdatebuttonid":"update2"},{"filtermenuid":"filtermenu3","filtermenuhtmlid":"filtermenuform3",
                "filtermenusubmitbuttonid":"submit3","filtermenuresetbuttonid":"reset3",
                "filtermenuupdatebuttonid":"update3"}];
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        filtermenu_str = 'var ' + 'filtermenu' + ' = ' + json.dumps(filtermenuobject_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_lineage' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str + '\n' + filtermenu_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
            file.write(filtermenu_str);

    def export_dataStage01ResequencingCoverage_js(self,analysis_id_I,data_dir_I="tmp"):
        """export heatmap to js file"""

        # get the analysis info
        #analysis_info = {};
        #analysis_info = self.stage01_resequencing_query.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.stage01_resequencing_query.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names,lineage_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        #get the data for the analysis
        data1_O = [];
        data2_O = [];
        for sn_cnt,sn in enumerate(sample_names):
            data1_tmp = [];
            data1_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverage_visualization(experiment_ids[sn_cnt],sn);
            data1_O.extend(data1_tmp);
            data2_tmp = [];
            data2_tmp = self.stage01_resequencing_query.get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverageStats(experiment_ids[sn_cnt],sn);
            data2_O.extend(data2_tmp);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'sample_name',
                    'genome_chromosome',
                    'genome_strand',
                    'sample_name_strand'
                    ]
        data1_nestkeys = [
                        #'sample_name',
                        'genome_strand'
                        ];
        data1_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'sample_name_strand',#custom for vis
                        'featureslabel':'reads'};
        data2_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                #'strand_start',
                #'strand_stop',
                #'reads_min',
                #'reads_max',
                #'reads_lb',
                #'reads_ub',
                #'reads_iq1',
                #'reads_iq3',
                #'reads_median',
                #'reads_mean',
                #'reads_var',
                #'reads_n',
                'amplification_start',
                'amplification_stop',
                'used_',
                'comment_'
                    ]
        data2_nestkeys = ['sample_name'];
        data2_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        # make the data object
        dataobject_O = [{"data":data1_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data2_O,"datakeys":data2_keys,"datanestkeys":data2_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"index","svgy1axislabel":"reads",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1',
                            "svgx1axistickformat":".2e",
                            "svgx1axisticktextattr":{"transform":"matrix(0,1,-1,0,16,6)",
                                                     #"transform":'rotate(90)',"transform":'translate(0,10)'
                                                     },
                            "svgx1axisticktextstyle":{"text-anchor":"start"}
                            };
        svgtileparameters_O = {'tileheader':'Resequencing coverage','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Resequencing coverage statistics','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,0],"tile3":[1]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_resequencing_lineage' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    #Deprecated:
    def export_dataStage01ResequencingLineage_d3(self, experiment_id, lineage_names,
                                                 filename='visualization/data/ALEsKOs01/resequencing/heatmap/data.js',
                                                 json_var_name='data',
                                                 mutation_id_exclusion_list = []):
        '''Export data for viewing using d3'''
        #Input:
        #   experiment_id
        #   lineage_names = list of lineage_names to export
        #Output:
        #   
        
        intermediates_lineage = [];
        mutation_data_lineage_all = [];
        rows_lineage = [];
        n_lineages = len(lineage_names)
        cnt_sample_names = 0;
        for lineage_name in lineage_names:
            ## get ALL sample names by experiment_id and lineage name
            #sample_names = [];
            #sample_names = self.stage01_resequencing_query.get_sampleNames_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_id,lineage_name);
            # get ALL intermediates by experiment_id and lineage name
            intermediates = [];
            intermediates = self.stage01_resequencing_query.get_intermediates_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_id,lineage_name);
            intermediates_lineage.append(intermediates);
            cnt_sample_names += len(intermediates)
            # get ALL mutation data by experiment_id and lineage name
            mutation_data = [];
            mutation_data = self.stage01_resequencing_query.get_mutationData_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_id,lineage_name);
            mutation_data_lineage_all.extend(mutation_data);
            # get ALL mutation frequencies by experiment_id and lineage name
            rows = [];
            rows = self.stage01_resequencing_query.get_row_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_id,lineage_name)
            rows_lineage.extend(rows);
        mutation_data_lineage_unique = list(set(mutation_data_lineage_all));
        mutation_data_lineage = [x for x in mutation_data_lineage_unique if not x in mutation_id_exclusion_list];
        min_inter = min(intermediates_lineage)
        max_inter = max(intermediates_lineage);
        # generate the frequency matrix data structure (mutation x intermediate)
        data_O = numpy.zeros((cnt_sample_names,len(mutation_data_lineage)));
        labels_O = {};
        labels_O['lineage']=[];
        col_cnt = 0;
        # order 2: groups each lineage by mutation (intermediate x mutation)
        for lineage_name_cnt,lineage_name in enumerate(lineage_names): #all lineages for intermediate j / mutation i
            for intermediate_cnt,intermediate in enumerate(intermediates_lineage[lineage_name_cnt]):
                if intermediate_cnt == min(intermediates_lineage[lineage_name_cnt]):
                    labels_O['lineage'].append(lineage_name+": "+"start"); # corresponding label from hierarchical clustering (in this case, arbitrary)
                elif intermediate_cnt == max(intermediates_lineage[lineage_name_cnt]):
                    labels_O['lineage'].append(lineage_name+": "+"end"); # corresponding label from hierarchical clustering (in this case, arbitrary)
                else:
                    labels_O['lineage'].append(lineage_name+": "+str(intermediate)); # corresponding label from hierarchical clustering (in this case, arbitrary)
                for mutation_cnt,mutation in enumerate(mutation_data_lineage): #all mutations i for intermediate j
                    for row in rows_lineage:
                        if row['mutation_id'] == mutation and row['intermediate'] == intermediate and row['lineage_name'] == lineage_name:
                            data_O[col_cnt,mutation_cnt] = row['mutation_frequency'];
                            print(col_cnt,mutation_cnt)
                col_cnt+=1;
        # generate the clustering for the heatmap
        json_O = {};
        json_O = self.calculate.heatmap(data_O,labels_O['lineage'],mutation_data_lineage);
        options_O = {};
        options_O['row_axis_label'] = 'lineage_id';
        options_O['col_axis_label'] = 'mutation_id';
        options_O['value_label'] = 'population frequency';
        options_O['domain'] = '2';
        json_O.update(labels_O);
        json_O['options'] = options_O;
        # dump the data to a json file
        json_str = 'var ' + json_var_name + ' = ' + json.dumps(json_O);
        with open(filename,'w') as file:
            file.write(json_str);

    def export_dataStage01ResequencingMutationsAnnotated_d3(self,experiment_id,strain_lineage,mutation_id_exclusion_list=[],frequency_threshold=0.1):
        '''Plot the mutation frequency accross the strain lineage for all filtered mutations'''
        
        print('Executing plotMutationFrequency_population...')
        for analysis_id,strain in strain_lineage.items():
            print('analyzing lineage ' + analysis_id);
            intermediates = list(strain.keys());
            intermediates.sort();
            mutation_data_O = [];
            mutation_ids = [];
            for intermediate in intermediates:
                print('analyzing intermediate ' + str(intermediate));
                # query mutation data:
                mutations = [];
                mutations = self.stage01_resequencing_query.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_id,strain[intermediate]);
                for end_cnt,mutation in enumerate(mutations):
                    print('analyzing mutations')
                    if mutation['mutation_position'] > 4000000: #ignore positions great than 4000000
                        continue;
                    if mutation['mutation_frequency']<frequency_threshold:
                        continue;
                    # mutation id
                    mutation_genes_str = '';
                    for gene in mutation['mutation_genes']:
                        mutation_genes_str = mutation_genes_str + gene + '-/-'
                    mutation_genes_str = mutation_genes_str[:-3];
                    mutation_id = mutation_genes_str + '_' + mutation['mutation_type'] + '_' + str(mutation['mutation_position'])
                    tmp = {};
                    tmp.update(mutation);
                    tmp.update({'mutation_id':mutation_id});
                    mutation_data_O.append(tmp);
                    mutation_ids.append(mutation_id);
            mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
            mutation_ids_unique = list(set(mutation_ids_screened));
            data_O = [];
            data_fitted_O = [];
            for intermediate in intermediates:
                for mutation_id in mutation_ids_unique:
                    tmp = {};
                    tmp_fitted = {};
                    tmp['samples']=mutation_id
                    tmp['x_data']=intermediate
                    tmp['y_data']=0.0;
                    tmp_fitted['samples']=mutation_id
                    tmp_fitted['x_data_fitted']=intermediate
                    tmp_fitted['y_data_fitted']=0.0;
                    for mutation in mutation_data_O:
                        if strain[intermediate] == mutation['sample_name'] and mutation_id == mutation['mutation_id']:
                            tmp['y_data']=mutation['mutation_frequency'];
                            tmp_fitted['y_data_fitted']=mutation['mutation_frequency'];
                            break;
                    data_O.append(tmp);
                    data_fitted_O.append(tmp_fitted);
            #Update js variable
            options_O = {};
            options_O['x_axis'] = [];
            options_O['y_axis'] = [];
            options_O['x_axis_label'] = 'lineage';
            options_O['y_axis_label'] = 'frequency';
            options_O['feature_name'] = 'mutation';
            options_O['fit_function'] = 'linear';
            json_O = {};
            json_O['data'] = data_O;
            json_O['data_fitted'] = data_fitted_O;
            json_O['options'] = options_O;
            # dump the data to a json file
            json_str = 'var ' + 'data' + ' = ' + json.dumps(json_O);
            filename_str = 'visualization/data/' + experiment_id + '/resequencing/scatterlineplot/' + analysis_id + '.js'
            with open(filename_str,'w') as file:
                file.write(json_str);
  
  