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


##Analysis tests:
#from tests import analysis_ale, analysis_physiology, analysis_resequencing
#analysis_ale.run_all_tests();
#analysis_physiology.run_all_tests();
#analysis_resequencing.run_all_tests();

##Visualization tests:
#from visualization.server import run
#run();
#run(port=8080,public=True);

#Debug mode:
#from sbaas.analysis.analysis_stage01_physiology import *
#from sbaas.models import *
#session = Session();
#ex01 = stage01_physiology_execute(session);
#io01 = stage01_physiology_io(session);
#io01.import_dataStage01PhysiologyRatesAverages_add(settings.workspace_data + '/_input/150728_Physiology_ALEWt01_dataStage01PhysiologyRatesAverages02.csv');
#io01.import_dataStage01PhysiologyAnalysis_add(settings.workspace_data + '/_input/150728_Physiology_ALEWt01_dataStage01PhysiologyAnalysis.csv');
## calculate the yield
#ex01.execute_calculateYield('ALEsKOs01',
#    sample_name_short_I=[
#    "OxicEvo04EcoliGlc_Broth-4",
#    "OxicEvo04EcoliGlc_Broth-5",
#    "OxicEvo04EcoliGlc_Broth-6"
#    ]
#    );
#def sample_names_abbreviation_exportRatesAverages_P():
#    return [
#        'OxicEvo04EcoliGlc',
#            'OxicEvo04gndEcoliGlc',
#            'OxicEvo04pgiEcoliGlc',
#            'OxicEvo04ptsHIcrrEcoliGlc',
#            'OxicEvo04sdhCBEcoliGlc',
#            'OxicEvo04tpiAEcoliGlc',
#            'OxicEvo04pgiEvo01EPEcoliGlc',
#            'OxicEvo04pgiEvo02EPEcoliGlc',
#            'OxicEvo04pgiEvo02EPEcoliGlc',
#            'OxicEvo04pgiEvo04EPEcoliGlc',
#            'OxicEvo04pgiEvo05EPEcoliGlc',
#            'OxicEvo04pgiEvo06EPEcoliGlc',
#            'OxicEvo04pgiEvo07EPEcoliGlc',
#            'OxicEvo04pgiEvo08EPEcoliGlc',
#            'OxicEvo04ptsHIcrrEvo01EPEcoliGlc',
#            'OxicEvo04ptsHIcrrEvo02EPEcoliGlc',
#            'OxicEvo04ptsHIcrrEvo02EPEcoliGlc',
#            'OxicEvo04ptsHIcrrEvo04EPEcoliGlc',
#            'OxicEvo04tpiAEvo01EPEcoliGlc',
#            'OxicEvo04tpiAEvo02EPEcoliGlc',
#            'OxicEvo04tpiAEvo02EPEcoliGlc',
#            'OxicEvo04tpiAEvo04EPEcoliGlc',
#            'OxicEvo04gndEvo01EPEcoliGlc',
#            'OxicEvo04gndEvo02EPEcoliGlc',
#            'OxicEvo04gndEvo02EPEcoliGlc',
#            'OxicEvo04sdhCBEvo01EPEcoliGlc',
#            'OxicEvo04sdhCBEvo02EPEcoliGlc',
#            'OxicEvo04sdhCBEvo02EPEcoliGlc',
#            'OxicEvo04Evo01EPEcoliGlc',
#            'OxicEvo04Evo02EPEcoliGlc'
#            ];
## calculate the average yield
#ex01.execute_calculateRatesAverages('ALEsKOs01',
#    sample_name_abbreviations_I=sample_names_abbreviation_exportRatesAverages_P(),
#    met_ids_I=[
#    "yield_ss"
#    ]
#    );


from sbaas.analysis.analysis_stage01_rnasequencing import *
from sbaas.models import *
session = Session();
ex01 = stage01_rnasequencing_execute(session);
io01 = stage01_rnasequencing_io(session);
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

# initialize the DB
ex01.initialize_dataStage01();

# upload the analysis file

# upload the visualization file

# import the driver file
iobase = base_importData();
iobase.read_csv(settings.workspace_data+'/_input/150806_RNASequencing_ALEsKOs01_genesFpkmTracking01.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('importing genes.pfkm_tracking data for sample ' + file['sample_name']);
    io01.import_dataStage01RNASequencingFpkmTracking_add(file['filename'],file['experiment_id'],file['sample_name']);
iobase.clear_data();

# export replicate boxAndWhiskers plot

# make the heatmap

# export the heatmap

# import the driver file
iobase = base_importData();
iobase.read_csv(settings.workspace_data+'/_input/150806_RNASequencing_ALEsKOs01_geneExpDiff01.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('importing gene_exp.diff ' + file['filename']);
    io01.import_dataStage01RNASequencingGeneExpDiff_add(file['filename'],file['experiment_id_1'],file['experiment_id_2'],file['sample_name_abbreviation_1'],file['sample_name_abbreviation_2']);
iobase.clear_data();

# export the volcano plot