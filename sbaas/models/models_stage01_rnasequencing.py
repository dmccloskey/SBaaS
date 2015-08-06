# ORMs
from .models_base import *
from sqlalchemy.orm import relationship

# ORM classes
class data_stage01_rnasequencing_analysis(Base):
    __tablename__ = 'data_stage01_rnasequencing_analysis'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_analysis_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(500)) # equivalent to sample_name_abbreviation
    sample_name = Column(String(500)) # equivalent to sample_name_abbreviation
    time_point = Column(String(10)) # converted to intermediate in lineage analysis
    analysis_type = Column(String(100)); # time-course (i.e., multiple time points), paired (i.e., control compared to multiple replicates), group (i.e., single grouping of samples).
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name_abbreviation','sample_name','time_point','analysis_type','analysis_id'),
            )

    def __init__(self,analysis_id_I,
                 experiment_id_I,
            sample_name_abbreviation_I,
            sample_name_I,
            time_point_I,
            analysis_type_I,
            used__I,
            comment__I):
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.sample_name=sample_name_I
        self.time_point=time_point_I
        self.analysis_type=analysis_type_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
            'experiment_id':self.experiment_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'sample_name':self.sample_name,
            'time_point':self.time_point,
            'analysis_type':self.analysis_type,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_rnasequencing_dendrogram(Base):
    __tablename__ = 'data_stage01_rnasequencing_dendrogram'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_dendrogram_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    leaves = Column(postgresql.ARRAY(Float))
    icoord = Column(postgresql.JSON)
    dcoord = Column(postgresql.JSON)
    ivl = Column(postgresql.ARRAY(String(100)))
    colors = Column(postgresql.ARRAY(String(25)))
    pdist_metric = Column(String(100))
    linkage_method = Column(String(100))
    value_units = Column(String(50))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('analysis_id','ivl','pdist_metric','linkage_method','value_units'),
            )

    def __init__(self,analysis_id_I,
                leaves_I,
                icoord_I,
                dcoord_I,
                ivl_I,
                colors_I,
                pdist_metric_I,
                linkage_method_I,
                value_units_I,
                used__I,
                comment__I):
        self.analysis_id=analysis_id_I
        self.leaves=leaves_I
        self.icoord=icoord_I
        self.dcoord=dcoord_I
        self.ivl=ivl_I
        self.colors=colors_I
        self.pdist_metric=pdist_metric_I
        self.linkage_method=linkage_method_I
        self.value_units = value_units_I;
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
            'leaves':self.leaves,
            'icoord':self.icoord,
            'dcoord':self.dcoord,
            'ivl':self.ivl,
            'colors':self.ivl,
            'pdist_metric':self.pdist_metric,
            'linkage_method':self.linkage_method,
            'value_units':self.value_units,
            'used_':self.used_,
            'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__());

