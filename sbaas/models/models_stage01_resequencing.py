# ORMs
from .models_base import *
from sqlalchemy.orm import relationship

# ORM classes
class data_stage01_resequencing_metadata(Base):
    
    __tablename__ = 'data_stage01_resequencing_metadata'
    id = Column(Integer, Sequence('data_stage01_resequencing_metadata_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100), unique=True)
    genome_diff = Column(Float)
    refseq = Column(String(500))
    readseq = Column(postgresql.ARRAY(String(500)))
    author = Column(String(100))

    def __init__(self, experiment_id_I,
            sample_name_I,
            genome_diff_I,
            refseq_I,
            readseq_I,
            author_I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_diff=genome_diff_I
        self.refseq=refseq_I
        self.readseq=readseq_I
        self.author=author_I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_diff':self.genome_diff,
                'refseq':self.refseq,
                'readseq':self.readseq,
                'author':self.author
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_resequencing_mutations(Base):
    
    __tablename__ = 'data_stage01_resequencing_mutations'
    id = Column(Integer, Sequence('data_stage01_resequencing_mutations_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    mutation_id = Column(Integer)
    parent_ids = Column(postgresql.ARRAY(Integer))
    mutation_data = Column(postgresql.JSON)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','mutation_id'),
            )

    def __init__(self, experiment_id_I,
                sample_name_I,
                mutation_id_I,
                parent_ids_I,
                mutation_data_I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.mutation_id=mutation_id_I
        self.parent_ids=parent_ids_I
        self.mutation_data=mutation_data_I

    def __repr__dict__(self):
        return {'experiment_id_I':self.experiment_id,
                'sample_name_I':self.sample_name,
                #TODO
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_evidence(Base):
    
    __tablename__ = 'data_stage01_resequencing_evidence'
    id = Column(Integer, Sequence('data_stage01_resequencing_evidence_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    parent_id = Column(Integer)
    evidence_data = Column(postgresql.JSON)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','parent_id'),
            )

    def __init__(self, experiment_id_I,
            sample_name_I,
            parent_id_I,
            evidence_data_I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.parent_id=parent_id_I
        self.evidence_data=evidence_data_I

    def __repr__dict__(self):
        return {'experiment_id_I':self.experiment_id,
                'sample_name_I':self.sample_name,
                #TODO
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_validation(Base):
    
    __tablename__ = 'data_stage01_resequencing_validation'
    id = Column(Integer, Sequence('data_stage01_resequencing_validation_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    validation_id = Column(Integer)
    validation_data = Column(postgresql.JSON)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','validation_id'),
            )

    def __init__(self, experiment_id_I,
            sample_name_I,
            validation_id_I,
            validation_data_I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.validation_id=validation_id_I
        self.validation_data=validation_data_I

    def __repr__dict__(self):
        return {'experiment_id_I':self.experiment_id,
                'sample_name_I':self.sample_name,
                #TODO
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_resequencing_mutationsFiltered(Base):
    
    __tablename__ = 'data_stage01_resequencing_mutationsFiltered'
    id = Column(Integer, Sequence('data_stage01_resequencing_mutationsFiltered_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    mutation_id = Column(Integer)
    parent_ids = Column(postgresql.ARRAY(Integer))
    mutation_data = Column(postgresql.JSON)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','mutation_id'),
            )

    def __init__(self, experiment_id_I,
                sample_name_I,
                mutation_id_I,
                parent_ids_I,
                mutation_data_I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.mutation_id=mutation_id_I
        self.parent_ids=parent_ids_I
        self.mutation_data=mutation_data_I

    def __repr__dict__(self):
        return {'experiment_id_I':self.experiment_id,
                'sample_name_I':self.sample_name,
                #TODO
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_resequencing_lineage(Base):
    #TODO: rename to _timecourse
    __tablename__ = 'data_stage01_resequencing_lineage'
    id = Column(Integer, Sequence('data_stage01_resequencing_lineage_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    lineage_name = Column(String(500)) #lineage_name
    sample_name = Column(String(100))
    intermediate = Column(Integer)
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_position = Column(Integer)
    mutation_data = Column(postgresql.JSON)
    mutation_annotations = Column(postgresql.ARRAY(String(500)))
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    mutation_links = Column(postgresql.ARRAY(String(500)))
    comment_ = Column(Text)

    __table_args__ = (UniqueConstraint('lineage_name','experiment_id','sample_name','intermediate'),
            )

    def __init__(self, 
                experiment_id_I,
                lineage_name_I,
                sample_name_I,
                intermediate_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_position_I,
                mutation_data_I,
                mutation_annotations_I,
                mutation_genes_I,
                mutation_locations_I,
                mutation_links_I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.lineage_name=lineage_name_I
        self.sample_name=sample_name_I
        self.intermediate=intermediate_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_position=mutation_position_I
        self.mutation_data=mutation_data_I
        self.mutation_annotations=mutation_annotations_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.mutation_links=mutation_links_I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'lineage_name':self.lineage_name,
                'sample_name':self.sample_name,
                'intermediate':self.intermediate,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_position':self.mutation_position,
                'mutation_data':self.mutation_data,
                'mutation_annotations':self.mutation_annotations,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'mutation_links':self.mutation_links,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_resequencing_endpoints(Base):
    #TODO: rename to _group
    __tablename__ = 'data_stage01_resequencing_endpoints'
    id = Column(Integer, Sequence('data_stage01_resequencing_endpoints_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    analysis_id = Column(String(500))
    sample_name = Column(String(100))
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_position = Column(Integer)
    mutation_data = Column(postgresql.JSON)
    isUnique = Column(Boolean)
    mutation_annotations = Column(postgresql.ARRAY(String(500)))
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    mutation_links = Column(postgresql.ARRAY(String(500)))
    comment_ = Column(Text)

    __table_args__ = (UniqueConstraint('analysis_id','experiment_id','sample_name'),
            )

    def __init__(self, experiment_id_I,
                analysis_id_I,
                sample_name_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_position_I,
                mutation_data_I,
                isUnique_I,
                mutation_annotations_I,
                mutation_genes_I,
                mutation_locations_I,
                mutation_links_I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.analysis_id=analysis_id_I
        self.sample_name=sample_name_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_position=mutation_position_I
        self.mutation_data=mutation_data_I
        self.isUnique=isUnique_I
        self.mutation_annotations=mutation_annotations_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.mutation_links=mutation_links_I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'analysis_id':self.analysis_id,
                'sample_name':self.sample_name,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_position':self.mutation_position,
                'mutation_data':self.mutation_data,
                'isUnique':self.isUnique,
                'mutation_annotations':self.mutation_annotations,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'mutation_links':self.mutation_links,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_mutationsAnnotated(Base):
    __tablename__ = 'data_stage01_resequencing_mutationsAnnotated'
    id = Column(Integer, Sequence('data_stage01_resequencing_mutationsAnnotated_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_position = Column(Integer)
    mutation_data = Column(postgresql.JSON)
    mutation_annotations = Column(postgresql.ARRAY(String(500)))
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    mutation_links = Column(postgresql.ARRAY(String(500)))
    used_ = Column(Boolean)
    comment_ = Column(Text)

    def __init__(self, experiment_id_I,
                sample_name_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_position_I,
                mutation_data_I,
                mutation_annotations_I,
                mutation_genes_I,
                mutation_locations_I,
                mutation_links_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_position=mutation_position_I
        self.mutation_data=mutation_data_I
        self.mutation_annotations=mutation_annotations_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.mutation_links=mutation_links_I
        self.used_ = used__I;
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_position':self.mutation_position,
                'mutation_data':self.mutation_data,
                'mutation_annotations':self.mutation_annotations,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'mutation_links':self.mutation_links,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_analysis(Base):
    __tablename__ = 'data_stage01_resequencing_analysis'
    id = Column(Integer, Sequence('data_stage01_resequencing_analysis_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    lineage_name = Column(String(500)) # equivalent to sample_name_abbreviation
    sample_name = Column(String(500)) # equivalent to sample_name_abbreviation
    time_point = Column(String(10)) # converted to intermediate in lineage analysis
    analysis_type = Column(String(100)); # time-course (i.e., multiple time points), paired (i.e., control compared to multiple replicates), group (i.e., single grouping of samples).
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','lineage_name','sample_name','time_point','analysis_type','analysis_id'),
            )

    def __init__(self,analysis_id_I,
                 experiment_id_I,
            lineage_name_I,
            sample_name_I,
            time_point_I,
            analysis_type_I,
            used__I,
            comment__I):
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.lineage_name=lineage_name_I
        self.sample_name=sample_name_I
        self.time_point=time_point_I
        self.analysis_type=analysis_type_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
            'experiment_id':self.experiment_id,
            'lineage_name':self.lineage_name,
            'sample_name':self.sample_name,
            'time_point':self.time_point,
            'analysis_type':self.analysis_type,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_dendrogram(Base):
    __tablename__ = 'data_stage01_resequencing_dendrogram'
    id = Column(Integer, Sequence('data_stage01_resequencing_dendrogram_id_seq'), primary_key=True)
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

class data_stage01_resequencing_heatmap(Base):
    __tablename__ = 'data_stage01_resequencing_heatmap'
    id = Column(Integer, Sequence('data_stage01_resequencing_heatmap_id_seq'), primary_key=True)
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

class data_stage01_resequencing_coverage(Base):
    
    __tablename__ = 'data_stage01_resequencing_coverage'
    id = Column(Integer, Sequence('data_stage01_resequencing_coverage_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    data_dir = Column(String(500)); #
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    genome_index = Column(Integer);
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads = Column(Float);
    scale_factor = Column(Boolean);
    downsample_factor = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
            )

    def __init__(self, 
        #analysis_id_I, 
        experiment_id_I,
        sample_name_I,
        data_dir_I,
        genome_chromosome_I,
        genome_strand_I,
        genome_index_I,
        strand_start_I,
        strand_stop_I,
        reads_I,
        scale_factor_I,
        downsample_factor_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.data_dir=data_dir_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.genome_index=genome_index_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads=reads_I
        self.scale_factor=scale_factor_I
        self.downsample_factor=downsample_factor_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'data_dir':self.data_dir,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'genome_index':self.genome_index,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads':self.reads,
                'scale_factor':self.scale_factor,
                'downsample_factor':self.downsample_factor,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_coverageStats(Base):
    
    __tablename__ = 'data_stage01_resequencing_coverageStats'
    id = Column(Integer, Sequence('data_stage01_resequencing_coverageStats_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads_min = Column(Float);
    reads_max = Column(Float);
    reads_lb = Column(Float);
    reads_ub = Column(Float);
    reads_iq1 = Column(Float);
    reads_iq3 = Column(Float);
    reads_median = Column(Float);
    reads_mean = Column(Float);
    reads_var = Column(Float);
    reads_n = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand'),
            )

    def __init__(self, 
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        strand_start_I,
        strand_stop_I,
        reads_min_I,
        reads_max_I,
        reads_lb_I,
        reads_ub_I,
        reads_iq1_I,
        reads_iq3_I,
        reads_median_I,
        reads_mean_I,
        reads_var_I,
        reads_n_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads_min=reads_min_I
        self.reads_max=reads_max_I
        self.reads_lb=reads_lb_I
        self.reads_ub=reads_ub_I
        self.reads_iq1=reads_iq1_I
        self.reads_iq3=reads_iq3_I
        self.reads_median=reads_median_I
        self.reads_mean=reads_mean_I
        self.reads_var=reads_var_I
        self.reads_n=reads_n_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads_min':self.reads_min,
                'reads_max':self.reads_max,
                'reads_lb':self.reads_lb,
                'reads_ub':self.reads_ub,
                'reads_iq1':self.reads_iq1,
                'reads_iq3':self.reads_iq3,
                'reads_median':self.reads_median,
                'reads_mean':self.reads_mean,
                'reads_var':self.reads_var,
                'reads_n':self.reads_n,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_amplifications(Base):
    
    __tablename__ = 'data_stage01_resequencing_amplifications'
    id = Column(Integer, Sequence('data_stage01_resequencing_amplifications_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    genome_index = Column(Integer);
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads = Column(Float);
    reads_min = Column(Float);
    reads_max = Column(Float);
    indices_min = Column(Integer);
    consecutive_tol = Column(Integer);
    scale_factor = Column(Boolean);
    downsample_factor = Column(Integer);
    amplification_start = Column(Integer);
    amplification_stop = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
            )

    def __init__(self, 
        #analysis_id_I, 
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        genome_index_I,
        strand_start_I,
        strand_stop_I,
        reads_I,
        reads_min_I,
        reads_max_I,
        indices_min_I,
        consecutive_tol_I,
        scale_factor_I,
        downsample_factor_I,
        amplification_start_I,
        amplification_stop_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.genome_index=genome_index_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads=reads_I
        self.reads_min=reads_min_I
        self.reads_max=reads_max_I
        self.indices_min=indices_min_I
        self.consecutive_tol=consecutive_tol_I
        self.scale_factor=scale_factor_I
        self.downsample_factor=downsample_factor_I
        self.amplification_start=amplification_start_I
        self.amplification_stop=amplification_stop_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'genome_index':self.genome_index,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads':self.reads,
                'reads_min':self.reads_min,
                'reads_max':self.reads_max,
                'indices_min':self.indices_min,
                'consecutive_tol':self.consecutive_tol,
                'scale_factor':self.scale_factor,
                'downsample_factor':self.downsample_factor,
                'amplification_start':self.amplification_start,
                'amplification_stop':self.amplification_stop,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_amplificationStats(Base):
    
    __tablename__ = 'data_stage01_resequencing_amplificationStats'
    id = Column(Integer, Sequence('data_stage01_resequencing_amplificationStats_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads_min = Column(Float);
    reads_max = Column(Float);
    reads_lb = Column(Float);
    reads_ub = Column(Float);
    reads_iq1 = Column(Float);
    reads_iq3 = Column(Float);
    reads_median = Column(Float);
    reads_mean = Column(Float);
    reads_var = Column(Float);
    reads_n = Column(Float);
    amplification_start = Column(Integer);
    amplification_stop = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop'),
            )

    def __init__(self,
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        strand_start_I,
        strand_stop_I,
        reads_min_I,
        reads_max_I,
        reads_lb_I,
        reads_ub_I,
        reads_iq1_I,
        reads_iq3_I,
        reads_median_I,
        reads_mean_I,
        reads_var_I,
        reads_n_I,
        amplification_start_I,
        amplification_stop_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads_min=reads_min_I
        self.reads_max=reads_max_I
        self.reads_lb=reads_lb_I
        self.reads_ub=reads_ub_I
        self.reads_iq1=reads_iq1_I
        self.reads_iq3=reads_iq3_I
        self.reads_median=reads_median_I
        self.reads_mean=reads_mean_I
        self.reads_var=reads_var_I
        self.reads_n=reads_n_I
        self.amplification_start=amplification_start_I
        self.amplification_stop=amplification_stop_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads_min':self.reads_min,
                'reads_max':self.reads_max,
                'reads_lb':self.reads_lb,
                'reads_ub':self.reads_ub,
                'reads_iq1':self.reads_iq1,
                'reads_iq3':self.reads_iq3,
                'reads_median':self.reads_median,
                'reads_mean':self.reads_mean,
                'reads_var':self.reads_var,
                'reads_n':self.reads_n,
                'amplification_start':self.amplification_start,
                'amplification_stop':self.amplification_stop,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_amplificationAnnotations(Base):
    
    __tablename__ = 'data_stage01_resequencing_amplificationAnnotations'
    id = Column(Integer, Sequence('data_stage01_resequencing_amplificationAnnotations_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    feature_annotations = Column(postgresql.ARRAY(String(500)))
    feature_genes = Column(postgresql.ARRAY(String(25)))
    feature_locations = Column(postgresql.ARRAY(String(100)))
    feature_links = Column(postgresql.ARRAY(String(500)))
    feature_start = Column(Integer);
    feature_stop = Column(Integer);
    feature_types = Column(postgresql.ARRAY(String(500)));
    amplification_start = Column(Integer);
    amplification_stop = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop',
                         'feature_locations','feature_genes','feature_annotations',
                         'feature_start','feature_stop','feature_types'
                         ),
            )

    def __init__(self,
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        strand_start_I,
        strand_stop_I,
        feature_annotations_I,
        feature_genes_I,
        feature_locations_I,
        feature_links_I,
        feature_start_I,
        feature_stop_I,
        feature_types_I,
        amplification_start_I,
        amplification_stop_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.feature_annotations=feature_annotations_I
        self.feature_genes=feature_genes_I
        self.feature_locations=feature_locations_I
        self.feature_links=feature_links_I
        self.feature_start=feature_start_I
        self.feature_stop=feature_stop_I
        self.feature_types=feature_types_I
        self.amplification_start=amplification_start_I
        self.amplification_stop=amplification_stop_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'feature_annotations':self.feature_annotations,
                'feature_genes':self.feature_genes,
                'feature_locations':self.feature_locations,
                'feature_links':self.feature_links,
                'feature_start':self.feature_start,
                'feature_stop':self.feature_stop,
                'feature_types':self.feature_types,
                'amplification_start':self.amplification_start,
                'amplification_stop':self.amplification_stop,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_rnasequencing_fpkmTracking(Base):
    
    __tablename__ = 'data_stage01_rnasequencing_fpkmTracking'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_fpkmTracking_id_seq'), primary_key=True)
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
    
    __tablename__ = 'data_stage01_rnasequencing_fpkmtrackin'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_fpkmtrackin_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name_1 = Column(String(100))
    sample_name_2 = Column(String(100))
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
    p_value = Column(Float);
    q_value = Column(Float);
    significant = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('analysis_id','experiment_id','sample_name_1','sample_name_2','gene_id'
                         ),
            )

    def __init__(self,
        analysis_id_I,
        experiment_id_I,
        sample_name_1_I,
        sample_name_2_I,
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
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name_1=sample_name_1_I
        self.sample_name_2=sample_name_2_I
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
                'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name_1':self.sample_name_1,
                'sample_name_2':self.sample_name_2,
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