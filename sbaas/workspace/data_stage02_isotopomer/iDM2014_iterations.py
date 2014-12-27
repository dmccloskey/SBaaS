from analysis.analysis_stage02_isotopomer import iterations
from analysis.analysis_stage02_isotopomer.sampling import find_loops, simulate_loops
from cobra.manipulation.modify import convert_to_irreversible, revert_to_reversible
from cobra.io.sbml import create_cobra_model_from_sbml_file
from cobra.io.sbml import write_cobra_model_to_sbml_file
from analysis.analysis_stage02_isotopomer.isotopomer import *
from analysis.analysis_stage02_isotopomer.reduce_model import *
from workspace.load_model import load_ALEWt

def _main_():
    # workflow to generate the reduced model:
    #iterations.isotopomer_model_iteration1();
    iterations.isotopomer_model_iteration2('data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_reduced_modified_pfba.csv',
                                           "data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_reduced.xml",
                                           'data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_netrxn_irreversible.xml',
                                           'data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_reduced_netrxn_lbub.csv');

    iterations.isotopomer_model_iteration3('data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_netrxn_irreversible.xml',
                                           'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',
                                           'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.mat',
                                           'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.csv',
                                           'data\\iteration3_140601_centralMets\\isotopomer_mapping_140528_centralMets.csv',
                                           [],{},'140601_iDM2014');

    # check for loops
    loops = simulate_loops('data\\iteration2_140601_centralMets\\iteration2_140601_ijo1366_netrxn_irreversible.xml','data\\iteration3_140601_centralMets\\iteration3_iDMisotopomer_loops_fva_centralMets.json');
    foundloops = find_loops('data\\iteration3_140601_centralMets\\iteration3_iDMisotopomer_loops_fva_centralMets.json')
    print len(foundloops);
    print foundloops;