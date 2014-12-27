-- query unknown samples from experiment
SELECT 
  data_stage01_quantification_mqresultstable.sample_name
FROM 
  public.data_stage01_quantification_mqresultstable,
  public.metabolomics_experiment
WHERE 
  data_stage01_quantification_mqresultstable.sample_type LIKE 'Unknown' AND
  metabolomics_experiment.id LIKE 'nadisotopomer02' AND
  metabolomics_experiment.metabolomics_sample_name LIKE data_stage01_quantification_mqresultstable.sample_name
GROUP BY data_stage01_quantification_mqresultstable.sample_name
ORDER BY data_stage01_quantification_mqresultstable.sample_name ASC;

-- query unknown samples (sample_name, component_name, height) 
-- that are used from experiment
SELECT 
  data_stage01_quantification_mqresultstable.sample_name,
  --data_stage01_quantification_mqresultstable.sample_comment,
  data_stage01_quantification_mqresultstable.component_group_name,
  data_stage01_quantification_mqresultstable.component_name,
  --data_stage01_quantification_mqresultstable.component_comment,
  data_stage01_quantification_mqresultstable.height
  --data_stage01_quantification_mqresultstable.comment_
FROM 
  public.data_stage01_quantification_mqresultstable,
  public.metabolomics_experiment
WHERE 
  data_stage01_quantification_mqresultstable.sample_type LIKE 'Unknown' AND
  metabolomics_experiment.id LIKE 'nadisotopomer02' AND
  metabolomics_experiment.metabolomics_sample_name LIKE data_stage01_quantification_mqresultstable.sample_name AND
  --(data_stage01_quantification_mqresultstable.sample_comment IS NOT NULL OR
  --data_stage01_quantification_mqresultstable.component_comment IS NOT NULL OR 
  --data_stage01_quantification_mqresultstable.comment_ IS NOT NULL)
  data_stage01_quantification_mqresultstable.used_
ORDER BY data_stage01_quantification_mqresultstable.sample_name ASC, data_stage01_quantification_mqresultstable.component_name ASC;