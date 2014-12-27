from analysis import *

def data_stage01():
    '''data import'''
    #data_io = stage01_quantification_io();
    #data_io.import_quantitationMethod_add('131015','131015_QMethod.csv');
    #data_io.import_metabolomicsSample_add('131015_metabolomics_sample.csv');
    #data_io.import_metabolomicsExperiment_add('131015_metabolomics_experiment.csv');
    #data_io.import_dataStage01MQResultsTable_add('131015_Samples.csv');
    #data_io.import_dataStage01MQResultsTable_add('131015_Calibrators.csv');

    '''table updates'''

    '''calibrator analysis'''
    #qm = stage01_quantification_QMethod();
    #qm.execute_quantitationMethodUpdate();

    '''data analysis'''
    ma = stage01_quantification_execute();
    #ma.initialize_dataStage01();
    #ma.reset_dataStage01();
    #ma.execute_checkISMatch('rpomut01');
    ma.execute_LLOQAndULOQ('rpomut01');
    #ma.execute_checkLLOQAndULOQ('rpomut01');
    #ma.execute_analyzeDilutions('rpomut01');
    #ma.execute_checkCV_dilutions('rpomut01');
    #ma.execute_analyzeQCs('rpomut01');
    #ma.execute_checkCV_QCs('rpomut01');
    #ma.execute_normalizeSamples2Biomass('rpomut01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #ma.execute_removeDuplicateDilutions('rpomut01');
    #ma.reset_datastage01_quantification_replicatesAndAverages('rpomut01');
    #ma.execute_analyzeReplicates('rpomut01');
    #ma.execute_analyzeAverages('rpomut01');
    #ma.execute_checkCVAndExtracelluar_averages('rpomut01');
    ma.reset_datastage01_quantification_replicatesAndAveragesMI('rpomut01')
    ma.execute_calculateMissingValues_replicates('rpomut01');
    ma.execute_calculateMissingComponents_replicates('rpomut01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    ma.execute_calculateAverages_replicates('rpomut01');
    ma.execute_calculateGeoAverages_replicates('rpomut01');
    ma.execute_physiologicalRatios_replicates('rpomut01');
    ma.execute_physiologicalRatios_averages('rpomut01');

    '''data export'''
    data_io = stage01_quantification_io();
    #data_io.export_dataStage01Replicates_csv('rpomut01','data\\_output\\dataStage01Replicates_rpomut01.csv');
    data_io.export_dataStage01ReplicatesMI_csv('rpomut01','data\\_output\\dataStage01ReplicatesMI2_rpomut01.csv');
    #data_io.export_dataStage01AveragesMI_json('rpomut01', "OxicWTGlyc", '0', "data\\_output\\rpomut01_OxicWTGlyc_0.json");
    #data_io.export_dataStage01AveragesMIgeo_json('rpomut01', "OxicWTGlyc", '0', "data\\_output\\rpomut01_OxicWTGlyc_0_geo.json");
    #data_io.export_dataStage01physiologicalRatios_d3('rpomut01');
    #data_io.export_dataStage01replicatesMI_d3('rpomut01');

def data_stage02():
    '''data analysis'''
    qe02 = stage02_quantification_execute();
    #qe02.drop_dataStage02_quantification();
    #qe02.initialize_dataStage02_quantification();
    #qe02.execute_glogNormalization('rpomut01');
    #qe02.execute_descriptiveStats('rpomut01');
    #qe02.execute_pca('rpomut01');
    #qe02.execute_anova('rpomut01');
    #qe02.execute_pairwiseTTest('rpomut01');
    #qe02.execute_pcaPlot('rpomut01');
    #qe02.execute_volcanoPlot('rpomut01');

    '''data export'''
    qio02 = stage02_quantification_io();
    #qio02.export_volcanoPlot_d3('rpomut01');
    #qio02.export_pcaPlot_d3('rpomut01');
    qio02.export_heatmap_d3('rpomut01');


