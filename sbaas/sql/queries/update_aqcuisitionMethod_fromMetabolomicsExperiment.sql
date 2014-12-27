UPDATE metabolomics_experiment
   SET acquisition_method_id='140719_McCloskey2013_13CFlux'
 WHERE id LIKE 'ALEsKOs01'
AND
metabolomics_sample_name LIKE '%EPEcoli13C%'
AND
metabolomics_sample_name LIKE '%1000.0x';
