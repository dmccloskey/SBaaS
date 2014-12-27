﻿SELECT sample_physiologicalparameters.sample_id, sample_physiologicalparameters.growth_condition_short, sample_physiologicalparameters.growth_condition_long, sample_physiologicalparameters.media_short, 
       sample_physiologicalparameters.media_long, sample_physiologicalparameters.isoxic, sample_physiologicalparameters.temperature, sample_physiologicalparameters.supplementation, sample_physiologicalparameters.od600, sample_physiologicalparameters.vcd, 
       sample_physiologicalparameters.culture_density, sample_physiologicalparameters.culture_volume_sampled, sample_physiologicalparameters.cells, sample_physiologicalparameters.dcw, sample_physiologicalparameters.wcw, sample_physiologicalparameters.vcd_units, 
       sample_physiologicalparameters.culture_density_units, sample_physiologicalparameters.culture_volume_sampled_units, sample_physiologicalparameters.dcw_units, 
       sample_physiologicalparameters.wcw_units
  FROM sample_physiologicalparameters, metabolomics_sample, metabolomics_experiment
  WHERE sample_physiologicalparameters.sample_id LIKE metabolomics_sample.sample_id
	AND metabolomics_sample.sample_name LIKE metabolomics_experiment.metabolomics_sample_name
	AND metabolomics_experiment.id LIKE 'WTEColi12C01';
