SELECT metabolomics_sample.sample_name, metabolomics_sample.sample_type, metabolomics_sample.calibrator_id, metabolomics_sample.calibrator_level, metabolomics_sample.sample_id, 
       metabolomics_sample.sample_dilution
  FROM metabolomics_sample, metabolomics_experiment
  WHERE metabolomics_sample.sample_name LIKE metabolomics_experiment.metabolomics_sample_name
	AND metabolomics_experiment.id LIKE 'WTEColi12C01';