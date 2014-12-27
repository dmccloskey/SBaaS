SELECT sample_storage.sample_id, sample_storage.sample_label, sample_storage.ph, sample_storage.box, sample_storage.pos
  FROM sample_storage, metabolomics_sample, metabolomics_experiment
  WHERE sample_storage.sample_id LIKE metabolomics_sample.sample_id
	AND metabolomics_sample.sample_name LIKE metabolomics_experiment.metabolomics_sample_name
	AND metabolomics_experiment.id LIKE 'WTEColi12C01';
