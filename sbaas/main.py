# define search paths manually
import sys
from data import sbaas_settings as settings
#sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\sbaas\\sbaas')
sys.path.append(settings.sbaas)
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\sequencing_utilities')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\thermodynamics')
sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\component-contribution')

##Analysis tests:
#from tests import analysis_ale, analysis_physiology, analysis_resequencing
#analysis_ale.run_all_tests();
#analysis_physiology.run_all_tests();
#analysis_resequencing.run_all_tests();

#Visualization tests:
from visualization.server import run
run();
#run(port=8080,public=True);

##Debug mode:
#from sbaas.analysis.analysis_stage01_resequencing import *
#from sbaas.analysis.analysis_base.base_importData import base_importData
#from sbaas.models import *
#session = Session();
#ex01 = stage01_resequencing_execute(session);
#io01 = stage01_resequencing_io(session);

## initialize the DB
#ex01.initialize_dataStage01();

## import the driver file
#iobase = base_importData();
#iobase.read_csv(settings.workspace_data+'/_input/140823_Resequencing_ALEsKOs01_coverage01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#    print('importing coverage data for sample ' + file['sample_name']);
#    io01.import_resequencingCoverageData_add(file['filename'],file['experiment_id'],file['sample_name'],file['strand_start'],file['strand_stop'],file['scale_factor'],file['downsample_factor']);
#iobase.clear_data();

## find amplifications
#ex01.reset_dataStage01_resequencing_amplifications('ALEsKOs01',sample_names_I = ['140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1'])
#ex01.execute_findAmplificationsAndCalculateStats_fromGff(
#        #analysis_id_I,
#        'ALEsKOs01',
#        0, 4640000,
#        sample_names_I = ['140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1'],
#        scale_factor=True, downsample_factor=200,reads_min=1.5,reads_max=5.0, indices_min=10000,consecutive_tol=25
#        );
#ex01.execute_amplificationStats_fromTable(
#        'ALEsKOs01',
#        sample_names_I = ['140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1']
#        );

# visualize the data
#io01.export_dataStage01ResequencingAmplifications_js('evo04ptsHIcrrevo04',data_dir_I="tmp")
#io01.export_dataStage01ResequencingCoverage_js('evo04ptsHIcrrevo04',data_dir_I="tmp")