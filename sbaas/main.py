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

##Visualization tests:
#from visualization.server import run
#run();
##run(port=8080,public=True);

#Debug mode:
#from sbaas.analysis.analysis_stage01_isotopomer import *
#from sbaas.analysis.analysis_base.base_importData import base_importData
#from sbaas.models import *
#session = Session();
#io01 = stage01_isotopomer_io(session);
#ex01 = stage01_isotopomer_execute(session);
#ex01.execute_buildSpectrumFromPeakData('ALEsKOs01','isotopomer_13C',
#    sample_name_abbreviations_I =[
#    'OxicEvo04pgiEvo06EPEcoli13CGlc',
#    #'OxicEvo04pgiEvo07EPEcoli13CGlc',
#    ],
#    #met_ids_I=['dhap','glyc3p','glyclt']
#    );

from sbaas.analysis.analysis_stage02_isotopomer import *
from sbaas.analysis.visualization import *
from sbaas.models import *
session=Session();
# initialize the execution object
ex02 = stage02_isotopomer_execute(session);
# initialize the io object
io02 = stage02_isotopomer_io(session);
# initialize global variables for import
ko_list = [];
flux_dict = {};
metID2RxnID = {'glc-D':{'model_id':'150526_iDM2015','rxn_id':'EX_glc_LPAREN_e_RPAREN_'},
        'ac':{'model_id':'150526_iDM2015','rxn_id':'EX_ac_LPAREN_e_RPAREN_'},
        'succ':{'model_id':'150526_iDM2015','rxn_id':'EX_succ_LPAREN_e_RPAREN_'},
        'lac-D':{'model_id':'150526_iDM2015','rxn_id':'EX_lac_DASH_D_LPAREN_e_RPAREN_'},
        'biomass':{'model_id':'150526_iDM2015','rxn_id':'Ec_biomass_iJO1366_WT_53p95M'}};
snaIsotopomer2snaPhysiology02 = {
        'OxicEvo04pgiEvo01EPEcoli13CGlc':'OxicEvo04pgiEvo01EPEcoliGlc',
        'OxicEvo04pgiEvo02EPEcoli13CGlc':'OxicEvo04pgiEvo02EPEcoliGlc',
        'OxicEvo04pgiEvo03EPEcoli13CGlc':'OxicEvo04pgiEvo03EPEcoliGlc',
        'OxicEvo04pgiEvo04EPEcoli13CGlc':'OxicEvo04pgiEvo04EPEcoliGlc',
        'OxicEvo04pgiEvo05EPEcoli13CGlc':'OxicEvo04pgiEvo05EPEcoliGlc',
        'OxicEvo04pgiEvo06EPEcoli13CGlc':'OxicEvo04pgiEvo06EPEcoliGlc',
        'OxicEvo04pgiEvo07EPEcoli13CGlc':'OxicEvo04pgiEvo07EPEcoliGlc',
        'OxicEvo04pgiEvo08EPEcoli13CGlc':'OxicEvo04pgiEvo08EPEcoliGlc',
        'OxicEvo04ptsHIcrrEvo01EPEcoli13CGlc':'OxicEvo04ptsHIcrrEvo01EPEcoliGlc',
        'OxicEvo04ptsHIcrrEvo02EPEcoli13CGlc':'OxicEvo04ptsHIcrrEvo02EPEcoliGlc',
        'OxicEvo04ptsHIcrrEvo03EPEcoli13CGlc':'OxicEvo04ptsHIcrrEvo03EPEcoliGlc',
        'OxicEvo04ptsHIcrrEvo04EPEcoli13CGlc':'OxicEvo04ptsHIcrrEvo04EPEcoliGlc',
        'OxicEvo04tpiAEvo01EPEcoli13CGlc':'OxicEvo04tpiAEvo01EPEcoliGlc',
        'OxicEvo04tpiAEvo02EPEcoli13CGlc':'OxicEvo04tpiAEvo02EPEcoliGlc',
        'OxicEvo04tpiAEvo03EPEcoli13CGlc':'OxicEvo04tpiAEvo03EPEcoliGlc',
        'OxicEvo04tpiAEvo04EPEcoli13CGlc':'OxicEvo04tpiAEvo04EPEcoliGlc',
        'OxicEvo04gndEvo01EPEcoli13CGlc':'OxicEvo04gndEvo01EPEcoliGlc',
        'OxicEvo04gndEvo02EPEcoli13CGlc':'OxicEvo04gndEvo02EPEcoliGlc',
        'OxicEvo04gndEvo03EPEcoli13CGlc':'OxicEvo04gndEvo03EPEcoliGlc',
        'OxicEvo04sdhCBEvo01EPEcoli13CGlc':'OxicEvo04sdhCBEvo01EPEcoliGlc',
        'OxicEvo04sdhCBEvo02EPEcoli13CGlc':'OxicEvo04sdhCBEvo02EPEcoliGlc',
        'OxicEvo04sdhCBEvo03EPEcoli13CGlc':'OxicEvo04sdhCBEvo03EPEcoliGlc',
        'OxicEvo04Evo01EPEcoli13CGlc':'OxicEvo04Evo01EPEcoliGlc',
        'OxicEvo04Evo02EPEcoli13CGlc':'OxicEvo04Evo02EPEcoliGlc'
            }
sample_name_abbreviations02 = [
        'OxicEvo04pgiEvo01EPEcoli13CGlc',
        'OxicEvo04pgiEvo02EPEcoli13CGlc',
        'OxicEvo04pgiEvo03EPEcoli13CGlc',
        'OxicEvo04pgiEvo04EPEcoli13CGlc',
        'OxicEvo04pgiEvo05EPEcoli13CGlc',
        'OxicEvo04pgiEvo06EPEcoli13CGlc',
        'OxicEvo04pgiEvo07EPEcoli13CGlc',
        'OxicEvo04pgiEvo08EPEcoli13CGlc',
        'OxicEvo04ptsHIcrrEvo01EPEcoli13CGlc',
        'OxicEvo04ptsHIcrrEvo02EPEcoli13CGlc',
        'OxicEvo04ptsHIcrrEvo03EPEcoli13CGlc',
        'OxicEvo04ptsHIcrrEvo04EPEcoli13CGlc',
        'OxicEvo04tpiAEvo01EPEcoli13CGlc',
        'OxicEvo04tpiAEvo02EPEcoli13CGlc',
        'OxicEvo04tpiAEvo03EPEcoli13CGlc',
        'OxicEvo04tpiAEvo04EPEcoli13CGlc',
        'OxicEvo04gndEvo01EPEcoli13CGlc',
        'OxicEvo04gndEvo02EPEcoli13CGlc',
        'OxicEvo04gndEvo03EPEcoli13CGlc',
        'OxicEvo04sdhCBEvo01EPEcoli13CGlc',
        'OxicEvo04sdhCBEvo02EPEcoli13CGlc',
        'OxicEvo04sdhCBEvo03EPEcoli13CGlc',
        'OxicEvo04Evo01EPEcoli13CGlc',
        'OxicEvo04Evo02EPEcoli13CGlc'
        ]
# import measured fluxes
# completed
#ex02.reset_datastage02_isotopomer_measuredFluxes('ALEsKOs01')
ex02.execute_makeMeasuredFluxes('ALEsKOs01',metID2RxnID_I=metID2RxnID,sample_name_abbreviations_I=sample_name_abbreviations02,snaIsotopomer2snaPhysiology_I=snaIsotopomer2snaPhysiology02)

