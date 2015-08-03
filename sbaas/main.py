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
##run(port=8080,public=True);

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


from sbaas.analysis.analysis_stage01_resequencing import *
from sbaas.models import *
session = Session();
ex01 = stage01_resequencing_execute(session);
io01 = stage01_resequencing_io(session);

#PASSED
## reset imported coverage data
#ex01.reset_dataStage01_resequencing_coverage(experiment_id_I='ALEsKOs01',
#    # sample_names_I=['140807_11_OxicEvo04sdhCadhBEvo01EPEcoliGlcM9_Broth-1',
#    #'140807_11_OxicEvo04sdhCadhBEvo02EPEcoliGlcM9_Broth-1',
#    #'140807_11_OxicEvo04sdhCadhBEvo03EPEcoliGlcM9_Broth-1',
#    # '140401_0_OxicEvo04sdhCadhBEcoliGlcM9_Broth-1'
#    #]
#     )
## import the driver file
#from io_utilities.base_importData import base_importData
#iobase = base_importData();
#iobase.read_csv(settings.workspace_data+'/_input/140823_Resequencing_ALEsKOs01_coverage01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#    print('importing coverage data for sample ' + file['sample_name']);
#    io01.import_resequencingCoverageData_add(file['filename'],file['experiment_id'],file['sample_name'],file['strand_start'],file['strand_stop'],file['scale_factor'],file['downsample_factor']);
#iobase.clear_data();

#TEST
# find amplifications
ex01.reset_dataStage01_resequencing_amplifications('ALEsKOs01',
    #sample_names_I = [
    #'140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1'
    #]
    )
ex01.execute_findAmplificationsAndCalculateStats_fromGff(
    #analysis_id_I,
    'ALEsKOs01',
    0, 4640000,
    sample_names_I = [
    '140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1',
    ],
    scale_factor=True, downsample_factor=200,reads_min=1.25,reads_max=4.0, indices_min=5000,consecutive_tol=50
    );
# annotate amplifications
ex01.execute_annotateAmplifications(
        'ALEsKOs01',
    sample_names_I = [
    '140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1',
    ],
    ref_genome_I=settings.sbaas+'/sbaas/data/U00096.2.gb'
        );

## initialize the DB
#ex01.initialize_dataStage01();

#io01.import_dataStage01RNASequencingFpkmTracking_add();
#io01.import_dataStage01RNASequencingGeneExpDiff_add()