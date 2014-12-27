SELECT 
  ms_method.id, 
  ms_method.ms_sourceparameters_id, 
  ms_method.ms_information_id, 
  ms_method.ms_experiment_id
FROM 
  public.metabolomics_experiment, 
  public.acquisition_method, 
  public.ms_method, 
  public.ms_component_list
WHERE 
  metabolomics_experiment.id LIKE 'WTEColi12C01' AND 
  metabolomics_experiment.acquisition_method_id LIKE acquisition_method.id AND 
  acquisition_method.ms_method_id LIKE ms_method.id
GROUP BY
  ms_method.id, 
  ms_method.ms_sourceparameters_id, 
  ms_method.ms_information_id, 
  ms_method.ms_experiment_id
ORDER BY 
  ms_method.id;
