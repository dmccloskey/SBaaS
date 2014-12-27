ALTER TABLE metabolomics_experiment DROP CONSTRAINT metabolomics_experiment_metabolomics_sample_name_fkey;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey1;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey2;

UPDATE metabolomics_experiment
   SET metabolomics_sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE metabolomics_sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE metabolomics_experiment
   SET metabolomics_sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE metabolomics_sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE metabolomics_experiment
   SET metabolomics_sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE metabolomics_sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE metabolomics_experiment
   SET metabolomics_sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE metabolomics_sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';

 UPDATE metabolomics_sample
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1',
       sample_id='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE metabolomics_sample
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1',
       sample_id='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE metabolomics_sample
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1',
       sample_id='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE metabolomics_sample
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1',
       sample_id='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE sample_description
   SET sample_id='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE sample_description
   SET sample_id='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE sample_description
   SET sample_id='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE sample_description
   SET sample_id='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE sample_storage
   SET sample_id='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE sample_storage
   SET sample_id='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE sample_storage
   SET sample_id='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE sample_storage
   SET sample_id='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE sample_physiologicalparameters
   SET sample_id='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE sample_physiologicalparameters
   SET sample_id='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE sample_physiologicalparameters
   SET sample_id='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE sample_physiologicalparameters
   SET sample_id='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_id LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_endpoints
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_endpoints
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_endpoints
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_endpoints
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE data_stage01_resequencing_evidence
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_evidence
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_evidence
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_evidence
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE data_stage01_resequencing_lineage
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_lineage
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_lineage
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_lineage
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE data_stage01_resequencing_metadata
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_metadata
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_metadata
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_metadata
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE data_stage01_resequencing_mutations
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_mutations
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_mutations
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_mutations
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE "data_stage01_resequencing_mutationsAnnotated"
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE "data_stage01_resequencing_mutationsAnnotated"
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE "data_stage01_resequencing_mutationsAnnotated"
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE "data_stage01_resequencing_mutationsAnnotated"
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE "data_stage01_resequencing_mutationsFiltered"
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE "data_stage01_resequencing_mutationsFiltered"
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE "data_stage01_resequencing_mutationsFiltered"
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE "data_stage01_resequencing_mutationsFiltered"
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';
 
 UPDATE data_stage01_resequencing_validation
   SET sample_name='140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_validation
   SET sample_name='140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_validation
   SET sample_name='140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1';

 UPDATE data_stage01_resequencing_validation
   SET sample_name='140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1'
 WHERE sample_name LIKE '140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1';

ALTER TABLE metabolomics_experiment
  ADD CONSTRAINT metabolomics_experiment_metabolomics_sample_name_fkey FOREIGN KEY (metabolomics_sample_name)
      REFERENCES metabolomics_sample (sample_name) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE metabolomics_sample
  ADD CONSTRAINT metabolomics_sample_sample_id_fkey FOREIGN KEY (sample_id)
      REFERENCES sample_storage (sample_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;
	  
ALTER TABLE metabolomics_sample
  ADD CONSTRAINT metabolomics_sample_sample_id_fkey1 FOREIGN KEY (sample_id)
      REFERENCES sample_physiologicalparameters (sample_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;
	  
ALTER TABLE metabolomics_sample
  ADD CONSTRAINT metabolomics_sample_sample_id_fkey2 FOREIGN KEY (sample_id)
      REFERENCES sample_description (sample_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;