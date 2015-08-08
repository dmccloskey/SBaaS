from sbaas.analysis.analysis_base import *
import json

class stage01_rnasequencing_query(base_analysis):
   
    # query gene names from biologicalMaterial_geneReferences
    def get_orderedLocusName_biologicalmaterialIDAndGeneName_biologicalMaterialGeneReferences(self,biologicalmaterial_id_I,gene_name_I):
        '''Query ordered locus name from gene name'''
        try:
            data = self.session.query(biologicalMaterial_geneReferences.biologicalmaterial_id,
                    biologicalMaterial_geneReferences.gene_name,
                    biologicalMaterial_geneReferences.ordered_locus_name).filter(
                    biologicalMaterial_geneReferences.biologicalmaterial_id.like(biologicalmaterial_id_I),
                    biologicalMaterial_geneReferences.gene_name.like(gene_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['ordered_locus_name'] = d.ordered_locus_name;
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_ecogeneAccessionNumber_biologicalmaterialIDAndGeneName_biologicalMaterialGeneReferences(self,biologicalmaterial_id_I,gene_name_I):
        '''Query ecogene accession number from gene name'''
        try:
            data = self.session.query(biologicalMaterial_geneReferences.biologicalmaterial_id,
                    biologicalMaterial_geneReferences.gene_name,
                    biologicalMaterial_geneReferences.ecogene_accession_number).filter(
                    biologicalMaterial_geneReferences.biologicalmaterial_id.like(biologicalmaterial_id_I),
                    biologicalMaterial_geneReferences.gene_name.like(gene_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['ecogene_accession_number'] = d.ecogene_accession_number;
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_geneName_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(self,biologicalmaterial_id_I,ordered_locus_name_I):
        '''Query gene name from ordered locus name'''
        try:
            data = self.session.query(biologicalMaterial_geneReferences.biologicalmaterial_id,
                    biologicalMaterial_geneReferences.gene_name,
                    biologicalMaterial_geneReferences.ordered_locus_name).filter(
                    biologicalMaterial_geneReferences.biologicalmaterial_id.like(biologicalmaterial_id_I),
                    biologicalMaterial_geneReferences.ordered_locus_name.like(ordered_locus_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['ordered_locus_name'] = d.ordered_locus_name;
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(self,biologicalmaterial_id_I,ordered_locus_name_I):
        '''Query ecogene accession number from ordered locus name name'''
        try:
            data = self.session.query(biologicalMaterial_geneReferences.biologicalmaterial_id,
                    biologicalMaterial_geneReferences.ordered_locus_name,
                    biologicalMaterial_geneReferences.ecogene_accession_number).filter(
                    biologicalMaterial_geneReferences.biologicalmaterial_id.like(biologicalmaterial_id_I),
                    biologicalMaterial_geneReferences.ordered_locus_name.like(ordered_locus_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['ecogene_accession_number'] = d.ecogene_accession_number;
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_rnasequencing_analysis
    def get_analysis_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).all();
            analysis_id_O = []
            experiment_id_O = []
            sample_name_abbreviation_O = []
            sample_name_O = []
            analysis_type_O = []
            analysis_O = {};
            if data: 
                for d in data:
                    analysis_id_O.append(d.analysis_id);
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation);
                    sample_name_O.append(d.sample_name);
                    analysis_type_O.append(d.analysis_type);
                analysis_id_O = list(set(analysis_id_O))
                experiment_id_O = list(set(experiment_id_O))
                sample_name_abbreviation_O = list(set(sample_name_abbreviation_O))
                sample_name_O = list(set(sample_name_O))
                analysis_type_O = list(set(analysis_type_O))
                analysis_O={
                        'analysis_id':analysis_id_O,
                        'experiment_id':experiment_id_O,
                        'sample_name_abbreviation':sample_name_abbreviation_O,
                        'sample_name':sample_name_O,
                        'analysis_type':analysis_type_O};
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAbbreviation_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation.asc()).all();
            experiment_id_O = []
            sample_name_abbreviation_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation);                
            return  experiment_id_O,sample_name_abbreviation_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleName_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name.asc()).all();
            experiment_id_O = []
            sample_name_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_O.append(d.sample_name);                
            return  experiment_id_O,sample_name_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name.asc(),
                    data_stage01_rnasequencing_analysis.time_point.asc()).all();
            experiment_id_O = []
            sample_name_O = []
            time_point_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_O.append(d.sample_name);    
                    time_point_O.append(d.time_point);              
            return  experiment_id_O,sample_name_O,time_point_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAbbreviationAndSampleNameAndTimePoint_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation.asc(),
                    data_stage01_rnasequencing_analysis.sample_name.asc(),
                    data_stage01_rnasequencing_analysis.time_point.asc()).all();
            experiment_id_O = []
            sample_name_abbreviation_O = []
            sample_name_O = []
            time_point_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation); 
                    sample_name_O.append(d.sample_name);    
                    time_point_O.append(d.time_point);              
            return  experiment_id_O,sample_name_abbreviation_O,sample_name_O,time_point_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).all();
            analysis_O = [];
            if data: 
                for d in data:
                    analysis_O.append({
                        'analysis_id':d.analysis_id,
                        'experiment_id':d.experiment_id,
                        'sample_name_abbreviation':d.sample_name_abbreviation,
                        'sample_name':d.sample_name,
                        'analysis_type':d.analysis_type});
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_rnasequencing_heatmap
    def get_rows_analysisID_dataStage01RNASequencingHeatmap(self,analysis_id_I):
        '''Query rows by analysisid and sample_name from data_stage01_rnasequencing_heatmap'''
        try:
            data = self.session.query(data_stage01_rnasequencing_heatmap).filter(
                    data_stage01_rnasequencing_heatmap.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_heatmap.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                'analysis_id':d.analysis_id,
                'col_index':d.col_index,
                'row_index':d.row_index,
                'value':d.value,
                'col_leaves':d.col_leaves,
                'row_leaves':d.row_leaves,
                'col_label':d.col_label,
                'row_label':d.row_label,
                'col_pdist_metric':d.col_pdist_metric,
                'row_pdist_metric':d.row_pdist_metric,
                'col_linkage_method':d.col_linkage_method,
                'row_linkage_method':d.row_linkage_method,
                'value_units':d.value_units,
                'used_':d.used_,
                'comment_':d.comment_}
                              );
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_rnasequencing_genesFpkmTracking
    def get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesFpkmTracking(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name'''
        try:
            data = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(
                    data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I),
                    data_stage01_rnasequencing_genesFpkmTracking.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'tracking_id':d.tracking_id,
                'class_code':d.class_code,
                'nearest_ref_id':d.nearest_ref_id,
                'gene_id':d.gene_id,
                'gene_short_name':d.gene_short_name,
                'tss_id':d.tss_id,
                'locus':d.locus,
                'length':d.length,
                'coverage':d.coverage,
                'FPKM':d.FPKM,
                'FPKM_conf_lo':d.FPKM_conf_lo,
                'FPKM_conf_hi':d.FPKM_conf_hi,
                'FPKM_status':d.FPKM_status,
                'used_':d.used_,
                'comment_':d.comment_};
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_rnasequencing_geneExpDiff