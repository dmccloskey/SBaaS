from analysis import *

def data_stage00():
    
    '''acqusition method import'''
    method_io = stage00_io();
    #method_io.import_MSMethod_add('data\\_input\\140720_ms_method.csv'); #completed
    #method_io.import_AcquisitionMethod_add('data\\_input\\140720_acquisition_method.csv'); #completed
    #method_io.import_MSComponentList_add('data\\_input\\140720_ms_components_list.csv'); #completed
    #method_io.import_MSMethod_add('data\\_input\\140719_ms_method.csv'); #completed
    #method_io.import_AcquisitionMethod_add('data\\_input\\140719_acquisition_method.csv'); #completed
    #method_io.import_MSComponentList_add('data\\_input\\140719_ms_components_list.csv'); #completed

    #method_io.import_sampleDescription_update('data\\_input\\141104_Isotopomer_ALEsKOs01_sampleFile02.csv');

    '''make the experiment from sample file'''
    execute00 = stage00_execute();
    #execute00.execute_deleteExperiments(['ALEsKOs01']); # DELETE does not seem to work
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\140722_ALEsKOs01_sampleFile01.csv',
    #                                             1,[10.0,100.0,1000.0]); #completed
    #execute00.execute_makeBatchFile('ALEsKOs01', '140722','data\\_output\\140720_ALEsKOs01_samplFile01.txt');
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\141104_Isotopomer_ALEsKOs01_sampleFile01.csv',
    #                                             1,[10.0,100.0,1000.0]); #completed
    #execute00.execute_makeBatchFile('ALEsKOs01', '141104','data\\_output\\141104_Isotopomer_ALEsKOs01_samplFile01.txt');
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\141104_Isotopomer_ALEsKOs01_sampleFile02.csv',
    #                                             1,[10.0,100.0,1000.0]); 
    #execute00.execute_makeBatchFile('ALEsKOs01', '141104','data\\_output\\141104_Isotopomer_ALEsKOs01_samplFile02.txt');
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\141104_Isotopomer_ALEsKOs01_sampleFile03.csv',
    #                                             1,[10.0,100.0,1000.0]); 
    #execute00.execute_makeBatchFile('ALEsKOs01', '141104','data\\_output\\141104_Isotopomer_ALEsKOs01_samplFile03.txt');
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\141216_Isotopomer_ALEsKOs01_sampleFile04.csv',
                                                 1,[10.0,100.0,1000.0]); 
    execute00.execute_makeBatchFile('ALEsKOs01', '141216','data\\_output\\141216_Isotopomer_ALEsKOs01_samplFile04.txt');


def data_stage01():

    '''isotopomer exeriment data imports'''
    data_io = stage01_isotopomer_io();
    #initial data imports;
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\140722_Isotopomer_ALEsKOs01_samples.csv'); #completed
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\140722_Isotopomer_ALEsKOs01_samples_glc-D.csv'); #completed

    ## updates after review:
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140722_Isotopomer_ALEsKOs01_samples02.csv'); #completed
    #data_io.import_dataStage01Normalized_update('data\\_input\\140722_Isotopomer_data_stage01_isotopomer_normalized_update01.csv'); #TODO
    #data_io.import_dataStage01Averages_updateUsedAndComment('data\\_input\\140722_Isotopomer_data_stage01_isotopomer_averages_update01.csv'); #TODO
    #data_io.import_dataStage01AveragesNormSum_updateUsedAndComment('data\\_input\\140722_Isotopomer_data_stage01_isotopomer_averagesNormSum_update01.csv'); #TODO
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\140722_Isotopomer_data_stage01_isotopomer_normalized_update01.csv'); #TODO

    ## import peakData from MRM/EPI
    #iobase = base_importData();
    #iobase.read_csv('data\\_input\\140722_Isotopomer_Samples_EPI\\fileList.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140722_Isotopomer_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();
    #iobase.read_csv('data\\_input\\140722_Isotopomer_Samples_EPI\\fileList_glc-D.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140722_Isotopomer_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();

    '''data analysis'''
    ma = stage01_isotopomer_execute();
    #ma.initialize_dataStage01();
    #ma.reset_dataStage01('ALEsKOs01')
    #ma.execute_buildSpectrumFromMRMs('ALEsKOs01',met_ids_I=[]); #completed
    ma.execute_updateNormalizedSpectrum('ALEsKOs01',sample_names_I=['140710_0_OxicEvo04Ecoli13CGlcM9_Broth-2-10.0x'],met_ids_I=['ru5p-D']);
    ma.plot_normalizedSpectrum('ALEsKOs01',sample_name_abbreviations_I=['OxicEvo04Ecoli13CGlc'],met_ids_I=['ru5p-D']);
    #ma.execute_updateNormalizedSpectrum('ALEsKOs01',met_ids_I=['succ','skm']);
    #ma.execute_recombineNormalizedSpectrum('ALEsKOs01');
    ###IMPORTANT###
    ###after running recombine for a particular compound, that compound MUST be excluded when running future updates###
    ###END###
    #ma.execute_updateNormalizedSpectrum('ALEsKOs01',met_ids_I=['icit']);
    #ma.execute_recombineNormalizedSpectrum('ALEsKOs01',met_ids_I=['icit']);
    #ma.execute_buildSpectrumFromPeakData('ALEsKOs01','isotopomer_13C',['OxicWtGlc'],
    #                                     met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.execute_filterValidatedFragments('ALEsKOs01');
    #ma.execute_updatePeakSpectrum('ALEsKOs01',['OxicWtGlc']);
    #ma.execute_normalizeSpectrumFromReference('ALEsKOs01',['OxicWtGlc'],True,
    #                                     met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.update_dataStage01NormalizedFromAverages('ALEsKOs01');
    ma.reset_datastage01_isotopomer_averages('ALEsKOs01');
    ma.execute_analyzeAverages('ALEsKOs01',met_ids_I=[],scan_types_I = []);
    ma.execute_analyzeAveragesNormSum('ALEsKOs01',met_ids_I=[],scan_types_I = []);
    ma.plot_averageSpectrumNormSum('ALEsKOs01');
    #ma.execute_analyzeSpectrumAccuracy('ALEsKOs01',scan_types_I = ['MRM','EPI']);
    #ma.execute_analyzeSpectrumAccuracyNormSum('ALEsKOs01',scan_types_I = ['MRM','EPI']);

