from analysis import *

'''data import'''
data_io = stage00_io();
#data_io.import_metabolomicsStandards_update('data\\_input\\140117_metabolomics_standards_update.csv');
#data_io.import_metabolomicsStandards_add('data\\_input\\140117_metabolomics_standards_add.csv');
#data_io.import_standardsOrdering_add('data\\_input\\140117_standards_ordering_add.csv');

#self.session = Session();
#oligos_storage.__table__.create(engine,True);
#oligos_description.__table__.create(engine,True);
#data_io.import_oligosStorage_add('data\\_input\\140128_oligos_storage.csv');
#data_io.import_oligosDescription_add('data\\_input\\140128_oligos_description.csv');

data_io.import_MSComponents_add('data\\_input\\140128_ms_components.csv');
