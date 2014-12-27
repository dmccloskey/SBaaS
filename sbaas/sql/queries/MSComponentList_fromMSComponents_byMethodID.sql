SELECT 
  ms_components.q1_mass, 
  ms_components.q3_mass,  
  ms_components.met_id,
  ms_components.met_name, 
  ms_components.component_name, 
  ms_components.ms_methodtype
FROM  
  public.ms_components
WHERE 
  ms_components.ms_methodtype LIKE 'quantification' AND
  ms_components.ms_include
ORDER BY
  ms_components.component_name ASC;
