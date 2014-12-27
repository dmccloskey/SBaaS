SELECT 
  sample_description.sample_id, 
  sample_description.sample_name_short, 
  sample_description.sample_name_abbreviation
FROM 
  public.metabolomics_experiment, 
  public.metabolomics_sample, 
  public.sample_description
WHERE 
  metabolomics_experiment.id LIKE  'ALEsKOs01' AND 
  metabolomics_experiment.exp_type_id =  4 AND 
  metabolomics_sample.sample_type LIKE 'Unknown' AND
  metabolomics_experiment.metabolomics_sample_name LIKE metabolomics_sample.sample_name AND 
  metabolomics_sample.sample_id LIKE sample_description.sample_id
GROUP BY 
  sample_description.sample_id, 
  sample_description.sample_name_short, 
  sample_description.sample_name_abbreviation
ORDER BY sample_id;
