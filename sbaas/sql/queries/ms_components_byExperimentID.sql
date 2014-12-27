SELECT  
  ms_components.q1_mass, 
  ms_components.q3_mass, 
  ms_components.met_id, 
  ms_components.component_name, 
  ms_components.ms_methodtype
FROM 
  public.metabolomics_experiment, 
  public.acquisition_method, 
  public.ms_method, 
  public.ms_component_list, 
  public.ms_components
WHERE 
  metabolomics_experiment.id LIKE 'WTEColi12C01' AND 
  metabolomics_experiment.acquisition_method_id LIKE acquisition_method.id AND 
  acquisition_method.ms_method_id LIKE ms_method.id AND 
  ms_method.id LIKE ms_component_list.ms_method_id AND
--   ms_component_list.q1_mass = ms_components.q1_mass AND
--   ms_component_list.q3_mass = ms_components.q3_mass AND
--   ms_component_list.met_id LIKE ms_components.met_id AND
  ms_component_list.component_name = ms_components.component_name AND
  ms_components.ms_include
GROUP BY
  ms_components.q1_mass, 
  ms_components.q3_mass, 
  ms_components.met_id, 
  ms_components.component_name, 
  ms_components.ms_methodtype
ORDER BY 
  ms_components.met_id,
  ms_components.q1_mass, 
  ms_components.q3_mass;