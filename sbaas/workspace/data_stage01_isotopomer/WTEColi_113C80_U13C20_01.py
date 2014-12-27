from analysis import *
from analysis.analysis_stage02_isotopomer.stage02_isotopomer_dependencies import *

def data_stage00():
    
    '''new components import'''
    #iobase = base_importData();
    #iobase.read_csv('data\\_input\\140602_13CFluxMRM.csv');

    #execute = stage00_execute();
    #execute.execute_13CFluxMRM(iobase.data);
    #iobase.clear_data();

    '''acqusition method import'''
    method_io = stage00_io();
    #method_io.import_MSMethod_add('data\\_input\\140509_ms_method.csv');
    #method_io.import_AcquisitionMethod_add('data\\_input\\140509_acquisition_method.csv');
    #method_io.import_MSComponentList_add('data\\_input\\140509_ms_components_list.csv');
    #method_io.import_MSMethod_add('data\\_input\\140602_ms_method.csv');
    #method_io.import_AcquisitionMethod_add('data\\_input\\140602_acquisition_method.csv');
    #method_io.import_MSComponentList_add('data\\_input\\140602_ms_components_list.csv');

    '''make the experiment from sample file'''
    execute00 = stage00_execute();
    #execute00.execute_makeExperimentFromSampleFile('data\\_input\\140509_WTEColi_113C80_U13C20_01_sample_file.csv',
    #                                             1,[10.0,100.0,1000.0]);
    #execute00.execute_makeBatchFile('WTEColi_113C80_U13C20_01', '140509','data\\_output\\140509_WTEColi_113C80_U13C20_01.txt');

