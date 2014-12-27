﻿ALTER TABLE metabolomics_experiment DROP CONSTRAINT metabolomics_experiment_metabolomics_sample_name_fkey;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey1;

ALTER TABLE metabolomics_sample DROP CONSTRAINT metabolomics_sample_sample_id_fkey2;

UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10-10.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10-100.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10-1000.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11-10.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11-100.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11-1000.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12-10.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12-100.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12-1000.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10-10.0x' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10-100.0x' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10-1000.0x' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16-1000.0x';

UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10-10.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16-10.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10-100.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16-100.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10-1000.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16-1000.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11-10.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17-10.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11-100.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17-100.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11-1000.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17-1000.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12-10.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18-10.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12-100.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18-100.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12-1000.0x',sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18-1000.0x';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10',sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10-10.0x',sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16-10.0x';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10-100.0x',sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16-100.0x';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10-1000.0x',sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16-1000.0x';

UPDATE sample_description SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10', sample_name_short='OxicEvo04Evo02EPEcoli13CGlc_Broth-10', sample_name_abbreviation='OxicEvo04Evo02EPEcoli13CGlc' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16';
UPDATE sample_description SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11', sample_name_short='OxicEvo04Evo02EPEcoli13CGlc_Broth-11', sample_name_abbreviation='OxicEvo04Evo02EPEcoli13CGlc' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17';
UPDATE sample_description SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12', sample_name_short='OxicEvo04Evo02EPEcoli13CGlc_Broth-12', sample_name_abbreviation='OxicEvo04Evo02EPEcoli13CGlc' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18';
UPDATE sample_description SET sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10', sample_name_short='OxicEvo04Evo02EPEcoli13CGlc_Filtrate-10', sample_name_abbreviation='OxicEvo04Evo02EPEcoli13CGlc' WHERE sample_id LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16';

UPDATE sample_storage SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16';
UPDATE sample_storage SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17';
UPDATE sample_storage SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18';
UPDATE sample_storage SET sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE sample_id LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16';

UPDATE sample_physiologicalparameters SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-10' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-16';
UPDATE sample_physiologicalparameters SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-11' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-17';
UPDATE sample_physiologicalparameters SET sample_id='141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-12' WHERE sample_id LIKE '141211_11_OxicEvo04Evo02EPEcoli13CGlcM9_Broth-18';
UPDATE sample_physiologicalparameters SET sample_id='141210_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-10' WHERE sample_id LIKE '141216_11_OxicEvo04Evo02EPEcoli13CGlcM9_Filtrate-16';


UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10-10.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10-100.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10-1000.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11-10.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11-100.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11-1000.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12-10.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12-100.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12-1000.0x' WHERE metabolomics_sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18-1000.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10-10.0x' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16-10.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10-100.0x' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16-100.0x';
UPDATE metabolomics_experiment SET metabolomics_sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10-1000.0x' WHERE metabolomics_sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16-1000.0x';

UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10-10.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16-10.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10-100.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16-100.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10-1000.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16-1000.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11-10.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17-10.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11-100.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17-100.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11-1000.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17-1000.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12-10.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18-10.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12-100.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18-100.0x';
UPDATE metabolomics_sample SET sample_name='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12-1000.0x',sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE sample_name LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18-1000.0x';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10',sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10-10.0x',sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16-10.0x';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10-100.0x',sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16-100.0x';
UPDATE metabolomics_sample SET sample_name='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10-1000.0x',sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE sample_name LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16-1000.0x';

UPDATE sample_description SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10', sample_name_short='OxicEvo04sdhCBEvo03EPEcoli13CGlc_Broth-10', sample_name_abbreviation='OxicEvo04sdhCBEvo03EPEcoli13CGlc' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16';
UPDATE sample_description SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11', sample_name_short='OxicEvo04sdhCBEvo03EPEcoli13CGlc_Broth-11', sample_name_abbreviation='OxicEvo04sdhCBEvo03EPEcoli13CGlc' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17';
UPDATE sample_description SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12', sample_name_short='OxicEvo04sdhCBEvo03EPEcoli13CGlc_Broth-12', sample_name_abbreviation='OxicEvo04sdhCBEvo03EPEcoli13CGlc' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18';
UPDATE sample_description SET sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10', sample_name_short='OxicEvo04sdhCBEvo03EPEcoli13CGlc_Filtrate-10', sample_name_abbreviation='OxicEvo04sdhCBEvo03EPEcoli13CGlc' WHERE sample_id LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16';

UPDATE sample_storage SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16';
UPDATE sample_storage SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17';
UPDATE sample_storage SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18';
UPDATE sample_storage SET sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE sample_id LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16';

UPDATE sample_physiologicalparameters SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-10' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-16';
UPDATE sample_physiologicalparameters SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-11' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-17';
UPDATE sample_physiologicalparameters SET sample_id='141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-12' WHERE sample_id LIKE '141211_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Broth-18';
UPDATE sample_physiologicalparameters SET sample_id='141210_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-10' WHERE sample_id LIKE '141216_11_OxicEvo04sdhCBEvo03EPEcoli13CGlcM9_Filtrate-16';

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