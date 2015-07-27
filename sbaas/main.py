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

#Debug mode:
from sbaas.analysis.analysis_stage01_resequencing import *
from sbaas.analysis.analysis_base.base_importData import base_importData
from sbaas.models import *
session = Session();
ex01 = stage01_resequencing_execute(session);
io01 = stage01_resequencing_io(session);

# initialize the DB
ex01.initialize_dataStage01();

io01.import_dataStage01RNASequencingFpkmTracking_add();
io01.import_dataStage01RNASequencingGeneExpDiff_add()

# visualize the data