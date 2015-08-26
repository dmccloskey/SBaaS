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

#Visualization tests:
from visualization.server import run
run();
#run(port=8080,public=True);

##Debug mode:
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