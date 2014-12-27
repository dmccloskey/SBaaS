SELECT exp_type_id, id, metabolomics_sample_name, metabolomics_experimentor_id, 
       extraction_method_id, acquisition_method_id, quantitation_method_id, 
       metabolomics_is_id
  FROM metabolomics_experiment
  WHERE id LIKE 'WTEColi12C01';


