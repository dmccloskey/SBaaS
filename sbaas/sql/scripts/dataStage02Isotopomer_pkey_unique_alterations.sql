ALTER TABLE "data_stage02_isotopomer_atomMappingMetabolites" DROP CONSTRAINT "data_stage02_isotopomer_atomMappingMetabolites_pkey";

ALTER TABLE "data_stage02_isotopomer_atomMappingMetabolites"
  ADD CONSTRAINT "data_stage02_isotopomer_atomMappingMetabolites_pkey" PRIMARY KEY(id);
  
-- ALTER TABLE "data_stage02_isotopomer_atomMappingMetabolites"
--   ADD CONSTRAINT "data_stage02_isotopomer_atomMappingMetabolites_key" UNIQUE(mapping_id, met_id);
  
ALTER TABLE "data_stage02_isotopomer_atomMappingReactions" DROP CONSTRAINT "data_stage02_isotopomer_atomMapping_pkey1";

ALTER TABLE "data_stage02_isotopomer_atomMappingReactions"
  ADD CONSTRAINT "data_stage02_isotopomer_atomMapping_pkey1" PRIMARY KEY(id);
  
-- ALTER TABLE "data_stage02_isotopomer_atomMappingReactions"
--   ADD CONSTRAINT "data_stage02_isotopomer_atomMapping_key1" UNIQUE(mapping_id, rxn_id);

ALTER TABLE "data_stage02_isotopomer_calcFluxes" DROP CONSTRAINT "data_stage02_isotopomer_calcFluxes_pkey";

ALTER TABLE "data_stage02_isotopomer_calcFluxes"
  ADD CONSTRAINT "data_stage02_isotopomer_calcFluxes_pkey" PRIMARY KEY(id);
--UNIQUE(experiment_id, model_id, mapping_id, sample_name_abbreviation, time_point, rxn_id)

ALTER TABLE "data_stage02_isotopomer_calcFragments" DROP CONSTRAINT "data_stage02_isotopomer_calcFragments_pkey";

ALTER TABLE "data_stage02_isotopomer_calcFragments"
  ADD CONSTRAINT "data_stage02_isotopomer_calcFragments_pkey" PRIMARY KEY(id);
--UNIQUE(experiment_id, mapping_id, sample_name_abbreviation, time_point, fragment_name);

ALTER TABLE data_stage02_isotopomer_experiment DROP CONSTRAINT data_stage02_isotopomer_experiment_pkey;

ALTER TABLE data_stage02_isotopomer_experiment
  ADD CONSTRAINT data_stage02_isotopomer_experiment_pkey PRIMARY KEY(id);
--UNIQUE(experiment_id, model_id, mapping_id, sample_name_abbreviation, time_point);

ALTER TABLE "data_stage02_isotopomer_experimentalFragments" DROP CONSTRAINT "data_stage02_isotopomer_experimentalFragments_pkey";

ALTER TABLE "data_stage02_isotopomer_experimentalFragments"
  ADD CONSTRAINT "data_stage02_isotopomer_experimentalFragments_pkey" PRIMARY KEY(id);
--UNIQUE(experiment_id, sample_name_abbreviation, time_point, met_id, fragment_id, fragment_formula, scan_type);

ALTER TABLE "data_stage02_isotopomer_experimentalPools" DROP CONSTRAINT "data_stage02_isotopomer_experimentalPools_pkey";

ALTER TABLE "data_stage02_isotopomer_experimentalPools"
  ADD CONSTRAINT "data_stage02_isotopomer_experimentalPools_pkey" PRIMARY KEY(id);
--UNIQUE();

ALTER TABLE "data_stage02_isotopomer_modelMetabolites" DROP CONSTRAINT "data_stage02_isotopomer_modelMetabolites_pkey";

ALTER TABLE "data_stage02_isotopomer_modelMetabolites"
  ADD CONSTRAINT "data_stage02_isotopomer_modelMetabolites_pkey" PRIMARY KEY(id);
--UNIQUE(model_id, met_id);

ALTER TABLE "data_stage02_isotopomer_modelReactions" DROP CONSTRAINT "data_stage02_isotopomer_modelReactions_pkey";

ALTER TABLE "data_stage02_isotopomer_modelReactions"
  ADD CONSTRAINT "data_stage02_isotopomer_modelReactions_pkey" PRIMARY KEY(id);
--UNIQUE(model_id, rxn_id);

ALTER TABLE data_stage02_isotopomer_models DROP CONSTRAINT data_stage02_isotopomer_models_pkey;

ALTER TABLE data_stage02_isotopomer_models
  ADD CONSTRAINT data_stage02_isotopomer_models_pkey PRIMARY KEY(id);
ALTER TABLE data_stage02_isotopomer_models
  ADD CONSTRAINT data_stage02_isotopomer_models_key UNIQUE(model_id);
  
ALTER TABLE data_stage02_isotopomer_tracers DROP CONSTRAINT data_stage02_isotopomer_tracers_pkey;

ALTER TABLE data_stage02_isotopomer_tracers
  ADD CONSTRAINT data_stage02_isotopomer_tracers_pkey PRIMARY KEY(id);
--UNIQUE(experiment_id, met_id, met_name);


--UNIQUE();