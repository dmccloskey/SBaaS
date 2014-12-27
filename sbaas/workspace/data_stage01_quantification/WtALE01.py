from analysis import *

def data_stage01():
    '''data import'''
    data_io = stage01_quantification_io();
    #data_io.import_quantitationMethod_add('131210','data\\_input\\131210_QMethod.csv');
    #data_io.import_sampleStorage_add('data\\_input\\131210_sample_storage.csv');
    #data_io.import_sampleStorage_add('data\\_input\\131210_sample_storage2.csv');
    #data_io.import_samplePhysiologicalParameters_add('data\\_input\\131210_sample_physiologicalparameters.csv');
    #data_io.import_samplePhysiologicalParameters_add('data\\_input\\131210_sample_physiologicalparameters2.csv');
    #data_io.import_sampleDescription_add('data\\_input\\131210_sample_description.csv');
    #data_io.import_sampleDescription_add('data\\_input\\131210_sample_description2.csv');
    #data_io.import_metabolomicsSample_add('data\\_input\\131210_metabolomics_sample.csv');
    #data_io.import_metabolomicsSample_add('data\\_input\\131210_metabolomics_sample2.csv');
    #data_io.import_metabolomicsSample_update('data\\_input\\131210_metabolomics_sample2.csv');
    #data_io.import_metabolomicsExperiment_add('data\\_input\\131210_metabolomics_experiment.csv');
    #data_io.import_metabolomicsExperiment_add('data\\_input\\131210_metabolomics_experiment2.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\131210_samples.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\131210_samples_update.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\131210_samples2.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\131210_calibrators.csv');
    
    '''calibrator analysis'''
    #qm = stage01_quantification_QMethod();
    #qm.execute_quantitationMethodUpdate();

    '''data analysis'''
    ma = stage01_quantification_execute();
    #ma.initialize_dataStage01_quantification();
    #ma.reset_dataStage01_quantification('ALEWt01');
    #ma.execute_checkISMatch('ALEWt01');
    #ma.execute_LLOQAndULOQ('ALEWt01');
    #ma.execute_checkLLOQAndULOQ('ALEWt01');
    #ma.execute_analyzeDilutions('ALEWt01');
    #ma.execute_checkCV_dilutions('ALEWt01');
    #ma.execute_analyzeQCs('ALEWt01');
    #ma.execute_checkCV_QCs('ALEWt01');
    #ma.execute_normalizeSamples2Biomass('ALEWt01','MG1655','ODspecificTotalCellVolume_Volkmer2011');

    #useful query that needs to be turned into a function:
    '''UPDATE data_stage01_quantification_mqresultstable
       SET used_=TRUE
     WHERE sample_name LIKE '131206%'
	    AND sample_type LIKE 'Unknown'
	    AND (sample_name LIKE '%Broth%' OR sample_name LIKE '%Filtrate%')
	    AND component_name LIKE 'icit.icit_2.Light';'''

    #ma.execute_normalizeSamples2Biomass('ALEWt01',
    #            ['131206_0_OxicWTEcoliGlcM9_Filtrate-2',
    #            '131206_0_OxicWTEcoliGlcM9_Filtrate-3',
    #            '131206_0_OxicWTEcoliGlcM9_Broth-4',
    #            '131206_0_OxicWTEcoliGlcM9_Broth-5',
    #            '131206_0_OxicWTEcoliGlcM9_Broth-6',
    #            '131206_0_OxicEvo03EcoliGlcM9_Filtrate-2',
    #            '131206_0_OxicEvo03EcoliGlcM9_Filtrate-3',
    #            '131206_0_OxicEvo03EcoliGlcM9_Broth-4',
    #            '131206_0_OxicEvo03EcoliGlcM9_Broth-5',
    #            '131206_0_OxicEvo03EcoliGlcM9_Broth-6',
    #            '131206_0_OxicEvo04EcoliGlcM9_Filtrate-2',
    #            '131206_0_OxicEvo04EcoliGlcM9_Filtrate-3',
    #            '131206_0_OxicEvo04EcoliGlcM9_Broth-4',
    #            '131206_0_OxicEvo04EcoliGlcM9_Broth-5',
    #            '131206_0_OxicEvo04EcoliGlcM9_Broth-6',
    #            '131206_0_OxicEvo08EcoliGlcM9_Filtrate-2',
    #            '131206_0_OxicEvo08EcoliGlcM9_Filtrate-3',
    #            '131206_0_OxicEvo08EcoliGlcM9_Broth-4',
    #            '131206_0_OxicEvo08EcoliGlcM9_Broth-5',
    #            '131206_0_OxicEvo08EcoliGlcM9_Broth-6',
    #            '131206_0_OxicEvo09EcoliGlcM9_Filtrate-2',
    #            '131206_0_OxicEvo09EcoliGlcM9_Filtrate-3',
    #            '131206_0_OxicEvo09EcoliGlcM9_Broth-4',
    #            '131206_0_OxicEvo09EcoliGlcM9_Broth-5',
    #            '131206_0_OxicEvo09EcoliGlcM9_Broth-6'],
    #            ["icit.icit_2.Light"],
    #            'MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #ma.execute_removeDuplicateDilutions('ALEWt01');
    #ma.reset_datastage01_quantification_replicatesAndAverages('ALEWt01');
    #ma.execute_analyzeReplicates('ALEWt01');
    #ma.execute_analyzeAverages('ALEWt01');
    #ma.execute_checkCVAndExtracelluar_averages('ALEWt01');

    #useful queries that need to be incorporated into functions:
    '''UPDATE data_stage01_quantification_normalized
       SET used_=FALSE, 
           comment_='Removed filtrate'
     WHERE experiment_id LIKE 'ALEWt01'
	    AND sample_id LIKE '%Filtrate%'
	    AND component_group_name LIKE 'icit';

    UPDATE data_stage01_quantification_normalized
       SET comment_='Broth samples only due to high filtrate'
     WHERE experiment_id LIKE 'ALEWt01'
	    AND sample_id LIKE '%Broth%'
	    AND component_group_name LIKE 'icit';

    -- UPDATE data_stage01_quantification_normalized
    --    SET used_=FALSE, 
    --        comment_='High % extracellular'
    --  WHERE experiment_id LIKE 'ALEWt01'
    -- 	AND component_group_name LIKE 'orn';

    -- UPDATE data_stage01_quantification_normalized
    --    SET comment_='Poor acquisition--may not be able to use in analyses'
    --  WHERE experiment_id LIKE 'ALEWt01'
    -- 	AND component_group_name LIKE 'pyr';'''

    #ma.execute_calculateMissingValues_replicates('ALEWt01');
    #ma.execute_calculateMissingComponents_replicates('ALEWt01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #ma.execute_calculateAverages_replicates('ALEWt01');
    #ma.execute_calculateGeoAverages_replicates('ALEWt01');
    #ma.execute_physiologicalRatios_replicates('ALEWt01');
    #ma.execute_physiologicalRatios_averages('ALEWt01');
    #ma.execute_scatterLinePlot_physiologicalRatios('ALEWt01',ratio_ids_I=['nc'])
    ma.execute_boxAndWhiskersPlot_averages('ALEWt01',component_names_I=['akg.akg_1.Light','cit.cit_2.Light','fum.fum_1.Light',
                                                                        'mal-L.mal-L_1.Light','succ.succ_1.Light',
                                                                        'gln-L.gln-L_1.Light','glu-L.glu-L_1.Light',
                                                                        'acon-C.acon-C_1.Light','icit.icit_2.Light'])
    #ma.execute_barPlot_averages('ALEWt01',component_names_I=['akg.akg_1.Light','cit.cit_2.Light','fum.fum_1.Light',
    #                                                                    'mal-L.mal-L_1.Light','succ.succ_1.Light',
    #                                                                    'gln-L.gln-L_1.Light','glu-L.glu-L_1.Light',
    #                                                                    'acon-C.acon-C_1.Light','icit.icit_2.Light'])

    '''data export'''
    #data_io.export_dataStage01Replicates_csv('ALEWt01','data\\_output\\dataStage01Replicates_ALEWt01.csv');
    #data_io.export_dataStage01ReplicatesMI_csv('ALEWt01','data\\_output\\dataStage01ReplicatesMI2_ALEWt01.csv');
    #data_io.export_dataStage01AveragesMIgeo_json('ALEWt01', "OxicWtGlc", '0', "data\\_output\\ALEWt01_OxicWtGlc_0_geo.json");
    #data_io.export_dataStage01AveragesMIgeo_json('ALEWt01', "OxicEvo03Glc", '0', "data\\_output\\ALEWt01_OxicEvo03Glc_0_geo.json");
    #data_io.export_dataStage01AveragesMIgeo_json('ALEWt01', "OxicEvo04Glc", '0', "data\\_output\\ALEWt01_OxicEvo04Glc_0_geo.json");
    #data_io.export_dataStage01AveragesMIgeo_json('ALEWt01', "OxicEvo08Glc", '0', "data\\_output\\ALEWt01_OxicEvo08Glc_0_geo.json");
    #data_io.export_dataStage01AveragesMIgeo_json('ALEWt01', "OxicEvo09Glc", '0', "data\\_output\\ALEWt01_OxicEvo09Glc_0_geo.json");
    #data_io.export_dataStage01physiologicalRatios_d3('ALEWt01');
    #data_io.export_dataStage01replicatesMI_d3('ALEWt01');

