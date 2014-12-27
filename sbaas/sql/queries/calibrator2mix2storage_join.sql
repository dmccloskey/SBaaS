SELECT 
  calibrator2mix.calibrator_id, 
  calibrator2mix.mix_id, 
  mix_storage.box, 
  mix_storage.posstart, 
  mix_storage.posend
FROM 
  public.calibrator2mix, 
  public.mix_storage
WHERE 
  mix_storage.mix_id = calibrator2mix.mix_id
ORDER BY 
  calibrator2mix.calibrator_id, 
  calibrator2mix.mix_id;
