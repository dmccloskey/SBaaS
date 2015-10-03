# define search paths manually
import sys
from data import sbaas_settings as settings
#sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\sbaas\\sbaas')
sys.path.append(settings.sbaas)
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\sequencing_utilities')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\thermodynamics')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\component-contribution')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\io_utilities')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\sequencing_analysis')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\calculate_utilities')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\MDV_utilities')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\molmass')

##Analysis tests:
#from tests import analysis_ale, analysis_physiology, analysis_resequencing
#analysis_ale.run_all_tests();
#analysis_physiology.run_all_tests();
#analysis_resequencing.run_all_tests();

##Visualization tests:
#from visualization.server import run
#run();
##run(port=8080,public=True);

###Debug mode:
#from sbaas.analysis.analysis_stage01_isotopomer import *
#from sbaas.models import *
#session=Session();
## initialize the execution object
#ex01 = stage01_isotopomer_execute(session);
## initialize the io object
#io01 = stage01_isotopomer_io(session);
#io01.export_compareAveragesNormSumSpectrumToTheoretical(
#    experiment_id_I="WTEColi12C01",
#    filename="WTEColi12C01_peakSpectrumAccuracy.csv",
#    #sample_name_abbreviations_I=["MRMQC","OxicWtGlc"],
#    scan_types_I=None,
#    met_ids_I = None
#    )
#io01.export_compareAveragesNormSumSpectrumToTheoretical(
#    experiment_id_I="WTEColi12C02",
#    filename="WTEColi12C02_peakSpectrumAccuracy.csv",
#    #sample_name_abbreviations_I=["OxicWtGlc"],
#    scan_types_I=None,
#    met_ids_I = None
#    )

##Debug mode:
from sbaas.analysis.analysis_stage02_isotopomer import *
from sbaas.analysis.visualization import *
from sbaas.models import *
session=Session();
# initialize the execution object
ex02 = stage02_isotopomer_execute(session);
# initialize the io object
io02 = stage02_isotopomer_io(session);
# initialize the iovis object
iovis = visualization_io(session);
analysis_ids = [
    'WTEColi_113C80_U13C20_01_ecoli_RL2013_02_ecoli_RL2013_02_OxicWtGlc_3',
    'WTEColi_113C80_U13C20_02_ecoli_core_iDM2014_02_ecoli_core_iDM2014_02_OxicWtGlc_3',
    'WTEColi_113C80_U13C20_02_iJS2012_iJS2012_01_OxicWtGlc_3',
    'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_3',
    'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_3_noCofactorsMS'
    ]
# reset previous imports
for analysis_id in analysis_ids:
    ex02.reset_datastage02_isotopomer_fittedData(analysis_id)
# import simulations 
io02.import_data_stage02_isotopomer_simulation_add('/_input/150924_Isotopomer_WTEColi_113C80_U13C20_01_simulation02.csv');
# import analyses
io02.import_data_stage02_isotopomer_analysis_add('/_input/150924_Isotopomer_WTEColi_113C80_U13C20_01_analysis02.csv')
# import visualization
iovis.import_visualizationProject_add(settings.workspace_data + '/_input/150924_Isotopomer_WTEColi_113C80_U13C20_01_project02.csv')
# import .mat files containing the estimated fluxes for ecoli_RL2013_02
io02.import_isotopomerSimulationResults_INCA('WTEColi_113C80_U13C20_01_ecoli_RL2013_02_ecoli_RL2013_02_OxicWtGlc_1',
                        'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/WTEColi_113C80_U13C20_01/WTEColi_113C80_U13C20_01_ecoli_RL2013_02_OxicWtGlc_3.mat')
io02.import_isotopomerSimulationResults_INCA('WTEColi_113C80_U13C20_01_ecoli_RL2013_02_ecoli_RL2013_02_OxicWtGlc_1_noEPI',
                        'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/WTEColi_113C80_U13C20_01/WTEColi_113C80_U13C20_01_ecoli_RL2013_02_OxicWtGlc_3_noEPI.mat')
io02.import_isotopomerSimulationResults_INCA('WTEColi_113C80_U13C20_01_ecoli_RL2013_02_ecoli_RL2013_02_OxicWtGlc_1_uniqueMIDs',
                        'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/WTEColi_113C80_U13C20_01/WTEColi_113C80_U13C20_01_ecoli_RL2013_02_OxicWtGlc_3_uniqueMIDs.mat')
## remove unbounded reactions
#for analysis_id in analysis_ids:
#    ex02.execute_removeUnboundedFittedFluxes(analysis_id);
# reset previous analyses
for analysis_id in analysis_ids:
    ex02.reset_datastage02_isotopomer_fittedNetFluxes(analysis_id)
#make net reactions
for analysis_id in analysis_ids:
    # break apart lumped reactions into individual reactions
    # normalize the fluxes to glucose uptake
    # convert irreversible reactions to net reactions
    ex02.execute_makeNetFluxes(analysis_id,
        normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
        convert_netRxn2IndividualRxns_I=True,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        lower_bound_I=0.0,upper_bound_I=1000.0);
    #make net reactions
    ex02.execute_makeNetFluxes(analysis_id,
        normalize_rxn_id_I=None,
        convert_netRxn2IndividualRxns_I=False,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        lower_bound_I=0.0,upper_bound_I=1000.0);
    #make net reactions
    ## normalize the fluxes to glucose uptake
    #ex02.execute_makeNetFluxes(analysis_id,
    #    normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
    #    convert_netRxn2IndividualRxns_I=False,
    #    calculate_fluxStdevFromLBAndUB_I=True,
    #    calculate_fluxAverageFromLBAndUB_I=False,
    #    substitute_zeroFluxForNone_I=False,
    #    lower_bound_I=0.0,upper_bound_I=1000.0);
