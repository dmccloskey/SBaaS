from analysis import *

def data_stage00():

    '''acqusition method import'''
    io00 = stage00_io();
    #io00.import_MSMethod_add('data\\_input\\140718_ms_method.csv'); # completed
    #io00.import_AcquisitionMethod_add('data\\_input\\140718_acquisition_method.csv'); # completed
    #io00.import_MSComponentList_add('data\\_input\\140718_ms_components_list.csv'); # completed
    
    '''make the experiment from sample file'''
    execute00 = stage00_execute();
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\140718_PLT_Test01_sample_file01.csv', 
    #                                             0,[10.0, 100.0]); # completed
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\140718_RBC_Test01_sample_file01.csv',
    #                                             0,[10.0]); # completed
    #execute00.execute_makeBatchFile('RBC_PLT_Test01', '140718','data\\_output\\140718_RBC_PLT_Test01.txt'); # completed

def data_stage01():
    '''data import'''
    qe01 = stage01_quantification_execute();
    #qe01.execute_deleteExperimentFromMQResultsTable('RBC_PLT_Test01'); # reserved for bad data imports
    qio01 = stage01_quantification_io();
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\140718_samples.csv'); # todo
    qio01.import_dataStage01MQResultsTable_update('data\\_input\\140718_samples_update01.csv');

    '''calibrator analysis'''
    #qm01 = stage01_quantification_QMethod();
    #qm01.execute_quantitationMethodUpdate();

    '''data analysis'''
    #qe01.initialize_dataStage01_quantification();
    qe01.reset_dataStage01_quantification('RBC_PLT_Test01');
    qe01.execute_normalizeSamples2Biomass('RBC_PLT_Test01');
    qe01.execute_removeDuplicateDilutions('RBC_PLT_Test01');
    qe01.reset_datastage01_quantification_replicatesAndAverages('RBC_PLT_Test01');
    qe01.execute_analyzeReplicates('RBC_PLT_Test01');
    qe01.execute_analyzeAverages('RBC_PLT_Test01');

    '''data export'''
    qio01.export_dataStage01Replicates_csv('RBC_PLT_Test01','data\\_output\\dataStage01Replicates_RBC_PLT_Test01.csv');