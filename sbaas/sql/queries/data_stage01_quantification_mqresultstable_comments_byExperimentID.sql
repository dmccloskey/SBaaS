-- query comments from mqresultstable from experiment
SELECT 
  data_stage01_quantification_mqresultstable.sample_name, 
  data_stage01_quantification_mqresultstable.sample_comment, 
  data_stage01_quantification_mqresultstable.component_name, 
  data_stage01_quantification_mqresultstable.component_comment, 
  data_stage01_quantification_mqresultstable.comment_
FROM 
  public.data_stage01_quantification_mqresultstable, 
  public.metabolomics_experiment
WHERE 
  metabolomics_experiment.id LIKE 'ibop_rbc02' AND 
  metabolomics_experiment.metabolomics_sample_name LIKE data_stage01_quantification_mqresultstable.sample_name AND 
  data_stage01_quantification_mqresultstable.used_  AND 
  (data_stage01_quantification_mqresultstable.sample_comment IS NOT NULL  OR 
  data_stage01_quantification_mqresultstable.component_comment IS NOT NULL  OR 
  data_stage01_quantification_mqresultstable.comment_ IS NOT NULL) 
ORDER BY data_stage01_quantification_mqresultstable.component_name,data_stage01_quantification_mqresultstable.sample_name;