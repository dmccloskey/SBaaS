COPY metabolomics_experimentor FROM 'C:/Users/Public/Documents/sql_COPY/experimentor/metabolomics_experimentor.csv' DELIMITER ',' CSV HEADER;
COPY metabolomics_experimentor_list FROM 'C:/Users/Public/Documents/sql_COPY/experimentor/metabolomics_experimentor_list.csv' DELIMITER ',' CSV HEADER;
COPY metabolomics_experimentor_id2name FROM 'C:/Users/Public/Documents/sql_COPY/experimentor/metabolomics_experimentor_id2name.csv' DELIMITER ',' CSV HEADER;

COPY extraction_method FROM 'C:/Users/Public/Documents/sql_COPY/extraction_method/extraction_method.csv' DELIMITER ',' CSV HEADER;

COPY metabolomics_standards FROM 'C:/Users/Public/Documents/sql_COPY/standards/metabolomics_standards.csv' DELIMITER ',' CSV HEADER;
COPY standards_ordering FROM 'C:/Users/Public/Documents/sql_COPY/standards/standards_ordering.csv' DELIMITER ',' CSV HEADER;
COPY standards2material FROM 'C:/Users/Public/Documents/sql_COPY/standards/standards2material.csv' DELIMITER ',' CSV HEADER;
COPY standards_storage FROM 'C:/Users/Public/Documents/sql_COPY/standards/standards_storage.csv' DELIMITER ',' CSV HEADER;

COPY mix_description FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/mix_description.csv' DELIMITER ',' CSV HEADER;
COPY mix_storage FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/mix_storage.csv' DELIMITER ',' CSV HEADER;
COPY mix_parameters FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/mix_parameters.csv' DELIMITER ',' CSV HEADER;
COPY calibrator_met_parameters FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/calibrator_met_parameters.csv' DELIMITER ',' CSV HEADER;
COPY metabolomics_calibrator FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/metabolomics_calibrator.csv' DELIMITER ',' CSV HEADER;
COPY calibrator_concentrations FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/calibrator_concentrations.csv' DELIMITER ',' CSV HEADER;
COPY calibrator2mix FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/calibrator2mix.csv' DELIMITER ',' CSV HEADER;
COPY mix2met_ID FROM 'C:/Users/Public/Documents/sql_COPY/calibrators/mix2met_ID.csv' DELIMITER ',' CSV HEADER;

COPY MS_components FROM 'C:/Users/Public/Documents/sql_COPY/batch/MS_component.csv' DELIMITER ',' CSV HEADER;

CREATE TEMP TABLE tmp AS SELECT * FROM MS_components LIMIT 0;
COPY tmp FROM 'C:/Users/Public/Documents/sql_COPY/batch/MS_components_update.csv' DELIMITER ',' CSV HEADER;
UPDATE MS_components
	SET    quantifier = tmp.quantifier, 
	threshold = tmp.threshold, 
	dwell_weight = tmp.dwell_weight, 
	ms_group = tmp.ms_group, 
	component_name = tmp.component_name, 
	ms_include = tmp.ms_include, 
	ms_is = tmp.ms_is 
	FROM  tmp
	WHERE  MS_components.met_id = tmp.met_id
		AND MS_components.q1_mass = tmp.q1_mass
		AND MS_components.q3_mass = tmp.q3_mass;
INSERT INTO MS_components
	SELECT tmp.*
	FROM   tmp
	LEFT   JOIN MS_components USING (met_id,q1_mass,q3_mass)
	WHERE  MS_components.met_id IS NULL AND MS_components.q1_mass IS NULL AND MS_components.q3_mass IS NULL;
DROP TABLE tmp;

