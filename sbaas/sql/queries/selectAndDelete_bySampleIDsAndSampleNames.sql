--Part 1: query the sample_names
-- SELECT 
--   metabolomics_sample.sample_name
-- FROM 
--   public.metabolomics_experiment, 
--   public.metabolomics_sample
-- WHERE 
--   metabolomics_experiment.id LIKE  'ALEsKOs01' AND 
--   metabolomics_sample.sample_name LIKE metabolomics_experiment.metabolomics_sample_name AND 
--   (metabolomics_sample.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2' OR
-- metabolomics_sample.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' OR
-- metabolomics_sample.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1' OR
-- metabolomics_sample.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4')
-- GROUP BY 
--   metabolomics_sample.sample_name;

 --Part 2: delete the sample_names in order
 DELETE FROM metabolomics_experiment
 WHERE metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-10.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2-10.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-100.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-100.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-10.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-1000.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2-1000.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2-100.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-10.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-1000.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-100.0x' OR
metabolomics_experiment.metabolomics_sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-1000.0x';

 DELETE FROM metabolomics_sample
 WHERE metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-10.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2-10.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-100.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-100.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-10.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-1000.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2-1000.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2-100.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-10.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-1000.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-100.0x' OR
metabolomics_sample.sample_name LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5-1000.0x';

 DELETE FROM sample_description
 WHERE sample_description.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2' OR
sample_description.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' OR
sample_description.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1' OR
sample_description.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4';

 DELETE FROM sample_storage
 WHERE sample_storage.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2' OR
sample_storage.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' OR
sample_storage.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1' OR
sample_storage.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4';

 DELETE FROM sample_physiologicalparameters
 WHERE sample_physiologicalparameters.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-2' OR
sample_physiologicalparameters.sample_id LIKE '141021_11_OxicEvo04ptsHIcrrEvo04EPEcoli13CGlcM9_Broth-5' OR
sample_physiologicalparameters.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1' OR
sample_physiologicalparameters.sample_id LIKE '141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4';