def data_stage01():

    '''isotopomer exeriment data imports'''
    data_io = stage01_isotopomer_io();
    #initial data imports;
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\140509_WTEColi_113C80_U13C20_01_samples.csv');
    #data_io.import_dataStage01MQResultsTable_add('data\\_input\\140509_WTEColi_113C80_U13C20_01_samples_glc-D.csv');

    ## updates after review:
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140509_WTEColi_113C80_U13C20_01_samples_g6p.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140509_WTEColi_113C80_U13C20_01_samples_pyr.csv');
    #data_io.import_dataStage01MQResultsTable_update('data\\_input\\140509_WTEColi_113C80_U13C20_01_samples_succ.csv');
    #data_io.import_dataStage01Normalized_update('data\\_input\\140509_data_stage01_isotopomer_normalized_update01.csv');
    #data_io.import_dataStage01Averages_updateUsedAndComment('data\\_input\\140509_data_stage01_isotopomer_averages_update01.csv');
    #data_io.import_dataStage01Averages_updateUsedAndComment('data\\_input\\140509_data_stage01_isotopomer_averages_update02.csv');
    #data_io.import_dataStage01AveragesNormSum_updateUsedAndComment('data\\_input\\140509_data_stage01_isotopomer_averagesNormSum_update01.csv');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\140509_data_stage01_isotopomer_normalized_update02.csv');
    #data_io.import_dataStage01Normalized_updateUsedAndComment('data\\_input\\140509_data_stage01_isotopomer_normalized_update03.csv');

    ## import peakData from MRM/EPI
    iobase = base_importData();
    #iobase.read_csv('data\\_input\\140509_Samples_EPI\\fileList.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140509_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();
    #iobase.read_csv('data\\_input\\140509_Samples_EPI\\fileList_glc-D.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'processing file ' + file['filename']
    #    data_io.import_peakData_add('data\\_input\\140509_Samples_EPI\\' + file['filename'],
    #                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
    #                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type']);
    #iobase.clear_data();

    '''data analysis'''
    ma = stage01_isotopomer_execute();
    #ma.initialize_dataStage01();
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_01');
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_01',met_ids_I=['g6p','pyr']);
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_01',met_ids_I=['succ']);
    #ma.execute_buildSpectrumFromMRMs('WTEColi_113C80_U13C20_01',met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.execute_updateNormalizedSpectrum('WTEColi_113C80_U13C20_01',met_ids_I=['succ','skm']);
    ma.execute_updateNormalizedSpectrum('WTEColi_113C80_U13C20_01',met_ids_I=['s7p']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi_113C80_U13C20_01');
    ###IMPORTANT###
    #after running recombine for a particular compound, that compound MUST be excluded when running future updates
    ###END###
    #ma.execute_updateNormalizedSpectrum('WTEColi_113C80_U13C20_01',met_ids_I=['icit']);
    #ma.execute_recombineNormalizedSpectrum('WTEColi_113C80_U13C20_01',met_ids_I=['icit']);
    #ma.execute_buildSpectrumFromPeakData('WTEColi_113C80_U13C20_01','isotopomer_13C',['OxicWtGlc']);
    #ma.execute_buildSpectrumFromPeakData('WTEColi_113C80_U13C20_01','isotopomer_13C',['OxicWtGlc'],
    #                                     met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.execute_filterValidatedFragments('WTEColi_113C80_U13C20_01');
    #ma.execute_updatePeakSpectrum('WTEColi_113C80_U13C20_01',['OxicWtGlc']);
    #ma.execute_normalizeSpectrumFromReference('WTEColi_113C80_U13C20_01',['OxicWtGlc'],True);
    #ma.execute_normalizeSpectrumFromReference('WTEColi_113C80_U13C20_01',['OxicWtGlc'],True,
    #                                     met_ids_I=['Hexose_Pool_fru_glc-D']);
    #ma.update_dataStage01NormalizedFromAverages('WTEColi_113C80_U13C20_01');
    #ma.reset_datastage01_isotopomer_averages('WTEColi_113C80_U13C20_01');
    #ma.execute_analyzeAverages('WTEColi_113C80_U13C20_01',met_ids_I=['Hexose_Pool_fru_glc-D'],scan_types_I = ['MRM','EPI']);
    ma.execute_analyzeAverages('WTEColi_113C80_U13C20_01',met_ids_I=['s7p'],scan_types_I = ['MRM']);
    #ma.execute_analyzeAveragesNormSum('WTEColi_113C80_U13C20_01',met_ids_I=['Hexose_Pool_fru_glc-D'],scan_types_I = ['MRM','EPI']);
    ma.execute_analyzeAveragesNormSum('WTEColi_113C80_U13C20_01',met_ids_I=['s7p'],scan_types_I = ['MRM']);
    #ma.execute_analyzeSpectrumAccuracy('WTEColi_113C80_U13C20_01',scan_types_I = ['MRM','EPI']);
    #ma.execute_analyzeSpectrumAccuracyNormSum('WTEColi_113C80_U13C20_01',scan_types_I = ['MRM','EPI']);

    ## WILL BE MOVED TO stage02_isotopomer_execute():
    ## make experiment
    #csource = [['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
    #                  ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O']];
    #csource_mix = [0.8,0.2];
    #ma.execute_makeIsotopomerExperiment_cobraMat('xglc_DASH_D_e',csource,csource_mix,'WTEColi_113C80_U13C20_01');

def data_stage02():
    '''data analysis'''
    ma = stage02_isotopomer_execute();
    ma.initialize_datastage02();

    '''isotopomer exeriment data imports'''
    data_io = stage02_isotopomer_io();
    #data_io.import_dataStage02IsotopomerAtomMapping_csv('data\\_input\\140827_atomMapping_central02.csv'); #completed
    #data_io.import_dataStage02IsotopomerAtomMapping_csv('data\\_input\\140827_atomMapping_full01.csv'); #completed
    #data_io.import_dataStage02IsotopomerModel_sbml('140407_iDM2014', '140407', 'data\\_input\\140407_iDM2014_oxicWtEColi.xml') #completed
    #data_io.import_data_stage02_isotopomer_tracers_add('data\\_input\\140827_tracers01.csv'); #todo
    #data_io.import_data_stage02_isotopomer_experiment_add('data\\_input\\140827_experiment01.csv'); #todo
    #data_io.import_data_stage02_isotopomer_atomMappingReactions_update('data\\_output\\140924a_data_stage02_isotopomer_atomMappingReactions.csv') #cannot update from .csv using sqlalchemy; use postgresql "copy" instead.

    '''make the reduced iJO1366 model'''
    # workflow to generate the reduced model:
    dep = stage02_isotopomer_dependencies();
    map = stage02_isotopomer_mappingUtilities();
    imm = stage02_isotopomer_metaboliteMapping()
    irm = stage02_isotopomer_reactionMapping()
    #dep.makeIsotopomerModel_iteration01('data\\iteration1_140407_ijo1366_reduced_modified_pfba.csv',
    #                                                  'data\\iteration1_140407_ijo1366_netrxn_irreversible.xml',
    #                                                  "data\\iteration1_140407_ijo1366_reduced.xml",
    #                                                  'data\\iteration1_140407_ijo1366_reduced_netrxn_lbub.csv'); #completed (need to test)
    #dep.makeIsotopomerModel_iteration02('data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_reduced_modified_pfba.csv',
    #                                       "data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_reduced.xml",
    #                                       'data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_netrxn_irreversible.xml',
    #                                       'data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_reduced_netrxn_lbub.csv');#todo

    #dep.makeIsotopomerModel_cobraMAT('data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_netrxn_irreversible.xml',
    #                                       'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',
    #                                       'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.mat',
    #                                       'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.csv',
    #                                       'data\\iteration3_140601_centralMets\\isotopomer_mapping_140528_centralMets.csv',
    #                                       [],{},'140601_iDM2014');#todo

    ## check for loops
    #loops = dep.simulate_loops('data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_netrxn_irreversible.xml','data\\iteration3_140601_centralMets\\iteration3_iDMisotopomer_loops_fva_centralMets.json');
    #foundloops = dep.find_loops('data\\iteration3_140601_centralMets\\iteration3_iDMisotopomer_loops_fva_centralMets.json')
    #print len(foundloops);
    #print foundloops;
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='140407_iDM2014',mapping_id_I='full04', date_I='140407', model_INCA_I='data\\140407_iDM2014_rxnAdd01.csv', model_rxn_CBM_I='data\\140407_iDM2014_rxnAdd01.csv');
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='140407_iDM2014',mapping_id_I='full04', date_I='140407', model_INCA_I='data\\140407_iDM2014_rxnAdd02.csv', model_rxn_CBM_I='data\\140407_iDM2014_rxnAdd02.csv');
    irm.get_reactionMapping('full04','CELLENV_6');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','CELLENV_9');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','CELLENV_3');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','CELLENV_11');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','CELLENV_4');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','CELLENV_2');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','CELLENV_7');irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_1');irm.add_balanceProducts('glu_DASH_L_c');irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_10');irm.add_balanceProducts('ichor_c',unbalanced_met_positions_tracked_I=[0,1,2,3,4,5,6]);irm.add_balanceProducts('ser_DASH_L_c');irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_2');irm.add_balanceProducts('ichor_c',unbalanced_met_positions_tracked_I=[0,1,2,3,4,5,6]);irm.add_balanceProducts('akg_c',unbalanced_met_positions_tracked_I=[1,2,3,4]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_9');irm.add_balanceProducts('amet_c',unbalanced_met_positions_tracked_I=[14]);irm.add_balanceProducts('chor_c',unbalanced_met_positions_tracked_I=[1,2,3,4,5,6]);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_5');irm.add_balanceProducts('gtp_c');irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_11');irm.add_balanceProducts('amet_c',unbalanced_met_position_I=1,unbalanced_met_positions_tracked_I=[14]);
    irm.add_balanceProducts('malACP_c',unbalanced_met_positions_tracked_I=[0,1]);irm.add_balanceProducts('ala_DASH_L_c');
    irm.add_balanceProducts('malcoa_c',unbalanced_met_positions_tracked_I=[21,22,23]);
    irm.add_balanceProducts('amet_c',unbalanced_met_position_I=7);irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','COFACTOR_3');irm.add_balanceProducts('amet_c',unbalanced_met_position_I=1,unbalanced_met_positions_tracked_I=[14]);
    irm.add_balanceProducts('tyr_DASH_L_c',unbalanced_met_positions_tracked_I=[2,3,4,5,6,7,8]);
    irm.add_balanceProducts('frdp_c');irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','VITB6');irm.add_balanceProducts('e4p_c',unbalanced_met_positions_tracked_I=[1,2,3]);irm.add_balanceProducts('dxyl5p_c');irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','MOLYBDOPTERIN_1');irm.add_balanceProducts('gtp_c');irm.update_reactionMapping();irm.clear_reactionMapping();
    irm.get_reactionMapping('full04','MOLYBDOPTERIN_1');irm.add_balanceProducts('gtp_c');irm.add_balanceProducts('ctp_c');irm.update_reactionMapping();irm.clear_reactionMapping();

    '''import iJS2012'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_mat(model_id_I='iJS2012',mapping_id_I='iJS2012_01', date_I='120101', model_mat_I='data\iJS2012_centralMets.mat',model_mat_name_I='iJS2012');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01',['iJS2012'],['iJS2012_01'],[]);

    '''make E. coli core from INCA ecoli network'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='ecoli_inca01',mapping_id_I='ecoli_inca01', date_I='141201', model_INCA_I='data\ecoli_inca01.csv', model_rxn_conversion_I='data\ecoli_inca01_rxn_id.csv', model_met_conversion_I='data\ecoli_inca01_met_id.csv');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01',['ecoli_inca01'],['ecoli_inca01'],[]); #manually update symmetric metabolites
    #dep.expand_ecoliINCA01('ecoli_inca01','ecoli_inca01','141203','ecoli_inca02','ecoli_inca02');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01',model_id_I=['ecoli_inca02'],
    #                                  mapping_id_rxns_I=['ecoli_inca02'],
    #                                  mapping_id_mets_I=[],
    #                                  mapping_id_new_I='ecoli_inca02'); #manually update symmetric metabolites
    #dep.expand_ecoliINCA02('WTEColi_113C80_U13C20_01','ecoli_inca02','ecoli_inca02','141207','ecoli_inca03','ecoli_inca03');

    '''make E. coli core from 10.1016/j.ymben.2013.08.006'''
    #data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='ecoli_RL2013_01',mapping_id_I='ecoli_RL2013_01', date_I='141201', model_INCA_I='data\ecoli_RL2013_01.csv', model_rxn_conversion_I='data\ecoli_RL2013_01_rxn_id.csv', model_met_conversion_I='data\ecoli_RL2013_01_met_id.csv');
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01',['ecoli_RL2013_01'],['ecoli_RL2013_01'],[]); #manually update symmetric metabolites
    #dep.expand_ecoliRL2013_01('WTEColi_113C80_U13C20_01','ecoli_RL2013_01','ecoli_RL2013_01','141203','ecoli_RL2013_02','ecoli_RL2013_02');

    '''make E. coli core from iJO1366'''
    #data_io.import_dataStage02IsotopomerModel_sbml('e_coli_core', '141204', 'data\\_input\\e_coli_core_irreversible.xml');
    #data_io.import_dataStage02IsotopomerAtomMapping_csv('data\\_input\\141204_atomMapping_e_coli_core_irreversible.csv');

    '''make E. coli core from iDM2014'''
    data_io.import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(model_id_I='ecoli_core_iDM2014_01',mapping_id_I='ecoli_core_iDM2014_01', date_I='141214', model_INCA_I='data\ecoli_core_iDM2014_01.csv', model_rxn_CBM_I='data\ecoli_core_iDM2014_01.csv');
    map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01',['ecoli_core_iDM2014_01'],['ecoli_core_iDM2014_01'],[]); #manually update symmetric metabolites
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','succ_c');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','succ_p');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','succ_e');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','fum_c');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','fum_p');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','fum_e');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','glyc_c');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','glyc_p');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','glyc_e');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','26dap_DASH_M_c');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','26dap_DASH_LL_c');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','ptrc_c');imm.make_symmetric();imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','phpyr_c');imm.make_symmetric(met_symmetry_elements_I=['C','C','C','C','C','C','C','C','C'],met_symmetry_atompositions_I=[0,1,2,3,8,7,6,5,4]);imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    imm.get_metaboliteMapping('ecoli_core_iDM2014_01','34hpp_c');imm.make_symmetric(met_symmetry_elements_I=['C','C','C','C','C','C','C','C','C'],met_symmetry_atompositions_I=[0,1,2,3,8,7,6,5,4]);imm.update_metaboliteMapping();imm.clear_metaboliteMapping();
    
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
    #ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_01',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);

    '''make the experiment for simulation using INCA1.1 with iDM2014'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':7.4*0.9,'ub':7.4*1.1};
    flux_dict['EX_etoh_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_for_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_fum_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_lac_DASH_D_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_pyr_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_succ_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #data_O,missing_mets_O = map.find_inconsistentMetaboliteMappings('WTEColi_113C80_U13C20_01');
    #unbalanced_rxns_O = map.find_unbalancedReactionMappings('WTEColi_113C80_U13C20_01');
    #ma.simulate_model('140407_iDM2014',ko_list=ko_list,flux_dict=flux_dict);
    #ma.execute_makeExperimentalFragments('WTEColi_113C80_U13C20_01');
    #ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_01',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);
    #ma.make_missingReactionMappings('WTEColi_113C80_U13C20_01',mapping_id_new_I='full03'); #current to new
    #ma.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01',['140407_iDM2014'],['full03'],['full02']); #current rxn mapping old metabolite mapping current metabolite mapping
    #ma.update_missingReactionMappings('WTEColi_113C80_U13C20_01',mapping_id_old_I='full02',model_id_I=['140407_iDM2014'],mapping_id_I=['full03']);
    #map.make_missingMetaboliteMappings('WTEColi_113C80_U13C20_01', model_id_I=['140407_iDM2014'],mapping_id_rxns_I=['full03'],mapping_id_mets_I=['full03'],mapping_id_new_I='full04');
    #map.make_missingReactionMappings('WTEColi_113C80_U13C20_01',model_id_I=['140407_iDM2014'],mapping_id_rxns_I=['full03'],mapping_id_mets_I=['full04'],mapping_id_new_I='full04');

    '''make the experiment for simulation using INCA1.1 with JR2013'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_Biomass_INCA'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':7.4*0.9,'ub':7.4*1.1};
    #ma.execute_makeExperimentalFragments('WTEColi_113C80_U13C20_01');
    #ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_01',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);

    '''make the experiment for simulation using INCA1.1 with iJS2012'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':7.4*0.9,'ub':7.4*1.1};
    flux_dict['EX_etoh_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_for_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_fum_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_glyc_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_lac_DASH_D_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_lac_DASH_L_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_pyr_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    flux_dict['EX_succ_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
    #ma.simulate_model('iJS2012',ko_list=ko_list,flux_dict=flux_dict);
    #ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_01',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);

    '''make the experiment for simulation using INCA1.1 with ecoli_core_iDM2014'''
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_INCA'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':7.4*0.9,'ub':7.4*1.1};
    ma.execute_makeIsotopomerExperiment_INCA('WTEColi_113C80_U13C20_01',stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);
    
    '''import the simulated results from INCA1.1'''
    #data_io.import_data_stage02_isotopomer_calcFluxes_add('data\\_input\\141216_data_stage02_isotopomer_calcFluxes_WTEColi_113C80_U13C20_01.csv');
    #data_io.export_fluxomicsAnalysis_escher('WTEColi_113C80_U13C20_01');
    
    '''analyze the simulated results from INCA1.1'''
