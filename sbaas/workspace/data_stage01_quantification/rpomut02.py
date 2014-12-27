from analysis import *

def data_stage00():

    # import new components
    io00 = stage00_io();
    #io00.import_MSComponents_add('data\\_input\\140521_ms_components.csv'); # complete

    execute00 = stage00_execute();
    ## import structure files into metabolomics_standards
    #execute00.execute_importStructureFile([{'met_id':'ara5p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'}]); # complete
    ## update formula, mass, and exact mass from structure files
    ##execute00.execute_updateFormulaAndMassFromStructure(['ara5p']); #cxcalc appears to be broken # complete
    ## update precursor formula and exact mass from structure files
    #execute00.execute_updatePrecursorFormulaAndMass(['skm','chor','udpg','udpglcur','succoa','malcoa','ara5p','xu5p-D']); # complete
    #execute00.execute_scheduledMRMPro_quant([{'met_id':'Pool_2pg_3pg','precursor_formula':'C3H6O7P-','product_formula':'O3P-'},
    #                                         {'met_id':'Pool_2pg_3pg','precursor_formula':'C3H6O7P-','product_formula':'H2O4P-'},
    #                                        {'met_id':'dgtp','precursor_formula':'C10H15N5O13P3-','product_formula':'C10H12N5O9P2-'},
    #                                        {'met_id':'dgtp','precursor_formula':'C10H15N5O13P3-','product_formula':'HO6P2-'},
    #                                        {'met_id':'dgdp','precursor_formula':'C10H14N5O10P2-','product_formula':'C5H9O9P2-'},
    #                                        {'met_id':'dgdp','precursor_formula':'C10H14N5O10P2-','product_formula':'O3P-'},
    #                                        {'met_id':'dgmp','precursor_formula':'C10H13N5O7P-','product_formula':'O3P-'},
    #                                        {'met_id':'dgmp','precursor_formula':'C10H13N5O7P-','product_formula':'C5H9O4'},
    #                                        {'met_id':'2mcit','precursor_formula':'C7H9O7-','product_formula':'C3H3O3-'},
    #                                        {'met_id':'2mcit','precursor_formula':'C7H9O7-','product_formula':'C5HO4'},
    #                                        {'met_id':'2obut','precursor_formula':'C4H5O3-','product_formula':'O2-'},
    #                                        {'met_id':'2obut','precursor_formula':'C4H5O3-','product_formula':'C2HO3-'},
    #                                        {'met_id':'chor','precursor_formula':'C10H9O6-','product_formula':'C6H3O-'},
    #                                        {'met_id':'malcoa','precursor_formula':'C24H37N7O19P3S-','product_formula':'O3P-'},
    #                                        {'met_id':'skm','precursor_formula':'C7H9O5-','product_formula':'C3H5O2-'},
    #                                        {'met_id':'skm','precursor_formula':'C7H9O5-','product_formula':'C6H5O-'},
    #                                        {'met_id':'succoa','precursor_formula':'C25H39N7O19P3S-','product_formula':'O3P-'},
    #                                        {'met_id':'udpg','precursor_formula':'C15H23N2O17P2-','product_formula':'C6H10O8P-'},
    #                                        {'met_id':'udpg','precursor_formula':'C15H23N2O17P2-','product_formula':'C9H11N2O11P2-'},
    #                                        {'met_id':'udpglcur','precursor_formula':'C15H21N2O18P2-','product_formula':'C9H12N2O9P-'},
    #                                        {'met_id':'udpglcur','precursor_formula':'C15H21N2O18P2-','product_formula':'C9H13N2O12P2-'},
    #                                        {'met_id':'ara5p','precursor_formula':'C5H10O8P-','product_formula':'H2O4P-'},
    #                                        {'met_id':'ara5p','precursor_formula':'C5H10O8P-','product_formula':'C2H4O5P-'},
    #                                        {'met_id':'xu5p-D','precursor_formula':'C5H10O8P-','product_formula':'C2H4O5P-'},
    #                                        {'met_id':'xu5p-D','precursor_formula':'C5H10O8P-','product_formula':'H2O4P-'}
                                            #]); # complete

    '''acqusition method import'''
    io00 = stage00_io();
    #io00.import_MSMethod_add('data\\_input\\140521_ms_method.csv'); # complete
    #io00.import_AcquisitionMethod_add('data\\_input\\140521_acquisition_method.csv'); # complete
    #io00.import_MSComponentList_add('data\\_input\\140521_ms_components_list.csv'); # complete

    '''quantitation method imports'''
    #io00.import_calibratorConcentrations_add('data\\_input\\140501_calibrator_concentrations.csv'); # complete
    
    '''make the experiment from sample file'''
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\140521_rpomut02_sample_file01.csv',
    #                                             1,[10.0]); # need to check if quantitation_method_id is in quantitation_method_list  # complete
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\140521_rpomut02_sample_file02.csv',
    #                                             1,[10.0]);  # complete
    #execute00.execute_makeBatchFile('rpomut02', '140521','data\\_output\\140521_rpomut02.txt'); # complete
    #execute00.execute_makeExperimentFromCalibrationFile('data\\_input\\140521_calibration_file.csv'); # complete
    #execute00.execute_exportCalibrationConcentrations('data\\_input\\140521_calibration_samplesAndComponents.csv','data\\_output\\140521_calibration_concentrations.csv'); # complete

