SELECT met_id, q1_mass, precursor_formula
  FROM ms_components
  WHERE met_id LIKE 'accoa'
  AND ms_methodtype LIKE 'isotopomer_13C'
  GROUP BY met_id, q1_mass, precursor_formula
  ORDER BY q1_mass asc;
