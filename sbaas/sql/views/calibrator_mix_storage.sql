--calibrator mix storage
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
  calibrator2mix.mix_id LIKE mix_storage.mix_id AND 
  calibrator2mix.calibrator_id = 2;