COPY MS_sourceParameters FROM 'C:/Users/Public/Documents/sql_COPY/batch/MS_sourceParameters.csv' DELIMITER ',' CSV HEADER;
COPY MS_information FROM 'C:/Users/Public/Documents/sql_COPY/batch/MS_information.csv' DELIMITER ',' CSV HEADER;
COPY MS_method FROM 'C:/Users/Public/Documents/sql_COPY/batch/MS_method.csv' DELIMITER ',' CSV HEADER;
COPY MS_component_list FROM 'C:/Users/Public/Documents/sql_COPY/batch/MS_component_list.csv' DELIMITER ',' CSV HEADER;
COPY Autosampler_parameters FROM 'C:/Users/Public/Documents/sql_COPY/batch/Autosampler_parameters.csv' DELIMITER ',' CSV HEADER;
COPY Autosampler_information FROM 'C:/Users/Public/Documents/sql_COPY/batch/Autosampler_information.csv' DELIMITER ',' CSV HEADER;
COPY Autosampler_method FROM 'C:/Users/Public/Documents/sql_COPY/batch/Autosampler_method.csv' DELIMITER ',' CSV HEADER;
COPY LC_information FROM 'C:/Users/Public/Documents/sql_COPY/batch/LC_information.csv' DELIMITER ',' CSV HEADER;
COPY LC_gradient FROM 'C:/Users/Public/Documents/sql_COPY/batch/LC_gradient.csv' DELIMITER ',' CSV HEADER;
COPY LC_parameters FROM 'C:/Users/Public/Documents/sql_COPY/batch/LC_parameters.csv' DELIMITER ',' CSV HEADER;
COPY LC_method FROM 'C:/Users/Public/Documents/sql_COPY/batch/LC_method.csv' DELIMITER ',' CSV HEADER;
COPY LC_elution FROM 'C:/Users/Public/Documents/sql_COPY/batch/LC_elution.csv' DELIMITER ',' CSV HEADER;
COPY acquisition_method FROM 'C:/Users/Public/Documents/sql_COPY/batch/acquisition_method.csv' DELIMITER ',' CSV HEADER;
COPY quantitation_method_list FROM 'C:/Users/Public/Documents/sql_COPY/batch/quantitation_method_list.csv' DELIMITER ',' CSV HEADER;
COPY quantitation_method FROM 'C:/Users/Public/Documents/sql_COPY/batch/quantitation_method.csv' DELIMITER ',' CSV HEADER;

COPY sample_massVolumeConversion FROM 'C:/Users/Public/Documents/sql_COPY/sample/sample_massVolumeConversion.csv' DELIMITER ',' CSV HEADER;
COPY sample_storage FROM 'C:/Users/Public/Documents/sql_COPY/sample/sample_storage.csv' DELIMITER ',' CSV HEADER;
COPY sample_physiologicalParameters FROM 'C:/Users/Public/Documents/sql_COPY/sample/sample_physiologicalParameters.csv' DELIMITER ',' CSV HEADER;
COPY sample_description FROM 'C:/Users/Public/Documents/sql_COPY/sample/sample_description.csv' DELIMITER ',' CSV HEADER;
COPY metabolomics_sample FROM 'C:/Users/Public/Documents/sql_COPY/sample/metabolomics_sample.csv' DELIMITER ',' CSV HEADER;

COPY IS_storage FROM 'C:/Users/Public/Documents/sql_COPY/IS/IS_storage.csv' DELIMITER ',' CSV HEADER;
COPY metabolomics_IS FROM 'C:/Users/Public/Documents/sql_COPY/IS/metabolomics_IS.csv' DELIMITER ',' CSV HEADER;

COPY metabolomics_experiment FROM 'C:/Users/Public/Documents/sql_COPY/experiment/metabolomics_experiment.csv' DELIMITER ',' CSV HEADER;

-- N/A, < 0, <2 points, degenerate, (No IS)
COPY data_stage01_MQResultsTable FROM 'C:/Users/Public/Documents/sql_COPY/data_stage01/Nitrate_Calibrators.csv' DELIMITER ',' CSV HEADER;
COPY data_stage01_MQResultsTable FROM 'C:/Users/Public/Documents/sql_COPY/data_stage01/Nitrate_Calibrators-area.csv' DELIMITER ',' CSV HEADER;
COPY data_stage01_MQResultsTable FROM 'C:/Users/Public/Documents/sql_COPY/data_stage01/HUGE_Calibrators_converted.csv' DELIMITER ',' CSV HEADER;
COPY data_stage01_MQResultsTable FROM 'C:/Users/Public/Documents/sql_COPY/data_stage01/RpoB_Calibrators_converted.csv' DELIMITER ',' CSV HEADER;
COPY data_stage01_MQResultsTable FROM 'C:/Users/Public/Documents/sql_COPY/data_stage01/SyringePH_Calibrators_converted.csv' DELIMITER ',' CSV HEADER;
