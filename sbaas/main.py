# define search paths manually
import sys
from data import sbaas_settings as settings
#sys.path.append('C:\\Users\\dmccloskey-sbrg\\Documents\\GitHub\\sbaas\\sbaas')
sys.path.append(settings.sbaas)
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
#from sbaas.analysis.analysis_stage00 import *
#from sbaas.models import *
#session = Session();
#ex00 = stage00_execute(session);
#ex00.execute_makeExperimentFromSampleFile(settings.workspace_data+'/_input/150608_Quantification_BloodProject01_sampleFile02.csv',
#                                             1,[10.0]);