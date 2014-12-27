-- query calibration parameters from experiment and met_id
SELECT 
  quantitation_method.met_id, 
  quantitation_method.component_name, 
  --quantitation_method.intercept, 
  --quantitation_method.slope, 
  quantitation_method.correlation, 
  quantitation_method.lloq, 
  quantitation_method.uloq, 
  quantitation_method.points
FROM 
  public.quantitation_method, 
  public.data_stage01_quantification_mqresultstable, 
  public.metabolomics_experiment
WHERE 
  metabolomics_experiment.id LIKE 'rpomut01' AND 
  metabolomics_experiment.metabolomics_sample_name LIKE data_stage01_quantification_mqresultstable.sample_name AND 
  metabolomics_experiment.quantitation_method_id LIKE quantitation_method.id AND 
  quantitation_method.component_name LIKE ddata_stage01_quantification_mqresultstable.component_name AND 
  data_stage01_quantification_mqresultstable.used_ AND 
  (
  quantitation_method.met_id LIKE 'f6p' OR
  quantitation_method.met_id LIKE 's7p' OR
  quantitation_method.met_id LIKE 'glyc3p' OR
  --quantitation_method.met_id LIKE 'dcdp' OR
  quantitation_method.met_id LIKE 'dgmp'
  )
GROUP BY quantitation_method.met_id, 
  quantitation_method.component_name, 
  quantitation_method.intercept, 
  quantitation_method.slope, 
  quantitation_method.correlation, 
  quantitation_method.lloq, 
  quantitation_method.uloq, 
  quantitation_method.points;