class data_stage01_rnasequencing_heatmap(Base):
    __tablename__ = 'data_stage01_rnasequencing_heatmap'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_heatmap_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    col_index = Column(Integer)
    row_index = Column(Integer)
    value = Column(Float)
    col_leaves = Column(Integer)
    row_leaves = Column(Integer)
    col_label = Column(String(100))
    row_label = Column(String(100))
    col_pdist_metric = Column(String(100))
    row_pdist_metric = Column(String(100))
    col_linkage_method = Column(String(100))
    row_linkage_method = Column(String(100))
    value_units = Column(String(50))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (#UniqueConstraint('experiment_id','sample_name_short','time_point','component_name'),
                      UniqueConstraint('analysis_id','col_label','row_label','col_pdist_metric','row_pdist_metric','col_linkage_method','row_linkage_method','value_units'),
            )

    def __init__(self,analysis_id_I,
                col_index_I,
                row_index_I,
                value_I,
                col_leaves_I,
                row_leaves_I,
                col_label_I,
                row_label_I,
                col_pdist_metric_I,
                row_pdist_metric_I,
                col_linkage_method_I,
                row_linkage_method_I,
                value_units_I,
                used__I,
                comment__I):
        self.analysis_id=analysis_id_I
        self.col_index=col_index_I
        self.row_index=row_index_I
        self.value=value_I
        self.col_leaves=col_leaves_I
        self.row_leaves=row_leaves_I
        self.col_label=col_label_I
        self.row_label=row_label_I
        self.col_pdist_metric=col_pdist_metric_I
        self.row_pdist_metric=row_pdist_metric_I
        self.col_linkage_method=col_linkage_method_I
        self.row_linkage_method=row_linkage_method_I
        self.value_units = value_units_I;
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self): 
        return {'id':self.id,
                'analysis_id':self.analysis_id,
            'col_index':self.col_index,
            'row_index':self.row_index,
            'value':self.value,
            'col_leaves':self.col_leaves,
            'row_leaves':self.row_leaves,
            'col_label':self.col_label,
            'row_label':self.row_label,
            'col_pdist_metric':self.col_pdist_metric,
            'row_pdist_metric':self.row_pdist_metric,
            'col_linkage_method':self.col_linkage_method,
            'row_linkage_method':self.row_linkage_method,
            'value_units':self.value_units,
            'used_':self.used_,
            'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__());

class data_stage01_rnasequencing_genesFpkmTracking(Base):
    #fpkm = fragments per kilobase of transcript
    __tablename__ = 'data_stage01_rnasequencing_genesFpkmTracking'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_genesFpkmTracking_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    tracking_id = Column(String(100))
    class_code = Column(String(100))
    nearest_ref_id = Column(String(100))
    gene_id = Column(String(100))
    gene_short_name = Column(String(100))
    tss_id = Column(String(100))
    locus = Column(String(100))
    length = Column(Float);
    coverage = Column(Float);
    FPKM = Column(Float);
    FPKM_conf_lo = Column(Float);
    FPKM_conf_hi = Column(Float);
    FPKM_status = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id','sample_name','gene_id'
                         ),
            )

    def __init__(self,
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        tracking_id_I,
        class_code_I,
        nearest_ref_id_I,
        gene_id_I,
        gene_short_name_I,
        tss_id_I,
        locus_I,
        length_I,
        coverage_I,
        FPKM_I,
        FPKM_conf_lo_I,
        FPKM_conf_hi_I,
        FPKM_status_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.tracking_id=tracking_id_I
        self.class_code=class_code_I
        self.nearest_ref_id=nearest_ref_id_I
        self.gene_id=gene_id_I
        self.gene_short_name=gene_short_name_I
        self.tss_id=tss_id_I
        self.locus=locus_I
        self.length=length_I
        self.coverage=coverage_I
        self.FPKM=FPKM_I
        self.FPKM_conf_lo=FPKM_conf_lo_I
        self.FPKM_conf_hi=FPKM_conf_hi_I
        self.FPKM_status=FPKM_status_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'tracking_id':self.tracking_id,
                'class_code':self.class_code,
                'nearest_ref_id':self.nearest_ref_id,
                'gene_id':self.gene_id,
                'gene_short_name':self.gene_short_name,
                'tss_id':self.tss_id,
                'locus':self.locus,
                'length':self.length,
                'coverage':self.coverage,
                'FPKM':self.FPKM,
                'FPKM_conf_lo':self.FPKM_conf_lo,
                'FPKM_conf_hi':self.FPKM_conf_hi,
                'FPKM_status':self.FPKM_status,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_rnasequencing_geneExpDiff(Base):
    
    __tablename__ = 'data_stage01_rnasequencing_geneExpDif'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_geneExpDif_id_seq'), primary_key=True)
    experiment_id_1 = Column(String(50))
    experiment_id_2 = Column(String(50))
    sample_name_abbreviation_1 = Column(String(100))
    sample_name_abbreviation_2 = Column(String(100))
    test_id = Column(String(100))
    gene_id = Column(String(100))
    gene = Column(String(100))
    sample_1 = Column(String(100))
    sample_2 = Column(String(100))
    status = Column(String(100))
    value_1 = Column(Float);
    value_2 = Column(Float);
    fold_change_log2 = Column(Float);
    test_stat = Column(String(100))
    p_value = Column(Float); # uncorrected p-value
    q_value = Column(Float); # FDR corrected p-value
    significant = Column(String(100)) #Yes/No
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id_1','experiment_id_2','sample_name_abbreviation_1','sample_name_abbreviation_2','gene_id'
                         ),
            )

    def __init__(self,
        experiment_id_1_I,
        experiment_id_2_I,
        sample_name_abbreviation_1_I,
        sample_name_abbreviation_2_I,
        test_id_I,
        gene_id_I,
        gene_I,
        sample_1_I,
        sample_2_I,
        status_I,
        value_1_I,
        value_2_I,
        fold_change_log2_I,
        test_stat_I,
        p_value_I,
        q_value_I,
        significant_I,
        used__I,
        comment__I):
        self.experiment_id_1=experiment_id_1_I
        self.experiment_id_2=experiment_id_2_I
        self.sample_name_abbreviation_1=sample_name_abbreviation_1_I
        self.sample_name_abbreviation_2=sample_name_abbreviation_2_I
        self.test_id=test_id_I
        self.gene_id=gene_id_I
        self.gene=gene_I
        self.sample_1=sample_1_I
        self.sample_2=sample_2_I
        self.status=status_I
        self.value_1=value_1_I
        self.value_2=value_2_I
        self.fold_change_log2=fold_change_log2_I
        self.test_stat=test_stat_I
        self.p_value=p_value_I
        self.q_value=q_value_I
        self.significant=significant_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id_1':self.experiment_id_1,
                'experiment_id_2':self.experiment_id_2,
                'sample_name_abbreviation_1':self.sample_name_abbreviation_1,
                'sample_name_abbreviation_2':self.sample_name_abbreviation_2,
                'test_id':self.test_id,
                'gene_id':self.gene_id,
                'gene':self.gene,
                'sample_1':self.sample_1,
                'sample_2':self.sample_2,
                'status':self.status,
                'value_1':self.value_1,
                'value_2':self.value_2,
                'fold_change_log2':self.fold_change_log2,
                'test_stat':self.test_stat,
                'p_value':self.p_value,
                'q_value':self.q_value,
                'significant':self.significant,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())