def data_stage01():
    '''data import'''
    qe01 = stage01_quantification_execute();
    #qe01.execute_deleteExperimentFromMQResultsTable('rpomut02'); # reserved for bad data imports
    qio01 = stage01_quantification_io();
    #qio01.import_quantitationMethod_add('140521','data\\_input\\140521_QMethod.csv'); # complete
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\140521_samples.csv'); # complete
    #qio01.import_dataStage01MQResultsTable_add('data\\_input\\140521_calibrationCurves.csv'); # complete
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140521_samples_update01.csv');
    #qio01.import_dataStage01MQResultsTable_update('data\\_input\\140521_calibrationCurves_update01.csv');
    #qio01.import_dataStage01Normalized_update('data\\_input\\140521_data_stage01_quantitation_normalized_rpomut02_update01.csv');

    '''calibrator analysis'''
    #qm01 = stage01_quantification_QMethod();
    #qm01.execute_quantitationMethodUpdate();

    '''data analysis'''
    #qe01.initialize_dataStage01_quantification();
    #qe01.reset_dataStage01_quantification('rpomut02');
    #qe01.execute_checkISMatch('rpomut02');
    #qe01.execute_LLOQAndULOQ('rpomut02');
    #qe01.execute_checkLLOQAndULOQ('rpomut02');
    #qe01.execute_analyzeDilutions('rpomut02');
    #qe01.execute_checkCV_dilutions('rpomut02');
    #qe01.execute_analyzeQCs('rpomut02');
    #qe01.execute_checkCV_QCs('rpomut02');
    #qe01.execute_normalizeSamples2Biomass('rpomut02','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_removeDuplicateDilutions('rpomut02');
    #qe01.reset_datastage01_quantification_replicatesAndAverages('rpomut02');
    #qe01.execute_analyzeReplicates('rpomut02');
    #qe01.execute_analyzeAverages('rpomut02');
    #qe01.execute_checkCVAndExtracelluar_averages('rpomut02');
    #qe01.reset_datastage01_quantification_replicatesAndAveragesMI('rpomut02')
    #qe01.execute_calculateMissingValues_replicates('rpomut02');
    #qe01.execute_calculateMissingComponents_replicates('rpomut02','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #qe01.execute_calculateAverages_replicates('rpomut02');
    #qe01.execute_calculateGeoAverages_replicates('rpomut02');
    #qe01.execute_physiologicalRatios_replicates('rpomut02');
    #qe01.execute_physiologicalRatios_averages('rpomut02');
    #qe01.execute_scatterLinePlot_physiologicalRatios('rpomut02',ratio_ids_I=['nc'])
    #qe01.execute_boxAndWhiskersPlot_averages('rpomut02',component_names_I=['akg.akg_1.Light','gln-L.gln-L_1.Light','glu-L.glu-L_1.Light'])
    qe01.execute_barPlot_averages('rpomut02',component_names_I=['akg.akg_1.Light','cit.cit_1.Light','fum.fum_1.Light',
                                                                        'mal-L.mal-L_1.Light','succ.succ_1.Light',
                                                                        'gln-L.gln-L_1.Light','glu-L.glu-L_1.Light',
                                                                        'acon-C.acon-C_1.Light','icit.icit_2.Light'])

    '''data export'''
    #qio01.export_dataStage01Replicates_csv('rpomut02','data\\_output\\dataStage01Replicates_rpomut02.csv');
    #qio01.export_dataStage01ReplicatesMI_csv('rpomut02','data\\_output\\dataStage01ReplicatesMI2_rpomut02.csv');
    #qio01.export_dataStage01AveragesMIgeo_json('rpomut02', "OxicRph-pyrE82", '0', "data\\_output\\rpomut02_OxicRph-pyrE82_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('rpomut02', "OxicRpoBE546V", '0', "data\\_output\\rpomut02_OxicRpoBE546V_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('rpomut02', "OxicRpoBE672K", '0', "data\\_output\\rpomut02_OxicRpoBE672K_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('rpomut02', "OxicRpoBE672K-rph-pyrE82", '0', "data\\_output\\rpomut02_OxicRpoBE672K-rph-pyrE82_0_geo.json");
    #qio01.export_dataStage01AveragesMIgeo_json('rpomut02', "OxicWtGlc", '0', "data\\_output\\rpomut02_OxicWtGlc_0_geo.json");
    #qio01.export_dataStage01physiologicalRatios_d3('rpomut02');
    #qio01.export_dataStage01replicatesMI_d3('rpomut02');

