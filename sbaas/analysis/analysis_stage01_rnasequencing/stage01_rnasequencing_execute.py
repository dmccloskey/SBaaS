'''rnasequencing class'''
from copy import copy
from sbaas.analysis.analysis_base import *
from .stage01_rnasequencing_query import *
from .stage01_rnasequencing_io import *

# resources

from sequencing_analysis.fpkms_heatmap import fpkms_heatmap
from sequencing_analysis.gff_coverage import gff_coverage
from sequencing_analysis.genome_annotations import genome_annotations

class stage01_rnasequencing_execute():
    '''class for rnasequencing analysis'''
    def __init__(self,session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage01_rnasequencing_query = stage01_rnasequencing_query(self.session);
        self.stage01_rnasequencing_io = stage01_rnasequencing_io(self.session);
        self.calculate = base_calculate();
    #analysis
    def execute_heatmap(self, analysis_id_I,gene_exclusion_list=[],
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete'):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');
        fpkmsheatmap =  fpkms_heatmap();
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.stage01_rnasequencing_query.get_experimentIDAndSampleName_analysisID_dataStage01RNASequencingAnalysis(analysis_id_I);
        fpkms_all = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query fpkm data:
            fpkms = [];
            fpkms = self.stage01_rnasequencing_query.get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesFpkmTracking(experiment_ids[sample_name_cnt],sample_name);
            fpkms_all.extend(fpkms);
        fpkmsheatmap.genesFpkmTracking = fpkms_all;
        fpkmsheatmap.sample_names = sample_names;
        fpkmsheatmap.make_heatmap(gene_exclusion_list=gene_exclusion_list,
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I)
        heatmap_O = fpkmsheatmap.heatmap;
        dendrogram_col_O = fpkmsheatmap.dendrogram_col;
        dendrogram_row_O = fpkmsheatmap.dendrogram_row;
        # add data to to the database for the heatmap
        for d in heatmap_O:
            row = None;
            row = data_stage01_rnasequencing_heatmap(
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
                'fpkm',True, None);
            self.session.add(row);
        ## add data to the database for the dendrograms
        #row = None;
        #row = data_stage01_rnasequencing_dendrogram(
        #    analysis_id_I,
        #    dendrogram_col_O['leaves'],
        #    dendrogram_col_O['icoord'],
        #    dendrogram_col_O['dcoord'],
        #    dendrogram_col_O['ivl'],
        #    dendrogram_col_O['colors'],
        #    dendrogram_col_O['pdist_metric'],
        #    dendrogram_col_O['pdist_metric'],
        #    'fpkm',True, None);
        #self.session.add(row);
        #row = None;
        #row = data_stage01_rnasequencing_dendrogram(
        #    analysis_id_I,
        #    dendrogram_row_O['leaves'],
        #    dendrogram_row_O['icoord'],
        #    dendrogram_row_O['dcoord'],
        #    dendrogram_row_O['ivl'],
        #    dendrogram_row_O['colors'],
        #    dendrogram_row_O['pdist_metric'],
        #    dendrogram_row_O['pdist_metric'],
        #    'fpkm',True, None);
        #self.session.add(row);
        self.session.commit();
    #table initializations:
    def drop_dataStage01(self):
        try:
            data_stage01_rnasequencing_analysis.__table__.drop(engine,True);
            data_stage01_rnasequencing_heatmap.__table__.drop(engine,True);
            data_stage01_rnasequencing_dendrogram.__table__.drop(engine,True);
            data_stage01_rnasequencing_genesFpkmTracking.__table__.drop(engine,True);
            data_stage01_rnasequencing_geneExpDiff.__table__.drop(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01(self):
        try:
            data_stage01_rnasequencing_analysis.__table__.create(engine,True);
            data_stage01_rnasequencing_heatmap.__table__.create(engine,True);
            data_stage01_rnasequencing_dendrogram.__table__.create(engine,True);
            data_stage01_rnasequencing_genesFpkmTracking.__table__.create(engine,True);
            data_stage01_rnasequencing_geneExpDiff.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01(self,experiment_id_I = None,analysis_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_rnasequencing_geneExpDiff).filter(data_stage01_rnasequencing_geneExpDiff.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            elif analysis_id_I:
                reset = self.session.query(data_stage01_rnasequencing_analysis).filter(data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_analysis).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_fpkmsAnnotated(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_rnasequencing_fpkmsAnnotated).filter(data_stage01_rnasequencing_fpkmsAnnotated.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_fpkmsAnnotated).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_rnasequencing_heatmap(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_rnasequencing_heatmap).filter(data_stage01_rnasequencing_heatmap.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_heatmap).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_rnasequencing_dendrogram(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_rnasequencing_dendrogram).filter(data_stage01_rnasequencing_dendrogram.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_dendrogram).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_rnasequencing_genesFpkmTracking(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(
                        data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I),
                        data_stage01_rnasequencing_genesFpkmTracking.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_rnasequencing_geneExpDiff(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_rnasequencing_geneExpDiff).filter(data_stage01_rnasequencing_geneExpDiff.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_geneExpDiff).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
