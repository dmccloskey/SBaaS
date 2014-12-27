from analysis import *

def data_stage01():
    '''update data'''
    #data = base_importData();
    #update = stage01_quantification_update();
    #data.read_csv('nitrate01_update_6pgc.csv');
    #data.format_data();
    #update.update_data_stage01_quantification_MQResultsTable(data.data);
    #data.clear_data();

    '''data analysis'''
    ma = stage01_quantification_execute();
    #ma.initialize_dataStage01();
    #ma.reset_dataStage01('nitrate01');
    #ma.execute_checkISMatch('nitrate01');
    #ma.execute_LLOQAndULOQ('nitrate01');
    #ma.execute_checkLLOQAndULOQ('nitrate01');
    #ma.execute_analyzeDilutions('nitrate01');
    #ma.execute_checkCV_dilutions('nitrate01');
    #ma.execute_normalizeSamples2Biomass('nitrate01','MG1655','ODspecificTotalCellVolume_Volkmer2011');
    #ma.execute_removeDuplicateDilutions('nitrate01');
    #ma.execute_normalizeSamples2Biomass('nitrate01',
    #                                                            ['130904_0_AnoxicWtGlcM9NitratepvdfACN_Broth-2',
    #                                                             '130904_0_AnoxicWtGlcM9NitratepvdfACN_Broth-3'],
    #                                                            ['6pgc.6pgc_1.Light'],
    #                                                             'MG1655',
    #                                                             'ODspecificTotalCellVolume_Volkmer2011')
    ma.reset_datastage01_quantification_replicatesAndAverages('nitrate01');
    ma.execute_analyzeReplicates('nitrate01');
    ma.execute_analyzeAverages('nitrate01');
    ma.execute_checkCVAndExtracelluar_averages('nitrate01');
    ma.execute_calculateMissingValues_replicates('nitrate01');
    ma.execute_calculateMissingComponents_replicates('nitrate01','MG1655','ODspecificTotalCellVolume_Volkmer2011');

    '''data export'''
    data_io = stage01_quantification_io();
    data_io.export_dataStage01Replicates_csv('nitrate01','dataStage01Replicates_nitrate01.csv');
    data_io.export_dataStage01ReplicatesMI_csv('nitrate01','dataStage01ReplicatesMI2_nitrate01.csv');