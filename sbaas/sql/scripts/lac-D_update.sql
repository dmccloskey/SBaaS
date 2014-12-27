ALTER TABLE standards2material DROP CONSTRAINT standards2material_met_id_fkey;
      
ALTER TABLE standards2material DROP CONSTRAINT standards2material_met_id_fkey1;

ALTER TABLE standards_storage DROP CONSTRAINT standards_storage_met_id_fkey;

ALTER TABLE ms_component_list DROP CONSTRAINT ms_component_list_ms_method_id_fkey;

ALTER TABLE metabolomics_calibrator DROP CONSTRAINT metabolomics_calibrator_met_id_fkey;

UPDATE ms_components SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE ms_components SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE ms_components SET component_name='lac-D.lac-D_m0-0' WHERE component_name LIKE 'lac-L.lac-L_m0-0';
UPDATE ms_components SET component_name='lac-D.lac-D_m1-0' WHERE component_name LIKE 'lac-L.lac-L_m1-0';
UPDATE ms_components SET component_name='lac-D.lac-D_m1-1' WHERE component_name LIKE 'lac-L.lac-L_m1-1';
UPDATE ms_components SET component_name='lac-D.lac-D_m2-1' WHERE component_name LIKE 'lac-L.lac-L_m2-1';
UPDATE ms_components SET component_name='lac-D.lac-D_m2-2' WHERE component_name LIKE 'lac-L.lac-L_m2-2';
UPDATE ms_components SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE ms_components SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE ms_components SET component_name='lac-D.lac-D_m3-2' WHERE component_name LIKE 'lac-L.lac-L_m3-2';
UPDATE ms_components SET ms_group='lac-D' WHERE ms_group LIKE 'lac-L';
UPDATE ms_components SET ms_group='lac-D.lac-D_m0-0' WHERE ms_group LIKE 'lac-L.lac-L_m0-0';
UPDATE ms_components SET ms_group='lac-D.lac-D_m1-0' WHERE ms_group LIKE 'lac-L.lac-L_m1-0';
UPDATE ms_components SET ms_group='lac-D.lac-D_m1-1' WHERE ms_group LIKE 'lac-L.lac-L_m1-1';
UPDATE ms_components SET ms_group='lac-D.lac-D_m2-1' WHERE ms_group LIKE 'lac-L.lac-L_m2-1';
UPDATE ms_components SET ms_group='lac-D.lac-D_m2-2' WHERE ms_group LIKE 'lac-L.lac-L_m2-2';
UPDATE ms_components SET ms_group='lac-D-UC13' WHERE ms_group LIKE 'lac-L-UC13';
UPDATE ms_components SET ms_group='lac-D.lac-D_m3-2' WHERE ms_group LIKE 'lac-L.lac-L_m3-2';
UPDATE ms_components SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE ms_component_list SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE ms_component_list SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE ms_component_list SET component_name='lac-D.lac-D_m0-0' WHERE component_name LIKE 'lac-L.lac-L_m0-0';
UPDATE ms_component_list SET component_name='lac-D.lac-D_m1-0' WHERE component_name LIKE 'lac-L.lac-L_m1-0';
UPDATE ms_component_list SET component_name='lac-D.lac-D_m1-1' WHERE component_name LIKE 'lac-L.lac-L_m1-1';
UPDATE ms_component_list SET component_name='lac-D.lac-D_m2-1' WHERE component_name LIKE 'lac-L.lac-L_m2-1';
UPDATE ms_component_list SET component_name='lac-D.lac-D_m2-2' WHERE component_name LIKE 'lac-L.lac-L_m2-2';
UPDATE ms_component_list SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE ms_component_list SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE ms_component_list SET component_name='lac-D.lac-D_m3-2' WHERE component_name LIKE 'lac-L.lac-L_m3-2';
UPDATE ms_component_list SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE calibrator_met_parameters SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE calibrator_concentrations SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE standards2material SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE standards_ordering SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE standards_ordering SET met_name='D-Lactate' WHERE met_name LIKE 'L-Lactate';
UPDATE standards_storage SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE standards_storage SET met_name='D-Lactate' WHERE met_name LIKE 'L-Lactate';
UPDATE data_stage01_physiology_data SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE data_stage01_physiology_rates SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_physiology_ratesAverages" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE data_stage01_isotopomer_averages SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_averagesNormSum" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_name='lac-D.lac-D_m0-0' WHERE component_name LIKE 'lac-L.lac-L_m0-0';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_name='lac-D.lac-D_m1-0' WHERE component_name LIKE 'lac-L.lac-L_m1-0';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_name='lac-D.lac-D_m1-1' WHERE component_name LIKE 'lac-L.lac-L_m1-1';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_name='lac-D.lac-D_m2-1' WHERE component_name LIKE 'lac-L.lac-L_m2-1';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_name='lac-D.lac-D_m2-2' WHERE component_name LIKE 'lac-L.lac-L_m2-2';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_name='lac-D.lac-D_m3-2' WHERE component_name LIKE 'lac-L.lac-L_m3-2';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_group_name='lac-D.lac-D_m0-0' WHERE component_group_name LIKE 'lac-L.lac-L_m0-0';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_group_name='lac-D.lac-D_m1-0' WHERE component_group_name LIKE 'lac-L.lac-L_m1-0';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_group_name='lac-D.lac-D_m1-1' WHERE component_group_name LIKE 'lac-L.lac-L_m1-1';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_group_name='lac-D.lac-D_m2-1' WHERE component_group_name LIKE 'lac-L.lac-L_m2-1';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_group_name='lac-D.lac-D_m2-2' WHERE component_group_name LIKE 'lac-L.lac-L_m2-2';
UPDATE "data_stage01_isotopomer_mqresultstable" SET component_group_name='lac-D.lac-D_m3-2' WHERE component_group_name LIKE 'lac-L.lac-L_m3-2';
UPDATE data_stage01_isotopomer_normalized SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_peakData" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_peakList" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_peakSpectrum" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_spectrumAccuracy" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage01_isotopomer_spectrumAccuracyNormSum" SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE "data_stage02_quantification_anova" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage02_quantification_anova" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage02_quantification_anova" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage02_quantification_descriptiveStats" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage02_quantification_descriptiveStats" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage02_quantification_descriptiveStats" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage02_quantification_glogNormalized" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage02_quantification_glogNormalized" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage02_quantification_glogNormalized" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage02_quantification_pairWiseTest" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage02_quantification_pairWiseTest" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage02_quantification_pairWiseTest" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage02_quantification_pca_loadings" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage02_quantification_pca_loadings" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage02_quantification_pca_loadings" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_checkISMatch" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_checkISMatch" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_checkISMatch" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_checkISMatch" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_averages" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_averages" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_averages" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_averages" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_averages" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_averagesmi" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_averagesmi" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_averagesmi" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_averagesmi" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_averagesmi" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_averagesmigeo" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_averagesmigeo" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_averagesmigeo" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_averagesmigeo" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_averagesmigeo" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_checkCV_dilutions" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_checkCV_dilutions" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_checkCV_dilutions" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_checkCV_dilutions" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_checkCV_dilutions" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_checkCV_QCs" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_checkCV_QCs" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_checkCV_QCs" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_checkCV_QCs" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_checkCV_QCs" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_checkCVAndExtracellular_averages" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_checkCVAndExtracellular_averages" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_checkCVAndExtracellular_averages" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_checkCVAndExtracellular_averages" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_checkCVAndExtracellular_averages" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_checkLLOQAndULOQ" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_checkLLOQAndULOQ" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_checkLLOQAndULOQ" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_checkLLOQAndULOQ" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_checkLLOQAndULOQ" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_dilutions" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_dilutions" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_dilutions" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_dilutions" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_dilutions" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_LLOQAndULOQ" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_LLOQAndULOQ" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_LLOQAndULOQ" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_LLOQAndULOQ" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_LLOQAndULOQ" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_mqresultstable" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_mqresultstable" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_mqresultstable" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_mqresultstable" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_mqresultstable" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_normalized" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_normalized" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_normalized" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_normalized" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_normalized" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_peakInformation" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_peakInformation" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_peakInformation" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_peakInformation" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_peakInformation" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_QCs" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_QCs" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_QCs" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_QCs" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_QCs" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_replicates" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_replicates" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_replicates" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_replicates" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_replicates" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE "data_stage01_quantification_replicatesmi" SET component_name='lac-D.lac-D_1.Light' WHERE component_name LIKE 'lac-L.lac-L_1.Light';
UPDATE "data_stage01_quantification_replicatesmi" SET component_name='lac-D.lac-D_2.Light' WHERE component_name LIKE 'lac-L.lac-L_2.Light';
UPDATE "data_stage01_quantification_replicatesmi" SET component_name='lac-D.lac-D_1.Heavy' WHERE component_name LIKE 'lac-L.lac-L_1.Heavy';
UPDATE "data_stage01_quantification_replicatesmi" SET component_name='lac-D.lac-D_2.Heavy' WHERE component_name LIKE 'lac-L.lac-L_2.Heavy';
UPDATE "data_stage01_quantification_replicatesmi" SET component_group_name='lac-D' WHERE component_group_name LIKE 'lac-L';
UPDATE metabolomics_standards SET met_id='lac-D' WHERE met_id LIKE 'lac-L';
UPDATE metabolomics_standards SET met_name='D-Lactate' WHERE met_name LIKE 'L-Lactate';
UPDATE metabolomics_calibrator SET met_id='lac-D' WHERE met_id LIKE 'lac-L';

