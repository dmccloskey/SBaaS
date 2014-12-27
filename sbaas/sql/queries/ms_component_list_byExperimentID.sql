SELECT  
  ms_component_list.q1_mass, 
  ms_component_list.q3_mass, 
  ms_component_list.met_id, 
  ms_component_list.component_name, 
  ms_component_list.ms_methodtype
FROM 
  public.metabolomics_experiment, 
  public.acquisition_method, 
  public.ms_method, 
  public.ms_component_list
WHERE 
  metabolomics_experiment.id LIKE 'WTEColi12C01' AND 
  metabolomics_experiment.acquisition_method_id LIKE acquisition_method.id AND 
  acquisition_method.ms_method_id LIKE ms_method.id AND 
  ms_method.id LIKE ms_component_list.ms_method_id
GROUP BY
  ms_component_list.ms_method_id, 
  ms_component_list.q1_mass, 
  ms_component_list.q3_mass, 
  ms_component_list.met_id, 
  ms_component_list.component_name, 
  ms_component_list.ms_methodtype
ORDER BY 
  ms_component_list.ms_method_id, 
  ms_component_list.met_id,
  ms_component_list.q1_mass, 
  ms_component_list.q3_mass;