def data_stage02():
    '''data analysis'''
    qe02 = stage02_quantification_execute();
    #qe02.drop_dataStage02_quantification();
    #qe02.initialize_dataStage02_quantification();
    #qe02.execute_glogNormalization('ALEWt01');
    #qe02.execute_descriptiveStats('ALEWt01');
    #qe02.execute_pca('ALEWt01');
    #qe02.execute_anova('ALEWt01');
    #qe02.execute_pairwiseTTest('ALEWt01');
    #qe02.execute_pcaPlot('ALEWt01');
    #qe02.execute_volcanoPlot('ALEWt01');

    '''data export'''
    qio02 = stage02_quantification_io();
    #qio02.export_volcanoPlot_d3('ALEWt01');
    #qio02.export_pcaPlot_d3('ALEWt01');
    qio02.export_heatmap_d3('ALEWt01',True);

def data_stage03():
    qe03 = stage03_quantification_execute();
    #qe03.drop_dataStage03_quantification();
    qe03.initialize_dataStage03_quantification();
    #qe03.reset_dataStage03_quantification_thermodynamicAnalysis('ALEWt01');

    '''data import'''
    qio03 = stage03_quantification_io();
    #qio03.import_dataStage03metid2keggid_add('data\\_input\\141007_metid2keggid.csv') #completed
    #qio03.import_dataStage03dG0f_add('data\\_input\\141007_compounds_dG0_f.json');
    #qio03.import_dataStage03Experiment_add('data\\_input\\141007_data_stage03_quantification_experiment.csv');
    #qio03.import_dataStage03QuantificationModel_sbml('iJO1366','10/11/2011 0:00','data\\iJO1366.xml')
    #qio03.import_dataStage03OtherData_add('data\\_input\\141007_data_stage03_quantification_otherData.csv');
    #qio03.import_dataStage03MetabolomicsData_add('data\\_input\\141007_data_stage03_quantification_metabolomicsData_glcM902.csv');
    #qio03.import_dataStage03modelPathways_add('data\\_input\\141013_data_stage03_quantification_modelPathways.csv')

    '''data analysis'''
    qe03.load_models('ALEWt01');
    #qe03.execute_makeMetabolomicsData_intracellular('ALEWt01');
    #qe03.execute_makeSimulatedData('ALEWt01');
    #qe03.execute_adjust_dG_f('ALEWt01');
    #qe03.reset_dataStage03_quantification_dG_r('ALEWt01');
    #qe03.execute_calculate_dG_r('ALEWt01');
    qe03.execute_calculate_dG_p('ALEWt01');

    '''data export'''
    #qio03.export_thermodynamicAnalysis_escher('ALEWt01');
    #qio03.export_thermodynamicAnalysisComparison_escher('ALEWt01','OxicWtGlc');
    #qio03.export_thermodynamicAnalysisComparison_csv('ALEWt01','OxicWtGlc');
