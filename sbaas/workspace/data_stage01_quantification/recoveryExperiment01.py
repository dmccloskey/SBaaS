from analysis import *

'''make the experiment from sample file'''
execute00 = stage00_execute();
#execute00.execute_makeExperimentFromSampleFile('data\\_input\\140509_recoveryExperiment01_sample_file.csv',
#                                             0,[]);

'''data import'''
data_io = stage01_quantification_io();
#data_io.import_dataStage01MQResultsTable_add('data\\_input\\140509_recoveryExperiment01_samples.csv');
#data_io.import_dataStage01MQResultsTable_update('data\\_input\\140509_recoveryExperiment01_samples.csv');

'''data analysis'''
ma = stage01_quantification_execute();
#ma.initialize_dataStage01_quantification();
#ma.reset_dataStage01_quantification('recoveryExperiment01');
#ma.execute_normalizeSamples2Biomass('recoveryExperiment01',None,None);
#ma.reset_datastage01_quantification_replicatesAndAverages('recoveryExperiment01');
#ma.execute_analyzeReplicates('recoveryExperiment01');
#ma.execute_analyzeAverages('recoveryExperiment01');
ma.execute_calculateMissingValues_replicates('recoveryExperiment01');
ma.execute_calculateAverages_replicates('recoveryExperiment01');
ma.execute_calculateGeoAverages_replicates('recoveryExperiment01');

'''data export'''
data_io.export_dataStage01Replicates_csv('recoveryExperiment01','data\\_output\\dataStage01Replicates_recoveryExperiment01.csv');
data_io.export_dataStage01ReplicatesMI_csv('recoveryExperiment01','data\\_output\\dataStage01ReplicatesMI2_recoveryExperiment01.csv');