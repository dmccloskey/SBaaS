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

##Debug mode:
from sbaas.analysis.analysis_stage01_isotopomer import *
from sbaas.models import *
session = Session();
io01 = stage01_isotopomer_io(session);
ex01 = stage01_isotopomer_execute(session);
#export spectrums to js
#io01.export_dataStage01IsotopomerNormalized_js('ALEsKOs01',
#    sample_name_abbreviations_I=[
#    #'OxicEvo04tpiAEvo01EPEcoli13CGlc',
#    'OxicEvo04tpiAEvo02EPEcoli13CGlc'
#    ],
#    #met_ids_I=['g6p',
#    #          'glu-L'
#    #],
#    #scan_types_I=['EPI'],
#    single_plot_I = False,
#    );
io01.export_dataStage01IsotopomerAveragesNormSum_js('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc'
    ],
    #met_ids_I=['g6p',
    #          'glu-L'
    #],
    #scan_types_I=['EPI'],
    single_plot_I = False,
    );
#ex01.plot_normalizedSpectrum('ALEsKOs01',
#    sample_name_abbreviations_I=[
#    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
#    'OxicEvo04tpiAEvo02EPEcoli13CGlc'
#    ],
#    #met_ids_I=['g6p',
#    #          'glu-L'
#    #],
#    scan_types_I=['EPI']
#    );

#from sbaas.analysis.analysis_stage01_quantification import *
#from sbaas.models import *
#session=Session();
## initialize the io object
#qio01 = stage01_quantification_io();
## initialize the execution object
#qe01 = stage01_quantification_execute();
## calculate the averages of the data using the formula ave(broth)-ave(filtrate)
#qe01.execute_analyzeAverages('chemoCLim01',
#        #sample_name_abbreviations_I=[
#        #'OxicWtGlcDil0p25',
#        #'OxicWtGlcDil0p32',
#        #'OxicWtGlcDil0p45',
#        #'OxicWtGlcDil0p58'
#        #]
#        );

## add as template for sequencing_analyis and add to tests
#from sbaas.analysis.analysis_stage01_rnasequencing import *
#from sbaas.models import *
#session = Session();
#ex01 = stage01_rnasequencing_execute(session);
#io01 = stage01_rnasequencing_io(session);
#from sbaas.analysis.visualization import *
#visio01 = visualization_io(session);
## Resources
#from io_utilities.base_importData import base_importData
#from io_utilities.base_exportData import base_exportData

## initialize the DB
#ex01.initialize_dataStage01();

## upload the analysis file
#io01.import_dataStage01RNASequencingAnalysis_add(settings.workspace_data+'/_input/150806_RNASequencing_ALEsKOs01_analysis02.csv');
## upload the visualization file
#visio01.import_visualizationProject_add(settings.workspace_data+'/_input/150806_Visualization_ALEsKOs01_project12.csv');

## reset the previous imports
#ex01.reset_dataStage01_rnasequencing_genesFpkmTracking('ALEsKOs01');
## import the driver file
#iobase = base_importData();
#iobase.read_csv(settings.workspace_data+'/_input/150806_RNASequencing_ALEsKOs01_genesFpkmTracking01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#    print('importing genes.pfkm_tracking data for sample ' + file['sample_name']);
#    io01.import_dataStage01RNASequencingGenesFpkmTracking_add(file['filename'],file['experiment_id'],file['sample_name']);
#iobase.clear_data();

## export replicate boxAndWhiskers plot
#analysis_ids = [
#    'ALEsKOs01_0_11_evo04pgi',
#    'ALEsKOs01_0_evo04_0_11_evo04pgi'
#                ];
## make the heatmap
#for analysis in analysis_ids:
#    ex01.execute_heatmap(analysis);
# export the heatmap

## reset the previous imports
#ex01.reset_dataStage01_rnasequencing_geneExpDiff('ALEsKOs01');
## import the driver file
#iobase = base_importData();
#iobase.read_csv(settings.workspace_data+'/_input/150806_RNASequencing_ALEsKOs01_geneExpDiff01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#    print('importing gene_exp.diff ' + file['filename']);
#    io01.import_dataStage01RNASequencingGeneExpDiff_add(file['filename'],file['experiment_id_1'],file['experiment_id_2'],file['sample_name_abbreviation_1'],file['sample_name_abbreviation_2']);
#iobase.clear_data();

# export the volcano plot