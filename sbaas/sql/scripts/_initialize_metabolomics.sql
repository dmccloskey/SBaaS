--Metabolomics data processing pipeline:
--Stage 1: Data acquisition, identification, and quantitation

DROP SCHEMA public;

CREATE SCHEMA public
  AUTHORIZATION postgres;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public
  IS 'standard public schema';


--DROP SEQUENCE IF EXISTS standards_WIDs CASCADE;
--DROP SEQUENCE IF EXISTS samples_WIDs CASCADE;

--CREATE SEQUENCE standards_WIDs START 1; --compound id
--CREATE SEQUENCE samples_WIDs START 1; --sample id
 
-- Experimentor
DROP TABLE IF EXISTS metabolomics_experimentor CASCADE;
DROP TABLE IF EXISTS metabolomics_experimentor_list CASCADE;
DROP TABLE IF EXISTS metabolomics_experimentor_id2name CASCADE;

-- Extraction Method
DROP TABLE IF EXISTS extraction_method CASCADE;

-- Standards
DROP TABLE IF EXISTS metabolomics_standards CASCADE;
DROP TABLE IF EXISTS standards_ordering CASCADE;
DROP TABLE IF EXISTS standards2material CASCADE;
DROP TABLE IF EXISTS standards_storage CASCADE;
 
-- Calibrators and mixes
DROP TABLE IF EXISTS mix_storage CASCADE;
DROP TABLE IF EXISTS mix_description CASCADE;
DROP TABLE IF EXISTS mix_parameters CASCADE;
DROP TABLE IF EXISTS calibrator_met_parameters CASCADE;
DROP TABLE IF EXISTS calibrator2mix CASCADE;
DROP TABLE IF EXISTS mix2met_ID CASCADE;
DROP TABLE IF EXISTS metabolomics_calibrator CASCADE;
DROP TABLE IF EXISTS calibrator_concentrations CASCADE;
DROP TABLE IF EXISTS calibrator_calculations CASCADE;
DROP TABLE IF EXISTS calibrator_met2mix_calculations CASCADE;
DROP TABLE IF EXISTS mix_calculations CASCADE;
DROP TABLE IF EXISTS calibrator_levels CASCADE;

-- Batch
DROP TABLE IF EXISTS MS_components CASCADE;
DROP TABLE IF EXISTS MS_sourceParameters CASCADE;
DROP TABLE IF EXISTS MS_information CASCADE;
DROP TABLE IF EXISTS MS_method CASCADE;
DROP TABLE IF EXISTS MS_component_list CASCADE; --drop reference to MS_component until all IS are populated
DROP TABLE IF EXISTS Autosampler_parameters CASCADE;
DROP TABLE IF EXISTS Autosampler_information CASCADE;
DROP TABLE IF EXISTS Autosampler_method CASCADE;
DROP TABLE IF EXISTS LC_information CASCADE;
DROP TABLE IF EXISTS LC_gradient CASCADE;
DROP TABLE IF EXISTS LC_parameters CASCADE;
DROP TABLE IF EXISTS LC_method CASCADE;
DROP TABLE IF EXISTS LC_elution CASCADE;
DROP TABLE IF EXISTS acquisition_method CASCADE;
DROP TABLE IF EXISTS quantitation_method CASCADE;
DROP TABLE IF EXISTS quantitation_method_list CASCADE;

-- Samples
DROP TABLE IF EXISTS metabolomics_sample CASCADE;
DROP TABLE IF EXISTS sample_storage CASCADE;
DROP TABLE IF EXISTS sample_physiologicalParameters CASCADE;
DROP TABLE IF EXISTS sample_description CASCADE;

-- IS
DROP TABLE IF EXISTS metabolomics_IS CASCADE;
DROP TABLE IF EXISTS IS_storage CASCADE;

-- Experiment (modified From OME; specific to metabolomics)
DROP SEQUENCE IF EXISTS wids CASCADE;
CREATE SEQUENCE wids START 1;

DROP TABLE IF EXISTS experiments CASCADE;
DROP TABLE IF EXISTS experiment_types CASCADE;
DROP TABLE IF EXISTS metabolomics_experiment CASCADE;
DROP TABLE IF EXISTS data_stage01 CASCADE;

--Stage 2: Data quality check
DROP TABLE IF EXISTS data_stage02 CASCADE;
DROP TABLE IF EXISTS data_stage02_normalized CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage02_replicates CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage02_averages CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage02_physiologicalRatios_replicates CASCADE;
DROP TABLE IF EXISTS data_stage03_physiologicalRatios_averages CASCADE;

--Stage 3: Missing value imputation and outlier detection
DROP TABLE IF EXISTS data_stage03 CASCADE;
DROP TABLE IF EXISTS data_stage03_normalized CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage03_replicates CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage03_averages CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage03_physiologicalRatios_replicates CASCADE; --make into a view
DROP TABLE IF EXISTS data_stage03_physiologicalRatios_averages CASCADE; --make into a view

--Stage 4: Significant feature identification

--Stage 5: Biological interpretation
--will require integration with a biochemical model
DROP TABLE IF EXISTS thermodynamic_data CASCADE;
DROP TABLE IF EXISTS thermodynamic_analysis CASCADE;
DROP TABLE IF EXISTS thermodynamic_pathwayAnalysis CASCADE;

DROP TABLE IF EXISTS enzymeKinetic_data CASCADE;
DROP TABLE IF EXISTS enzymeKinetic_references CASCADE;
DROP TABLE IF EXISTS enzymeKinetic_analysis CASCADE;



