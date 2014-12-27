SELECT sample_description.sample_id, sample_description.sample_name_short, sample_description.sample_name_abbreviation, sample_description.sample_date, 
       sample_description.time_point, sample_description.sample_condition, sample_description.extraction_method_id, sample_description.biological_material, 
       sample_description.sample_description, sample_description.sample_replicate, sample_description.is_added, sample_description.is_added_units, 
       sample_description.reconsitution_volume, sample_description.reconstitution_volume_units, sample_description.istechnical, 
       sample_description.sample_replicate_biological
  FROM sample_description, metabolomics_sample, metabolomics_experiment
  WHERE sample_description.sample_id LIKE metabolomics_sample.sample_id
	AND metabolomics_sample.sample_name LIKE metabolomics_experiment.metabolomics_sample_name
	AND metabolomics_experiment.id LIKE 'WTEColi12C01';
