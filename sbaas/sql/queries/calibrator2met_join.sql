SELECT 
  calibrator2mix.calibrator_id, 
  mix2met_id.met_id
FROM 
  public.calibrator2mix, 
  public.mix2met_id
WHERE 
  calibrator2mix.mix_id LIKE mix2met_id.mix_id
ORDER BY calibrator_id ASC;
