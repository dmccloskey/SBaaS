-- QC of lloq and uloq
-- components outside the lloq and uloq
SELECT 
  data_stage01_mqresultstable.sample_name, 
  data_stage01_mqresultstable.component_group_name, 
  data_stage01_mqresultstable.component_name, 
  data_stage01_mqresultstable.calculated_concentration, 
  data_stage01_mqresultstable.conc_units, 
  quantitation_method.correlation, 
  quantitation_method.lloq, 
  quantitation_method.uloq, 
  quantitation_method.points
FROM 
  public.data_stage01_mqresultstable, 
  public.quantitation_method, 
  public.metabolomics_experiment
WHERE 
  metabolomics_experiment.id LIKE 'nitrate01' AND --change per experiment
  metabolomics_experiment.metabolomics_sample_name LIKE data_stage01_mqresultstable.sample_name AND 
  metabolomics_experiment.quantitation_method_id LIKE quantitation_method.id AND 
  data_stage01_mqresultstable.component_name LIKE quantitation_method.component_name AND 
  NOT data_stage01_mqresultstable.is_  AND 
  data_stage01_mqresultstable.used_ AND
  (data_stage01_mqresultstable.sample_type LIKE 'Unknown' OR
  data_stage01_mqresultstable.sample_type LIKE 'Quality Control')
  quantitation_method.points > 0 AND
  (data_stage01_mqresultstable.calculated_concentration < quantitation_method.lloq OR
  data_stage01_mqresultstable.calculated_concentration > quantitation_method.uloq)
ORDER BY
  data_stage01_mqresultstable.component_name ASC, 
  data_stage01_mqresultstable.sample_name ASC;