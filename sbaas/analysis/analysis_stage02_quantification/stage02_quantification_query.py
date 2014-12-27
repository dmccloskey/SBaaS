from analysis.analysis_base import *

class stage02_quantification_query(base_analysis):
    # data_stage01_quantification_replicatesMI
    # Query sample names from data_stage01_quantification_replicatesMI:
    def get_sampleNameAbbreviations_experimentID_dataStage01ReplicatesMI(self,experiment_id_I,exp_type_I=4):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.metabolomics_sample_name.like(metabolomics_sample.sample_name),
                    metabolomics_sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,exp_type_I=4):
        '''Querry sample names that are used from the experiment by sample name abbreviation and sample description'''
        #Not tested
        try:
            sample_names = self.session.query(data_stage01_quantification_replicatesMI.sample_name_short).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.sample_name_short).order_by(
                    data_stage01_quantification_replicatesMI.sample_name_short.asc()).all();
            sample_names_short_O = [];
            for sn in sample_names: sample_names_short_O.append(sn.sample_name_short);
            return sample_names_short_O;
        except SQLAlchemyError as e:
            print(e);
    # Query time points from data_stage01_quantification_replicatesMI
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry time points that are used from the experiment'''
        #Not tested
        try:
            time_points = self.session.query(data_stage01_quantification_replicatesMI.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.metabolomics_sample_name.like(metabolomics_sample.sample_name),
                    metabolomics_sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(data_stage01_quantification_replicatesMI.sample_name_short),
                    sample_description.time_point.like(data_stage01_quantification_replicatesMI.time_point),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.time_point).order_by(
                    data_stage01_quantification_replicatesMI.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentID_dataStage01ReplicatesMI(self,experiment_id_I,exp_type_I=4):
        '''Querry time points that are used from the experiment'''
        #Tested
        try:
            time_points = self.session.query(data_stage01_quantification_replicatesMI.time_point).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.metabolomics_sample_name.like(metabolomics_sample.sample_name),
                    metabolomics_sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(data_stage01_quantification_replicatesMI.sample_name_short),
                    sample_description.time_point.like(data_stage01_quantification_replicatesMI.time_point),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.time_point).order_by(
                    data_stage01_quantification_replicatesMI.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_replicatesMI:
    def get_concentrationAndUnits_experimentIDAndTimePointAndSampleNameShortAndComponentName_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,sample_name_short_I,component_name_I):
        """get concentration and units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).all();
            concentration_O = None;
            concentration_units_O = None;
            if data: 
                concentration_O=data[0].calculated_concentration;
                concentration_units_O=data[0].calculated_concentration_units;
            return concentration_O,concentration_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentID_dataStage01ReplicatesMI(self, experiment_id_I):
        """get data from experiment ID"""
        #Not tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndTimePointAndSampleNameShortAndUnits_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,sample_name_short_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndTimePointAndUnits_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,component_name_I,sample_name_abbreviation_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            concentrations_O = [];
            for d in data: 
                concentrations_O.append(d.calculated_concentration);
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O,concentrations_O;
        except SQLAlchemyError as e:
            print(e);
    # Query concentration_units from data_stage01_quantification_replicatesMI:    
    def get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).order_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_concentrationUnits_experimentIDAndTimePointAndSampleNameShort_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,sample_name_short_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).order_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);

    # data_stage02_quantification_glogNormalized
    # Query time points from data_stage02_quantification_glogNormalized
    def get_timePoint_experimentID_dataStage02GlogNormalized(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        #Tested
        try:
            time_points = self.session.query(data_stage02_quantification_glogNormalized.time_point).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.time_point).order_by(
                    data_stage02_quantification_glogNormalized.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query concentration_units from data_stage01_quantification_glogNormalized:    
    def get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(self, experiment_id_I,time_point_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage02_quantification_glogNormalized.calculated_concentration_units).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).order_by(
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);
    # Query component_names from data_stage01_quantification_glogNormalized:    
    def get_componentNames_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(self, experiment_id_I,time_point_I, concentration_units_I):
        """get component_names from experiment ID and time point and concentration_units"""
        try:
            data = self.session.query(data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.component_group_name).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.component_group_name).order_by(
                    data_stage02_quantification_glogNormalized.component_name.asc()).all();
            component_names_O = [];
            component_group_names_O = [];
            for d in data: 
                component_names_O.append(d.component_name);
                component_group_names_O.append(d.component_group_name);
            return component_names_O, component_group_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query sample_name_abbreviations from data_stage01_quantification_glogNormalized:    
    def get_sampleNameAbbreviations_experimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(self, experiment_id_I,time_point_I, concentration_units_I,component_name_I,exp_type_I=4):
        """get component_names from experiment ID and time point and concentration_units"""
        try:
            data = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_glogNormalized.component_name.like(component_name_I),
                    data_stage02_quantification_glogNormalized.used_.is_(True),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage02_quantification_glogNormalized.sample_name_short.like(sample_description.sample_name_short)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            component_names_O = [];
            for d in data: 
                component_names_O.append(d[0]);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_glogNormalized
    def get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage02_quantification_glogNormalized.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_glogNormalized.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RDataFrame_experimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(self, experiment_id_I,time_point_I,concentration_units_I,component_name_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage02_quantification_glogNormalized.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.component_name.like(component_name_I),
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_glogNormalized.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(self, experiment_id_I,time_point_I,concentration_units_I,component_name_I,sample_name_abbreviation_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage02_quantification_glogNormalized.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.component_name.like(component_name_I),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_glogNormalized.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).all();
            data_O = [];
            concentrations_O = [];
            for d in data: 
                concentrations_O.append(d.calculated_concentration);
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O,concentrations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage02_quantification_glogNormalized.experiment_id,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).filter(
                    data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                    data_stage02_quantification_glogNormalized.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_glogNormalized.used_.is_(True)).group_by(
                    data_stage02_quantification_glogNormalized.experiment_id,
                    data_stage02_quantification_glogNormalized.sample_name_short,
                    data_stage02_quantification_glogNormalized.time_point,
                    data_stage02_quantification_glogNormalized.component_group_name,
                    data_stage02_quantification_glogNormalized.component_name,
                    data_stage02_quantification_glogNormalized.calculated_concentration,
                    data_stage02_quantification_glogNormalized.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # Update data_stage02_quantification_glogNormalized
    def update_concentrations_dataStage02GlogNormalized(self, experiment_id_I, time_point_I, dataListUpdated_I):
        # update the data_stage02_quantification_glogNormalized
        updates = [];
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage02_quantification_glogNormalized).filter(
                        data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                        data_stage02_quantification_glogNormalized.sample_name_short.like(d['sample_name_short']),
                        data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                        data_stage02_quantification_glogNormalized.component_name.like(d['component_name'])).update(		
                        {
                        'calculated_concentration':d['calculated_concentration']},
                        synchronize_session=False);
                if data_update == 0:
                    print 'row not found.'
                    print d
                updates.append(data_update);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
    def update_concentrationsAndUnits_dataStage02GlogNormalized(self, experiment_id_I, time_point_I, dataListUpdated_I):
        # update the data_stage02_quantification_glogNormalized
        updates = [];
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage02_quantification_glogNormalized).filter(
                        data_stage02_quantification_glogNormalized.experiment_id.like(experiment_id_I),
                        data_stage02_quantification_glogNormalized.sample_name_short.like(d['sample_name_short']),
                        data_stage02_quantification_glogNormalized.time_point.like(time_point_I),
                        data_stage02_quantification_glogNormalized.component_name.like(d['component_name'])).update(		
                        {
                        'calculated_concentration':d['calculated_concentration'],
                        'calculated_concentration_units':d['calculated_concentration_units']},
                        synchronize_session=False);
                if data_update == 0:
                    print 'row not found.'
                    print d
                updates.append(data_update);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    # data_stage02_quantification_pca_scores/loadings 
    # Query time points from data_stage02_quantification_pca_scores
    def get_timePoint_experimentID_dataStage02Scores(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        #Tested
        try:
            time_points = self.session.query(data_stage02_quantification_pca_scores.time_point).filter(
                    data_stage02_quantification_pca_scores.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pca_scores.used_.is_(True)).group_by(
                    data_stage02_quantification_pca_scores.time_point).order_by(
                    data_stage02_quantification_pca_scores.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query concentration_units from data_stage01_quantification_pca_scores:    
    def get_concentrationUnits_experimentIDAndTimePoint_dataStage02Scores(self, experiment_id_I,time_point_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage02_quantification_pca_scores.calculated_concentration_units).filter(
                    data_stage02_quantification_pca_scores.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pca_scores.time_point.like(time_point_I),
                    data_stage02_quantification_pca_scores.used_.is_(True)).group_by(
                    data_stage02_quantification_pca_scores.calculated_concentration_units).order_by(
                    data_stage02_quantification_pca_scores.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_pca_scores and data_stage01_quantification_pca_loadings
    def get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage02ScoresLoadings(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        try:
            data_scores = self.session.query(data_stage02_quantification_pca_scores.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_pca_scores.sample_name_short,
                    data_stage02_quantification_pca_scores.time_point,
                    data_stage02_quantification_pca_scores.score,
                    data_stage02_quantification_pca_scores.axis,
                    data_stage02_quantification_pca_scores.var_proportion,
                    data_stage02_quantification_pca_scores.calculated_concentration_units).filter(
                    data_stage02_quantification_pca_scores.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pca_scores.time_point.like(time_point_I),
                    data_stage02_quantification_pca_scores.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_pca_scores.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(metabolomics_sample.sample_id),
                    metabolomics_sample.sample_name.like(metabolomics_experiment.metabolomics_sample_name),
                    metabolomics_experiment.id.like(experiment_id_I),
                    metabolomics_experiment.exp_type_id == exp_type_I,
                    data_stage02_quantification_pca_scores.used_.is_(True)).group_by(
                    data_stage02_quantification_pca_scores.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage02_quantification_pca_scores.sample_name_short,
                    data_stage02_quantification_pca_scores.time_point,
                    data_stage02_quantification_pca_scores.score,
                    data_stage02_quantification_pca_scores.axis,
                    data_stage02_quantification_pca_scores.var_proportion,
                    data_stage02_quantification_pca_scores.calculated_concentration_units).all();
            data_scores_O = []; #data_loadings_O = [];
            for d in data_scores: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['score'] = d.score;
                data_1['axis'] = d.axis;
                data_1['var_proportion'] = d.var_proportion;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_scores_O.append(data_1);
            # query loadings
            data_loadings = self.session.query(data_stage02_quantification_pca_loadings.experiment_id,
                    data_stage02_quantification_pca_loadings.axis,
                    data_stage02_quantification_pca_loadings.component_group_name,
                    data_stage02_quantification_pca_loadings.component_name,
                    data_stage02_quantification_pca_loadings.loadings,
                    data_stage02_quantification_pca_loadings.calculated_concentration_units,
                    data_stage02_quantification_pca_scores.time_point).filter(
                    data_stage02_quantification_pca_loadings.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pca_loadings.time_point.like(time_point_I),
                    data_stage02_quantification_pca_loadings.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_pca_loadings.used_.is_(True)).group_by(data_stage02_quantification_pca_loadings.experiment_id,
                    data_stage02_quantification_pca_loadings.axis,
                    data_stage02_quantification_pca_loadings.component_group_name,
                    data_stage02_quantification_pca_loadings.component_name,
                    data_stage02_quantification_pca_loadings.loadings,
                    data_stage02_quantification_pca_loadings.calculated_concentration_units,
                    data_stage02_quantification_pca_scores.time_point).all();
            data_loadings_O = [];
            for d in data_loadings: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['time_point'] = d.time_point;
                data_1['axis'] = d.axis;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['loadings'] = d.loadings;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_loadings_O.append(data_1);
            return data_scores_O, data_loadings_O;
        except SQLAlchemyError as e:
            print(e);
            
    # data_stage02_quantification_pairWiseTest
    # Query time points from data_stage02_quantification_pairWiseTest
    def get_timePoint_experimentID_dataStage02pairWiseTest(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        #Tested
        try:
            time_points = self.session.query(data_stage02_quantification_pairWiseTest.time_point_1,
                    data_stage02_quantification_pairWiseTest.time_point_2).filter(
                    data_stage02_quantification_pairWiseTest.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pairWiseTest.used_.is_(True)).group_by(
                    data_stage02_quantification_pairWiseTest.time_point_1,
                    data_stage02_quantification_pairWiseTest.time_point_2).order_by(
                    data_stage02_quantification_pairWiseTest.time_point_1.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point_1);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query concentration_units from data_stage01_quantification_pairWiseTest:    
    def get_concentrationUnits_experimentIDAndTimePoint_dataStage02pairWiseTest(self, experiment_id_I,time_point_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage02_quantification_pairWiseTest.calculated_concentration_units).filter(
                    data_stage02_quantification_pairWiseTest.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pairWiseTest.time_point_1.like(time_point_I),
                    data_stage02_quantification_pairWiseTest.used_.is_(True)).group_by(
                    data_stage02_quantification_pairWiseTest.calculated_concentration_units).order_by(
                    data_stage02_quantification_pairWiseTest.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);
    # Query sample_name_abbreviations from data_stage01_quantification_pairWiseTest:    
    def get_sampleNameAbbreviations_experimentIDAndTimePointAndUnits_dataStage02pairWiseTest(self, experiment_id_I,time_point_I, concentration_units_I):
        """get component_names from experiment ID and time point and concentration_units"""
        try:
            data = self.session.query(data_stage02_quantification_pairWiseTest.sample_name_abbreviation_1).filter(
                    data_stage02_quantification_pairWiseTest.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pairWiseTest.time_point_1.like(time_point_I),
                    data_stage02_quantification_pairWiseTest.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_pairWiseTest.used_.is_(True)).group_by(
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_1).order_by(
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_1.asc()).all();
            component_names_O = [];
            for d in data: 
                component_names_O.append(d[0]);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_pairWiseTest
    def get_RDataList_experimentIDAndTimePointAndUnitsAndSampleNameAbbreviations_dataStage02pairWiseTest(self, experiment_id_I,time_point_I,
              concentration_units_I,sample_name_abbreviation_1_I,sample_name_abbreviation_2_I):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage02_quantification_pairWiseTest.experiment_id,
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_1,
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_2,
                    data_stage02_quantification_pairWiseTest.time_point_1,
                    data_stage02_quantification_pairWiseTest.time_point_2,
                    data_stage02_quantification_pairWiseTest.component_group_name,
                    data_stage02_quantification_pairWiseTest.component_name,
                    data_stage02_quantification_pairWiseTest.test_stat,
                    data_stage02_quantification_pairWiseTest.test_description,
                    data_stage02_quantification_pairWiseTest.pvalue,
                    data_stage02_quantification_pairWiseTest.pvalue_corrected,
                    data_stage02_quantification_pairWiseTest.pvalue_corrected_description,
                    data_stage02_quantification_pairWiseTest.mean,
                    data_stage02_quantification_pairWiseTest.ci_lb,
                    data_stage02_quantification_pairWiseTest.ci_ub,
                    data_stage02_quantification_pairWiseTest.ci_level,
                    data_stage02_quantification_pairWiseTest.fold_change,
                    data_stage02_quantification_pairWiseTest.calculated_concentration_units).filter(
                    data_stage02_quantification_pairWiseTest.experiment_id.like(experiment_id_I),
                    data_stage02_quantification_pairWiseTest.time_point_1.like(time_point_I),
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_1.like(sample_name_abbreviation_1_I),
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_2.like(sample_name_abbreviation_2_I),
                    data_stage02_quantification_pairWiseTest.calculated_concentration_units.like(concentration_units_I),
                    data_stage02_quantification_pairWiseTest.used_.is_(True),
                    data_stage02_quantification_pairWiseTest.ci_level != None).group_by(
                    data_stage02_quantification_pairWiseTest.experiment_id,
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_1,
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_2,
                    data_stage02_quantification_pairWiseTest.time_point_1,
                    data_stage02_quantification_pairWiseTest.time_point_2,
                    data_stage02_quantification_pairWiseTest.component_group_name,
                    data_stage02_quantification_pairWiseTest.component_name,
                    data_stage02_quantification_pairWiseTest.test_stat,
                    data_stage02_quantification_pairWiseTest.test_description,
                    data_stage02_quantification_pairWiseTest.pvalue,
                    data_stage02_quantification_pairWiseTest.pvalue_corrected,
                    data_stage02_quantification_pairWiseTest.pvalue_corrected_description,
                    data_stage02_quantification_pairWiseTest.mean,
                    data_stage02_quantification_pairWiseTest.ci_lb,
                    data_stage02_quantification_pairWiseTest.ci_ub,
                    data_stage02_quantification_pairWiseTest.ci_level,
                    data_stage02_quantification_pairWiseTest.fold_change,
                    data_stage02_quantification_pairWiseTest.calculated_concentration_units).order_by(
                    data_stage02_quantification_pairWiseTest.sample_name_abbreviation_2.asc(),
                    data_stage02_quantification_pairWiseTest.component_group_name.asc()).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation_1'] = d.sample_name_abbreviation_1;
                data_1['sample_name_abbreviation_2'] = d.sample_name_abbreviation_2;
                data_1['time_point_1'] = d.time_point_1;
                data_1['time_point_2'] = d.time_point_2;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['test_stat'] = d.test_stat;
                data_1['test_description'] = d.test_description;
                data_1['pvalue_negLog10'] = -log(d.pvalue,10);
                data_1['pvalue_corrected_negLog10'] = -log(d.pvalue_corrected,10);
                data_1['pvalue_corrected_description'] = d.pvalue_corrected_description;
                data_1['mean'] = d.mean;
                data_1['ci_lb'] = d.ci_lb;
                data_1['ci_ub'] = d.ci_ub;
                data_1['ci_level'] = d.ci_level;
                data_1['fold_change_log2'] = log(d.fold_change,2);
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
