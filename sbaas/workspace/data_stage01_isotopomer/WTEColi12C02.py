from analysis import *

def data_stage00():
    iobase = base_importData();
    #iobase.read_csv('data\\_input\\140415_13CFluxMRM.csv');

    #execute = stage00_execute();
    #execute.execute_13CFluxMRM(iobase.data);
    #iobase.clear_data();

    '''data import'''
    method_io = stage00_io();
    #method_io.import_MSMethod_add('data\\_input\\140415_ms_method.csv');
    #method_io.import_MSComponentList_add('data\\_input\\140415_ms_components_list.csv');
    #method_io.import_AcquisitionMethod_add('data\\_input\\140415_acquisition_method.csv');

def data_stage01():
    data_io = stage01_isotopomer_io();
    #initial data imports
    #data_io.import_sampleStorage_add('data\\_input\\140415_sample_storage.csv');
    #data_io.import_samplePhysiologicalParameters_add('data\\_input\\140415_sample_physiologicalparameters.csv');
    #data_io.import_sampleDescription_add('data\\_input\\140415_sample_description.csv');
    #data_io.import_sample_add('data\\_input\\140415_sample.csv');
    #data_io.import_experiment_add('data\\_input\\140415_experiment.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\140415_samples.csv');

    ## updates after review:
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140415_samples_update01.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140415_data_stage01_isotopomer_normalized_update01.csv');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\140415_data_stage01_isotopomer_normalized_update02.csv');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\140415_data_stage01_isotopomer_normalized_update03.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140415_samples_update01.csv');
    #data_io.import_dataStage01PeakSpectrum_add('data\\data_stage01_isotopomer_peakSpectrum_update01.csv');

    ## import peakData from MRM/EPI
    #iobase.read_csv('data\\_input\\140415_Samples_EPI\\fileList.csv'); #only phe-L and phpyr
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140415_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();

    '''data analysis'''
    ma = stage01_isotopomer_execute();
    #ma.initialize_dataStage01();
    #ma.execute_buildSpectrumFromMRMs('WTEColi12C02');
    #ma.execute_buildSpectrumFromMRMs('WTEColi12C02',met_ids_I=['icit']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi12C02');
    ###IMPORTANT###
    #after running recombine for a particular compound, that compound MUST be excluded when running future updates
    ###END###
    #ma.execute_updateNormalizedSpectrum('WTEColi12C02',met_ids_I=['icit']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi12C02',met_ids_I=['icit']);

    #ma.execute_buildSpectrumFromPeakData('WTEColi12C02','isotopomer_13C',['OxicWtGlc']);
    #ma.execute_updatePeakSpectrum('WTEColi12C02',['OxicWtGlc']);
    #ma.execute_normalizeSpectrumFromReference('WTEColi12C02',['OxicWtGlc'],True);

    #ma.update_dataStage01NormalizedFromAverages('WTEColi12C02');

    #ma.execute_analyzeAverages('WTEColi12C02',scan_types_I = ['MRM','EPI']);
    #ma.execute_analyzeAveragesNormSum('WTEColi12C02',scan_types_I = ['MRM','EPI']);
    #ma.execute_analyzeSpectrumAccuracy('WTEColi12C02',scan_types_I = ['MRM','EPI']);
    #ma.execute_analyzeSpectrumAccuracyNormSum('WTEColi12C02',scan_types_I = ['MRM','EPI']);

    '''data export'''
    data_io.export_compareAveragesNormSumSpectrumToTheoretical('WTEColi12C02','data\\_output\\140415_compareAveragesNormSumSpectrumToTheoretical.csv');
    #data_io.export_compareAveragesSpectrumToTheoretical('WTEColi12C02','data\\_output\\140415_compareAveragesSpectrumToTheoretical.csv');