def data_stage02():
    '''data analysis'''
    qe02 = stage02_quantification_execute();
    #qe02.drop_dataStage02_quantification();
    #qe02.reset_dataStage02_quantification('rpomut02');
    #qe02.execute_glogNormalization('rpomut02');
    #qe02.execute_descriptiveStats('rpomut02');
    #qe02.execute_pca('rpomut02');
    #qe02.execute_anova('rpomut02');
    #qe02.execute_pairwiseTTest('rpomut02');
    #qe02.execute_pcaPlot('rpomut02');
    #qe02.execute_volcanoPlot('rpomut02');

    '''data export'''
    qio02 = stage02_quantification_io();
    #qio02.export_volcanoPlot_d3('rpomut02');
    #qio02.export_pcaPlot_d3('rpomut02');
    qio02.export_heatmap_d3('rpomut02');

def data_stage03():
    qe03 = stage03_quantification_execute();
    #qe03.drop_dataStage03_quantification();
    #qe03.initialize_dataStage03_quantification();
    qe03.reset_dataStage03_quantification_thermodynamicAnalysis('rpomut02');

    '''data import'''
    qio03 = stage03_quantification_io();
    #qio03.import_dataStage03Experiment_add('data\\_input\\141010_data_stage03_quantification_experiment.csv');
    #qio03.import_dataStage03OtherData_add('data\\_input\\141010_data_stage03_quantification_otherData.csv');
    #qio03.import_dataStage03MetabolomicsData_add('data\\_input\\141010_data_stage03_quantification_metabolomicsData_glcM9.csv');

    '''data analysis'''
    qe03.load_models('rpomut02');
    #qe03.execute_makeMetabolomicsData_intracellular('rpomut02');
    #qe03.execute_makeSimulatedData('rpomut02');
    qe03.execute_adjust_dG_f('rpomut02');
    qe03.execute_calculate_dG_r('rpomut02');

    '''data export'''
    #qio03.export_thermodynamicAnalysis_escher('rpomut02');
    qio03.export_thermodynamicAnalysisComparison_escher('rpomut02','OxicWtGlc');
    qio03.export_thermodynamicAnalysisComparison_csv('rpomut02','OxicWtGlc');

def _main_():
    data_stage00;
    data_stage01;
    data_stage02;

