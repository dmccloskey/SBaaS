SELECT 
  ms_components.q1_mass, 
  ms_components.q3_mass, 
  lc_elution.rt, 
  ms_components.component_name, 
  ms_components.ms_group, 
  lc_elution.ms_window, 
  ms_components.quantifier, 
  ms_components.threshold, 
  ms_components.dwell_weight, 
  ms_components.dp, 
  ms_components.ep, 
  ms_components.ce, 
  ms_components.cxp, 
  ms_components.ms_include, 
  ms_components.precursor_formula, 
  ms_components.product_formula
FROM 
  public.lc_elution, 
  public.ms_components
WHERE 
  ms_components.met_id LIKE lc_elution.met_id AND 
  lc_elution.lc_method_id LIKE 'McCloskey2013' AND 
  ms_components.ms_methodtype LIKE 'quantification' AND
  ms_components.ms_include
ORDER BY
  lc_elution.rt ASC, 
  ms_components.component_name ASC;
