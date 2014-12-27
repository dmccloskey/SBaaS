from analysis import *
from analysis.analysis_stage02_isotopomer.stage02_isotopomer_dependencies import *

def data_stage00():

    '''acqusition method import'''
    method_io = stage00_io();
    #method_io.import_MSMethod_add('data\\_input\\141216_ms_method.csv');
    #method_io.import_AcquisitionMethod_add('data\\_input\\141216_acquisition_method.csv');
    #method_io.import_MSComponentList_add('data\\_input\\141216_ms_components_list.csv');

    '''make the experiment from sample file'''
    execute00 = stage00_execute();
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\141216_Isotopomer_WTEColi_113C80_U13C20_02_samplFile01.csv',
                                                 1,[10.0,100.0,1000.0]);
    execute00.execute_makeBatchFile('WTEColi_113C80_U13C20_02', '141216','data\\_output\\141216_WTEColi_113C80_U13C20_02.txt');

def data_stage01():

    '''isotopomer exeriment data imports'''
    data_io = stage01_isotopomer_io();
    #initial data imports;
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\141216_WTEColi_113C80_U13C20_02_samples.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\141216_WTEColi_113C80_U13C20_02_samples_glc-D.csv');

    ## updates after review:
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\141216_WTEColi_113C80_U13C20_02_samples_g6p.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\141216_WTEColi_113C80_U13C20_02_samples_pyr.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\141216_WTEColi_113C80_U13C20_02_samples_succ.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\141216_data_stage01_isotopomer_normalized_update01.csv');
    #data_io.import_dataStage01Averages_updateUsedAndComment('data\\_input\\141216_data_stage01_isotopomer_averages_update01.csv');
    #data_io.import_dataStage01Averages_updateUsedAndComment('data\\_input\\141216_data_stage01_isotopomer_averages_update02.csv');
    #data_io.import_dataStage01AveragesNormSum_updateUsedAndComment('data\\_input\\141216_data_stage01_isotopomer_averagesNormSum_update01.csv');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\141216_data_stage01_isotopomer_normalized_update02.csv');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\141216_data_stage01_isotopomer_normalized_update03.csv');

    ## import peakData from MRM/EPI
    iobase = base_importData();
    #iobase.read_csv('data\\_input\\141216_Samples_EPI\\fileList.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\141216_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();
    #iobase.read_csv('data\\_input\\141216_Samples_EPI\\fileList_glc-D.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\141216_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();

    '''data analysis'''
    ma = stage01_isotopomer_execute();
    #ma.initialize_dataStage01();
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_02');
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_02',met_ids_I=['g6p','pyr']);
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_02',met_ids_I=['succ']);
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_02',met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.execute_updateNormalizedSpectrum('WTEColi_113C80_U13C20_02',met_ids_I=['succ','skm']);
    #ma.execute_updateNormalizedSpectrum('WTEColi_113C80_U13C20_02',met_ids_I=['s7p']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi_113C80_U13C20_02');
    ###IMPORTANT###
    #after running recombine for a particular compound, that compound MUST be excluded when running future updates
    ###END###
    #ma.execute_updateNormalizedSpectrum('WTEColi_113C80_U13C20_02',met_ids_I=['icit']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi_113C80_U13C20_02',met_ids_I=['icit']);
    #ma.execute_buildSpectrumFromPeakData('WTEColi_113C80_U13C20_02','isotopomer_13C',['OxicWtGlc']);
    #ma.execute_buildSpectrumFromPeakData('WTEColi_113C80_U13C20_02','isotopomer_13C',['OxicWtGlc'],
    #                                     met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.execute_filterValidatedFragments('WTEColi_113C80_U13C20_02');
    #ma.execute_updatePeakSpectrum('WTEColi_113C80_U13C20_02',['OxicWtGlc']);
    #ma.execute_normalizeSpectrumFromReference('WTEColi_113C80_U13C20_02',['OxicWtGlc'],True);
    #ma.execute_normalizeSpectrumFromReference('WTEColi_113C80_U13C20_02',['OxicWtGlc'],True,
    #                                     met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.update_dataStage01NormalizedFromAverages('WTEColi_113C80_U13C20_02');
    #ma.reset_datastage01_isotopomer_averages('WTEColi_113C80_U13C20_02');
    #ma.execute_analyzeAverages('WTEColi_113C80_U13C20_02',met_ids_I=['Hexose_Pool_fru_glc-D'],scan_types_I = ['MRM','EPI']);
    ma.execute_analyzeAverages('WTEColi_113C80_U13C20_02',met_ids_I=['s7p'],scan_types_I = ['MRM']);
    #ma.execute_analyzeAveragesNormSum('WTEColi_113C80_U13C20_02',met_ids_I=['Hexose_Pool_fru_glc-D'],scan_types_I = ['MRM','EPI']);
    ma.execute_analyzeAveragesNormSum('WTEColi_113C80_U13C20_02',met_ids_I=['s7p'],scan_types_I = ['MRM']);
    #ma.execute_analyzeSpectrumAccuracy('WTEColi_113C80_U13C20_02',scan_types_I = ['MRM','EPI']);
    #ma.execute_analyzeSpectrumAccuracyNormSum('WTEColi_113C80_U13C20_02',scan_types_I = ['MRM','EPI']);

    ## WILL BE MOVED TO stage02_isotopomer_execute():
    ## make experiment
    #csource = [['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
    #                  ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O']];
    #csource_mix = [0.8,0.2];
    #ma.execute_makeIsotopomerExperiment_cobraMat('xglc_DASH_D_e',csource,csource_mix,'WTEColi_113C80_U13C20_02');

