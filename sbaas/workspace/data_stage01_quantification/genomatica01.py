from analysis import *

def data_stage00():

    # import new components
    io00 = stage00_io();

    execute00 = stage00_execute();

    '''acqusition method import'''

    '''quantitation method imports'''
    
    '''make the experiment from sample file'''
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\140826_Quantification_genomatica01_sampleFile01.csv',
                                                 1,[0.4,10.0]);  # QCs from rpomut02 and chemoNLim01 experiments # completed
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\140826_Quantification_genomatica01_sampleFile02.csv',
                                                 1,[]);  # QCs from rpomut02 and chemoNLim01 experiments # completed
    #execute00.execute_makeExperimentFromCalibrationFile('data\\_input\\140826_Quantification_calibration_file.csv'); # completed
    #execute00.execute_makeBatchFile('genomatica01', '140826','data\\_output\\140826_Quantification_genomatica01.txt'); # completed
    #execute00.execute_exportCalibrationConcentrations('data\\_input\\140826_calibration_samplesAndComponents.csv','data\\_output\\140826_calibration_concentrations.csv'); # Not needed

def data_stage01():
    '''data import'''
    qe01 = stage01_quantification_execute();
    #qe01.execute_deleteExperimentFromMQResultsTable('genomatica01'); # reserved for bad data imports
    qio01 = stage01_quantification_io();
    #qio01.import_quantitationMethod_add('140826','data\\_input\\140826_Quantification_QMethod.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\140826_Quantification_samples01.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140826_Quantification_samples02.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140826_Quantification_samples03.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140826_Quantification_samples04.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140826_Quantification_samples06.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\140826_Quantification_calibrators01.csv'); # completed
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140826_Quantification_calibrators02.csv'); # completed

    '''calibrator analysis'''
    qm01 = stage01_quantification_QMethod();
    #qm01.execute_quantitationMethodUpdate();

    '''data analysis'''
    qe01.initialize_dataStage01_quantification();
    #qe01.reset_dataStage01_quantification('genomatica01');
    #qe01.execute_checkISMatch('genomatica01');
    #qe01.execute_LLOQAndULOQ('genomatica01');
    #qe01.execute_checkLLOQAndULOQ('genomatica01');
    #qe01.execute_analyzeDilutions('genomatica01');
    #qe01.execute_checkCV_dilutions('genomatica01');
    #qe01.execute_analyzeQCs('genomatica01');
    #qe01.execute_checkCV_QCs('genomatica01');
    #qe01.execute_normalizeSamples2Biomass('genomatica01',biological_material_I='MG1655',conversion_name_I='ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_removeDuplicateDilutions('genomatica01');
    #qe01.reset_datastage01_quantification_replicatesAndAverages('genomatica01');
    #qe01.execute_analyzeReplicates('genomatica01');
    #qe01.execute_analyzeAverages('genomatica01');
    #qe01.execute_checkCVAndExtracelluar_averages('genomatica01');
    #qe01.execute_calculateMissingValues_replicates('genomatica01');
    #qe01.execute_calculateMissingComponents_replicates('genomatica01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_calculateAverages_replicates('genomatica01');
    #qe01.execute_calculateGeoAverages_replicates('genomatica01');
    qe01.execute_physiologicalRatios_replicates('genomatica01');
    qe01.execute_physiologicalRatios_averages('genomatica01');
    #qe01.execute_boxAndWhiskersPlot_physiologicalRatios('genomatica01',sample_name_abbreviations_I=["ControlFermentor","ControlFermentorGEN"]);
    #qe01.execute_boxAndWhiskersPlot_averages('genomatica01',sample_name_abbreviations_I=["ControlFermentor","ControlFermentorGEN"]);

    '''data export'''
    #qio01.export_dataStage01Replicates_csv('genomatica01','data\\_output\\dataStage01Replicates_genomatica01.csv');
    #qio01.export_dataStage01ReplicatesMI_csv('genomatica01','data\\_output\\dataStage01ReplicatesMI2_genomatica01.csv');
    #qio01.export_dataStage01AveragesMIgeo_json('genomatica01', "ControlFermentor", '0', "data\\_output\\genomatica01_ControlFermentor_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('genomatica01', "ControlFermentor_25uL", '0', "data\\_output\\genomatica01_ControlFermentor_25uL_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('genomatica01', "ControlFermentorGEN", '0', "data\\_output\\genomatica01_ControlFermentorGEN_0_geo.json");
    qio01.export_dataStage01physiologicalRatios_d3('genomatica01');
    #qio01.export_dataStage01replicatesMI_d3('genomatica01');
    
def data_stage02():
    qe02 = stage02_quantification_execute();
    #qe02.initialize_dataStage02_quantification();
    #qe02.reset_dataStage02_quantification('genomatica01');
    #qe02.execute_componentNameSpecificNormalization('genomatica01',sample_name_abbreviations_I=["ControlFermentor","ControlFermentorGEN"]);
    #qe02.execute_glogNormalization_update('genomatica01');
    #qe02.execute_descriptiveStats('genomatica01');
    #qe02.execute_pca('genomatica01');
    #qe02.execute_anova('genomatica01');
    #qe02.execute_pairwiseTTest('genomatica01');
    #qe02.execute_pcaPlot('genomatica01');
    #qe02.execute_volcanoPlot('genomatica01');
    #qe02.execute_boxAndWhiskersPlot('genomatica01',component_names_I=['atp.atp_1.Light']);

def _main_():
    data_stage00;
    data_stage01;
    data_stage02;