def data_stage02():
    '''data analysis'''
    ma = stage02_isotopomer_execute();
    ma.initialize_datastage02();

    '''isotopomer exeriment data imports'''
    data_io = stage02_isotopomer_io();

    '''make the model'''

    '''make the experiment for simulation using INCA1.1 with JR2013'''
    ko_list = [];
    flux_dict = {};
    metID2RxnID = {'glc-D':{'model_id':'ecoli_RL2013_02','rxn_id':'EX_glc_LPAREN_e_RPAREN_'},
                                'ac':{'model_id':'ecoli_RL2013_02','rxn_id':'EX_ac_LPAREN_e_RPAREN_'},
                                'succ':{'model_id':'ecoli_RL2013_02','rxn_id':'EX_succ_LPAREN_e_RPAREN_'},
                                'lac-D':{'model_id':'ecoli_RL2013_02','rxn_id':'EX_lac_DASH_D_LPAREN_e_RPAREN_'},
                                'biomass':{'model_id':'ecoli_RL2013_02','rxn_id':'Ec_Biomass_INCA'}};
    snaIsotopomer2snaPhysiology = {'OxicEvo04Ecoli13CGlc':'OxicEvo04EcoliGlc',
                                'OxicEvo04gndEcoli13CGlc':'OxicEvo04gndEcoliGlc',
                                'OxicEvo04pgiEcoli13CGlc':'OxicEvo04pgiEcoliGlc',
                                'OxicEvo04sdhCBEcoli13CGlc':'OxicEvo04sdhCBEcoliGlc',
                                'OxicEvo04tpiAEcoli13CGlc':'OxicEvo04tpiAEcoliGlc'}
    sample_name_abbreviations01 = ['OxicEvo04Ecoli13CGlc',
                                'OxicEvo04gndEcoli13CGlc',
                                'OxicEvo04pgiEcoli13CGlc',
                                'OxicEvo04sdhCBEcoli13CGlc',
                                'OxicEvo04tpiAEcoli13CGlc']
    #ma.execute_makeExperimentalFluxes('ALEsKOs01',metID2RxnID_I=metID2RxnID,sample_name_abbreviations_I=sample_name_abbreviations01,snaIsotopomer2snaPhysiology_I=snaIsotopomer2snaPhysiology);
    #ma.execute_makeExperimentalFragments('ALEsKOs01',sample_name_abbreviations_I=sample_name_abbreviations01);
    #ma.execute_makeIsotopomerExperiment_INCA('ALEsKOs01',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);

    '''import the simulated results from INCA1.1'''
    data_io.import_data_stage02_isotopomer_calcFluxes_add('data\\_input\\141216_data_stage02_isotopomer_calcFluxes_ALEsKOs01.csv');
    data_io.export_fluxomicsAnalysis_escher('ALEsKOs01');

    '''analyze the simulated results from INCA1.1'''

