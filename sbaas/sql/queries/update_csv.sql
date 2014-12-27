DROP TABLE tmp_x;
CREATE TEMP TABLE tmp_x AS SELECT * FROM "data_stage02_isotopomer_atomMappingReactions" LIMIT 0;
COPY tmp_x FROM 'C:/Users/Public/Documents/140924a_data_stage02_isotopomer_atomMappingReactions.csv' DELIMITER ',' CSV HEADER;

UPDATE "data_stage02_isotopomer_atomMappingReactions"
   SET mapping_id=tmp_x.mapping_id,
       rxn_id=tmp_x.rxn_id,
       rxn_description=tmp_x.rxn_description,
       reactants_stoichiometry_tracked=tmp_x.reactants_stoichiometry_tracked, 
       products_stoichiometry_tracked=tmp_x.products_stoichiometry_tracked,
       reactants_ids_tracked=tmp_x.reactants_ids_tracked,
       products_ids_tracked=tmp_x.products_ids_tracked, 
       reactants_mapping=tmp_x.reactants_mapping,
       products_mapping=tmp_x.products_mapping,
       rxn_equation=tmp_x.rxn_equation,
       used_=tmp_x.used_, 
       comment_=tmp_x.comment_,
       reactants_elements_tracked=tmp_x.reactants_elements_tracked,
       products_elements_tracked=tmp_x.products_elements_tracked, 
       reactants_positions_tracked=tmp_x.reactants_positions_tracked,
       products_positions_tracked=tmp_x.products_positions_tracked
   FROM tmp_x
 WHERE "data_stage02_isotopomer_atomMappingReactions".id=tmp_x.id;

 DROP TABLE tmp_x;