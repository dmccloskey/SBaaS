from analysis import *

def data_stage00():

    # import new components
    io00 = stage00_io();
    #io00.import_MSComponents_add('data\\_input\\xxxxxx_ms_components.csv');

    execute00 = stage00_execute();
    # make quant transition for udpg 565 -> 323
    #execute00.execute_scheduledMRMPro_quant([{'met_id':'udpg','precursor_formula':'C15H23N2O17P2-','product_formula':'C9H12N2O9P-'}]); # complete
    execute00.execute_exportAcqusitionMethod('McCloskey2013','-','quantification','data\\_output\\xxxxxx_acqusition_method.csv')

    '''acqusition method import'''
    io00 = stage00_io();
    #io00.import_MSMethod_add('data\\_input\\xxxxxx_ms_method.csv'); # todo
    #io00.import_AcquisitionMethod_add('data\\_input\\xxxxxx_acquisition_method.csv'); # todo
    #io00.import_MSComponentList_add('data\\_input\\xxxxxx_ms_components_list.csv'); # todo

    '''quantitation method imports'''
    #io00.import_calibratorConcentrations_add('data\\_input\\xxxxxx_calibrator_concentrations.csv'); # todo
    
    '''make the experiment from sample file'''
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\xxxxxx_experiment01_sample_file01.csv',
    #                                             1,[10.0]); # need to check if quantitation_method_id is in quantitation_method_list
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\xxxxxx_experiment01_sample_file02.csv',
    #                                             1,[10.0]);
    #execute00.execute_makeBatchFile('experiment01', 'xxxxxx','data\\_output\\xxxxxx_experiment01.txt');
    #execute00.execute_makeExperimentFromCalibrationFile('data\\_input\\xxxxxx_calibration_file.csv');
    #execute00.execute_exportCalibrationConcentrations('data\\_input\\xxxxxx_calibration_samplesAndComponents.csv','data\\_output\\xxxxxx_calibration_concentrations.csv');