def data_stage02():
    '''data analysis'''
    ma = stage02_isotopomer_execute();
    ma.initialize_datastage02();

    '''isotopomer exeriment data imports'''
    data_io = stage02_isotopomer_io();

    '''make the reduced iJO1366 model'''
    # workflow to generate the reduced model:
    dep = stage02_isotopomer_dependencies();
    map = stage02_isotopomer_mappingUtilities();

    '''import iJS2012'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_mat(model_id_I='iJS2012',mapping_id_I='iJS2012_01', date_I='120101', model_mat_I='data\iJS2012_centralMets.mat',model_mat_name_I='iJS2012');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02',['iJS2012'],['iJS2012_01'],[]);

    '''make E. coli core from INCA ecoli network'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='ecoli_inca01',mapping_id_I='ecoli_inca01', date_I='141201', model_INCA_I='data\ecoli_inca01.csv', model_rxn_conversion_I='data\ecoli_inca01_rxn_id.csv', model_met_conversion_I='data\ecoli_inca01_met_id.csv');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02',['ecoli_inca01'],['ecoli_inca01'],[]); #manually update symmetric metabolites
    #dep.expand_ecoliINCA01('ecoli_inca01','ecoli_inca01','141203','ecoli_inca02','ecoli_inca02');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02',model_id_I=['ecoli_inca02'],
    #                                  mapping_id_rxns_I=['ecoli_inca02'],
    #                                  mapping_id_mets_I=[],
    #                                  mapping_id_new_I='ecoli_inca02'); #manually update symmetric metabolites
    #dep.expand_ecoliINCA02('WTEColi_113C80_U13C20_02','ecoli_inca02','ecoli_inca02','141207','ecoli_inca03','ecoli_inca03');

    '''make E. coli core from 10.1016/j.ymben.2013.08.006'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='ecoli_RL2013_01',mapping_id_I='ecoli_RL2013_01', date_I='141201', model_INCA_I='data\ecoli_RL2013_01.csv', model_rxn_conversion_I='data\ecoli_RL2013_01_rxn_id.csv', model_met_conversion_I='data\ecoli_RL2013_01_met_id.csv');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02',['ecoli_RL2013_01'],['ecoli_RL2013_01'],[]); #manually update symmetric metabolites
    #dep.expand_ecoliRL2013_01('WTEColi_113C80_U13C20_02','ecoli_RL2013_01','ecoli_RL2013_01','141203','ecoli_RL2013_02','ecoli_RL2013_02');

    '''make E. coli core from iJO1366'''
    #data_io.import_dataStage02IsotopomerModel_sbml('e_coli_core', '141204', 'data\\_input\\e_coli_core_irreversible.xml');
    #data_io.import_dataStage02IsotopomerAtomMapping_csv('data\\_input\\141204_atomMapping_e_coli_core_irreversible.csv');

    '''make E. coli core from iDM2014'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='ecoli_core_iDM2014_01',mapping_id_I='ecoli_core_iDM2014_01', date_I='141214', model_INCA_I='data\ecoli_core_iDM2014_01.csv', model_rxn_CBM_I='data\ecoli_core_iDM2014_01.csv');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02',['ecoli_core_iDM2014_01'],['ecoli_core_iDM2014_01'],[]); #manually update symmetric metabolites

    '''isotopomer exeriment data exports'''
    #data_io.export_data_stage02_isotopomer_models('140407_iDM2014','data\\_output\\140407_iDM2014.xml');

    '''make the experiment for simulation using INCA1.1 with the example model'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_Biomass_INCA'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':7.4*0.9,'ub':7.4*1.1};
    flux_dict['EX_cit_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['v64']={'lb':0.0,'ub':0.0};
    #flux_dict['v60']={'lb':0.0,'ub':0.0};
    flux_dict['EX_glyc_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #ma.execute_testModel('140407_iDM2014',ko_list=ko_list,flux_dict=flux_dict);
    #ma.execute_makeExperimentalFragments('WTEColi_113C80_U13C20_02');
    #ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_02',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);

    '''make the experiment for simulation using INCA1.1'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.4*1.1,'ub':-7.4*0.9};
    #flux_dict['EX_etoh_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_for_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_fum_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_glyc_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_lac_DASH_D_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_lac_DASH_L_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_pyr_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #flux_dict['EX_succ_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #ma.execute_testModel('140407_iDM2014',ko_list=ko_list,flux_dict=flux_dict);
    #ma.execute_makeExperimentalFragments('WTEColi_113C80_U13C20_02');
    #ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_02',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);
    #ma.make_missingReactionMappings('WTEColi_113C80_U13C20_02',mapping_id_new_I='full03'); #current to new
    #ma.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02',['140407_iDM2014'],['full03'],['full02']); #current rxn mapping old metabolite mapping current metabolite mapping
    #ma.update_missingReactionMappings('WTEColi_113C80_U13C20_02',mapping_id_old_I='full02',model_id_I=['140407_iDM2014'],mapping_id_I=['full03']);
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_02', model_id_I=['140407_iDM2014'],mapping_id_rxns_I=['full03'],mapping_id_mets_I=['full03'],mapping_id_new_I='full04');
    #map.make_missingReactionMappings('WTEColi_113C80_U13C20_02',model_id_I=['140407_iDM2014'],mapping_id_rxns_I=['full03'],mapping_id_mets_I=['full04'],mapping_id_new_I='full04');

    '''make the experiment for simulation using INCA1.1 with JR2013'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_Biomass_INCA'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':7.4*0.9,'ub':7.4*1.1};
    #ma.execute_makeExperimentalFragments('WTEColi_113C80_U13C20_02');
    ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_02',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);
    
    '''import the simulated results from INCA1.1'''

    '''analyze the simulated results from INCA1.1'''