ALTER TABLE standards2material
  ADD CONSTRAINT standards2material_met_id_fkey FOREIGN KEY (met_id)
      REFERENCES metabolomics_standards (met_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE standards2material
  ADD CONSTRAINT standards2material_met_id_fkey1 FOREIGN KEY (met_id, provider, provider_reference)
      REFERENCES standards_ordering (met_id, provider, provider_reference) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE standards_storage
  ADD CONSTRAINT standards_storage_met_id_fkey FOREIGN KEY (met_id, provider, provider_reference)
      REFERENCES standards2material (met_id, provider, provider_reference) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE ms_component_list
  ADD CONSTRAINT ms_component_list_ms_method_id_fkey FOREIGN KEY (ms_method_id)
      REFERENCES ms_method (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE NO ACTION;

ALTER TABLE metabolomics_calibrator
  ADD CONSTRAINT metabolomics_calibrator_met_id_fkey FOREIGN KEY (met_id, stockdate)
      REFERENCES standards_storage (met_id, stockdate) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;

-- ALTER TABLE calibrator_met2mix_calculations DROP CONSTRAINT calibrator_met2mix_calculations_met_id_fkey;
-- 
-- ALTER TABLE calibrator_met2mix_calculations
--   ADD CONSTRAINT calibrator_met2mix_calculations_met_id_fkey FOREIGN KEY (met_id)
--       REFERENCES calibrator_met_parameters (met_id) MATCH SIMPLE
--       ON UPDATE NO ACTION ON DELETE NO ACTION;
-- 
-- ALTER TABLE calibrator_met2mix_calculations DROP CONSTRAINT calibrator_met2mix_calculations_met_id_fkey1;
-- 
-- ALTER TABLE calibrator_met2mix_calculations
--   ADD CONSTRAINT calibrator_met2mix_calculations_met_id_fkey1 FOREIGN KEY (met_id)
--       REFERENCES calibrator_calculations (met_id) MATCH SIMPLE
--       ON UPDATE NO ACTION ON DELETE NO ACTION;
-- 
-- ALTER TABLE calibrator_met2mix_calculations DROP CONSTRAINT calibrator_met2mix_calculations_mix_id_fkey;
-- 
-- ALTER TABLE calibrator_met2mix_calculations
--   ADD CONSTRAINT calibrator_met2mix_calculations_mix_id_fkey FOREIGN KEY (mix_id)
--       REFERENCES mix_calculations (mix_id) MATCH SIMPLE
--       ON UPDATE NO ACTION ON DELETE NO ACTION;
-- 
-- 
-- ALTER TABLE calibrator_met2mix_calculations DROP CONSTRAINT calibrator_met2mix_calculations_mix_id_fkey1;
-- 
-- ALTER TABLE calibrator_met2mix_calculations
--   ADD CONSTRAINT calibrator_met2mix_calculations_mix_id_fkey1 FOREIGN KEY (mix_id)
--       REFERENCES mix_parameters (mix_id) MATCH SIMPLE
--       ON UPDATE NO ACTION ON DELETE NO ACTION;
