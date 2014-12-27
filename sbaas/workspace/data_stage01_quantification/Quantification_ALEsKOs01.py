from analysis import *

def data_stage00():
    
    '''make the experiment from sample file'''
    #execute00 = stage00_execute();
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\141220_Quantification ALEsKOs01_sampleFile01.csv',
    #                                             1,[10.0]);
    #execute00.execute_makeExperimentFromCalibrationFile('data\\_input\\141220_Quantification_ALEsKOs01_calibrationFile01.csv');
    #execute00.execute_makeBatchFile('ALEsKOs01', '141220','data\\_output\\141220_Quantification ALEsKOs01.txt',experiment_type_I=4);
    execute00.execute_exportCalibrationConcentrations('data\\_input\\141220_calibration_samplesAndComponents.csv','data\\_output\\141220_calibration_concentrations.csv'); #todo

def data_stage01():
    '''data import'''
    qe01 = stage01_quantification_execute();
    #qe01.execute_deleteExperimentFromMQResultsTable('ALEsKOs01'); # reserved for bad data imports
    qio01 = stage01_quantification_io();
    #qio01.import_quantitationMethod_add('141220','data\\_input\\141220_QMethod.csv'); # complete
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\141220_samples.csv'); # complete
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\141220_calibrationCurves.csv'); # complete
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\141220_samples_update01.csv');
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\141220_calibrationCurves_update01.csv');
    #qio01.import_dataStage01Normalized_update('data\\_input\\141220_data_stage01_quantitation_normalized_ALEsKOs01_update01.csv');

    '''calibrator analysis'''
    #qm01 = stage01_quantification_QMethod();
    #qm01.execute_quantitationMethodUpdate();

    '''data analysis'''
    #qe01.initialize_dataStage01_quantification();
    #qe01.reset_dataStage01_quantification('ALEsKOs01');
    #qe01.execute_checkISMatch('ALEsKOs01');
    #qe01.execute_LLOQAndULOQ('ALEsKOs01');
    #qe01.execute_checkLLOQAndULOQ('ALEsKOs01');
    #qe01.execute_analyzeDilutions('ALEsKOs01');
    #qe01.execute_checkCV_dilutions('ALEsKOs01');
    #qe01.execute_analyzeQCs('ALEsKOs01');
    #qe01.execute_checkCV_QCs('ALEsKOs01');
    #qe01.execute_normalizeSamples2Biomass('ALEsKOs01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_removeDuplicateDilutions('ALEsKOs01');
    #qe01.reset_datastage01_quantification_replicatesAndAverages('ALEsKOs01');
    #qe01.execute_analyzeReplicates('ALEsKOs01');
    #qe01.execute_analyzeAverages('ALEsKOs01');
    #qe01.execute_checkCVAndExtracelluar_averages('ALEsKOs01');
    #qe01.reset_datastage01_quantification_replicatesAndAveragesMI('ALEsKOs01')
    #qe01.execute_calculateMissingValues_replicates('ALEsKOs01');
    #qe01.execute_calculateMissingComponents_replicates('ALEsKOs01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_calculateAverages_replicates('ALEsKOs01');
    #qe01.execute_calculateGeoAverages_replicates('ALEsKOs01');
    #qe01.execute_physiologicalRatios_replicates('ALEsKOs01');
    #qe01.execute_physiologicalRatios_averages('ALEsKOs01');
    #qe01.execute_scatterLinePlot_physiologicalRatios('ALEsKOs01',ratio_ids_I=['nc'])
    #qe01.execute_boxAndWhiskersPlot_averages('ALEsKOs01',component_names_I=['akg.akg_1.Light','gln-L.gln-L_1.Light','glu-L.glu-L_1.Light'])
    #qe01.execute_barPlot_averages('ALEsKOs01',component_names_I=['akg.akg_1.Light','cit.cit_1.Light','fum.fum_1.Light',
    #                                                                    'mal-L.mal-L_1.Light','succ.succ_1.Light',
    #                                                                    'gln-L.gln-L_1.Light','glu-L.glu-L_1.Light',
    #                                                                    'acon-C.acon-C_1.Light','icit.icit_2.Light'])

    '''data export'''
    #qio01.export_dataStage01Replicates_csv('ALEsKOs01','data\\_output\\dataStage01Replicates_ALEsKOs01.csv');
    #qio01.export_dataStage01ReplicatesMI_csv('ALEsKOs01','data\\_output\\dataStage01ReplicatesMI2_ALEsKOs01.csv');
    #qio01.export_dataStage01AveragesMIgeo_json('ALEsKOs01', "OxicWtGlc", '0', "data\\_output\\ALEsKOs01_OxicWtGlc_0_geo.json");
    #qio01.export_dataStage01physiologicalRatios_d3('ALEsKOs01');
    #qio01.export_dataStage01replicatesMI_d3('ALEsKOs01');

def data_stage02():
    '''data analysis'''
    qe02 = stage02_quantification_execute();
    #qe02.reset_dataStage02_quantification('ALEsKOs01');
    qe02.execute_glogNormalization('ALEsKOs01');
    qe02.execute_descriptiveStats('ALEsKOs01');
    qe02.execute_pca('ALEsKOs01');
    qe02.execute_anova('ALEsKOs01');
    qe02.execute_pairwiseTTest('ALEsKOs01');
    qe02.execute_pcaPlot('ALEsKOs01');
    qe02.execute_volcanoPlot('ALEsKOs01');

    '''data export'''
    qio02 = stage02_quantification_io();
    qio02.export_volcanoPlot_d3('ALEsKOs01');
    qio02.export_pcaPlot_d3('ALEsKOs01');
    qio02.export_heatmap_d3('ALEsKOs01');

def data_stage03():
    qe03 = stage03_quantification_execute();
    #qe03.reset_dataStage03_quantification_thermodynamicAnalysis('ALEsKOs01');

    '''data import'''
    qio03 = stage03_quantification_io();
    qio03.import_dataStage03Experiment_add('data\\_input\\141010_data_stage03_quantification_experiment.csv');
    qio03.import_dataStage03OtherData_add('data\\_input\\141010_data_stage03_quantification_otherData.csv');
    qio03.import_dataStage03MetabolomicsData_add('data\\_input\\141010_data_stage03_quantification_metabolomicsData_glcM9.csv');

    '''data analysis'''
    qe03.load_models('ALEsKOs01');
    qe03.execute_makeMetabolomicsData_intracellular('ALEsKOs01');
    qe03.execute_makeSimulatedData('ALEsKOs01');
    qe03.execute_adjust_dG_f('ALEsKOs01');
    qe03.execute_calculate_dG_r('ALEsKOs01');

    '''data export'''
    qio03.export_thermodynamicAnalysis_escher('ALEsKOs01');
    qio03.export_thermodynamicAnalysisComparison_escher('ALEsKOs01','OxicWtGlc');
    qio03.export_thermodynamicAnalysisComparison_csv('ALEsKOs01','OxicWtGlc');

def _main_():
    data_stage00;
    data_stage01;
    data_stage02;