## manually remove reactions in loops
#cmd = '''UPDATE "data_stage02_isotopomer_fittedNetFluxes"
#SET used_=false
#  WHERE 
#  (flux_units LIKE 'mmol*gDCW-1*hr-1' AND simulation_id LIKE 'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_3_noCofactorsMS' AND (rxn_id LIKE 'ALAR' OR rxn_id LIKE 'PRPPS'))
#  OR
#  (flux_units LIKE 'mmol*gDCW-1*hr-1' AND simulation_id LIKE 'WTEColi_113C80_U13C20_02_ecoli_core_iDM2014_02_ecoli_core_iDM2014_02_OxicWtGlc_3' AND rxn_id LIKE 'EX_co2_LPAREN_e_RPAREN__unlabeled')
#  OR
#  (flux_units LIKE 'mmol*gDCW-1*hr-1' AND simulation_id LIKE 'WTEColi_113C80_U13C20_02_iJS2012_iJS2012_01_OxicWtGlc_3' AND (rxn_id LIKE 'CO2tex' OR rxn_id LIKE 'CO2tpp'))
#  ;'''
#ex02.session.execute(cmd);
#ex02.session.commit();
# reset previous analysis
for analysis_id in analysis_ids:
    ex02.reset_datastage02_isotopomer_fittedFluxStatistics(analysis_id)
    ex02.reset_datastage02_isotopomer_fittedNetFluxStatistics(analysis_id)
#calculate the net flux statistics
for analysis_id in analysis_ids:
    ex02.execute_calculateFluxStatistics(analysis_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
    ex02.execute_calculateNetFluxStatistics(analysis_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
    #ex02.execute_calculateNetFluxStatistics(analysis_id,
    #                                    flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'],
    #                                    rxn_ids_I = ['ATPM','PGI','MDH','EDA','EDD','SUCOAS','PGL','PGM','PGK','ACONTa','ACONTb','GLCptspp','FUM','ENO','SUCDi','RPE','AKGDH','PDH','GAPD','MALS','CS','GND','PPC','TPI','RPI','PYK','ME1','ME2','TALA','ICDHyr','FBA','PFK','ICL','PPCK']
    #                                    )
io02.export_data_stage02_isotopomer_fittedFluxStatistics_csv(analysis_ids,'WTEColi_113C80_U13C20_01_fittedFluxStatistics.csv');
io02.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(analysis_ids,'WTEColi_113C80_U13C20_01_fittedNetFluxStatistics.csv',flux_units_I = ['mmol*gDCW-1*hr-1']);
#io02.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(analysis_ids,'WTEColi_113C80_U13C20_01_fittedNetFluxStatistics_coreFluxes.csv',flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized']);
io02.export_data_stage02_isotopomer_fittedNetFluxes_csv(analysis_ids,'WTEColi_113C80_U13C20_01_fittedNetFluxes.csv');
io02.export_data_stage02_isotopomer_fittedMeasuredFragments_csv(analysis_ids,'WTEColi_113C80_U13C20_01_fittedMeasuredFragments.csv');
io02.export_data_stage02_isotopomer_fittedData_csv(analysis_ids,'WTEColi_113C80_U13C20_01_fittedData.csv');
io02.export_data_stage02_isotopomer_measuredFragments_csv(
    experiment_ids_I=['WTEColi_113C80_U13C20_01'],
    sample_name_abbreviations_I=['OxicWtGlc'],
    filename_O='WTEColi_113C80_U13C20_01_measuredFragments.csv')
io02.export_data_stage02_isotopomer_measuredFluxes_csv(
    experiment_ids_I=['WTEColi_113C80_U13C20_01'],
    model_ids_I=[
        'ecoli_RL2013_02',
        #'ecoli_core_iDM2014_02',
        #'iJS2012',
        #'140407_iDM2014'
        ],
    sample_name_abbreviations_I=['OxicWtGlc'],
    filename_O='WTEColi_113C80_U13C20_01_measuredFluxes.csv')

#simulation_ids_changes = [
#    'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_0',
#    'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_1',
#    'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_3',
#    ]
#io02.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(simulation_ids_changes,'WTEColi_113C80_U13C20_02_fittedNetFluxStatistics.csv',flux_units_I = ['mmol*gDCW-1*hr-1']);
#io02.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(simulation_ids_changes,'WTEColi_113C80_U13C20_02_fittedNetFluxStatistics_coreFluxes.csv',flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized']);

## Look for significant flux differences
#ex02.reset_datastage02_isotopomer_fittedNetFluxDifferences('WTEColi_113C80_U13C20_02_SSR');
#ex02.execute_findNetFluxSignificantDifferences('WTEColi_113C80_U13C20_02_SSR',
#                    control_simulation_id_I='WTEColi_113C80_U13C20_02_ecoli_RL2013_02_ecoli_RL2013_02_OxicWtGlc_3',
#                    control_simulation_dateAndTime_I="2015-09-19 13:32:17");
# Look for significant flux differences
ex02.reset_datastage02_isotopomer_fittedNetFluxDifferences('WTEColi_113C80_U13C20_01_EPIMRM');
ex02.execute_findNetFluxSignificantDifferences('WTEColi_113C80_U13C20_01_EPIMRM');