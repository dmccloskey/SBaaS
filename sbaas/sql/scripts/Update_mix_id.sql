ALTER TABLE mix2met_id DROP CONSTRAINT mix2met_id_mix_id_fkey;

ALTER TABLE mix2met_id DROP CONSTRAINT mix2met_id_mix_id_fkey1;

ALTER TABLE mix2met_id DROP CONSTRAINT mix2met_id_mix_id_fkey2;

UPDATE mix2met_id
   SET mix_id='misc1'
 WHERE mix_id LIKE 'misc';

 UPDATE mix_storage
   SET mix_id='misc1'
 WHERE mix_id LIKE 'misc';
 
UPDATE mix_parameters
   SET mix_id='misc1'
 WHERE mix_id LIKE 'misc';
 
UPDATE mix_description
   SET mix_id='misc1'
 WHERE mix_id LIKE 'misc';

UPDATE calibrator2mix
   SET mix_id='misc1'
 WHERE mix_id LIKE 'misc';
 
ALTER TABLE mix2met_id
  ADD CONSTRAINT mix2met_id_mix_id_fkey FOREIGN KEY (mix_id)
      REFERENCES mix_description (mix_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE mix2met_id
  ADD CONSTRAINT mix2met_id_mix_id_fkey1 FOREIGN KEY (mix_id)
      REFERENCES mix_storage (mix_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;
      
ALTER TABLE mix2met_id
  ADD CONSTRAINT mix2met_id_mix_id_fkey2 FOREIGN KEY (mix_id)
      REFERENCES calibrator2mix (mix_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;