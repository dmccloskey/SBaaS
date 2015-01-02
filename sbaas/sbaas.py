#Analysis tests:
from tests import analysis_ale, analysis_physiology, analysis_resequencing
analysis_ale.run_all_tests();
analysis_physiology.run_all_tests();
analysis_resequencing.run_all_tests();

#Visualization tests:
from visualization.server import run
run();