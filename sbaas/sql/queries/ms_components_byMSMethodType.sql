-- get components in tuning not in quantification
SELECT t1.q1_mass, t1.q3_mass, t1.met_id
FROM ms_components t1
LEFT JOIN (SELECT tune.q1_mass, tune.q3_mass, tune.met_id FROM ms_components tune, ms_components quant
	WHERE tune.ms_methodtype LIKE 'tuning' AND
	quant.ms_methodtype LIKE 'quantification' AND
	tune.q1_mass = quant.q1_mass AND
	tune.q3_mass = quant.q3_mass AND
	tune.met_id LIKE quant.met_id
	GROUP BY tune.q1_mass, tune.q3_mass, tune.met_id) t2 ON t2.q1_mass = t1.q1_mass AND t2.q3_mass = t1.q3_mass AND t2.met_id = t1.met_id
WHERE t2.met_id IS NULL
and t1.ms_mode LIKE '-'
and t1.ms_methodtype LIKE 'tuning'
  GROUP BY t1.q1_mass, t1.q3_mass, t1.met_id
  ORDER BY t1.met_id, t1.q1_mass, t1.q3_mass;

-- get components in tuning and quantification
-- SELECT tune.q1_mass, tune.q3_mass, tune.met_id FROM ms_components tune, ms_components quant
--   WHERE tune.ms_methodtype LIKE 'tuning' AND
--   quant.ms_methodtype LIKE 'quantification' AND
--   tune.q1_mass = quant.q1_mass AND
--   tune.q3_mass = quant.q3_mass AND
--   tune.met_id LIKE quant.met_id
--   GROUP BY tune.q1_mass, tune.q3_mass, tune.met_id
--   ORDER BY tune.met_id, tune.q1_mass, tune.q3_mass;

  
  
