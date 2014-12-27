-- query acquisition method parameters for ms_methodtype and lc_method_id
SELECT 
  ms_components.component_name, 
  ms_components.met_id, 
  ms_components.met_name, 
  ms_components.q1_mass, 
  ms_components.q3_mass, 
  ms_components.dp, 
  ms_components.ep, 
  ms_components.ce, 
  ms_components.cxp, 
  ms_components.precursor_formula, 
  ms_components.product_formula, 
  ms_components.quantifier, 
  ms_components.ms_group, 
  ms_components.threshold, 
  ms_components.dwell_weight, 
  ms_components.dp_units, 
  ms_components.ep_units, 
  ms_components.ce_units, 
  ms_components.cxp_units, 
  lc_elution.rt, 
  lc_elution.ms_window, 
  lc_elution.rt_units, 
  lc_elution.window_units
FROM 
  public.ms_components, 
  public.ms_component_list, 
  public.lc_elution
WHERE 
  ms_components.ms_methodtype LIKE 'isotopomer_13C' AND 
  ms_components.met_id LIKE lc_elution.met_id AND 
  lc_elution.lc_method_id LIKE 'McCloskey2013' AND
  ms_components.ms_include
GROUP BY 
  ms_components.component_name, 
  ms_components.met_id, 
  ms_components.met_name, 
  ms_components.q1_mass, 
  ms_components.q3_mass, 
  ms_components.dp, 
  ms_components.ep, 
  ms_components.ce, 
  ms_components.cxp, 
  ms_components.precursor_formula, 
  ms_components.product_formula, 
  ms_components.quantifier, 
  ms_components.ms_group, 
  ms_components.threshold, 
  ms_components.dwell_weight, 
  ms_components.dp_units, 
  ms_components.ep_units, 
  ms_components.ce_units, 
  ms_components.cxp_units, 
  lc_elution.rt, 
  lc_elution.ms_window, 
  lc_elution.rt_units, 
  lc_elution.window_units
ORDER BY
  lc_elution.rt ASC,
  ms_components.component_name ASC;