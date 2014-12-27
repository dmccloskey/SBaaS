from analysis import *

def data_stage00():
    '''make the experiment from sample file'''
    execute00 = stage00_execute();
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\140521_chemoNLim01_sample_file.csv',
                                                 1,[10.0]);
    execute00.execute_makeBatchFile('chemoNLim01', '140521','data\\_output\\140521_chemoNLim01.txt');

def data_stage01():    
    '''data import'''
    qio01 = stage01_quantification_io();
    # combined with chemoNLim01 (i.e., already in the DB)
    #qio01.import_quantitationMethod_add('140521','data\\_input\\140521_QMethod.csv');
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\140521_samples.csv');
    # updates:
    #qio01.import_dataStage01Normalized_update('data\\_input\\140521_data_stage01_quantitation_normalized_chemoNLim01_update01.csv');
    #qio01.import_dataStage01Normalized_update('data\\_input\\140521_data_stage01_quantitation_normalized_chemoNLim01_update02.csv');

    '''calibrator analysis'''
    # combined with chemoNLim01 (i.e., already in the DB)
    #qm01 = stage01_quantification_QMethod();
    #qm01.execute_quantitationMethodUpdate();

    '''data analysis'''
    qe01 = stage01_quantification_execute();
    #qe01.initialize_dataStage01_quantification();
    #qe01.reset_dataStage01_quantification('chemoNLim01');
    #qe01.execute_checkISMatch('chemoNLim01');
    #qe01.execute_LLOQAndULOQ('chemoNLim01');
    #qe01.execute_checkLLOQAndULOQ('chemoNLim01');
    #qe01.execute_analyzeDilutions('chemoNLim01');
    #qe01.execute_checkCV_dilutions('chemoNLim01');
    #qe01.execute_analyzeQCs('chemoNLim01');
    #qe01.execute_checkCV_QCs('chemoNLim01');
    #qe01.execute_normalizeSamples2Biomass('chemoNLim01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.reset_datastage01_quantification_replicatesAndAveragesMI('chemoNLim01');
    #qe01.execute_calculateMissingValues_replicates('chemoNLim01');
    #qe01.execute_calculateMissingComponents_replicates('chemoNLim01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_calculateAverages_replicates('chemoNLim01');
    #qe01.execute_calculateGeoAverages_replicates('chemoNLim01');
    #qe01.execute_physiologicalRatios_replicates('chemoNLim01');
    #qe01.execute_physiologicalRatios_averages('chemoNLim01');
    qe01.execute_boxAndWhiskersPlot_averages('chemoNLim01',component_names_I=['akg.akg_1.Light','gln-L.gln-L_1.Light','glu-L.glu-L_1.Light','fdp.fdp_1.Light'])

    '''data export'''
    #qio01.export_dataStage01Replicates_csv('chemoNLim01','data\\_output\\dataStage01Replicates_chemoNLim01.csv');
    #qio01.export_dataStage01ReplicatesMI_csv('chemoNLim01','data\\_output\\dataStage01ReplicatesMI2_chemoNLim01.csv');
    #qio01.export_dataStage01AveragesMIgeo_json('chemoNLim01', "OxicWtGlcDil0p25", '0', "data\\_output\\chemoNLim01_OxicWtGlcDil0p25_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('chemoNLim01', "OxicWtGlcDil0p33", '0', "data\\_output\\chemoNLim01_OxicWtGlcDil0p33_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('chemoNLim01', "OxicWtGlcDil0p46", '0', "data\\_output\\chemoNLim01_OxicWtGlcDil0p46_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('chemoNLim01', "OxicWtGlcDil0p59", '0', "data\\_output\\chemoNLim01_OxicWtGlcDil0p59_0_geo.json");
    #qio01.export_dataStage01physiologicalRatios_d3('chemoNLim01');
    #qio01.export_dataStage01replicatesMI_d3('chemoNLim01');

def data_stage02():
    qe02 = stage02_quantification_execute();
    #qe02.initialize_dataStage02_quantification();
    #qe02.reset_dataStage02_quantification('chemoNLim01');
    #qe02.execute_glogNormalization('chemoNLim01');
    #qe02.execute_descriptiveStats('chemoNLim01');
    #qe02.execute_pca('chemoNLim01');
    #qe02.execute_anova('chemoNLim01');
    #qe02.execute_pairwiseTTest('chemoNLim01');
    #qe02.execute_pcaPlot('chemoNLim01');
    #qe02.execute_volcanoPlot('chemoNLim01');

    '''data export'''
    qio02 = stage02_quantification_io();
    #qio02.export_volcanoPlot_d3('chemoNLim01');
    #qio02.export_pcaPlot_d3('chemoNLim01');
    qio02.export_heatmap_d3('chemoNLim01');


