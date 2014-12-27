SELECT 
  acquisition_method.id, 
  acquisition_method.ms_method_id, 
  acquisition_method.autosampler_method_id, 
  acquisition_method.lc_method_id
FROM 
  public.metabolomics_experiment, 
  public.acquisition_method, 
  public.ms_method, 
  public.ms_component_list
WHERE 
  metabolomics_experiment.id LIKE 'WTEColi12C01' AND 
  metabolomics_experiment.acquisition_method_id LIKE acquisition_method.id
GROUP BY 
  acquisition_method.id, 
  acquisition_method.ms_method_id, 
  acquisition_method.autosampler_method_id, 
  acquisition_method.lc_method_id
ORDER BY 
  acquisition_method.id;
