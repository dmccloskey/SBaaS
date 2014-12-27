ALTER TABLE "data_stage02_physiology_experimentalFluxes" DROP CONSTRAINT "data_stage02_physiology_experimentalFluxes_pkey";

ALTER TABLE "data_stage02_physiology_experimentalFluxes"
  ADD CONSTRAINT "data_stage02_physiology_experimentalFluxes_pkey" PRIMARY KEY(id);

ALTER TABLE "data_stage02_physiology_experimentalFluxes"
  ADD CONSTRAINT "data_stage02_physiology_experimentalFluxes_key" UNIQUE(experiment_id, sample_name_abbreviation, rxn_id);
