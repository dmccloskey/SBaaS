ALTER TABLE metabolomics_experiment DROP CONSTRAINT metabolomics_experiment_metabolomics_sample_name_fkey;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey1;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey2;

UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-10.0x' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-100.0x' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-1000.0x' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-10.0x' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-100.0x' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-1000.0x' WHERE metabolomics_sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7-1000.0x';

UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5',sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-10.0x',sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8-10.0x';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-100.0x',sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8-100.0x';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-1000.0x',sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE sample_name LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8-1000.0x';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4',sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-10.0x',sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7-10.0x';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-100.0x',sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7-100.0x';
UPDATE metabolomics_sample SET sample_name='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-1000.0x',sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE sample_name LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7-1000.0x';

UPDATE sample_physiologicalparameters SET sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE sample_id LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8';
UPDATE sample_physiologicalparameters SET sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE sample_id LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7';

UPDATE sample_description SET sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5', sample_name_short='OxicEvo04ptsHIcrrEvo04EPEcoli13CGlc_Broth-5', sample_name_abbreviation='OxicEvo04ptsHIcrrEvo04EPEcoli13CGlc' WHERE sample_id LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8';
UPDATE sample_description SET sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4', sample_name_short='OxicEvo04tpiAEvo01EPEcoli13CGlc_Broth-4', sample_name_abbreviation='OxicEvo04tpiAEvo01EPEcoli13CGlc' WHERE sample_id LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7';

UPDATE sample_storage SET sample_id='141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' WHERE sample_id LIKE '141125_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-8';
UPDATE sample_storage SET sample_id='141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' WHERE sample_id LIKE '141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-7';

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