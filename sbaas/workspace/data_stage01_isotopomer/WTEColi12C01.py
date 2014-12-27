from analysis import *

def test_ORM2Excel():
    from resources.pyvot import ORM2Excel

    #pyvot update does not always update:
    com = ORM2Excel();
    com.execute_ORM2Excel_data_stage01_isotopomer_peakSpectrum('WTEColi12C01');

def data_stage00():
    #iobase = base_importData();
    #iobase.read_csv('data\\_input\\140415_13CFluxMRM.csv');

    #execute = stage00_execute();
    #execute.execute_13CFluxMRM(iobase.data);

    '''add f6p and g1p into ms_components-ms_methodtype='isotopomer_13C'
    explanation: f6p and g1p were created on the fly in MQ from g6p trace'''
    #import the data
    iobase = base_importData();
    #iobase.read_csv('data\\_input\\140228_13CFluxMRM.csv');
    #iobase.clear_data();
    ##make the method
    #execute = stage00_execute();
    #execute.execute_13CFluxMRM(iobase.data);
    #iobase.clear_data();

    '''data import'''
    #method_io = stage00_io();
    #method_io.import_MSComponentList_add('data\\_input\\140228_ms_components_list.csv');
    
def data_stage01():
    data_io = stage01_isotopomer_io();
    ##initial data imports
    #data_io.import_quantitationMethod_add('140228','data\\_input\\140228_QMethod.csv'); Not used for fluxomics
    #data_io.import_sampleStorage_add('data\\_input\\140228_sample_storage.csv');
    #data_io.import_samplePhysiologicalParameters_add('data\\_input\\140228_sample_physiologicalparameters.csv');
    #data_io.import_sampleDescription_add('data\\_input\\140228_sample_description.csv');
    #data_io.import_metabolomicsSample_add('data\\_input\\140228_metabolomics_sample.csv');
    #data_io.import_metabolomicsExperiment_add('data\\_input\\140228_metabolomics_experiment.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\140228_samples.csv');

    ## updates after review:
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update01.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140228_samples_update01.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update02.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update03.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update04.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update05.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140228_samples_update02.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update06.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140228_data_stage01_isotopomer_normalized_update07.csv');
    #data_io.import_dataStage01PeakSpectrum_add('data\\data_stage01_isotopomer_peakSpectrum_update01.csv');

    ## import peakData from MRM/EPI for QCs
    ## warning: these files do not contain headers
    #iobase.read_csv('data\\_input\\140228_MRM_EPI\\fileList.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140228_MRM_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();
    ## import peakData from ER/EPI for QCs
    ## warning: these files do not contain headers
    #iobase.read_csv('data\\_input\\140228_ER_EPI\\fileList.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140228_ER_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();
    ## import peakData from MRM/EPI for Unknowns
    #iobase.read_csv('data\\_input\\140228_Samples_EPI\\fileList.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140228_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type'],header_I=True);
    #iobase.clear_data();

    '''data analysis'''
    ma = stage01_isotopomer_execute();
    #ma.initialize_dataStage01();
    #ma.execute_buildSpectrumFromMRMs('WTEColi12C01');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\140228_data_stage01_isotopomer_normalized_update08.csv');
    #ma.execute_buildSpectrumFromMRMs('WTEColi12C01',met_ids_I=['glu-L','acon-C']);
    #ma.execute_buildSpectrumFromMRMs('WTEColi12C01',met_ids_I=['amp','pep','icit','gtp']);
    #ma.execute_updateNormalizedSpectrum('WTEColi12C01');
    #ma.execute_recombineNormalizedSpectrum('WTEColi12C01');
    ###IMPORTANT###
    #after running recombine for a particular compound, that compound MUST be excluded when running future updates
    ###END###
    #ma.execute_updateNormalizedSpectrum('WTEColi12C01',met_ids_I=['icit']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi12C01',met_ids_I=['icit']);
    #ma.execute_buildSpectrumFromPeakData('WTEColi12C01','isotopomer_13C',['MRMQC','ERQC','OxicWtGlc']);
    #ma.execute_updatePeakSpectrum('WTEColi12C01',['ERQC','MRMQC','OxicWtGlc']);
    #ma.execute_normalizeSpectrumFromReference('WTEColi12C01',['MRMQC','OxicWtGlc'],True);
    #ma.execute_normalizeSpectrumFromReference('WTEColi12C01',['ERQC'],False);
    #ma.update_dataStage01NormalizedFromAverages('WTEColi12C01');
    ma.execute_analyzeAverages('WTEColi12C01',scan_types_I = ['MRM','EPI','ER']);
    ma.execute_analyzeAveragesNormSum('WTEColi12C01',scan_types_I = ['MRM','EPI','ER']);
    ma.execute_analyzeSpectrumAccuracy('WTEColi12C01',scan_types_I = ['MRM','EPI','ER']);
    ma.execute_analyzeSpectrumAccuracyNormSum('WTEColi12C01',scan_types_I = ['MRM','EPI','ER']);

    '''data export'''
    data_io.export_compareAveragesNormSumSpectrumToTheoretical('WTEColi12C01','data\\_output\\140228_compareAveragesNormSumSpectrumToTheoretical.csv');
    #data_io.export_compareAveragesSpectrumToTheoretical('WTEColi12C01','data\\_output\\140228_compareAveragesSpectrumToTheoretical.csv');
