'''isotopomer metabolomics analysis class'''

from analysis.analysis_base import *
from stage02_isotopomer_query import *
from stage02_isotopomer_io import *
# Dependencies
import operator, json, csv
from copy import copy
# Dependencies from 3rd party
import scipy.io
from numpy import histogram, mean, std, loadtxt
import matplotlib as mpl
import matplotlib.pyplot as plt
import h5py
from resources.molmass import Formula
# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file
from cobra.io.sbml import write_cobra_model_to_sbml_file
from cobra.io.mat import save_matlab_model
from cobra.manipulation.modify import convert_to_irreversible, revert_to_reversible
from cobra.flux_analysis.objective import update_objective
from cobra.flux_analysis.variability import flux_variability_analysis
from cobra.flux_analysis.parsimonious import optimize_minimal_flux
from cobra.flux_analysis import flux_variability_analysis, single_deletion
from cobra.core.Reaction import Reaction
from cobra.core.Metabolite import Metabolite

class stage02_isotopomer_dependencies():
    def __init__(self):
        self.calculate = base_calculate();
        #variables:
        self.isotopomer_rxns_net_irreversible = {
                'ptrc_to_4abut_1':{'reactions':['PTRCTA','ABUTD'],
                                   'stoichiometry':[1,1]},
                'ptrc_to_4abut_2':{'reactions':['GGPTRCS','GGPTRCO','GGGABADr','GGGABAH'],
                                   'stoichiometry':[1,1,1,1]},
                'glu_DASH_L_to_acg5p':{'reactions':['ACGS','ACGK'],
                                   'stoichiometry':[1,1]},
                '2obut_and_pyr_to_3mop':{'reactions':['ACHBS','KARA2','DHAD2'],
                                   'stoichiometry':[1,1,1]},
                'pyr_to_23dhmb':{'reactions':['ACLS','KARA1_reverse'],
                                   'stoichiometry':[1,1]},
                #'met_DASH_L_and_ptrc_to_spmd_and_5mta':{'reactions':['METAT','ADMDC','SPMS'],
                #                   'stoichiometry':[1,1,1]}, #cannot be lumped
                'chor_and_prpp_to_3ig3p':{'reactions':['ANS','ANPRT','PRAIi','IGPS'],
                                   'stoichiometry':[1,1,1,1]},
                'hom_DASH_L_and_cyst_DASH_L_to_pyr_hcys_DASH_L':{'reactions':['HSST','SHSL1','CYSTL'],
                                   'stoichiometry':[1,1,1]},
                'e4p_and_pep_to_3dhq':{'reactions':['DDPA','DHQS'],
                                   'stoichiometry':[1,1]},
                'aspsa_to_sl2a6o':{'reactions':['DHDPS','DHDPRy','THDPS'],
                                   'stoichiometry':[1,1,1]},
                'glu_DASH_L_to_glu5sa':{'reactions':['GLU5K','G5SD'],
                                   'stoichiometry':[1,1]},
                'g1p_to_glycogen':{'reactions':['GLGC','GLCS1'],
                                   'stoichiometry':[1,1]},
                'thr_DASH_L_to_gly':{'reactions':['THRD','GLYAT_reverse'],
                                   'stoichiometry':[1,1]}, #need to remove deadend mets: athr-L: ATHRDHr, ATHRDHr_reverse; aact: AACTOOR, AOBUTDs
                'dhap_to_lac_DASH_D':{'reactions':['MGSA','LGTHL','GLYOX'],
                                   'stoichiometry':[1,1,1]},
                'hom_DASH_L_to_thr_DASH_L':{'reactions':['HSK','THRS'],
                                   'stoichiometry':[1,1]},
                '3pg_to_ser_DASH_L':{'reactions':['PGCD','PSERT','PSP_L'],
                                   'stoichiometry':[1,1,1]},
                'prpp_to_his_DASH_L':{'reactions':['ATPPRT','PRATPP','PRAMPC','PRMICI','IG3PS','IGPDH','HSTPT','HISTP','HISTD'],
                                   'stoichiometry':[1,1,1,1,1,1,1,1,1]},
                'UMPSYN_aerobic':{'reactions':['ASPCT','DHORTS_reverse','DHORD2','ORPT_reverse','OMPDC'],
                                   'stoichiometry':[1,1,1,1,1]},
                #'UMPSYN_anaerobic':{'reactions':['ASPCT','DHORTS_reverse','DHORD5','ORPT_reverse','OMPDC'],
                #                   'stoichiometry':[1,1,1,1,1]},
                'IMPSYN_1':{'reactions':['GLUPRT','PRAGSr','PRFGS','PRAIS'],
                                   'stoichiometry':[1,1,1,1]},
                'IMPSYN_2':{'reactions':['AIRC2','AIRC3_reverse','PRASCSi','ADSL2r'],
                                   'stoichiometry':[1,1,1,1]},
                'IMPSYN_3':{'reactions':['AICART','IMPC_reverse'],
                                   'stoichiometry':[1,1]},
                'imp_to_gmp':{'reactions':['IMPD','GMPS2'],
                                   'stoichiometry':[1,1]},
                'imp_to_amp':{'reactions':['ADSS','ADSL1r'],
                                   'stoichiometry':[1,1]},
                #'utp_to_dump_anaerobic':{'reactions':['RNTR4c2','DUTPDP'],
                #                   'stoichiometry':[1,1]},
                'udp_to_dump_aerobic':{'reactions':['RNDR4','NDPK6','DUTPDP'],
                                   'stoichiometry':[1,1,1]},
                #'dtmp_to_dttp':{'reactions':['DTMPK','NDPK4'],
                #                   'stoichiometry':[1,1]}, #cannot be lumped
                'COASYN':{'reactions':['ASP1DC','MOHMT','DPR','PANTS','PNTK','PPNCL2','PPCDC','PTPATi','DPCOAK'],
                                   'stoichiometry':[1,1,1,1,1,1,1,1,1]},
                'FADSYN_1':{'reactions':['GTPCII2','DHPPDA2','APRAUR','PMDPHT','RBFSb'],
                                   'stoichiometry':[1,1,1,1,1]},
                'FADSYN_2':{'reactions':['RBFSa','DB4PS'],
                                   'stoichiometry':[1,1]},
                'FADSYN_3':{'reactions':['RBFK','FMNAT'],
                                   'stoichiometry':[1,1]},
                'NADSYN_aerobic':{'reactions':['ASPO6','QULNS','NNDPR','NNATr','NADS1','NADK'],
                                   'stoichiometry':[1,1,1,1,1,1]},
                #'NADSYN_anaerobic':{'reactions':['ASPO5','QULNS','NNDPR','NNATr','NADS1','NADK'],
                #                   'stoichiometry':[1,1,1,1,1,1]},
                #'NADSALVAGE':{'reactions':['NADPPPS','NADN','NNAM','NAMNPP','NMNN','NMNDA','NMNAT','NADDP','ADPRDP'],
                #                   'stoichiometry':[1,1,1,1,1,1,1,1,1]}, #cannot be lumped
                'THFSYN':{'reactions':['GTPCI','DNTPPA','DNMPPA','DHNPA2r','HPPK2','ADCS','ADCL','DHPS2','DHFS'],
                                   'stoichiometry':[1,1,1,1,1,1,1,1,1]},
                'GTHSYN':{'reactions':['GLUCYS','GTHS'],
                                   'stoichiometry':[1,1]},
                'GLYCPHOSPHOLIPID_1':{'reactions':['DASYN181','AGPAT181','G3PAT181'],'stoichiometry':[1,1,1]},
                'GLYCPHOSPHOLIPID_2':{'reactions':['PSSA181','PSD181'],'stoichiometry':[1,1]},
                'GLYCPHOSPHOLIPID_3':{'reactions':['PGSA160','PGPP160'],'stoichiometry':[1,1]},
                'GLYCPHOSPHOLIPID_4':{'reactions':['DASYN161','AGPAT161','G3PAT161'],'stoichiometry':[1,1,1]},
                'GLYCPHOSPHOLIPID_5':{'reactions':['PGSA181','PGPP181'],'stoichiometry':[1,1]},
                'GLYCPHOSPHOLIPID_6':{'reactions':['PSD161','PSSA161'],'stoichiometry':[1,1]},
                'GLYCPHOSPHOLIPID_7':{'reactions':['PSSA160','PSD160'],'stoichiometry':[1,1]},
                'GLYCPHOSPHOLIPID_8':{'reactions':['DASYN160','AGPAT160','G3PAT160'],'stoichiometry':[1,1,1]},
                'GLYCPHOSPHOLIPID_9':{'reactions':['PGSA161','PGPP161'],'stoichiometry':[1,1]},
                'MOLYBDOPTERIN_1':{'reactions':['MPTAT','MPTS','CPMPS'],'stoichiometry':[1,1,1]},
                'MOLYBDOPTERIN_2':{'reactions':['MOCDS','MOGDS'],'stoichiometry':[1,1]},
                'MOLYBDOPTERIN_3':{'reactions':['MOADSUx','MPTSS'],'stoichiometry':[1,1]},
                'COFACTOR_1':{'reactions':['GLUTRR','G1SAT','GLUTRS'],'stoichiometry':[1,1,1]},
                'COFACTOR_2':{'reactions':['DHNAOT4','UPPDC1','DHNCOAT','DHNCOAS','SEPHCHCS','SUCBZS','SUCBZL','PPPGO3','FCLT','CPPPGO','SHCHCS3'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1]},
                'COFACTOR_3':{'reactions':['TYRL','AMMQLT8','HEMEOS','UPP3MT','SHCHD2','SHCHF','ENTCS','CBLAT'],'stoichiometry':[1,1,1,1,1,1,1,1]},
                'VITB6':{'reactions':['E4PD','PERD','OHPBAT','PDX5PS','PDX5PO2'],'stoichiometry':[1,1,1,1,1]},
                #'THIAMIN':{'reactions':['AMPMS2','PMPK','THZPSN3','TMPPP','TMPK'],'stoichiometry':[1,1,1,1,1]}, # original pathway without correction
                'THIAMIN':{'reactions':['AMPMS3','PMPK','THZPSN3','TMPPP','TMPK'],'stoichiometry':[1,1,1,1,1]},
                'COFACTOR_4':{'reactions':['I4FE4ST','I4FE4SR','I2FE2SS2'],'stoichiometry':[1,1,1]},
                'COFACTOR_5':{'reactions':['BMOGDS1','BMOGDS2','BMOCOS'],'stoichiometry':[1,1,1]},
                'COFACTOR_6':{'reactions':['DMPPS','GRTT','DMATT'],'stoichiometry':[1,1,1]},
                'COFACTOR_7':{'reactions':['MECDPS','DXPRIi','MEPCT','CDPMEK','MECDPDH5'],'stoichiometry':[1,1,1,1,1]},
                'COFACTOR_8':{'reactions':['LIPOS','LIPOCT'],'stoichiometry':[1,1]},
                'COFACTOR_9':{'reactions':['OMMBLHX','OMPHHX','OPHHX','HBZOPT','DMQMT','CHRPL','OMBZLM','OPHBDC','OHPHM'],'stoichiometry':[1,1,1,1,1,1,1,1,1]},
                'COFACTOR_10':{'reactions':['SERASr','DHBD','UPP3S','HMBS','ICHORT','DHBS'],'stoichiometry':[1,1,1,1,1,1]},
                'COFACTOR_11':{'reactions':['PMEACPE','EGMEACPR','DBTS','AOXSr2','I2FE2SR','OPMEACPD','MALCOAMT','AMAOTr','OPMEACPS','OPMEACPR','OGMEACPD','OGMEACPR','OGMEACPS','EPMEACPR','BTS5'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]},
                'CELLENV_1':{'reactions':['UAMAGS','UAPGR','UAGPT3','PAPPT3','GLUR_reverse','UAGCVT','UAMAS','UDCPDP','UGMDDS','UAAGDS'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1]},
                'CELLENV_2':{'reactions':['3HAD181','3OAR181','3OAS181','EAR181x'],'stoichiometry':[1,1,1,1]},
                'CELLENV_3':{'reactions':['3HAD160','3OAR160','EAR160x','3OAS160'],'stoichiometry':[1,1,1,1]},
                'CELLENV_4':{'reactions':['EAR120x','3OAR120','3HAD120','3OAS120','EAR100x'],'stoichiometry':[1,1,1,1,1]},
                'CELLENV_5':{'reactions':['G1PACT','UAGDP','PGAMT_reverse','GF6PTA'],'stoichiometry':[1,1,1,1]},
                'CELLENV_6':{'reactions':['3OAR40','EAR40x','3OAS60','3OAR60','3HAD80','3OAS80','3OAR80','EAR60x','3HAD60','EAR80x','3HAD40'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1]},
                'CELLENV_7':{'reactions':['3HAD161','EAR161x','3OAS161','3OAR161','3OAS141','3HAD141','3OAR121','EAR121x','3HAD121','EAR141x','T2DECAI','3OAR141','3OAS121'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1,1,1]},
                'CELLENV_8':{'reactions':['TDPGDH','TDPDRR','TDPDRE','G1PTT'],'stoichiometry':[1,1,1,1]},
                'CELLENV_9':{'reactions':['3OAS140','3OAR140'],'stoichiometry':[1,1]},
                'CELLENV_10':{'reactions':['3HAD140','EAR140x'],'stoichiometry':[1,1]},
                'CELLENV_11':{'reactions':['3OAR100','3HAD100','3OAS100'],'stoichiometry':[1,1,1]},
                'LIPOPOLYSACCHARIDE_1':{'reactions':['COLIPAabcpp','COLIPAabctex','EDTXS1','EDTXS2','GALT1','GLCTR1','GLCTR2','GLCTR3','HEPK1','HEPK2','HEPT1','HEPT2','HEPT3','HEPT4','LPADSS','MOAT','MOAT2','MOAT3C','RHAT1','TDSK','USHD'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]},
                'LIPOPOLYSACCHARIDE_2':{'reactions':['AGMHE','GMHEPAT','GMHEPK','GMHEPPA','S7PI'],'stoichiometry':[1,1,1,1,1]},
                'LIPOPOLYSACCHARIDE_3':{'reactions':['U23GAAT','UHGADA','UAGAAT'],'stoichiometry':[1,1,1]},
                'LIPOPOLYSACCHARIDE_4':{'reactions':['KDOPP','KDOCT2','KDOPS'],'stoichiometry':[1,1,1]},
                'ASTPathway':{'reactions':['AST','SADH','SGDS','SGSAD','SOTA'],'stoichiometry':[1,1,1,1,1]}
                };
    #model reduction functions
    def load_ALEWt(self,anoxic = False):
        '''load iJO1366 with the following changes:
	    1. update to AMPMS2 to account for carbon monoxide
	    2. changes to uptake bounds for glucose M9 media
	    3. constrain the model to use 'PFK' instead of 'F6PA', 'DHAPT' when grown on glucose
	    4. constrain the model to use the physiologically perferred glutamate synthesis enzymes
	    5. depending on oxygen availability, constrain the model to use the correct RNR enzymes
	    6. depending on oxygen availability, constrain the model to use the correct Dihydroorotate dehydrogenase (PyrD) enzymes
	    7. constrain fatty acid biosynthesis to use the physiologically preferred enzymes'''
        ijo1366_sbml = "data\\iJO1366.xml"
        # Read in the sbml file and define the model conditions
        cobra_model = create_cobra_model_from_sbml_file(ijo1366_sbml, print_time=True)
        # Update AMPMS2
        coc = Metabolite('co_c','CO','carbon monoxide','c');
        cop = Metabolite('co_p','CO','carbon monoxide','p');
        coe = Metabolite('co_e','CO','carbon monoxide','e');
        cobra_model.add_metabolites([coc,cop,coe])
        ampms2_mets = {};
        ampms2_mets[cobra_model.metabolites.get_by_id('air_c')] = -1;
        ampms2_mets[cobra_model.metabolites.get_by_id('amet_c')] = -1;
        ampms2_mets[cobra_model.metabolites.get_by_id('dad_DASH_5_c')] = 1;
        ampms2_mets[cobra_model.metabolites.get_by_id('met_DASH_L_c')] = 1;
        ampms2_mets[cobra_model.metabolites.get_by_id('4ampm_c')] = 1;
        ampms2_mets[cobra_model.metabolites.get_by_id('h_c')] = 3;
        ampms2_mets[cobra_model.metabolites.get_by_id('for_c')] = 1;
        ampms2_mets[cobra_model.metabolites.get_by_id('co_c')] = 1;
        ampms2 = Reaction('AMPMS3');
        ampms2.add_metabolites(ampms2_mets);
        copp_mets = {};
        copp_mets[cobra_model.metabolites.get_by_id('co_c')] = -1;
        copp_mets[cobra_model.metabolites.get_by_id('co_p')] = 1;
        copp = Reaction('COtpp');
        copp.add_metabolites(copp_mets);
        coex_mets = {};
        coex_mets[cobra_model.metabolites.get_by_id('co_p')] = -1;
        coex_mets[cobra_model.metabolites.get_by_id('co_e')] = 1;
        coex = Reaction('COtex');
        coex.add_metabolites(coex_mets);
        cotrans_mets = {};
        cotrans_mets[cobra_model.metabolites.get_by_id('co_e')] = -1;
        cotrans = Reaction('EX_co_LPAREN_e_RPAREN_');
        cotrans.add_metabolites(cotrans_mets);
        cobra_model.add_reactions([ampms2,copp,coex,cotrans]);
        cobra_model.remove_reactions(['AMPMS2']);
        # Define the model conditions:
        system_boundaries = [x.id for x in cobra_model.reactions if x.boundary == 'system_boundary'];
        for b in system_boundaries:
                cobra_model.reactions.get_by_id(b).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(b).upper_bound = 0.0;
        # Reset demand reactions
        demand = ['DM_4CRSOL',
                'DM_5DRIB',
                'DM_AACALD',
                'DM_AMOB',
                'DM_MTHTHF',
                'DM_OXAM'];
        for d in demand:
                cobra_model.reactions.get_by_id(d).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(d).upper_bound = 1000.0;
        # Change the objective
        update_objective(cobra_model,{'Ec_biomass_iJO1366_WT_53p95M':1.0})
        # Assign KOs

        # Specify media composition (M9 glucose):
        cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_').lower_bound = -10.0;
        cobra_model.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN_').lower_bound = -18.0;
        #uptake = ['EX_cl_LPAREN_e_RPAREN_',
        #            'EX_so4_LPAREN_e_RPAREN_',
        #            'EX_ca2_LPAREN_e_RPAREN_',
        #            'EX_pi_LPAREN_e_RPAREN_',
        #            'EX_fe2_LPAREN_e_RPAREN_',
        #            'EX_cu2_LPAREN_e_RPAREN_',
        #            'EX_zn2_LPAREN_e_RPAREN_',
        #            'EX_cbl1_LPAREN_e_RPAREN_',
        #            'EX_mobd_LPAREN_e_RPAREN_',
        #            'EX_ni2_LPAREN_e_RPAREN_',
        #            'EX_mn2_LPAREN_e_RPAREN_',
        #            'EX_k_LPAREN_e_RPAREN_',
        #            'EX_nh4_LPAREN_e_RPAREN_',
        #            'EX_cobalt2_LPAREN_e_RPAREN_',
        #            'EX_mg2_LPAREN_e_RPAREN_'];
        uptake = ['EX_ca2_LPAREN_e_RPAREN_',
                    'EX_cbl1_LPAREN_e_RPAREN_',
                    'EX_cl_LPAREN_e_RPAREN_',
                    'EX_co2_LPAREN_e_RPAREN_',
                    'EX_cobalt2_LPAREN_e_RPAREN_',
                    'EX_cu2_LPAREN_e_RPAREN_',
                    'EX_fe2_LPAREN_e_RPAREN_',
                    'EX_fe3_LPAREN_e_RPAREN_',
                    'EX_h_LPAREN_e_RPAREN_',
                    'EX_h2o_LPAREN_e_RPAREN_',
                    'EX_k_LPAREN_e_RPAREN_',
                    'EX_mg2_LPAREN_e_RPAREN_',
                    'EX_mn2_LPAREN_e_RPAREN_',
                    'EX_mobd_LPAREN_e_RPAREN_',
                    'EX_na1_LPAREN_e_RPAREN_',
                    'EX_nh4_LPAREN_e_RPAREN_',
                    'EX_ni2_LPAREN_e_RPAREN_',
                    'EX_pi_LPAREN_e_RPAREN_',
                    'EX_sel_LPAREN_e_RPAREN_',
                    'EX_slnt_LPAREN_e_RPAREN_',
                    'EX_so4_LPAREN_e_RPAREN_',
                    'EX_tungs_LPAREN_e_RPAREN_',
                    'EX_zn2_LPAREN_e_RPAREN_'];
        for u in uptake:
            cobra_model.reactions.get_by_id(u).lower_bound = -1000.0;
        # Specify allowed secretion products
        secrete = ['EX_meoh_LPAREN_e_RPAREN_',
                    'EX_5mtr_LPAREN_e_RPAREN_',
                    'EX_h_LPAREN_e_RPAREN_',
                    'EX_co2_LPAREN_e_RPAREN_',
                    'EX_co_LPAREN_e_RPAREN_',
                    'EX_h2o_LPAREN_e_RPAREN_',
                    'EX_ac_LPAREN_e_RPAREN_',
                    'EX_fum_LPAREN_e_RPAREN_',
                    'EX_for_LPAREN_e_RPAREN_',
                    'EX_etoh_LPAREN_e_RPAREN_',
                    'EX_lac_DASH_L_LPAREN_e_RPAREN_',
                    'EX_pyr_LPAREN_e_RPAREN_',
                    'EX_succ_LPAREN_e_RPAREN_'];
        for s in secrete:
            cobra_model.reactions.get_by_id(s).upper_bound = 1000.0;
        # Constrain specific reactions
        noFlux = ['F6PA', 'DHAPT'];
        ammoniaExcess = ['GLUDy']; # PMCID: 196288
        # RNR control (DOI:10.1111/j.1365-2958.2006.05493.x)
        # Dihydroorotate dehydrogenase (PyrD) (DOI:10.1016/S0076-6879(78)51010-0, PMID: 199252, DOI:S0969212602008316 [pii])
        aerobic = ['RNDR1', 'RNDR2', 'RNDR3', 'RNDR4', 'DHORD2', 'ASPO6','LCARR','PFL','FRD2','FRD3']; # see DOI:10.1111/j.1365-2958.2011.07593.x; see DOI:10.1089/ars.2006.8.773 for a review
        anaerobic = ['RNTR1c2', 'RNTR2c2', 'RNTR3c2', 'RNTR4c2', 'DHORD5', 'ASPO5','PDH','SUCDi']; # see DOI:10.1074/jbc.274.44.31291, DOI:10.1128/JB.00440-07
        if anaerobic:
            rxnList = noFlux + ammoniaExcess + anaerobic;
            for rxn in rxnList:
                cobra_model.reactions.get_by_id(rxn).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(rxn).upper_bound = 0.0;
        else:
            rxnList = noFlux + ammoniaExcess + aerobic;
            for rxn in rxnList:
                cobra_model.reactions.get_by_id(rxn).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(rxn).upper_bound = 0.0;
        # Set the direction for specific reactions
        # Fatty acid biosynthesis: DOI: 10.1016/j.ymben.2010.10.007, PMCID: 372925
        fattyAcidSynthesis = ['ACCOAC', 'ACOATA', 'HACD1', 'HACD2', 'HACD3', 'HACD4', 'HACD5', 'HACD6', 'HACD7', 'HACD8', 'KAS14', 'KAS15', 'MACPD', 'MCOATA', '3OAR100', '3OAR120', '3OAR121', '3OAR140', '3OAR141', '3OAR160', '3OAR161', '3OAR180', '3OAR181', '3OAR40', '3OAR60', '3OAR80']
        fattyAcidOxidation = ['ACACT1r', 'ACACT2r', 'ACACT3r', 'ACACT4r', 'ACACT5r', 'ACACT6r', 'ACACT7r', 'ACACT8r', 'ACOAD1f', 'ACOAD2f', 'ACOAD3f', 'ACOAD4f', 'ACOAD5f', 'ACOAD6f', 'ACOAD7f', 'ACOAD8f', 'CTECOAI6', 'CTECOAI7', 'CTECOAI8', 'ECOAH1', 'ECOAH2', 'ECOAH3', 'ECOAH4', 'ECOAH5', 'ECOAH6', 'ECOAH7', 'ECOAH8']
        ndpk = ['NDPK1','NDPK2','NDPK3','NDPK4','NDPK5','NDPK7','NDPK8'];
        rxnList = fattyAcidSynthesis + fattyAcidOxidation;
        for rxn in rxnList:
            cobra_model.reactions.get_by_id(rxn).lower_bound = 0.0;
            cobra_model.reactions.get_by_id(rxn).upper_bound = 1000.0;

        return cobra_model;
    def reduce_model(self,cobra_model,cobra_model_outFileName=None):
        '''reduce model'''
        # Input: cobra_model
        # Output: cobra_model 
        #         the lower and upper bounds have been set to 0.0
        #         for all reactions that cannot carry a flux
        cobra_model.optimize()
        sol_f = cobra_model.solution.f

        fva_data = flux_variability_analysis(cobra_model, fraction_of_optimum=0.9,
                                              objective_sense='maximize', the_reactions=None,
                                              allow_loops=True, solver='gurobi',
                                              the_problem='return', tolerance_optimality=1e-6,
                                              tolerance_feasibility=1e-6, tolerance_barrier=1e-8,
                                              lp_method=1, lp_parallel=0, new_objective=None,
                                              relax_b=None, error_reporting=None,
                                              number_of_processes=1, copy_model=False);
        #with open("data\\ijo1366_irrev_fva.json", 'w') as outfile:
        #    json.dump(data, outfile, indent=4);

        #fva_data = json.load(open("data\\ijo1366_irrev_fva.json"));

        # Reduce model
        rxns_noflux = [];
        for k,v in fva_data.iteritems():
            if v['minimum'] == 0.0 and v['maximum'] == 0.0:
                cobra_model.reactions.get_by_id(k).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(k).upper_bound = 0.0;
                rxns_noflux.append(k);

        if cobra_model_outFileName:
            write_cobra_model_to_sbml_file(cobra_model,cobra_model_outFileName)

        cobra_model.optimize()
        sol_reduced_f = cobra_model.solution.f

        # Check that the reduced model is consistent with the original model
        if not sol_f == sol_reduced_f:
            print 'reduced model is inconsistent with the original model'
            print 'original model solution: ' + str(sol_f)
            print 'reduced model solution: ' + str(sol_reduced_f)
    def reduce_model_pfba(self,cobra_model,cobra_model_outFileName=None,fba_outFileName=None,subs=[]):
        '''reduce model using pfba'''
        # Input: cobra_model
        #        cobra_model_outFileName
        #        subs = string of specific subsystems to reduce
        # Output: cobra_model 
        #         the lower and upper bounds have been set to 0.0
        #         for all reactions that cannot carry a flux
        cobra_model.optimize()
        sol_f = cobra_model.solution.f

        # Find minimal flux solution:
        pfba = optimize_minimal_flux(cobra_model,True,solver='gurobi');

        # Reduce model
        rxns_noflux = [];
        # set lb and ub for all reactions with 0 flux to 0;
        for k,v in cobra_model.solution.x_dict.iteritems():
            if (v < 0.0 or v == 0.0) and cobra_model.reactions.get_by_id(k).subsystem in subs:
                cobra_model.reactions.get_by_id(k).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(k).upper_bound = 0.0;
                rxns_noflux.append(k);

        if cobra_model_outFileName:
            write_cobra_model_to_sbml_file(cobra_model,cobra_model_outFileName)

        if pfba_outFileName:
            # Write pfba solution to file
            with open(pfba_outFileName,mode='wb') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['Reaction','Flux'])
                for k,v in cobra_model.solution.x_dict.iteritems():
                    writer.writerow([k,v]);

        cobra_model.optimize()
        sol_reduced_f = cobra_model.solution.f

        # Check that the reduced model is consistent with the original model
        if not sol_f == sol_reduced_f:
            print 'reduced model is inconsistent with the original model'
            print 'original model solution: ' + str(sol_f)
            print 'reduced model solution: ' + str(sol_reduced_f)
    def add_net_reaction(self,cobra_model_IO, rxn_dict_I,remove_reverse=False):
        '''add a net reaction to the model after removing
        the individual reactions'''
        # input: rxn_dict_I = dictionary of net reaction ids and
        #                       corresponding list of individual reaction ids
        # output: cobra_model_IO = individual reactions replaced with a
        #                           net reaction

        cobra_model_IO.optimize();
        sol_orig = cobra_model_IO.solution.f;
        print "original model solution", sol_orig

        try:
            cobra_model_tmp = cobra_model_IO.copy2();
        except KeyError as e:
            print e; 

        # make net reactions:
        rxn_dict_net = {};
        for k,v in rxn_dict_I.iteritems():
            rxn_net = make_net_reaction(cobra_model_tmp, k, v['reactions'],v['stoichiometry']);
            if rxn_net:
                rxn_net.lower_bound = 0.0;
                rxn_net.upper_bound = 1000.0;
                rxn_net.objective_coefficient = 0.0;
            else:
                print 'an error occured in add_net_reaction'
                exit(-1)

            #rxn_net.reversibility = False;
            rxn_dict_net[k] = (v['reactions'],rxn_net);

        # add replace individual reactions with net reaction
        for k,v in rxn_dict_net.iteritems():
            cobra_model_IO.remove_reactions(v[0]);
            # remove the reverse reaction if it exists for irreversible models
            if remove_reverse:
                for rxn in v[0]:
                    if '_reverse' in rxn:
                        rxn_rev = rxn.replace('_reverse','')
                        if cobra_model_IO.reactions.has_id(rxn_rev): cobra_model_IO.remove_reactions(rxn_rev);
                    else:
                        rxn_rev = rxn+'_reverse';
                        if cobra_model_IO.reactions.has_id(rxn_rev): cobra_model_IO.remove_reactions(rxn_rev);
            cobra_model_IO.add_reaction(v[1]);
            cobra_model_IO.optimize();
            sol_new = cobra_model_IO.solution.f;
            print k, sol_new
    def make_net_reaction(self,cobra_model_I, rxn_id_I, rxn_list_I,stoich_list_I):
        '''generate a net reaction from a list of individual reactions'''
        # input: rxn_list_I = list of reaction IDs
        # output: rxn_net_O = net reaction (cobra Reaction object)
        from cobra.core.Reaction import Reaction

        #rxn_net_O = cobra_model_I.reactions.get_by_id(rxn_list_I[0]);
        #for r in rxn_list_I[1:]:
        #    if cobra_model_I.reactions.get_by_id(r).reversibility:
        #        print r + " is reversible!";
        #        print "continue?"
        #    rxn_net_O += cobra_model_I.reactions.get_by_id(r);

        # check input:
        if not len(stoich_list_I) == len(rxn_list_I):
            print "error in " + rxn_id_I + ": there are " + str(len(rxn_list_I)) + " rxn ids and " + str(len(stoich_list_I)) + " coefficients";
            exit(-1);

        rxn_net_O = Reaction(rxn_id_I);
        for i,r in enumerate(rxn_list_I):
            mets = {};
            metlist = [];
            metlist = cobra_model_I.reactions.get_by_id(r).products + cobra_model_I.reactions.get_by_id(r).reactants;
            for met in metlist:
                mets[met] = cobra_model_I.reactions.get_by_id(r).get_coefficient(met)*stoich_list_I[i];
            rxn_net_O.add_metabolites(mets);
            rxn_net_O.subsystem = cobra_model_I.reactions.get_by_id(r).subsystem; #copy over the subsystem
    
        # check net reaction
        #if not rxn_net_O.check_mass_balance():  
            #print "error: " + rxn_id_I + " is not elementally balanced";

        #print rxn_net_O.id;
        #print rxn_net_O.build_reaction_string();
        return rxn_net_O;
    def get_solBySub(self,cobra_model_I,sol_I,sub_I):

        sol_O = {};
        for k,v in sol_I.iteritems():
            try:
                if cobra_model_I.reactions.get_by_id(k).subsystem == sub_I:
                    sol_O[k] = v;
            except:
                print k + ' reaction not found'

        return sol_O;
    def groupBySameFlux(self,cobra_model_I,sol_I):

        flux_list = [];
        for r,f in sol_I.iteritems():
            if not f in flux_list and float(f)>0.0:
                flux_list.append(f)
            
        sameFlux_O = {};
        for f in flux_list:
            rxn_list = [];
            for r,v in sol_I.iteritems():
                if v==f:
                    rxn_list.append(r);
            stoich = [1]*len(rxn_list)
            rxnName = '';
            for rxn in rxn_list:
                rxnName = rxnName + rxn + '_';
            rxnName = rxnName[:-1];
            # check that the reaction name is less than 225 characters
            if len(rxnName)>224:
                rxnName = rxnName[:224];
            sameFlux_O[rxnName] = {'reactions':rxn_list,
                               'stoichiometry':stoich,
                                'flux':f};
            #netRxn = make_net_reaction(cobra_model_copy,rxnName,rxn_list,stoich)
            #sameFlux_O[rxnName] = {'reactions':rxn_list,
            #                   'stoichiometry':stoich,
            #                    'flux':f,
            #                    'net':netRxn};

        return sameFlux_O
    def add_net_reaction_subsystem(self,cobra_model_IO,sol_I,subs_I):
        '''make net reactions for specific subsystems grouped 
        by reactions that have the same flux from pfba'''
        #input: cobra_model
        #       sol_I = pfba solution
        #       sub_I = list of model subsystems
        #output: cobra_model
    
        # convert model to irreversible
        # convert_to_irreversible(cobra_model_IO);
        # Make net reactions for pathways outside of the scope
        # of the isotopomer model
        for s in subs_I:
            sol = get_solBySub(cobra_model_IO,sol_I,s)
            sameFlux = groupBySameFlux(cobra_model_IO,sol)
            netRxns = {};
            for k,v in sameFlux.iteritems():
                if len(v['reactions'])>1: 
                    netRxns[k] = v;
            add_net_reaction(cobra_model_IO,netRxns);
            # add subsystem information back in
            for k in sameFlux.iterkeys():
                cobra_model_IO.reactions.get_by_id(k).subsystem = s
            remove_noflux_reactions(cobra_model_IO,sol_I,subs_I)
        # convert model back to reversible
        # revert_to_reversible(cobra_model_IO);
    def remove_noflux_reactions(self,cobra_model,sol=None,subs=[]):
        '''remove noflux reactions'''
        # Input: cobra_model
        #        sol = pfba solution
        #        subs = string of specific subsystems to reduce
        # Output: cobra_model 
        #         if the lower and upper bounds are zero, the reactions
        #         are removed
        cobra_model.optimize()
        sol_f = cobra_model.solution.f
    
        # Reduce model
        rxns_noflux = [];
        # set lb and ub for all reactions with 0 flux to 0;
        if sol:
            if subs:
                for k,v in sol.iteritems():
                    try:
                        if (float(v) < 0.0 or float(v) == 0.0) and cobra_model.reactions.get_by_id(k).subsystem in subs:
                            cobra_model.reactions.get_by_id(k).lower_bound = 0.0;
                            cobra_model.reactions.get_by_id(k).upper_bound = 0.0;
                            cobra_model.remove_reactions(k)
                            rxns_noflux.append(k);
                    except:
                        print 'reaction is not in model: ' + k
            else:
                for k,v in sol.iteritems():
                    try:
                        if (float(v) < 0.0 or float(v) == 0.0):
                            cobra_model.reactions.get_by_id(k).lower_bound = 0.0;
                            cobra_model.reactions.get_by_id(k).upper_bound = 0.0;
                            cobra_model.remove_reactions(k)
                            rxns_noflux.append(k);
                    except:
                        print 'reaction is not in model: ' + k
        else:
            if subs:
                for r in cobra_model.reactions:
                    if r.lower_bound == 0.0 and r.upper_bound == 0.0 and cobra_model.reactions.get_by_id(r.id).subsystem in subs:
                        cobra_model.remove_reactions(r.id)
            else:
                for r in cobra_model.reactions:
                    if r.lower_bound == 0.0 and r.upper_bound == 0.0:
                        cobra_model.remove_reactions(r.id)
                
        cobra_model.optimize()
        sol_reduced_f = cobra_model.solution.f

        # Check that the reduced model is consistent with the original model
        if not sol_f == sol_reduced_f:
            print 'reduced model is inconsistent with the original model'
            print 'original model solution: ' + str(sol_f)
            print 'reduced model solution: ' + str(sol_reduced_f)
    def get_reactionsInfo(self,cobra_model):
        '''return the number of reactions and the number of reactions 
        that cannot carry a flux (i.e. lb and ub of 0.0)'''
        nrxn_O = len(cobra_model.reactions);
        nrxn_noflux_O = 0;
        for r in cobra_model.reactions:
            if r.lower_bound == 0.0 and r.upper_bound == 0.0:
                nrxn_noflux_O += 1;
        return nrxn_O, nrxn_noflux_O
    #model reduction iteration functions
    def makeIsotopomerModel_iteration01(self,pfba_file,netrxn_irreversible_model_filename,fva_reduced_model_filename,reduced_lbub_filename):
        '''iteration 1:
        identification of reactions that can be lumped in pathways outside the model scope'''
        cobra_model = self.load_ALEWt();
        # Make the model irreversible for downstream manipulations:
        convert_to_irreversible(cobra_model);
        # Add lumped isotopomer reactions
        self.add_net_reaction(cobra_model,isotopomer_rxns_net_irreversible);
        # Find minimal flux solution:
        pfba = optimize_minimal_flux(cobra_model,True,solver='gurobi');
        # Write pfba solution to file
        with open(pfba_file,mode='wb') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Reaction','Flux'])
            for k,v in cobra_model.solution.x_dict.iteritems():
                writer.writerow([k,v]);
        # Read in pfba solution 
        pfba_sol = {};
        with open(pfba_file,mode='r') as infile:
            dictreader = csv.DictReader(infile)
            for r in dictreader:
                pfba_sol[r['Reaction']] = r['Flux'];
        # Make net reactions for pathways outside of the scope
        # of the isotopomer model
        subs = ['Cell Envelope Biosynthesis',
	        'Glycerophospholipid Metabolism',
	        'Lipopolysaccharide Biosynthesis / Recycling',
	        'Membrane Lipid Metabolism',
	        'Murein Biosynthesis'
            'Murein Recycling',
            'Cofactor and Prosthetic Group Biosynthesis',
            #'Transport, Inner Membrane',
            #'Transport, Outer Membrane',
            #'Transport, Outer Membrane Porin',
            'tRNA Charging',
            'Unassigned',
            'Exchange',
            'Inorganic Ion Transport and Metabolism',
            'Nitrogen Metabolism'];
        self.add_net_reaction_subsystem(cobra_model,pfba_sol,subs);
        self.remove_noflux_reactions(cobra_model,pfba_sol,['Transport, Outer Membrane Porin','Transport, Inner Membrane','Transport, Outer Membrane'])
        revert_to_reversible(cobra_model);
        # write model to sbml
        write_cobra_model_to_sbml_file(cobra_model,netrxn_irreversible_model_filename)
        # Reduce model using FVA:
        self.reduce_model(cobra_model,fva_reduced_model_filename)
        # Remove all reactions with 0 flux
        self.remove_noflux_reactions(cobra_model);
        with open(reduced_lbub_filename,mode='wb') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Reaction','Formula','LB','UB','Subsystem'])
            for r in cobra_model.reactions:
                writer.writerow([r.id,
                                 r.build_reaction_string(),
                                r.lower_bound,
                                r.upper_bound,
                                r.subsystem]);
    def makeIsotopomerModel_iteration02(self,pfba_filename,fva_reduced_model_filename,netrxn_irreversible_model_filename,reduced_lbub_filename):
        '''iteration 2:
        addition of finalized lumped reactions that are in pathways that are within the scope of the model
        and reduction by removing reactions with zero optimal minimal flux outside the scope of the model'''
        cobra_model = load_ALEWt();
        # Make the model irreversible for downstream manipulations:
        convert_to_irreversible(cobra_model);
        cobra_model.optimize();
        # Add lumped isotopomer reactions
        self.add_net_reaction(cobra_model,isotopomer_rxns_net_irreversible,True);
        cobra_model.optimize();
        # Find minimal flux solution:
        pfba = optimize_minimal_flux(cobra_model,True,solver='gurobi');
        # Write pfba solution to file
        with open(pfba_filename,mode='wb') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Reaction','Flux','Subsystem'])
            for k,v in cobra_model.solution.x_dict.iteritems():
                writer.writerow([k,v,cobra_model.reactions.get_by_id(k).subsystem]);
        # Read in pfba solution 
        pfba_sol = {};
        with open(pfba_filename,mode='r') as infile:
            dictreader = csv.DictReader(infile)
            for r in dictreader:
                pfba_sol[r['Reaction']] = r['Flux'];
        # remove noflux reactions for pathways outside of the scope
        # of the isotopomer model
        subs = ['Cell Envelope Biosynthesis',
	        'Glycerophospholipid Metabolism',
	        'Lipopolysaccharide Biosynthesis / Recycling',
	        'Membrane Lipid Metabolism',
	        'Murein Biosynthesis'
            'Murein Recycling',
            'Cofactor and Prosthetic Group Biosynthesis',
            'Transport, Inner Membrane',
            'Transport, Outer Membrane',
            'Transport, Outer Membrane Porin',
            'tRNA Charging',
            'Unassigned',
            #'Exchange',
            'Inorganic Ion Transport and Metabolism',
            'Nitrogen Metabolism',
            'Alternate Carbon Metabolism'];
        self.remove_noflux_reactions(cobra_model,pfba_sol,subs)
        # Reduce model using FVA:
        self.reduce_model(cobra_model,fva_reduced_model_filename)
        # Reset secretion products that may have been turned off
        secrete = ['EX_meoh_LPAREN_e_RPAREN_',
                    'EX_5mtr_LPAREN_e_RPAREN_',
                    'EX_h_LPAREN_e_RPAREN_',
                    'EX_co2_LPAREN_e_RPAREN_',
                    'EX_co_LPAREN_e_RPAREN_',
                    'EX_h2o_LPAREN_e_RPAREN_',
                    'EX_ac_LPAREN_e_RPAREN_',
                    'EX_fum_LPAREN_e_RPAREN_',
                    'EX_for_LPAREN_e_RPAREN_',
                    'EX_etoh_LPAREN_e_RPAREN_',
                    'EX_lac_DASH_L_LPAREN_e_RPAREN_',
                    'EX_pyr_LPAREN_e_RPAREN_',
                    'EX_succ_LPAREN_e_RPAREN_'];
        for s in secrete:
            cobra_model.reactions.get_by_id(s).upper_bound = 1000.0;
        # Remove all reactions with 0 flux
        r1,r2 = self.get_reactionsInfo(cobra_model);
        while r2 !=0:
            self.remove_noflux_reactions(cobra_model);
            r1,r2 = self.get_reactionsInfo(cobra_model);
            print r1,r2;
        # write model to sbml
        write_cobra_model_to_sbml_file(cobra_model,netrxn_irreversible_model_filename)
        with open(reduced_lbub_filename,mode='wb') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Reaction','Formula','LB','UB','Subsystem'])
            for r in cobra_model.reactions:
                writer.writerow([r.id,
                                 r.build_reaction_string(),
                                r.lower_bound,
                                r.upper_bound,
                                r.subsystem]);
    def makeIsotopomerModel_cobraMAT(self,model_filename,xml_filename,mat_filename,csv_filename,isotopomer_mapping_filename,ko_list=[],flux_dict={},description=None):
        '''iteration 3:
        Remove reactions that are thermodynamically unfavorable and add isotopomer data'''
        # Read in the sbml file and define the model conditions
        cobra_model = create_cobra_model_from_sbml_file(model_filename, print_time=True)
        # Modify glucose uptake:
        if cobra_model.reactions.has_id('EX_glc_LPAREN_e_RPAREN__reverse'):
            lb,ub = cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN__reverse').lower_bound,cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN__reverse').upper_bound;
            EX_glc_mets = {};
            EX_glc_mets[cobra_model.metabolites.get_by_id('glc_DASH_D_e')] = -1;
            EX_glc = Reaction('EX_glc_LPAREN_e_RPAREN_');
            EX_glc.add_metabolites(EX_glc_mets);
            cobra_model.add_reaction(EX_glc)
            cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_').lower_bound = -ub;
            cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_').upper_bound = lb;
            cobra_model.remove_reactions(['EX_glc_LPAREN_e_RPAREN__reverse'])
        ## Remove thermodynamically infeasible reactions:
        #infeasible = [];
        #loops = [];
        #cobra_model.remove_reactions(infeasible + loops);
        # Apply KOs, if any:
        for ko in ko_list:
            cobra_model.reactions.get_by_id(ko).lower_bound = 0.0;
            cobra_model.reactions.get_by_id(ko).upper_bound = 0.0;
        # Apply flux constraints, if any:
        for rxn,flux in flux_dict.iteritems():
            cobra_model.reactions.get_by_id(rxn).lower_bound = flux['lb'];
            cobra_model.reactions.get_by_id(rxn).upper_bound = flux['ub'];
        # Change description, if any:
        if description:
            cobra_model.description = description;
        # Read in isotopomer model
        isotopomer_mapping = self.read_isotopomer_mapping_csv(isotopomer_mapping_filename); #broken
        isotopomer_str = self.build_isotopomer_str(isotopomer_mapping);
        # write model to sbml
        write_cobra_model_to_sbml_file(cobra_model,xml_filename)
        # Add isotopomer field to model
        for r in cobra_model.reactions:
            if isotopomer_str.has_key(r.id):
                cobra_model.reactions.get_by_id(r.id).isotopomer = isotopomer_str[r.id];
            else:
                cobra_model.reactions.get_by_id(r.id).isotopomer = '';
        # Add null basis:
        cobra_model_array = cobra_model.to_array_based_model();
        N = self.calculate.null(cobra_model_array.S.todense()) #convert S from sparse to full and compute the nullspace
        cobra_model.N = N;
        # solve and save pFBA for later use:
        optimize_minimal_flux(cobra_model,True,solver='gurobi');
        # add match field:
        match = numpy.zeros(len(cobra_model.reactions));
        cobra_model.match = match;
        # write model to mat
        save_matlab_model_isotopomer(cobra_model,mat_filename);
        with open(csv_filename,mode='wb') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Reaction','Formula','LB','UB','Genes','Subsystem','Isotopomer'])
            for r in cobra_model.reactions:
                writer.writerow([r.id,
                                 r.build_reaction_string(),
                                r.lower_bound,
                                r.upper_bound,
                                r.gene_reaction_rule,
                                r.subsystem,
                                r.isotopomer]);
    #analysis functions
    def load_isotopomer_matlab(self,matlab_data,isotopomer_data=None):
        '''Load 13CFlux isotopomer simulation data from matlab file'''
        # load measured isotopomers from MATLAB file into numpy array
        # load names and calculated isotopomers from MATLAB file into numpy array
        names = scipy.io.loadmat(matlab_data)['output']['names'][0][0];
        calculated_ave = scipy.io.loadmat(matlab_data)['output']['ave'][0][0];
        calculated_stdev = scipy.io.loadmat(matlab_data)['output']['stdev'][0][0];
        # load residuals from MATLAB file into numpy array
        residuals = scipy.io.loadmat(matlab_data)['residuals'];
        if isotopomer_data:
            measured_dict = json.load(open(isotopomer_data,'r'));
            measured_names = [];
            measured_ave = [];
            measured_stdev = [];
            # extract data to lists
            for frag,data in measured_dict['fragments'].iteritems():
                for name in data['data_names']:
                    measured_names.append(name);
                for ave in data['data_ave']:
                    measured_ave.append(ave);
                for stdev in data['data_stdev']:
                    measured_stdev.append(stdev);
            # convert lists to dict
            measured_dict = {};
            for i,name in enumerate(measured_names):
                measured_dict[name]={'measured_ave':measured_ave[i],
                                       'measured_stdev':measured_stdev[i]};
            # match measured names to calculated names
            measured_ave = [];
            measured_stdev = [];
            residuals = [];
            for i,name in enumerate(names):
                if measured_dict.has_key(name[0][0]):
                    measured_ave.append(measured_dict[name[0][0]]['measured_ave']);
                    measured_stdev.append(measured_dict[name[0][0]]['measured_stdev']);
                    residuals.append(measured_dict[name[0][0]]['measured_ave']-calculated_ave[i][0]);
                else:
                    measured_ave.append(None);
                    measured_stdev.append(None);
                    residuals.append(None);
        else:
            measured_ave_tmp = scipy.io.loadmat(matlab_data)['toCompare'];
            measured_ave = [];
            for d in measured_ave_tmp:
                measured_ave.append(d[0]);
            measured_stdev = numpy.zeros(len(measured_ave));
        # combine into a dictionary
        isotopomer = {};
        for i in range(len(names)):
            isotopomer[names[i][0][0]] = {'measured_ave':measured_ave[i], #TODO: extract out by fragment names
                                    'measured_stdev':measured_stdev[i],
                                    'calculated_ave':calculated_ave[i][0],
                                    'calculated_stdev':calculated_stdev[i][0],
                                    'residuals':residuals[i]};

        return isotopomer;
    def load_confidenceIntervals_matlab(self,matlab_data,cobra_model_matlab,cobra_model_name):
        '''Load confidence intervals from matlab file'''
        # load confidence intervals from MATLAB file into numpy array
        cimin_h5py = h5py.File(matlab_data)['ci']['minv'][0];
        cimax_h5py = h5py.File(matlab_data)['ci']['maxv'][0];
        cimin = numpy.array(cimin_h5py);
        cimax = numpy.array(cimax_h5py);
        # load cobramodel
        rxns = scipy.io.loadmat(cobra_model_matlab)[cobra_model_name]['rxns'][0][0]
        # combine cimin, cimax, and rxns into dictionary
        ci = {};
        for i in range(len(cimin)):
            ci[rxns[i][0][0]] = {'minv':cimin[i],'maxv':cimax[i]};

        return ci;
    def compare_isotopomers_calculated(self,isotopomer_1, isotopomer_2):
        '''compare two calculated isotopomer distributions'''
        # extract into lists
        absDif_list = [];
        ssr_1_list = [];
        ssr_2_list = [];
        bestFit_list = [];
        frag_list = [];
        ssr_1 = 0.0; # sum of squared residuals (threshold of 10e1, Antoniewicz poster, co-culture, Met Eng X)
        ssr_2 = 0.0;
        measured_1_list = [];
        measured_2_list = [];
        calculatedAve_1_list = [];
        calculatedAve_2_list = [];
        measuredStdev_1_list = [];
        measuredStdev_2_list = [];
        for frag,data in isotopomer_1.iteritems():
            absDif = 0.0;
            sr_1 = 0.0;
            sr_2 = 0.0;
            bestFit = None;
            absDif = fabs(isotopomer_1[frag]['calculated_ave'] - isotopomer_2[frag]['calculated_ave']);
            sr_1 = pow(isotopomer_1[frag]['calculated_ave']-isotopomer_1[frag]['measured_ave'],2);
            sr_2 = pow(isotopomer_2[frag]['calculated_ave']-isotopomer_2[frag]['measured_ave'],2);
            if sr_1>sr_2: bestFit = '2';
            elif sr_1<sr_2: bestFit = '1';
            elif sr_1==sr_2: bestFit = None;
            absDif_list.append(absDif);
            ssr_1_list.append(sr_1);
            ssr_2_list.append(sr_2);
            bestFit_list.append(bestFit);
            frag_list.append(frag);
            ssr_1 += sr_1;
            ssr_2 += sr_2;
            measured_1_list.append(isotopomer_1[frag]['measured_ave'])
            measured_2_list.append(isotopomer_2[frag]['measured_ave'])
            calculatedAve_1_list.append(isotopomer_1[frag]['calculated_ave']);
            calculatedAve_2_list.append(isotopomer_2[frag]['calculated_ave']);
            measuredStdev_1_list.append(isotopomer_1[frag]['measured_stdev']);
            measuredStdev_2_list.append(isotopomer_2[frag]['measured_stdev']);

        # calculate the correlation coefficient
        # 1. between measured vs. calculated (1 and 2)
        # 2. between calculated 1 vs. calculated 2
        r_measuredVsCalculated_1 = None;
        r_measuredVsCalculated_2 = None;
        r_measured1VsMeasured2 = None;
        p_measuredVsCalculated_1 = None;
        p_measuredVsCalculated_2 = None;
        p_measured1VsMeasured2 = None;

        r_measuredVsCalculated_1, p_measuredVsCalculated_1 = scipy.stats.pearsonr(measured_1_list,calculatedAve_1_list);
        r_measuredVsCalculated_2, p_measuredVsCalculated_2 = scipy.stats.pearsonr(measured_2_list,calculatedAve_2_list);
        r_measured1VsMeasured2, p_measured1VsMeasured2 = scipy.stats.pearsonr(calculatedAve_1_list,calculatedAve_2_list);

        # wrap stats into a dictionary
        isotopomer_comparison_stats = {};
        isotopomer_comparison_stats = dict(zip(('r_measuredVsCalculated_1', 'p_measuredVsCalculated_1',
            'r_measuredVsCalculated_2', 'p_measuredVsCalculated_2',
            'r_measured1VsMeasured2', 'p_measured1VsMeasured2',
            'ssr_1,ssr_2'),
                                               (r_measuredVsCalculated_1, p_measuredVsCalculated_1,
            r_measuredVsCalculated_2, p_measuredVsCalculated_2,
            r_measured1VsMeasured2, p_measured1VsMeasured2,
            ssr_1,ssr_2)));

        ## zip, sort, unzip # does not appear to sort correctly!
        #zipped = zip(absDif_list,ssr_1_list,ssr_2_list,bestFit_list,frag_list,
        #             measured_1_list,measured_2_list,calculatedAve_1_list,calculatedAve_2_list,
        #             measuredStdev_1_list,measuredStdev_2_list);
        #zipped.sort();
        #zipped.reverse();
        #absDif_list,ssr_1_list,sst_2_list,bestFit_list,frag_list,\
        #             measured_1_list,measured_2_list,calculatedAve_1_list,calculatedAve_2_list,\
        #             measuredStdev_1_list,measuredStdev_2_list = zip(*zipped);
        # restructure into a list of dictionaries for easy parsing or data base viewing
        isotopomer_comparison = [];
        for i in range(len(absDif_list)):
            isotopomer_comparison.append({'isotopomer_absDif':absDif_list[i],
                                           'isotopomer_1_sr':ssr_1_list[i],
                                           'isotopomer_2_sr':ssr_2_list[i],
                                           'bestFit':bestFit_list[i],
                                           'frag':frag_list[i],
                                           'measured_1_ave':measured_1_list[i],
                                           'measured_2_ave':measured_2_list[i],
                                           'measured_1_stdev':measuredStdev_1_list[i],
                                           'measured_2_stdev':measuredStdev_2_list[i],
                                           'calculated_1_ave':calculatedAve_1_list[i],
                                           'calculated_2_ave':calculatedAve_2_list[i]});

        return isotopomer_comparison,isotopomer_comparison_stats;
    def compare_ci_calculated(self,ci_1,ci_2):
        '''compare 2 calculated confidence intervals'''
        # extract into lists
        rxns_1_list = [];
        rxns_2_list = [];
        ciminv_1_list = [];
        ciminv_2_list = [];
        cimaxv_1_list = [];
        cimaxv_2_list = [];
        cirange_1_list = [];
        cirange_2_list = [];
        cirange_1_sum = 0.0;
        cirange_2_sum = 0.0;
        # ci_1:
        for k,v in ci_1.iteritems():
            rxns_1_list.append(k);
            ciminv_1_list.append(v['minv']);
            cimaxv_1_list.append(v['maxv']);
            cirange_1_list.append(v['maxv']-v['minv']);
            cirange_1_sum += v['maxv']-v['minv'];
        ## zip, sort, unzip
        #zipped1 = zip(rxns_1_list,ciminv_1_list,cimaxv_1_list,cirange_1_list);
        #zipped1.sort();
        #rxns_1_list,ciminv_1_list,cimaxv_1_list,cirange_1_list = zip(*zipped1);
        # ci_2:
        for k,v in ci_2.iteritems():
            rxns_2_list.append(k);
            ciminv_2_list.append(v['minv']);
            cimaxv_2_list.append(v['maxv']);
            cirange_2_list.append(v['maxv']-v['minv']);
            cirange_2_sum += v['maxv']-v['minv'];
        ## zip, sort, unzip
        #zipped2 = zip(rxns_2_list,ciminv_2_list,cimaxv_2_list,cirange_2_list);
        #zipped2.sort();
        #rxns_2_list,ciminv_2_list,cimaxv_2_list,cirange_2_list = zip(*zipped2);
        # compare by rxn_id
        cirange_absDev_list = [];
        rxns_combined_list = [];
        ciminv_1_combined_list = [];
        ciminv_2_combined_list = [];
        cimaxv_1_combined_list = [];
        cimaxv_2_combined_list = [];
        cirange_1_combined_list = [];
        cirange_2_combined_list = [];
        cirange_1_combined_sum = 0.0;
        cirange_2_combined_sum = 0.0;
        for i in range(len(rxns_1_list)):
            for j in range(len(rxns_2_list)):
                if rxns_1_list[i] == rxns_2_list[j]:
                    rxns_combined_list.append(rxns_1_list[i]);
                    cirange_absDev_list.append(fabs(cirange_1_list[i]-cirange_2_list[j]));
                    ciminv_1_combined_list.append(ciminv_1_list[i]);
                    ciminv_2_combined_list.append(ciminv_2_list[j]);
                    cimaxv_1_combined_list.append(cimaxv_1_list[i]);
                    cimaxv_2_combined_list.append(cimaxv_2_list[j]);
                    cirange_1_combined_list.append(cirange_1_list[i]);
                    cirange_2_combined_list.append(cirange_2_list[j]);
                    cirange_1_combined_sum += cirange_1_list[i]
                    cirange_2_combined_sum += cirange_2_list[j]
        ## zip, sort, unzip
        #zippedCombined = zip(cirange_absDev_list,rxns_combined_list,ciminv_1_combined_list,ciminv_2_combined_list,cimaxv_1_combined_list,cimaxv_2_combined_list,cirange_1_combined_list,cirange_2_combined_list);
        #zippedCombined.sort();
        #zippedCombined.reverse();
        #cirange_absDev_list,rxns_combined_list,ciminv_1_combined_list,ciminv_2_combined_list,cimaxv_1_combined_list,cimaxv_2_combined_list,cirange_1_combined_list,cirange_2_combined_list = zip(*zippedCombined);
        # restructure into a list of dictionaries for easy parsing or data base viewing
        ci_comparison = [];
        for i in range(len(cirange_absDev_list)):
            ci_comparison.append({'cirange_absDev_list':cirange_absDev_list[i],
                                  'rxns_combined_list':rxns_combined_list[i],
                                  'ciminv_1_combined_list':ciminv_1_combined_list[i],
                                  'ciminv_2_combined_list':ciminv_2_combined_list[i],
                                  'cimaxv_1_combined_list':cimaxv_1_combined_list[i],
                                  'cimaxv_2_combined_list':cimaxv_2_combined_list[i],
                                  'cirange_1_combined_list':cirange_1_combined_list[i],
                                  'cirange_2_combined_list':cirange_2_combined_list[i]});

        return ci_comparison,cirange_1_sum,cirange_2_sum,cirange_1_combined_sum,cirange_2_combined_sum;
    def plot_compare_isotopomers_calculated(self,isotopomer_comparison,isotopomer_comparison_stats):
        '''Plot 1: isotopomer fitting comparison
        Plot 2: isotopomer residual comparison'''
        io = base_exportData(isotopomer_comparison);
        # Plot 1 and Plot 2:
        io.write_dict2tsv('data//data.tsv');
    def plot_ci_calculated(self,ci):
        '''plot confidence intervals from fluxomics experiment using escher'''
        data = [];
        flux1 = {};
        flux2 = {};
        for k,v in ci.iteritems():
            flux1[k] = v['minv'];
            flux2[k] = v['maxv'];
        data.append(flux1);
        data.append(flux2);
        io = base_exportData(data);
        io.write_dict2json('visualization\\escher\\ci.json');
    def export_modelWithFlux(self,cobra_model_xml_I,ci_list_I,cobra_model_xml_O):
        '''update model lower_bound/upper_bound with calculated flux confidence intervals'''

        cobra_model = create_cobra_model_from_sbml_file(cobra_model_xml_I);

        rxns_add = [];
        rxns_omitted = [];
        rxns_break = [];

        system_boundaries = [x.id for x in cobra_model.reactions if x.boundary == 'system_boundary'];
        objectives = [x.id for x in cobra_model.reactions if x.objective_coefficient == 1];

        for i,ci_I in enumerate(ci_list_I):
            print 'add flux from ci ' + str(i);
            for rxn in cobra_model.reactions:
                if rxn.id in ci_I.keys() and not(rxn.id in system_boundaries)\
                    and not(rxn.id in objectives):
                    cobra_model_copy = cobra_model.copy();
                    # check for reactions that break the model:
                    if ci_I[rxn.id]['minv'] > 0:
                        cobra_model_copy.reactions.get_by_id(rxn.id).lower_bound = ci_I[rxn.id]['minv'];
                    if ci_I[rxn.id]['maxv'] > 0 and ci_I[rxn.id]['maxv'] > ci_I[rxn.id]['minv']:
                        cobra_model_copy.reactions.get_by_id(rxn.id).upper_bound = ci_I[rxn.id]['maxv'];
                    cobra_model_copy.optimize(solver='gurobi');
                    if not cobra_model_copy.solution.f:
                        print rxn.id + ' broke the model!'
                        rxns_break.append(rxn.id);
                    else: 
                        if ci_I[rxn.id]['minv'] > 0:
                            cobra_model.reactions.get_by_id(rxn.id).lower_bound = ci_I[rxn.id]['minv'];
                        if ci_I[rxn.id]['maxv'] > 0 and ci_I[rxn.id]['maxv'] > ci_I[rxn.id]['minv']:
                            cobra_model.reactions.get_by_id(rxn.id).upper_bound = ci_I[rxn.id]['maxv'];
                        rxns_add.append(rxn.id);
                else:
                    rxns_omitted.append(rxn.id);

        write_cobra_model_to_sbml_file(cobra_model,cobra_model_xml_O)

class stage02_isotopomer_metaboliteMapping():
    """Class to standardize metabolite mapping:

    A mapped metabolite takes the following form:
    'met_id' + 'nMet_id' + '_' + 'element' + nElement
    
    Input:
    met_ids_elements_I = [{met_id:element},...]
                         [{'f6p_c':'C'},{'f6p_c':'C'},{'f6p_c':'H'},{'f6p_c':'H'},{'ac_c':'C'},{'utp_c':'C'}]
                         NOTE: The order matters if using multiple elements! will need to further test in future versions
                         
    Base metabolites: default base metabolite is co2 for carbon and oh for hydrogen
    Base reaction: co2 + oh- + h+ = ch2o + o2"""

    def __init__(self,
            mapping_id_I=None,
            #met_name_I=None,
            met_id_I=None,
            #formula_I=None,
            met_elements_I=[],
            met_atompositions_I=[],
            met_symmetry_elements_I=[],
            met_symmetry_atompositions_I=[],
            used__I=True,
            comment__I=None,
            met_mapping_I=[],
            base_met_ids_I=[],
            base_met_elements_I=[],
            base_met_atompositions_I=[],
            base_met_symmetry_elements_I=[],
            base_met_symmetry_atompositions_I=[],
            base_met_indices_I=[]):
        #self.session = Session();
        self.stage02_isotopomer_query = stage02_isotopomer_query();
        self.calculate = base_calculate();
        self.metaboliteMapping={};
        self.metaboliteMapping['mapping_id']=mapping_id_I;
        #self.metaboliteMapping['met_name']=met_name_I;
        self.metaboliteMapping['met_id']=met_id_I;
        #self.metaboliteMapping['formula']=formula_I;
        self.metaboliteMapping['met_elements']=met_elements_I;
        self.metaboliteMapping['met_atompositions']=met_atompositions_I;
        self.metaboliteMapping['met_symmetry_elements']=met_symmetry_elements_I;
        self.metaboliteMapping['met_symmetry_atompositions']=met_symmetry_atompositions_I;
        self.metaboliteMapping['used_']=used__I;
        self.metaboliteMapping['comment_']=comment__I;
        self.metaboliteMapping['met_mapping']=met_mapping_I;
        self.metaboliteMapping['base_met_ids']=base_met_ids_I;
        self.metaboliteMapping['base_met_elements']=base_met_elements_I;
        self.metaboliteMapping['base_met_atompositions']=base_met_atompositions_I;
        self.metaboliteMapping['base_met_symmetry_elements']=base_met_symmetry_elements_I;
        self.metaboliteMapping['base_met_symmetry_atompositions']=base_met_symmetry_atompositions_I;
        self.metaboliteMapping['base_met_indices']=base_met_indices_I;
    def make_elementsAndPositionsTracked(self,met_id_I,element_I,n_elements_I):
        #Input: met_id_I,element_I,n_elements_I
        #Output: mapping_O,positions_O,elements_O
        #E.g: make_elementsTracked('fdp','C',6)
        mapping_O = [];
        positions_O = [];
        elements_O = [];
        for elements_cnt in range(n_elements_I):
            mapping = '[' + met_id_I + '_'  + element_I + str(elements_cnt) + ']';
            mapping_O.append(mapping);
            positions_O.append(elements_cnt);
            elements_O.append(element_I);
        return mapping_O,positions_O,elements_O;
    def make_trackedMetabolite(self,mapping_id_I,model_id_I,met_id_element_I,met_index_I=None):
        '''Make an unique atom mapping for the given metabolite and element'''
        currentElementPos = 0;
        mapping_O = [];
        positions_O = [];
        elements_O = [];
        base_met_ids_O = [];
        base_met_elements_O = [];
        base_met_atompositions_O = [];
        base_met_symmetry_elements_O = [];
        base_met_symmetry_atompositions_O = [];
        base_met_indices_O = [];
        for k,v in met_id_element_I.iteritems():
            # check if the metabolite is already in the database
            met_data = {}
            met_data = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id_I,k)
            #NOTE: need to add in a constraint to make sure that the elements in the database and the elments in the input match!
            if met_data and met_data.has_key('met_elements') and v==met_data['met_elements'][0]:
                nElements = len(met_data['met_elements']);
            else:
                # get the formula for the met_id
                formula_I = self.stage02_isotopomer_query.get_formula_modelIDAndMetID_dataStage02IsotopomerModelMetabolites(model_id_I,k);
                # get the number of elements
                if not Formula(formula_I)._elements.has_key(v): break; #check if the element is even contained in the formula
                if Formula(formula_I)._elements[v].has_key(0):
                    nElements = Formula(formula_I)._elements[v][0]; #get the # of the elements
            # make the tracking
            nMet = 0;
            if met_index_I: nMet = met_index_I
            mapping,positions,elements = self.make_elementsAndPositionsTracked(k+str(nMet),v,nElements);
            positions_corrected = [currentElementPos+pos for pos in positions];
            currentElementPos += max(positions)+1;
            mapping_O.append(mapping);
            positions_O.extend(positions_corrected);
            elements_O.extend(elements);
            base_met_ids_O.append(k)
            base_met_elements_O.append(elements)
            base_met_atompositions_O.append(positions)
            base_met_indices_O.append(nMet)
        self.metaboliteMapping['mapping_id']=mapping_id_I
        self.metaboliteMapping['met_id']=k
        self.metaboliteMapping['met_elements']=elements_O
        self.metaboliteMapping['met_atompositions']=positions_O
        self.metaboliteMapping['met_mapping']=mapping_O
        self.metaboliteMapping['base_met_ids']=base_met_ids_O
        self.metaboliteMapping['base_met_elements']=base_met_elements_O
        self.metaboliteMapping['base_met_atompositions']=base_met_atompositions_O
        self.metaboliteMapping['base_met_indices']=base_met_indices_O
    def make_compoundTrackedMetabolite(self,mapping_id_I,model_id_I,met_ids_elements_I,met_id_O,met_ids_indices_I = []):
        '''Make an unique atom mapping for the given metabolite based on base metabolites and elements'''
        #Input:
        #   metIDs_elements_I = [{met_id:element},..]
        # met_ids_elements_I = [{'f6p_c':'C'},{'ac_c':'C'},{'utp_c':'C'}}]
        #   metIDs_elements_I = [met_id:{elements=[string,...],stoichiometry:float}},..]
        # met_ids_elements_I = [{'f6p_c':{'elements':['C'],'stoichiometry':1}},{'ac_c':{'elements':['C'],'stoichiometry':1}},{'utp_c':{'elements':['C'],'stoichiometry':1}}]
        # make_compoundTrackedMetabolite('full04','140407_iDM2014',met_ids_elements_I,'uacgam_c')
        currentElementPos = 0;
        mapping_O = [];
        positions_O = [];
        elements_O = [];
        base_met_ids_O = [];
        base_met_elements_O = [];
        base_met_atompositions_O = [];
        base_met_symmetry_elements_O = [];
        base_met_symmetry_atompositions_O = [];
        base_met_indices_O = [];
        # get unique met_ids
        met_ids_all = [];
        for row in met_ids_elements_I:
            for k,v in row.iteritems():
                met_ids_all.append(k);
        met_ids_unique = list(set(met_ids_all))
        met_ids_cnt = {};
        met_ids_elements = {};
        for met_id in met_ids_unique:
            met_ids_cnt[met_id] = 0;
            met_ids_elements[met_id] = [];
        # make the compound mapping
        for row_cnt,row in enumerate(met_ids_elements_I):
            for k,v in row.iteritems():
                # check if the metabolite is already in the database
                met_data = {}
                met_data = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id_I,k)
                #NOTE: need to add in a constraint to make sure that the elements in the database and the elments in the input match!
                if met_data and met_data.has_key('met_elements') and v==met_data['met_elements'][0]:
                    nElements = len(met_data['met_elements']);
                else:
                    # get the formula for the met_id
                    formula_I = self.stage02_isotopomer_query.get_formula_modelIDAndMetID_dataStage02IsotopomerModelMetabolites(model_id_I,k);
                    # get the number of elements
                    if not Formula(formula_I)._elements.has_key(v): break; #check if the element is even contained in the formula
                    if Formula(formula_I)._elements[v].has_key(0):
                        nElements = Formula(formula_I)._elements[v][0]; #get the # of the elements
                # determine the metabolite index
                nMets = met_ids_cnt[k];
                if met_ids_indices_I: nMets = met_ids_indices_I[row_cnt]
                # make the tracking
                mapping,positions,elements = self.make_elementsAndPositionsTracked(k+str(nMets),v,nElements);
                positions_corrected = [currentElementPos+pos for pos in positions];
                currentElementPos += max(positions)+1;
                # add to the compound tracking
                mapping_O.append(mapping);
                positions_O.extend(positions_corrected);
                elements_O.extend(elements);
                base_met_ids_O.append(k)
                base_met_elements_O.append(elements)
                base_met_atompositions_O.append(positions)
                base_met_indices_O.append(nMets)
            met_ids_cnt[k] += 1; # needed to ensure a unique metabolite mapping if the same met_id is used multiple times
        self.metaboliteMapping['mapping_id']=mapping_id_I
        self.metaboliteMapping['met_id']=met_id_O
        self.metaboliteMapping['met_elements']=elements_O
        self.metaboliteMapping['met_atompositions']=positions_O
        self.metaboliteMapping['met_mapping']=mapping_O
        self.metaboliteMapping['base_met_ids']=base_met_ids_O
        self.metaboliteMapping['base_met_elements']=base_met_elements_O
        self.metaboliteMapping['base_met_atompositions']=base_met_atompositions_O
        self.metaboliteMapping['base_met_indices']=base_met_indices_O
    def append_baseMetabolites_toMetabolite(self,model_id_I,met_ids_elements_I,met_id_O=None):
        '''Append a base metabolite to the current metabolite'''
        #get the currentElementPos
        currentElementPos = max(self.metaboliteMapping['met_atompositions'])+1;
        # get unique met_ids
        met_ids_unique = list(set(self.metaboliteMapping['base_met_ids']))
        met_ids_cnt = {};
        met_ids_elements = {};
        for met_id in met_ids_unique:
            met_ids_cnt[met_id] = 0;
            met_ids_elements[met_id] = [];
        for met_id_cnt,met_id in enumerate(self.metaboliteMapping['base_met_ids']):
            # determine the number of met_ids
            met_ids_cnt[met_id]+=1
            # determine the unique elements
            if not self.metaboliteMapping['met_elements'][0] in met_ids_elements[met_id]:
                met_ids_elements[met_id].append(self.metaboliteMapping['met_elements'][met_id_cnt][0]);
        # add the mapping for the new metabolites
        for row in met_ids_elements_I:
            for k,v in row.iteritems():
                # check if the metabolite is already in the database
                met_data = {}
                met_data = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(self.metaboliteMapping['mapping_id'],k)
                #NOTE: need to add in a constraint to make sure that the elements in the database and the elments in the input match!
                if met_data and met_data.has_key('met_elements') and v==met_data['met_elements'][0]:
                    nElements = len(met_data['met_elements']);
                else:
                    # get the formula for the met_id
                    formula_I = self.stage02_isotopomer_query.get_formula_modelIDAndMetID_dataStage02IsotopomerModelMetabolites(model_id_I,k);
                    # get the number of elements
                    if not Formula(formula_I)._elements.has_key(v): break; #check if the element is even contained in the formula
                    if Formula(formula_I)._elements[v].has_key(0):
                        nElements = Formula(formula_I)._elements[v][0]; #get the # of the elements
                # adjust the metabolite number if the same metabolite already exists
                nMets = met_ids_cnt[k];
                met_id_mapping = k+nMets;
                # make the tracking
                mapping,positions,elements = self.make_elementsAndPositionsTracked(met_id_mapping,v,nElements);
                positions_corrected = [currentElementPos+pos for pos in positions];
                currentElementPos += max(positions)+1;
                # add to the compound tracking
                self.metaboliteMapping['met_mapping'].append(mapping);
                self.metaboliteMapping['met_atompositions'].extend(positions_corrected);
                self.metaboliteMapping['met_elements'].extend(elements);
                self.metaboliteMapping['base_met_ids'].append(k)
                self.metaboliteMapping['base_met_elements'].append(elements)
                self.metaboliteMapping['base_met_atompositions'].append(positions)
                self.metaboliteMapping['base_met_indices'].append(met_ids_cnt[k]);
                met_ids_cnt[met_id]+=1;
        if met_id_O: self.metaboliteMapping['met_id']=met_id_O
    def pop_baseMetabolite_fromMetabolite(self,model_id_I,met_id_element_I,met_id_O=None):
        '''Remove a base metabolite from the current metabolite:
        metabolites are removed FILO;
        NOTE: this can lead to problems downstream when the mapping
        is reconstructed from the base metabolites if multiple elements are used'''
        #Input:
        #   met_id_element_I = {met_id:element}
        '''Unit Test:
        '''
        met_mapping = self.metaboliteMapping['met_mapping'];
        base_met_ids = self.metaboliteMapping['base_met_ids'];
        base_met_elements = self.metaboliteMapping['base_met_elements'];
        base_met_atompositions = self.metaboliteMapping['base_met_atompositions'];
        base_met_indices = self.metaboliteMapping['base_met_indices'];
        #base_met_symmetry_elements=self.metaboliteMapping['base_met_symmetry_elements'];
        #base_met_symmetry_atompositions=self.metaboliteMapping['base_met_symmetry_atompositions'];
        met_mapping.reverse();
        base_met_ids.reverse();
        base_met_elements.reverse();
        base_met_atompositions.reverse();
        base_met_indices.reverse();
        #base_met_symmetry_elements.reverse();
        #base_met_symmetry_atompositions.reverse();
        self.metaboliteMapping['met_mapping']=[]
        self.metaboliteMapping['base_met_ids']=[]
        self.metaboliteMapping['base_met_elements']=[]
        self.metaboliteMapping['base_met_atompositions']=[]
        self.metaboliteMapping['base_met_indices']=[]
        #self.metaboliteMapping['base_met_symmetry_elements']=[]
        #self.metaboliteMapping['base_met_symmetry_atompositions']=[]
        for met_id_remove,v in met_id_element_I.iteritems():
            removed = False
            for met_cnt,met_id in enumerate(base_met_ids):
                if met_id_remove == met_id and v==base_met_elements[met_cnt][0] and not removed:
                    removed = True;
                else: 
                    self.metaboliteMapping['met_mapping'].insert(0,met_mapping[met_cnt]);
                    self.metaboliteMapping['base_met_ids'].insert(0,base_met_ids[met_cnt]);
                    self.metaboliteMapping['base_met_elements'].insert(0,base_met_elements[met_cnt]);
                    self.metaboliteMapping['base_met_atompositions'].insert(0,base_met_atompositions[met_cnt]);
                    self.metaboliteMapping['base_met_indices'].insert(0,base_met_indices[met_cnt])
                    #self.metaboliteMapping['base_met_symmetry_elements'].insert(0,base_met_symmetry_elements[met_cnt]);
                    #self.metaboliteMapping['base_met_symmetry_atompositions'].insert(0,base_met_symmetry_atompositions[met_cnt]);
        '''v1: removes ALL base metabolites that match the met_id'''
        #for met_id_remove in met_ids_I:
        #    for met_cnt,met_id in enumerate(base_met_ids):
        #        if met_id_remove != met_id:
        #            self.metaboliteMapping['met_mapping'].append(met_mapping[met_cnt]);
        #            self.metaboliteMapping['base_met_ids'].append(base_met_ids[met_cnt]);
        #            self.metaboliteMapping['base_met_elements'].append(base_met_elements[met_cnt]);
        #            self.metaboliteMapping['base_met_atompositions'].append(base_met_atompositions[met_cnt]);
        #            #self.metaboliteMapping['base_met_symmetry_elements'].append(base_met_symmetry_elements[met_cnt]);
        #            #self.metaboliteMapping['base_met_symmetry_atompositions'].append(base_met_symmetry_atompositions[met_cnt]);
        if met_id_O: self.metaboliteMapping['met_id']=met_id_O
        self.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
    def remove_baseMetabolite_fromMetabolite(self,model_id_I,met_id_element_I,met_id_O=None,met_index_I=None):
        '''Remove a base metabolite from the current metabolite:
        metabolites are removed FIFO if the index is not specified;'''
        #Input:
        #   met_id_element = {met_id:element}
        '''Unit Test:'''

        met_mapping = self.metaboliteMapping['met_mapping'];
        base_met_ids = self.metaboliteMapping['base_met_ids'];
        base_met_elements = self.metaboliteMapping['base_met_elements'];
        base_met_atompositions = self.metaboliteMapping['base_met_atompositions'];
        base_met_indices = self.metaboliteMapping['base_met_indices'];
        #base_met_symmetry_elements=self.metaboliteMapping['base_met_symmetry_elements'];
        #base_met_symmetry_atompositions=self.metaboliteMapping['base_met_symmetry_atompositions'];
        self.metaboliteMapping['met_mapping']=[]
        self.metaboliteMapping['base_met_ids']=[]
        self.metaboliteMapping['base_met_elements']=[]
        self.metaboliteMapping['base_met_atompositions']=[]
        self.metaboliteMapping['base_met_indices']=[]
        #self.metaboliteMapping['base_met_symmetry_elements']=[]
        #self.metaboliteMapping['base_met_symmetry_atompositions']=[]
        for met_id_remove,v in met_id_element_I.iteritems():
            removed = False
            for met_cnt,met_id in enumerate(base_met_ids):
                if met_index_I:
                    if met_index_I == base_met_indices[met_cnt] and met_id_remove == met_id and v==base_met_elements[met_cnt][0] and not removed:
                        removed = True
                    else: 
                        self.metaboliteMapping['met_mapping'].append(met_mapping[met_cnt]);
                        self.metaboliteMapping['base_met_ids'].append(base_met_ids[met_cnt]);
                        self.metaboliteMapping['base_met_elements'].append(base_met_elements[met_cnt]);
                        self.metaboliteMapping['base_met_atompositions'].append(base_met_atompositions[met_cnt]);
                        self.metaboliteMapping['base_met_indices'].append(base_met_indices[met_cnt]);
                        #self.metaboliteMapping['base_met_symmetry_elements'].append(base_met_symmetry_elements[met_cnt]);
                        #self.metaboliteMapping['base_met_symmetry_atompositions'].append(base_met_symmetry_atompositions[met_cnt]);
                else:
                    if met_id_remove == met_id and v==base_met_elements[met_cnt][0] and not removed:
                        removed = True
                    else: 
                        self.metaboliteMapping['met_mapping'].append(met_mapping[met_cnt]);
                        self.metaboliteMapping['base_met_ids'].append(base_met_ids[met_cnt]);
                        self.metaboliteMapping['base_met_elements'].append(base_met_elements[met_cnt]);
                        self.metaboliteMapping['base_met_atompositions'].append(base_met_atompositions[met_cnt]);
                        self.metaboliteMapping['base_met_indices'].append(base_met_indices[met_cnt]);
                        #self.metaboliteMapping['base_met_symmetry_elements'].append(base_met_symmetry_elements[met_cnt]);
                        #self.metaboliteMapping['base_met_symmetry_atompositions'].append(base_met_symmetry_atompositions[met_cnt]);
        '''v1: removes ALL base metabolites that match the met_id'''
        #for met_id_remove in met_ids_I:
        #    for met_cnt,met_id in enumerate(base_met_ids):
        #        if met_id_remove != met_id:
        #            self.metaboliteMapping['met_mapping'].append(met_mapping[met_cnt]);
        #            self.metaboliteMapping['base_met_ids'].append(base_met_ids[met_cnt]);
        #            self.metaboliteMapping['base_met_elements'].append(base_met_elements[met_cnt]);
        #            self.metaboliteMapping['base_met_atompositions'].append(base_met_atompositions[met_cnt]);
        #            #self.metaboliteMapping['base_met_symmetry_elements'].append(base_met_symmetry_elements[met_cnt]);
        #            #self.metaboliteMapping['base_met_symmetry_atompositions'].append(base_met_symmetry_atompositions[met_cnt]);
        if met_id_O: self.metaboliteMapping['met_id']=met_id_O
        self.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
    def extract_baseMetabolite_fromMetabolite(self,model_id_I,met_id_element_I,met_index_I=None):
        '''Returns a base metabolites from the current metabolite:
        returns metabolites in FIFO'''
        base_metaboliteMapping = stage02_isotopomer_metaboliteMapping();
        base_met_ids = self.metaboliteMapping['base_met_ids'];
        met_id_remove = {};
        met_index = None
        for k,v in met_id_element_I.iteritems():
            for met_cnt,met_id in enumerate(base_met_ids):
                if met_index_I:
                    if met_index_I == self.metaboliteMapping['base_met_indices'][met_cnt] and k == met_id and v==self.metaboliteMapping['base_met_elements'][met_cnt][0]:
                        met_id_remove = {k:self.metaboliteMapping['base_met_elements'][met_cnt][0]};
                        met_index = met_index_I;
                        break;
                else:
                    if k == met_id and v==self.metaboliteMapping['base_met_elements'][met_cnt][0]:
                        met_id_remove = {k:self.metaboliteMapping['base_met_elements'][met_cnt][0]};
                        met_index = self.metaboliteMapping['base_met_indices'][met_cnt]
                        break;
        base_metaboliteMapping.make_trackedMetabolite(self.metaboliteMapping['mapping_id'],model_id_I,met_id_remove,met_index);
        return base_metaboliteMapping
    def update_trackedMetabolite_fromBaseMetabolites(self,model_id_I):
        '''update mapping, elements, and atompositions from base metabolites;
        NOTE: issues may arise in the number assigned to each metabolite if multiple elements are used'''
        # get unique met_ids
        met_ids_unique = list(set(self.metaboliteMapping['base_met_ids']))
        met_ids_cnt = {};
        met_ids_elements = {};
        for met_id in met_ids_unique:
            met_ids_cnt[met_id] = 0;
            met_ids_elements[met_id] = [];
        # make the input structure
        met_ids_elements_I = [];
        for met_id_cnt,met_id in enumerate(self.metaboliteMapping['base_met_ids']):
            met_ids_elements_I.append({met_id:self.metaboliteMapping['base_met_elements'][met_id_cnt][0]})
        self.make_compoundTrackedMetabolite(self.metaboliteMapping['mapping_id'],model_id_I,met_ids_elements_I,self.metaboliteMapping['met_id'],self.metaboliteMapping['base_met_indices'])
    def make_newMetaboliteMapping(self):
        '''Make a new mapping for the metabolite that switches out the names of the base metabolites
        for the current metabolite'''
        mapping_O= [];
        elements = list(set(self.metaboliteMapping['met_elements']))
        element_cnt = {};
        for element in elements:
            element_cnt[element] = 0;
        for met_element in self.metaboliteMapping['met_elements']:
            mapping = '[' + self.metaboliteMapping['met_id'] + '_'  + met_element + str(element_cnt[met_element]) + ']';
            mapping_O.append(mapping);
            element_cnt[met_element]+=1
        return mapping_O
    def make_defaultBaseMetabolites(self):
        '''Add default base metabolite to the metabolite'''
        self.metaboliteMapping['base_met_ids']=[];
        self.metaboliteMapping['base_met_elements']=[];
        self.metaboliteMapping['base_met_atompositions']=[];
        self.metaboliteMapping['base_met_symmetry_elements']=[];
        self.metaboliteMapping['base_met_symmetry_atompositions']=[];
        self.metaboliteMapping['base_met_indices']=[];
        compartment = self.metaboliteMapping['met_id'].split('_')[-1]
        for cnt,element in enumerate(self.metaboliteMapping['met_elements']):
            if element == 'C':
                self.metaboliteMapping['base_met_ids'].append('co2'+'_'+compartment);
                self.metaboliteMapping['base_met_elements'].append([element]);
                self.metaboliteMapping['base_met_atompositions'].append([0]);
                self.metaboliteMapping['base_met_indices'].append(cnt);
            elif element == 'H':
                self.metaboliteMapping['base_met_ids'].append('h'+'_'+element);
                self.metaboliteMapping['base_met_elements'].append([element]);
                self.metaboliteMapping['base_met_atompositions'].append([0]);
                self.metaboliteMapping['base_met_indices'].append(cnt);
            else: print "element not yet supported"
    def convert_arrayMapping2StringMapping(self):
        arrayMapping = self.metaboliteMapping['met_mapping']
        stringMapping = ''
        for mapping in self.metaboliteMapping['met_mapping']:
            stringMapping+=''.join(mapping)
        return stringMapping;
    def convert_stringMapping2ArrayMapping(self):
        '''Convert a string representation of a mapping to an array representation'''
        #TODO:
        arrayMapping = self.metaboliteMapping['met_mapping']
        stringMapping = ''
        for mapping in self.metaboliteMapping['met_mapping']:
            stringMapping+=''.join(mapping)
        return stringMapping;
    def add_metaboliteMapping(self,
            mapping_id_I=None,
            met_id_I=None,
            met_elements_I=None,
            met_atompositions_I=None,
            met_symmetry_elements_I=None,
            met_symmetry_atompositions_I=None,
            used__I=True,
            comment__I=None):
        '''Add tracked metabolite to the database'''
        if mapping_id_I: self.metaboliteMapping['mapping_id']=mapping_id_I;
        if met_id_I: self.metaboliteMapping['met_id']=met_id_I;
        if met_elements_I: self.metaboliteMapping['met_elements']=met_elements_I;
        if met_atompositions_I: self.metaboliteMapping['met_atompositions']=met_atompositions_I;
        if met_symmetry_elements_I: self.metaboliteMapping['met_symmetry_elements']=met_symmetry_elements_I;
        if met_symmetry_atompositions_I: self.metaboliteMapping['met_symmetry_atompositions']=met_symmetry_atompositions_I;
        if used__I: self.metaboliteMapping['used_']=used__I;
        if comment__I: self.metaboliteMapping['comment_']=comment__I;
        #add data to the database
        #row = None;
        #row = data_stage02_isotopomer_atomMappingMetabolites(self.metaboliteMapping['mapping_id'],
        #    self.metaboliteMapping['met_id'],
        #    self.metaboliteMapping['met_elements'],
        #    self.metaboliteMapping['met_atompositions'],
        #    self.metaboliteMapping['met_symmetry_elements'],
        #    self.metaboliteMapping['met_symmetry_atompositions'],
        #    self.metaboliteMapping['used_'],
        #    self.metaboliteMapping['comment_'],
        #    self.make_newMetaboliteMapping(),
        #    self.metaboliteMapping['base_met_ids'],
        #    self.metaboliteMapping['base_met_elements'],
        #    self.metaboliteMapping['base_met_atompositions'],
        #    self.metaboliteMapping['base_met_symmetry_elements'],
        #    self.metaboliteMapping['base_met_symmetry_atompositions'],
        #    self.metaboliteMapping['base_met_indices']);
        #self.session.add(row);
        #self.session.commit();
        data = self.metaboliteMapping;
        data['met_mapping'] = self.make_newMetaboliteMapping();
        self.stage02_isotopomer_query.add_data_dataStage02IsotopomerAtomMappingMetabolites([data]);
    def update_metaboliteMapping(self,
            mapping_id_I=None,
            met_id_I=None,
            met_elements_I=None,
            met_atompositions_I=None,
            met_symmetry_elements_I=None,
            met_symmetry_atompositions_I=None,
            used__I=True,
            comment__I=None):
        '''Add tracked metabolite to the database'''
        if mapping_id_I: self.metaboliteMapping['mapping_id']=mapping_id_I;
        if met_id_I: self.metaboliteMapping['met_id']=met_id_I;
        if met_elements_I: self.metaboliteMapping['met_elements']=met_elements_I;
        if met_atompositions_I: self.metaboliteMapping['met_atompositions']=met_atompositions_I;
        if met_symmetry_elements_I: self.metaboliteMapping['met_symmetry_elements']=met_symmetry_elements_I;
        if met_symmetry_atompositions_I: self.metaboliteMapping['met_symmetry_atompositions']=met_symmetry_atompositions_I;
        if used__I: self.metaboliteMapping['used_']=used__I;
        if comment__I: self.metaboliteMapping['comment_']=comment__I;
        self.metaboliteMapping['met_mapping']=self.make_newMetaboliteMapping()
        #add update data in the database
        self.stage02_isotopomer_query.update_rows_dataStage02IsotopomerAtomMappingMetabolites([self.metaboliteMapping]);
    def get_metaboliteMapping(self,mapping_id_I,met_id_I):
        '''Get tracked metabolite from the database'''
        row = {}
        row = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id_I,met_id_I);
        self.metaboliteMapping=row;
    def get_baseMetabolites(self):
        '''Get base metabolite from the database for the current metabolite'''
        row = {}
        row = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(self.metaboliteMapping['mapping_id'],self.metaboliteMapping['met_id']);
        self.metaboliteMapping['base_met_ids']=row['base_met_ids'];
        self.metaboliteMapping['base_met_elements']=row['base_met_elements']
        self.metaboliteMapping['base_met_atompositions']=row['base_met_atompositions']
        self.metaboliteMapping['base_met_symmetry_elements']=row['base_met_symmetry_elements']
        self.metaboliteMapping['base_met_symmetry_atompositions']=row['base_met_symmetry_atompositions']
        # if the current base_met_indices are already set, add to them
        # NOTE: works only if the base metabolite is also the current metabolite
        if len(self.metaboliteMapping['base_met_indices'])==1:
            currentIndex = self.metaboliteMapping['base_met_indices'][0]
            self.metaboliteMapping['base_met_indices'] = [currentIndex + i for i in row['base_met_indices']];
        # else ensure that all met_id/base_met_index pairs are unique
        else:
            ## get unique met_ids
            #met_ids_unique = list(set(self.metaboliteMapping['base_met_ids']))
            #met_ids_cnt = {};
            #for met_id in met_ids_unique:
            #    met_ids_cnt[met_id] = 0;
            #for cnt,met_id in self.metaboliteMapping['base_met_ids']:
            #    self.metaboliteMapping['base_met_indices'].append(met_ids_cnt[met_id])
            self.metaboliteMapping['base_met_indices']=row['base_met_indices']
    def clear_metaboliteMapping(self):
        self.metaboliteMapping={};
        self.metaboliteMapping['mapping_id']=None;
        #self.metaboliteMapping['met_name']=None;
        self.metaboliteMapping['met_id']=None;
        #self.metaboliteMapping['formula']=None;
        self.metaboliteMapping['met_elements']=None;
        self.metaboliteMapping['met_atompositions']=None;
        self.metaboliteMapping['met_symmetry_elements']=None;
        self.metaboliteMapping['met_symmetry_atompositions']=None;
        self.metaboliteMapping['used_']=True;
        self.metaboliteMapping['comment_']=None;
        self.metaboliteMapping['met_mapping']=None;
        self.metaboliteMapping['base_met_ids']=None;
        self.metaboliteMapping['base_met_elements']=None;
        self.metaboliteMapping['base_met_atompositions']=None;
        self.metaboliteMapping['base_met_symmetry_elements']=None;
        self.metaboliteMapping['base_met_symmetry_atompositions']=None;
        self.metaboliteMapping['base_met_indices']=None;
    def copy_metaboliteMappingDict(self):
        '''Copy the current metabolite mapping'''
        copy_metaboliteMapping = {};
        copy_metaboliteMapping['mapping_id']=self.metaboliteMapping['mapping_id']
        #copy_metaboliteMapping['met_name']=self.metaboliteMapping['met_name']
        copy_metaboliteMapping['met_id']=self.metaboliteMapping['met_id']
        #copy_metaboliteMapping['formula']=self.metaboliteMapping['formula']
        copy_metaboliteMapping['met_elements']=self.metaboliteMapping['met_elements']
        copy_metaboliteMapping['met_atompositions']=self.metaboliteMapping['met_atompositions']
        copy_metaboliteMapping['met_symmetry_elements']=self.metaboliteMapping['met_symmetry_elements']
        copy_metaboliteMapping['met_symmetry_atompositions']=self.metaboliteMapping['met_symmetry_atompositions']
        copy_metaboliteMapping['used_']=self.metaboliteMapping['used_']
        copy_metaboliteMapping['comment_']=self.metaboliteMapping['comment_']
        copy_metaboliteMapping['met_mapping']=self.metaboliteMapping['met_mapping']
        copy_metaboliteMapping['base_met_ids']=self.metaboliteMapping['base_met_ids']
        copy_metaboliteMapping['base_met_elements']=self.metaboliteMapping['base_met_elements']
        copy_metaboliteMapping['base_met_atompositions']=self.metaboliteMapping['base_met_atompositions']
        copy_metaboliteMapping['base_met_symmetry_elements']=self.metaboliteMapping['base_met_symmetry_elements']
        copy_metaboliteMapping['base_met_symmetry_atompositions']=self.metaboliteMapping['base_met_symmetry_atompositions']
        copy_metaboliteMapping['base_met_indices']=self.metaboliteMapping['base_met_indices'];
        return copy_metaboliteMapping
    def copy_metaboliteMapping(self):
        '''Copy the current metabolite mapping'''
        return self;

class stage02_isotopomer_reactionMapping():
    def __init__(self,
            mapping_id_I=None,
            rxn_id_I=None,
            rxn_description_I=None,
            reactants_stoichiometry_tracked_I=[],
            products_stoichiometry_tracked_I=[],
            reactants_ids_tracked_I=[],
            products_ids_tracked_I=[],
            reactants_elements_tracked_I=[],
            products_elements_tracked_I=[],
            reactants_positions_tracked_I=[],
            products_positions_tracked_I=[],
            reactants_mapping_I=[],
            products_mapping_I=[],
            rxn_equation_I=None,
            used__I=None,
            comment__I=None,
            reactants_metaboliteMappings_I=[],
            products_metaboliteMappings_I=[]):
        #self.session = Session();
        self.stage02_isotopomer_query = stage02_isotopomer_query();
        self.calculate = base_calculate();
        self.reactionMapping={}
        self.reactionMapping['mapping_id']=mapping_id_I
        self.reactionMapping['rxn_id']=rxn_id_I
        self.reactionMapping['rxn_description']=rxn_description_I
        self.reactionMapping['reactants_stoichiometry_tracked']=reactants_stoichiometry_tracked_I
        self.reactionMapping['products_stoichiometry_tracked']=products_stoichiometry_tracked_I
        self.reactionMapping['reactants_ids_tracked']=reactants_ids_tracked_I
        self.reactionMapping['products_ids_tracked']=products_ids_tracked_I
        self.reactionMapping['reactants_elements_tracked']=reactants_elements_tracked_I
        self.reactionMapping['products_elements_tracked']=products_elements_tracked_I
        self.reactionMapping['reactants_positions_tracked']=reactants_positions_tracked_I
        self.reactionMapping['products_positions_tracked']=products_positions_tracked_I
        self.reactionMapping['reactants_mapping']=reactants_mapping_I
        self.reactionMapping['products_mapping']=products_mapping_I
        self.reactionMapping['rxn_equation']=rxn_equation_I
        self.reactionMapping['used_']=used__I
        self.reactionMapping['comment_']=comment__I
        self.reactionMapping['reactants_metaboliteMappings']=reactants_metaboliteMappings_I
        self.reactionMapping['products_metaboliteMappings']=products_metaboliteMappings_I
        self.reactants_base_met_ids=[];
        self.reactants_base_met_elements=[];
        self.reactants_base_met_atompositions=[];
        self.reactants_base_met_symmetry_elements=[];
        self.reactants_base_met_symmetry_atompositions=[];
        self.reactants_base_met_indices=[];
        self.products_base_met_ids=[];
        self.products_base_met_elements=[];
        self.products_base_met_atompositions=[];
        self.products_base_met_symmetry_elements=[];
        self.products_base_met_symmetry_atompositions=[];
        self.products_base_met_indices=[];
    def make_trackedBinaryReaction(self,mapping_id_I,model_id_I,rxn_id_I,reactant_ids_elements_I,product_id_I):
        '''Make a binary reaction of the form A + B + ... = C'''
        #Input
        # reactant_ids_elements_I = [met_id:{elements=[string,...],stoichiometry:float}},..]
        # product_ids_elements_I = {met_id:{elements=[string,...],stoichiometry:float}}}
        # e.g. met_ids_elements_I = [{'f6p_c':'C'},{'ac_c':'C'},{'utp_c','C'}]
        # e.g. irm.make_trackedBinaryReaction('full04','140407_iDM2014','rxn01',met_ids_elements_I,'uacgam_c')

        imm = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        reactant_ids_all = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                reactant_ids_all.append(k);
        reactant_ids_unique = list(set(reactant_ids_all))
        reactant_ids_cnt = {};
        for reactant_id in reactant_ids_unique:
            reactant_ids_cnt[reactant_id] = 0;
        # make the reactants mapping
        reactants_stoichiometry_tracked_O = [];
        reactants_ids_tracked_O = [];
        reactants_elements_tracked_O = [];
        reactants_positions_tracked_O = [];
        reactants_mapping_O = [];
        reactants_metaboliteMappings_O = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(mapping_id_I,model_id_I,{k:v},reactant_ids_cnt[k]);
                reactants_elements_tracked_O.append(imm.metaboliteMapping['met_elements']);
                reactants_positions_tracked_O.append(imm.metaboliteMapping['met_atompositions']);
                reactants_mapping_O.append(imm.convert_arrayMapping2StringMapping());
                reactants_stoichiometry_tracked_O.append(-1.0);
                reactants_ids_tracked_O.append(k);
                reactants_metaboliteMappings_O.append(copy(imm.copy_metaboliteMapping()));
                imm.clear_metaboliteMapping()
                reactant_ids_cnt[k]+=1
        # make the products mapping
        products_stoichiometry_tracked_O = [];
        products_ids_tracked_O = [];
        products_elements_tracked_O = [];
        products_positions_tracked_O = [];
        products_mapping_O = [];
        products_metaboliteMappings_O = [];
        if product_id_I:
            imm.make_compoundTrackedMetabolite(mapping_id_I,model_id_I,reactant_ids_elements_I,product_id_I);
            products_elements_tracked_O.append(imm.metaboliteMapping['met_elements']);
            products_positions_tracked_O.append(imm.metaboliteMapping['met_atompositions']);
            products_mapping_O.append(imm.convert_arrayMapping2StringMapping());
            products_stoichiometry_tracked_O.append(1.0);
            products_ids_tracked_O.append(product_id_I);
            products_metaboliteMappings_O.append(copy(imm.copy_metaboliteMapping()));
        # save the reaction
        self.reactionMapping['mapping_id']=mapping_id_I
        self.reactionMapping['rxn_id']=rxn_id_I
        self.reactionMapping['rxn_description']=None
        self.reactionMapping['reactants_stoichiometry_tracked']=reactants_stoichiometry_tracked_O
        self.reactionMapping['products_stoichiometry_tracked']=products_stoichiometry_tracked_O
        self.reactionMapping['reactants_ids_tracked']=reactants_ids_tracked_O
        self.reactionMapping['products_ids_tracked']=products_ids_tracked_O
        self.reactionMapping['reactants_elements_tracked']=reactants_elements_tracked_O
        self.reactionMapping['products_elements_tracked']=products_elements_tracked_O
        self.reactionMapping['reactants_positions_tracked']=reactants_positions_tracked_O
        self.reactionMapping['products_positions_tracked']=products_positions_tracked_O
        self.reactionMapping['reactants_mapping']=reactants_mapping_O
        self.reactionMapping['products_mapping']=products_mapping_O
        self.reactionMapping['rxn_equation']=None
        self.reactionMapping['used_']=True
        self.reactionMapping['comment_']=None
        self.reactionMapping['reactants_metaboliteMappings']=reactants_metaboliteMappings_O
        self.reactionMapping['products_metaboliteMappings']=products_metaboliteMappings_O
    def make_trackedCompoundReaction(self,mapping_id_I,model_id_I,rxn_id_I,reactant_ids_elements_I,base_reactant_positions_I,base_reactant_indices_I,compound_product_id_I,base_product_ids_elements_I,base_product_ids_O):
        '''Make a compound tracked reaction
        1. make compound product
        2. remove specified base products from compound product
        3. update the compound product
        4. rename the base products
        5. append base products to products list'''

        #Input
        # reactant_ids_elements_I = [{met_id:elements},...]
        # base_reactant_positions_I = [{met_id_reactant:position},...] #Note: must be listed in order (positions of the reactant to be partitioned)
        # base_reactant_indices_I = [{met_id_product:position in base_reactants_ids},...] #Note: must be listed in order (positions of the reactant to be partitioned)
        #                                                                                        index referes to the position of the base met_id in the reactant to be partitioned
        # compound_product_id_I = met_id
        # base_product_ids_elements_I = [{met_id:elements},...] #Note: must be listed in order
        # base_product_ids_O = [met_id_new,...] #Note: must be listed in order

        imm = stage02_isotopomer_metaboliteMapping();
        imm_product = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        reactant_ids_all = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                reactant_ids_all.append(k);
        reactant_ids_unique = list(set(reactant_ids_all))
        reactant_ids_cnt = {};
        for reactant_id in reactant_ids_unique:
            reactant_ids_cnt[reactant_id] = 0;
        # get all reactants_base_met_ids and reactants_base_indices in the input:
        reactants_base_met_ids = [];
        reactants_base_indices = [];
        for row in base_reactant_indices_I:
            for k,v in row.iteritems():
                reactants_base_met_ids.append(k)
                reactants_base_indices.append(v)
        # get unique reactants_base_met_ids
        reactants_base_met_ids_unique = list(set(reactants_base_met_ids));
        reactants_base_met_ids_cnt = {};
        for base_met_id in reactants_base_met_ids:
            reactants_base_met_ids_cnt[base_met_id]=0;
        # make the reactants mapping
        reactants_stoichiometry_tracked_O = [];
        reactants_ids_tracked_O = [];
        reactants_elements_tracked_O = [];
        reactants_positions_tracked_O = [];
        reactants_mapping_O = [];
        reactants_metaboliteMappings_O = [];
        imm_product.metaboliteMapping['mapping_id'] = mapping_id_I
        imm_product.metaboliteMapping['base_met_ids']=[];
        imm_product.metaboliteMapping['base_met_elements']=[];
        imm_product.metaboliteMapping['base_met_atompositions']=[];
        imm_product.metaboliteMapping['base_met_symmetry_elements']=[];
        imm_product.metaboliteMapping['base_met_symmetry_atompositions']=[];
        imm_product.metaboliteMapping['base_met_indices']=[];
        matched_cnt = 0;      
        for row_cnt,row in enumerate(reactant_ids_elements_I):
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(mapping_id_I,model_id_I,{k:v},reactant_ids_cnt[k]);
                # update base_metabolites from the database for reactant that will be partitioned
                base_found = False;
                if matched_cnt < len(base_reactant_positions_I):
                    for k1,v1 in base_reactant_positions_I[matched_cnt].iteritems(): #there will be only 1 key-value pair
                        if k1 == k and row_cnt == v1:
                            imm.get_baseMetabolites();
                            imm.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
                            base_found = True;
                            break;
                # check that there are no duplicate met_id/met_index pairs
                duplicates_found=False;
                met_id_duplicate_found=[];
                for cnt1,met_id1 in enumerate(imm.metaboliteMapping['base_met_ids']):
                    #for cnt2,met_id2 in enumerate(imm_product.metaboliteMapping['base_met_ids']):
                    #    if met_id1==met_id2 and imm.metaboliteMapping['base_met_indices'][cnt1]==imm_product.metaboliteMapping['base_met_indices'][cnt2]:
                            #imm.metaboliteMapping['base_met_indices'][cnt1]+=1;
                            #duplicates_found=True
                    for cnt2,met_id2 in enumerate(reactants_base_met_ids + imm_product.metaboliteMapping['base_met_ids']): # reactant base_met_ids that are already a part of the reaction + 
                                                                                                                           # base_met_ids that will be added to the reaction
                        if met_id1==met_id2 and imm.metaboliteMapping['base_met_indices'][cnt1]<=(reactants_base_indices + imm_product.metaboliteMapping['base_met_indices'])[cnt2]:
                                                                            #the base_met_ids match and the base_indices_match
                                                                            #need to increase the base_index +1 over the current index
                            imm.metaboliteMapping['base_met_indices'][cnt1]=reactants_base_met_ids_cnt[met_id1];
                            duplicates_found=True
                            reactants_base_met_ids_cnt[met_id1]+=1;
                            met_id_duplicate_found.append(met_id1)
                # update the base_reactant_indices_I if the corresponding base_met_index was changed
                if matched_cnt < len(base_reactant_positions_I):
                    for k1,v1 in base_reactant_positions_I[matched_cnt].iteritems(): #there will be only 1 key-value pair
                        if k1 == k and row_cnt == v1:
                            for k2,v2 in base_reactant_indices_I[matched_cnt].iteritems():
                                base_reactant_indices_I[matched_cnt][k2]=imm.metaboliteMapping['base_met_indices'][v2];
                # update counter for matched input
                if base_found: matched_cnt+=1;
                # update met_mapping
                imm.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
                ## increase the count for the reactants_base_met_ids for duplicates that were found
                #if duplicates_found: 
                #    for k1 in met_id_duplicate_found:
                #        reactants_base_met_ids_cnt[k1]+=1;
                # update reactants_base_met_ids_cnt for any new base_met_ids that were added
                base_met_ids_cnt_all_tmp=[];
                for cnt,base_met_id in enumerate(imm.metaboliteMapping['base_met_ids']):
                    base_met_ids_cnt_all_tmp.append(base_met_id);
                base_met_ids_cnt_unqiue_tmp=list(set(base_met_ids_cnt_all_tmp));
                base_met_ids_cnt_tmp = {};
                for base_met_id in base_met_ids_cnt_unqiue_tmp:
                    base_met_ids_cnt_tmp[base_met_id] = 0;
                for cnt,base_met_id in enumerate(imm.metaboliteMapping['base_met_ids']):
                    if imm.metaboliteMapping['base_met_indices'][cnt]>=base_met_ids_cnt_tmp[base_met_id]:
                        base_met_ids_cnt_tmp[base_met_id] = imm.metaboliteMapping['base_met_indices'][cnt]+1; 
                for cnt,base_met_id in enumerate(imm.metaboliteMapping['base_met_ids']):
                    if not base_met_id in reactants_base_met_ids_cnt.keys():
                        reactants_base_met_ids_cnt[base_met_id]=base_met_ids_cnt_tmp[base_met_id];
                self.reactionMapping['reactants_elements_tracked'].append(imm.metaboliteMapping['met_elements']);
                self.reactionMapping['reactants_positions_tracked'].append(imm.metaboliteMapping['met_atompositions']);
                self.reactionMapping['reactants_mapping'].append(imm.convert_arrayMapping2StringMapping());
                self.reactionMapping['reactants_stoichiometry_tracked'].append(-1.0);
                self.reactionMapping['reactants_ids_tracked'].append(k);
                #
                reactants_elements_tracked_O.append(imm.metaboliteMapping['met_elements']);
                reactants_positions_tracked_O.append(imm.metaboliteMapping['met_atompositions']);
                reactants_mapping_O.append(imm.convert_arrayMapping2StringMapping());
                reactants_stoichiometry_tracked_O.append(-1.0);
                reactants_ids_tracked_O.append(k);
                # copy out all of the base information
                imm_product.metaboliteMapping['base_met_ids'].extend(imm.metaboliteMapping['base_met_ids']);
                imm_product.metaboliteMapping['base_met_elements'].extend(imm.metaboliteMapping['base_met_elements']);
                imm_product.metaboliteMapping['base_met_atompositions'].extend(imm.metaboliteMapping['base_met_atompositions']);
                #imm_product.metaboliteMapping['base_met_symmetry_elements'].extend(imm.metaboliteMapping['base_met_symmetry_elements']);
                #imm_product.metaboliteMapping['base_met_symmetry_atompositions'].extend(imm.metaboliteMapping['base_met_symmetry_atompositions']);
                imm_product.metaboliteMapping['base_met_indices'].extend(imm.metaboliteMapping['base_met_indices']); 
                #
                reactants_metaboliteMappings_O.append(copy(imm.copy_metaboliteMapping()));  
                imm.clear_metaboliteMapping()
                reactant_ids_cnt[k]+=1
        # make the initial compound product mapping
        imm_product.update_trackedMetabolite_fromBaseMetabolites(model_id_I)
        # extract out the products from the compound product
        base_products = [];
        for cnt,row in enumerate(base_product_ids_elements_I):
            for k,v in row.iteritems():
                base_products.append(imm_product.extract_baseMetabolite_fromMetabolite(model_id_I,{k:v},base_reactant_indices_I[cnt][k]));
        # remove the base_products from the compound product
        for cnt,row in enumerate(base_product_ids_elements_I):
            for k,v in row.iteritems():
                imm_product.remove_baseMetabolite_fromMetabolite(model_id_I,{k:v},met_id_O=compound_product_id_I,met_index_I=base_reactant_indices_I[cnt][k]);
        # make the final products
        if compound_product_id_I: imm_final_products = [imm_product];
        else: imm_final_products = [];
        for d in base_products:
            imm_final_products.append(d);
        if compound_product_id_I: imm_final_products_ids = [compound_product_id_I];
        else: imm_final_products_ids = [];
        for id in base_product_ids_O:
            imm_final_products_ids.append(id);
        products_stoichiometry_tracked_O = [];
        products_ids_tracked_O = [];
        products_elements_tracked_O = [];
        products_positions_tracked_O = [];
        products_mapping_O = [];
        products_metaboliteMappings_O = [];
        for cnt,d in enumerate(imm_final_products):
            products_elements_tracked_O.append(d.metaboliteMapping['met_elements']);
            products_positions_tracked_O.append(d.metaboliteMapping['met_atompositions']);
            products_mapping_O.append(d.convert_arrayMapping2StringMapping());
            products_stoichiometry_tracked_O.append(1.0);
            products_ids_tracked_O.append(imm_final_products_ids[cnt]);
            products_metaboliteMappings_O.append(copy(d.copy_metaboliteMapping()));
        # save the reaction
        self.reactionMapping['mapping_id']=mapping_id_I
        self.reactionMapping['rxn_id']=rxn_id_I
        self.reactionMapping['rxn_description']=None
        self.reactionMapping['reactants_stoichiometry_tracked']=reactants_stoichiometry_tracked_O
        self.reactionMapping['products_stoichiometry_tracked']=products_stoichiometry_tracked_O
        self.reactionMapping['reactants_ids_tracked']=reactants_ids_tracked_O
        self.reactionMapping['products_ids_tracked']=products_ids_tracked_O
        self.reactionMapping['reactants_elements_tracked']=reactants_elements_tracked_O
        self.reactionMapping['products_elements_tracked']=products_elements_tracked_O
        self.reactionMapping['reactants_positions_tracked']=reactants_positions_tracked_O
        self.reactionMapping['products_positions_tracked']=products_positions_tracked_O
        self.reactionMapping['reactants_mapping']=reactants_mapping_O
        self.reactionMapping['products_mapping']=products_mapping_O
        self.reactionMapping['rxn_equation']=None
        self.reactionMapping['used_']=True
        self.reactionMapping['comment_']=None
        self.reactionMapping['reactants_metaboliteMappings']=reactants_metaboliteMappings_O
        self.reactionMapping['products_metaboliteMappings']=products_metaboliteMappings_O
    def make_trackedUnitaryReactions(self,mapping_id_I,model_id_I,rxn_id_I,reactant_ids_elements_I,product_ids_I):
        '''Make a unitary reaction of the form aA = bB where the coefficient a = b'''
        #Input
        # reactant_ids_elements_I = [{met_id:elements},]
        # product_ids_elements_I = [met_id,...]

        # check input
        if len(reactant_ids_elements_I)!=len(product_ids_I):
            print "length of reactants_ids does not match the length of products_ids";
            return;
        imm = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        reactant_ids_all = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                reactant_ids_all.append(k);
        reactant_ids_unique = list(set(reactant_ids_all))
        reactant_ids_cnt = {};
        for reactant_id in reactant_ids_unique:
            reactant_ids_cnt[reactant_id] = 0;
        # make the reactants mapping
        reactants_stoichiometry_tracked_O = [];
        reactants_ids_tracked_O = [];
        reactants_elements_tracked_O = [];
        reactants_positions_tracked_O = [];
        reactants_mapping_O = [];
        reactants_metaboliteMappings_O = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(mapping_id_I,model_id_I,{k:v},reactant_ids_cnt[k]);
                reactants_elements_tracked_O.append(imm.metaboliteMapping['met_elements']);
                reactants_positions_tracked_O.append(imm.metaboliteMapping['met_atompositions']);
                reactants_mapping_O.append(imm.convert_arrayMapping2StringMapping());
                reactants_stoichiometry_tracked_O.append(-abs(1));
                reactants_ids_tracked_O.append(k);
                reactants_metaboliteMappings_O.append(copy(imm.copy_metaboliteMapping()));
                imm.clear_metaboliteMapping()
                reactant_ids_cnt[k]+=1
        # make the products mapping
        products_stoichiometry_tracked_O = [];
        products_ids_tracked_O = [];
        products_elements_tracked_O = [];
        products_positions_tracked_O = [];
        products_mapping_O = [];
        products_metaboliteMappings_O = [];
        for product_cnt,product in enumerate(product_ids_I):
            products_elements_tracked_O.append(reactants_elements_tracked_O[product_cnt]);
            products_positions_tracked_O.append(reactants_positions_tracked_O[product_cnt]);
            products_mapping_O.append(reactants_mapping_O[product_cnt]);
            products_stoichiometry_tracked_O.append(abs(reactants_stoichiometry_tracked_O[product_cnt]));
            products_ids_tracked_O.append(product);
            imm_tmp = copy(reactants_metaboliteMappings_O[product_cnt].copy_metaboliteMapping());
            imm_tmp.metaboliteMapping['met_id']=product; # change the name
            products_metaboliteMappings_O.append(imm_tmp);
        # save the reaction
        self.reactionMapping['mapping_id']=mapping_id_I
        self.reactionMapping['rxn_id']=rxn_id_I
        self.reactionMapping['rxn_description']=None
        self.reactionMapping['reactants_stoichiometry_tracked']=reactants_stoichiometry_tracked_O
        self.reactionMapping['products_stoichiometry_tracked']=products_stoichiometry_tracked_O
        self.reactionMapping['reactants_ids_tracked']=reactants_ids_tracked_O
        self.reactionMapping['products_ids_tracked']=products_ids_tracked_O
        self.reactionMapping['reactants_elements_tracked']=reactants_elements_tracked_O
        self.reactionMapping['products_elements_tracked']=products_elements_tracked_O
        self.reactionMapping['reactants_positions_tracked']=reactants_positions_tracked_O
        self.reactionMapping['products_positions_tracked']=products_positions_tracked_O
        self.reactionMapping['reactants_mapping']=reactants_mapping_O
        self.reactionMapping['products_mapping']=products_mapping_O
        self.reactionMapping['rxn_equation']=None
        self.reactionMapping['used_']=True
        self.reactionMapping['comment_']=None
        self.reactionMapping['reactants_metaboliteMappings']=reactants_metaboliteMappings_O
        self.reactionMapping['products_metaboliteMappings']=products_metaboliteMappings_O
    def make_reverseReaction(self,rxn_id_I=None):
        '''Make the reverse of the current reaction'''
        forward_reactionMapping = {}
        forward_reactionMapping['mapping_id']=self.reactionMapping['mapping_id']
        forward_reactionMapping['rxn_id']=self.reactionMapping['rxn_id']
        forward_reactionMapping['rxn_description']=self.reactionMapping['rxn_description']
        forward_reactionMapping['reactants_stoichiometry_tracked']=self.reactionMapping['reactants_stoichiometry_tracked']
        forward_reactionMapping['products_stoichiometry_tracked']=self.reactionMapping['products_stoichiometry_tracked']
        forward_reactionMapping['reactants_ids_tracked']=self.reactionMapping['reactants_ids_tracked']
        forward_reactionMapping['products_ids_tracked']=self.reactionMapping['products_ids_tracked']
        forward_reactionMapping['reactants_elements_tracked']=self.reactionMapping['reactants_elements_tracked']
        forward_reactionMapping['products_elements_tracked']=self.reactionMapping['products_elements_tracked']
        forward_reactionMapping['reactants_positions_tracked']=self.reactionMapping['reactants_positions_tracked']
        forward_reactionMapping['products_positions_tracked']=self.reactionMapping['products_positions_tracked']
        forward_reactionMapping['reactants_mapping']=self.reactionMapping['reactants_mapping']
        forward_reactionMapping['products_mapping']=self.reactionMapping['products_mapping']
        forward_reactionMapping['rxn_equation']=self.reactionMapping['rxn_equation']
        forward_reactionMapping['used_']=self.reactionMapping['used_']
        forward_reactionMapping['comment_']=self.reactionMapping['comment_']
        forward_reactionMapping['reactants_metaboliteMappings']=self.reactionMapping['reactants_metaboliteMappings']
        forward_reactionMapping['products_metaboliteMappings']=self.reactionMapping['products_metaboliteMappings']
        reverse_reactionMapping = {}
        reverse_reactionMapping['mapping_id']=self.reactionMapping['mapping_id']
        if rxn_id_I: reverse_reactionMapping['rxn_id']=rxn_id_I
        else: reverse_reactionMapping['rxn_id']=self.reactionMapping['rxn_id']
        reverse_reactionMapping['rxn_description']=self.reactionMapping['rxn_description']
        reverse_reactionMapping['reactants_stoichiometry_tracked']=[-s for s in self.reactionMapping['products_stoichiometry_tracked']]
        reverse_reactionMapping['products_stoichiometry_tracked']=[-s for s in self.reactionMapping['reactants_stoichiometry_tracked']]
        reverse_reactionMapping['reactants_ids_tracked']=self.reactionMapping['products_ids_tracked']
        reverse_reactionMapping['products_ids_tracked']=self.reactionMapping['reactants_ids_tracked']
        reverse_reactionMapping['reactants_elements_tracked']=self.reactionMapping['products_elements_tracked']
        reverse_reactionMapping['products_elements_tracked']=self.reactionMapping['reactants_elements_tracked']
        reverse_reactionMapping['reactants_positions_tracked']=self.reactionMapping['products_positions_tracked']
        reverse_reactionMapping['products_positions_tracked']=self.reactionMapping['reactants_positions_tracked']
        reverse_reactionMapping['reactants_mapping']=self.reactionMapping['products_mapping']
        reverse_reactionMapping['products_mapping']=self.reactionMapping['reactants_mapping']
        reverse_reactionMapping['rxn_equation']=self.reactionMapping['rxn_equation']
        reverse_reactionMapping['used_']=self.reactionMapping['used_']
        reverse_reactionMapping['comment_']=self.reactionMapping['comment_']
        reverse_reactionMapping['reactants_metaboliteMappings']=self.reactionMapping['products_metaboliteMappings']
        reverse_reactionMapping['products_metaboliteMappings']=self.reactionMapping['reactants_metaboliteMappings']
        self.reactionMapping = reverse_reactionMapping;
    def add_trackedBinaryReaction_toReaction(self,model_id_I,reactant_ids_elements_I,product_id_I):
        '''Add binary reaction to the current reaction'''
        imm = stage02_isotopomer_metaboliteMapping();
        imm_product = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        reactant_ids_all = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                reactant_ids_all.append(k);
        for k in self.reactionMapping['reactants_ids_tracked']:
            reactant_ids_all.append(k);
        reactant_ids_unique = list(set(reactant_ids_all))
        reactant_ids_cnt = {};
        for reactant_id in reactant_ids_unique:
            reactant_ids_cnt[reactant_id] = 0;
        # get all reactants_base_met_ids and reactants_base_indices:
        reactants_base_met_ids = [];
        reactants_base_indices = [];
        for cnt,mm in enumerate(self.reactionMapping['reactants_metaboliteMappings']):
            reactants_base_met_ids.extend(mm.metaboliteMapping['base_met_ids'])
            reactants_base_indices.extend(self.reactionMapping['reactants_metaboliteMappings'][cnt].metaboliteMapping['base_met_indices'])
        reactants_base_met_ids_I = [];
        # get unique reactants_base_met_ids
        reactants_base_met_ids_unique = list(set(reactants_base_met_ids));
        reactants_base_met_ids_cnt = {};
        for base_met_id in reactants_base_met_ids_unique:
            reactants_base_met_ids_cnt[base_met_id]=0;
        for cnt,base_met_id in enumerate(reactants_base_met_ids):
            reactants_base_met_ids_cnt[base_met_id]=reactants_base_indices[cnt]+1
        # make the reactants mapping
        imm_product.metaboliteMapping['mapping_id'] = self.reactionMapping['mapping_id']
        imm_product.metaboliteMapping['base_met_ids']=[];
        imm_product.metaboliteMapping['base_met_elements']=[];
        imm_product.metaboliteMapping['base_met_atompositions']=[];
        imm_product.metaboliteMapping['base_met_symmetry_elements']=[];
        imm_product.metaboliteMapping['base_met_symmetry_atompositions']=[];
        imm_product.metaboliteMapping['base_met_indices']=[];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(self.reactionMapping['mapping_id'],model_id_I,{k:v},reactant_ids_cnt[k]);
                # check that there are no duplicate met_id/met_index pairs
                duplicates_found=False;
                met_id_duplicate_found=[];
                for cnt1,met_id1 in enumerate(imm.metaboliteMapping['base_met_ids']): # the current base_met_ids
                    for cnt2,met_id2 in enumerate(reactants_base_met_ids + imm_product.metaboliteMapping['base_met_ids']): # reactant base_met_ids that are already a part of the reaction + 
                                                                                                                           # base_met_ids that will be added to the reaction
                        if met_id1==met_id2 and imm.metaboliteMapping['base_met_indices'][cnt1]==(reactants_base_indices + imm_product.metaboliteMapping['base_met_indices'])[cnt2]:
                                                                            #the base_met_ids match and the base_indices_match
                                                                            #need to increase the base_index +1 over the current index
                            imm.metaboliteMapping['base_met_indices'][cnt1]=reactants_base_met_ids_cnt[met_id1];
                            duplicates_found=True
                            met_id_duplicate_found.append(met_id1)
                # update met_mapping
                imm.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
                if duplicates_found: 
                    for k2 in met_id_duplicate_found:
                        reactants_base_met_ids_cnt[k2]+=1;
                self.reactionMapping['reactants_elements_tracked'].append(imm.metaboliteMapping['met_elements']);
                self.reactionMapping['reactants_positions_tracked'].append(imm.metaboliteMapping['met_atompositions']);
                self.reactionMapping['reactants_mapping'].append(imm.convert_arrayMapping2StringMapping());
                self.reactionMapping['reactants_stoichiometry_tracked'].append(-1.0);
                self.reactionMapping['reactants_ids_tracked'].append(k);
                self.reactionMapping['reactants_metaboliteMappings'].append(copy(imm.copy_metaboliteMapping()));
                # copy out all of the base information
                imm_product.metaboliteMapping['base_met_ids'].extend(imm.metaboliteMapping['base_met_ids']);
                imm_product.metaboliteMapping['base_met_elements'].extend(imm.metaboliteMapping['base_met_elements']);
                imm_product.metaboliteMapping['base_met_atompositions'].extend(imm.metaboliteMapping['base_met_atompositions']);
                #imm_product.metaboliteMapping['base_met_symmetry_elements'].extend(imm.metaboliteMapping['base_met_symmetry_elements']);
                #imm_product.metaboliteMapping['base_met_symmetry_atompositions'].extend(imm.metaboliteMapping['base_met_symmetry_atompositions']);
                imm_product.metaboliteMapping['base_met_indices'].extend(imm.metaboliteMapping['base_met_indices']); 
                imm.clear_metaboliteMapping();
                reactant_ids_cnt[k]+=1
        # add the products mapping
        if product_id_I:
            # make the compound product mapping
            imm_product.update_trackedMetabolite_fromBaseMetabolites(model_id_I)
            self.reactionMapping['products_elements_tracked'].append(imm_product.metaboliteMapping['met_elements']);
            self.reactionMapping['products_positions_tracked'].append(imm_product.metaboliteMapping['met_atompositions']);
            self.reactionMapping['products_mapping'].append(imm_product.convert_arrayMapping2StringMapping());
            self.reactionMapping['products_stoichiometry_tracked'].append(1.0);
            self.reactionMapping['products_ids_tracked'].append(product_id_I);
            self.reactionMapping['products_metaboliteMappings'].append(copy(imm_product.copy_metaboliteMapping()));
    def add_trackedBinaryReactionReverse_toReaction(self,model_id_I,reactant_id_I,product_ids_elements_I):
        '''Add a binary reaction of the form C = A + B to the current reaction'''
        imm = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        product_ids_all = [];
        for row in product_ids_elements_I:
            for k,v in row.iteritems():
                product_ids_all.append(k);
        #for k in self.reactionMapping['products_ids_tracked']:
        #    product_ids_all.append(k);
        product_ids_unique = list(set(product_ids_all))
        product_ids_cnt = {};
        for product_id in product_ids_unique:
            product_ids_cnt[product_id] = 0;
        # add the product mappings
        for row in product_ids_elements_I:
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(mapping_id_I,model_id_I,{k:v},product_ids_cnt[k]);
                self.reactionMapping['products_elements_tracked'].append(imm.metaboliteMapping['met_elements']);
                self.reactionMapping['products_positions_tracked'].append(imm.metaboliteMapping['met_atompositions']);
                self.reactionMapping['products_mapping'].append(imm.convert_arrayMapping2StringMapping());
                self.reactionMapping['products_stoichiometry_tracked'].append(1.0);
                self.reactionMapping['products_ids_tracked'].append(k);
                self.reactionMapping['products_metaboliteMappings'].append(copy(imm.copy_metaboliteMapping()));
                imm.clear_metaboliteMapping();
                product_ids_cnt[k]+=1
        # add the reactant mapping
        imm.make_compoundTrackedMetabolite(self.reactionMapping['mapping_id'],model_id_I,reactant_ids_elements_I,product_id_I);
        self.reactionMapping['reactants_elements_tracked'].append(imm.metaboliteMapping['met_elements']);
        self.reactionMapping['reactants_positions_tracked'].append(imm.metaboliteMapping['met_atompositions']);
        self.reactionMapping['reactants_mapping'].append(imm.convert_arrayMapping2StringMapping());
        self.reactionMapping['reactants_stoichiometry_tracked'].append(-1.0);
        self.reactionMapping['reactants_ids_tracked'].append(reactant_id_I);
        self.reactionMapping['reactants_metaboliteMappings'].append(copy(imm.copy_metaboliteMapping()));
        imm.clear_metaboliteMapping();
    def add_trackedUnitaryReactions_toReaction(self,model_id_I,reactant_ids_elements_I,product_ids_I):
        #Input
        # reactant_ids_elements_I = [met_id:{elements=[string,...],stoichiometry:float}},..]
        # product_ids_elements_I = [met_id,...]

        # check input
        if len(reactant_ids_elements_I)!=len(product_ids_I):
            print "length of reactants_ids does not match the length of products_ids";
            return;
        imm = stage02_isotopomer_metaboliteMapping();
        imm_product = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        reactant_ids_all = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                reactant_ids_all.append(k);
        for k in self.reactionMapping['reactants_ids_tracked']:
            reactant_ids_all.append(k);
        reactant_ids_unique = list(set(reactant_ids_all))
        reactant_ids_cnt = {};
        for reactant_id in reactant_ids_unique:
            reactant_ids_cnt[reactant_id] = 0;
        # get all reactants_base_met_ids and reactants_base_indices:
        reactants_base_met_ids = [];
        reactants_base_indices = [];
        for cnt,mm in enumerate(self.reactionMapping['reactants_metaboliteMappings']):
            reactants_base_met_ids.extend(mm.metaboliteMapping['base_met_ids'])
            reactants_base_indices.extend(self.reactionMapping['reactants_metaboliteMappings'][cnt].metaboliteMapping['base_met_indices'])
        reactants_base_met_ids_I = [];
        # get unique reactants_base_met_ids
        reactants_base_met_ids_unique = list(set(reactants_base_met_ids));
        reactants_base_met_ids_cnt = {};
        for base_met_id in reactants_base_met_ids_unique:
            reactants_base_met_ids_cnt[base_met_id]=0;
        for cnt,base_met_id in enumerate(reactants_base_met_ids):
            reactants_base_met_ids_cnt[base_met_id]=reactants_base_indices[cnt]+1
        # make the reactants mapping
        imm_product.metaboliteMapping['mapping_id'] = self.reactionMapping['mapping_id']
        imm_product.metaboliteMapping['base_met_ids']=[];
        imm_product.metaboliteMapping['base_met_elements']=[];
        imm_product.metaboliteMapping['base_met_atompositions']=[];
        imm_product.metaboliteMapping['base_met_symmetry_elements']=[];
        imm_product.metaboliteMapping['base_met_symmetry_atompositions']=[];
        imm_product.metaboliteMapping['base_met_indices']=[];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(self.reactionMapping['mapping_id'],model_id_I,{k:v},reactant_ids_cnt[k]);
                # check that there are no duplicate met_id/met_index pairs
                duplicates_found=False;
                met_id_duplicate_found=[];
                for cnt1,met_id1 in enumerate(imm.metaboliteMapping['base_met_ids']): # the current base_met_ids
                    for cnt2,met_id2 in enumerate(reactants_base_met_ids + imm_product.metaboliteMapping['base_met_ids']): # reactant base_met_ids that are already a part of the reaction + 
                                                                                                                           # base_met_ids that will be added to the reaction
                        if met_id1==met_id2 and imm.metaboliteMapping['base_met_indices'][cnt1]==(reactants_base_indices + imm_product.metaboliteMapping['base_met_indices'])[cnt2]:
                                                                            #the base_met_ids match and the base_indices_match
                                                                            #need to increase the base_index +1 over the current index
                            imm.metaboliteMapping['base_met_indices'][cnt1]=reactants_base_met_ids_cnt[met_id1];
                            duplicates_found=True
                            met_id_duplicate_found.append(met_id1)
                # update met_mapping
                imm.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
                if duplicates_found: 
                    for k2 in met_id_duplicate_found:
                        reactants_base_met_ids_cnt[k2]+=1;
                self.reactionMapping['reactants_elements_tracked'].append(imm.metaboliteMapping['met_elements']);
                self.reactionMapping['reactants_positions_tracked'].append(imm.metaboliteMapping['met_atompositions']);
                self.reactionMapping['reactants_mapping'].append(imm.convert_arrayMapping2StringMapping());
                self.reactionMapping['reactants_stoichiometry_tracked'].append(-abs(1));
                self.reactionMapping['reactants_ids_tracked'].append(k);
                self.reactionMapping['reactants_metaboliteMappings'].append(copy(imm.copy_metaboliteMapping()));
                # copy out all of the base information
                imm_product.metaboliteMapping['base_met_ids'].extend(imm.metaboliteMapping['base_met_ids']);
                imm_product.metaboliteMapping['base_met_elements'].extend(imm.metaboliteMapping['base_met_elements']);
                imm_product.metaboliteMapping['base_met_atompositions'].extend(imm.metaboliteMapping['base_met_atompositions']);
                #imm_product.metaboliteMapping['base_met_symmetry_elements'].extend(imm.metaboliteMapping['base_met_symmetry_elements']);
                #imm_product.metaboliteMapping['base_met_symmetry_atompositions'].extend(imm.metaboliteMapping['base_met_symmetry_atompositions']);
                imm_product.metaboliteMapping['base_met_indices'].extend(imm.metaboliteMapping['base_met_indices']); 
                imm.clear_metaboliteMapping();
                reactant_ids_cnt[k]+=1
        # make the products mapping
        for product_cnt,product in enumerate(product_ids_I):
            self.reactionMapping['products_elements_tracked'].append(self.reactionMapping['reactants_elements_tracked'][product_cnt+len(self.reactionMapping['reactants_elements_tracked'])-len(product_ids_I)]);
            self.reactionMapping['products_positions_tracked'].append(self.reactionMapping['reactants_positions_tracked'][product_cnt+len(self.reactionMapping['reactants_positions_tracked'])-len(product_ids_I)]);
            self.reactionMapping['products_mapping'].append(self.reactionMapping['reactants_mapping'][product_cnt+len(self.reactionMapping['reactants_mapping'])-len(product_ids_I)]);
            self.reactionMapping['products_stoichiometry_tracked'].append(abs(self.reactionMapping['reactants_stoichiometry_tracked'][product_cnt+len(self.reactionMapping['reactants_stoichiometry_tracked'])-len(product_ids_I)]));
            self.reactionMapping['products_ids_tracked'].append(product);
            imm_tmp = self.reactionMapping['reactants_metaboliteMappings'][product_cnt+len(self.reactionMapping['reactants_metaboliteMappings'])-len(product_ids_I)].copy_metaboliteMapping();
            imm_tmp.metaboliteMapping['met_id']=product; # change the name
            self.reactionMapping['products_metaboliteMappings'].append(imm_tmp);
    def add_trackedCompoundReaction_toReaction(self,model_id_I,reactant_ids_elements_I,base_reactant_positions_I,base_reactant_indices_I,compound_product_id_I,base_product_ids_elements_I,base_product_ids_O):
        '''Make a compound tracked reaction
        1. make compound product
        2. remove specified base products from compound product
        3. update the compound product
        4. rename the base products
        5. append base products to products list'''

        #Input
        # reactant_ids_elements_I = [{met_id:elements},...]
        # base_reactant_positions_I = [{met_id_reactant:position},...] #Note: must be listed in order (positions of the reactant to be partitioned)
        # base_reactant_indices_I = [{met_id_product:position in base_reactants_ids},...] #Note: must be listed in order (positions of the reactant to be partitioned)
        # compound_product_id_I = met_id
        # base_product_ids_elements_I = [{met_id:elements},...] #Note: must be listed in order
        # base_product_ids_O = [met_id_new,...] #Note: must be listed in order

        imm = stage02_isotopomer_metaboliteMapping();
        imm_product = stage02_isotopomer_metaboliteMapping();
        # get unique met_ids
        reactant_ids_all = [];
        for row in reactant_ids_elements_I:
            for k,v in row.iteritems():
                reactant_ids_all.append(k);
        for k in self.reactionMapping['reactants_ids_tracked']:
            reactant_ids_all.append(k);
        reactant_ids_unique = list(set(reactant_ids_all))
        reactant_ids_cnt = {};
        for reactant_id in reactant_ids_unique:
            reactant_ids_cnt[reactant_id] = 0;
        # get all reactants_base_met_ids and reactants_base_indices:
        reactants_base_met_ids = [];
        reactants_base_indices = [];
        for cnt,mm in enumerate(self.reactionMapping['reactants_metaboliteMappings']):
            reactants_base_met_ids.extend(mm.metaboliteMapping['base_met_ids'])
            reactants_base_indices.extend(self.reactionMapping['reactants_metaboliteMappings'][cnt].metaboliteMapping['base_met_indices'])
        reactants_base_met_ids_I = [];
        for row in base_reactant_indices_I:
            for k,v in row.iteritems():
                reactants_base_met_ids_I.append(k)
        # get unique reactants_base_met_ids
        reactants_base_met_ids_unique = list(set(reactants_base_met_ids+reactants_base_met_ids_I));
        reactants_base_met_ids_cnt = {};
        for base_met_id in reactants_base_met_ids_unique:
            reactants_base_met_ids_cnt[base_met_id]=0;
        for cnt,base_met_id in enumerate(reactants_base_met_ids):
            reactants_base_met_ids_cnt[base_met_id]=reactants_base_indices[cnt]+1
        # make the reactants mapping
        reactants_stoichiometry_tracked_O = [];
        reactants_ids_tracked_O = [];
        reactants_elements_tracked_O = [];
        reactants_positions_tracked_O = [];
        reactants_mapping_O = [];
        reactants_metaboliteMappings_O = [];
        imm_product.metaboliteMapping['mapping_id'] = self.reactionMapping['mapping_id']
        imm_product.metaboliteMapping['base_met_ids']=[];
        imm_product.metaboliteMapping['base_met_elements']=[];
        imm_product.metaboliteMapping['base_met_atompositions']=[];
        imm_product.metaboliteMapping['base_met_symmetry_elements']=[];
        imm_product.metaboliteMapping['base_met_symmetry_atompositions']=[];
        imm_product.metaboliteMapping['base_met_indices']=[];
        matched_cnt = 0;      
        for row_cnt,row in enumerate(reactant_ids_elements_I):
            for k,v in row.iteritems():
                imm.make_trackedMetabolite(self.reactionMapping['mapping_id'],model_id_I,{k:v},reactant_ids_cnt[k]);
                # update base_metabolites from the database for reactant that will be partitioned
                base_found=False;
                if matched_cnt < len(base_reactant_positions_I):
                    for k1,v1 in base_reactant_positions_I[matched_cnt].iteritems(): #there will be only 1 key-value pair
                        if k1 == k and row_cnt == v1:
                            imm.get_baseMetabolites();
                            imm.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
                            base_found=True;
                            break;
                # check that there are no duplicate met_id/met_index pairs
                duplicates_found=False;
                met_id_duplicate_found=[];
                for cnt1,met_id1 in enumerate(imm.metaboliteMapping['base_met_ids']): # the current base_met_ids
                    for cnt2,met_id2 in enumerate(reactants_base_met_ids + imm_product.metaboliteMapping['base_met_ids']): # reactant base_met_ids that are already a part of the reaction + 
                                                                                                                           # base_met_ids that will be added to the reaction
                        if met_id1==met_id2 and imm.metaboliteMapping['base_met_indices'][cnt1]==(reactants_base_indices + imm_product.metaboliteMapping['base_met_indices'])[cnt2]:
                                                                            #the base_met_ids match and the base_indices_match
                                                                            #need to increase the base_index +1 over the current index
                            imm.metaboliteMapping['base_met_indices'][cnt1]=reactants_base_met_ids_cnt[met_id1];
                            duplicates_found=True
                            met_id_duplicate_found.append(met_id1)
                # update the base_reactant_indices_I if the corresponding base_met_index was changed
                if matched_cnt < len(base_reactant_positions_I):
                    for k1,v1 in base_reactant_positions_I[matched_cnt].iteritems(): #there will be only 1 key-value pair
                        if k1 == k and row_cnt == v1:
                            for k2,v2 in base_reactant_indices_I[matched_cnt].iteritems():
                                for cnt1,met_id1 in enumerate(imm.metaboliteMapping['base_met_ids']):
                                    if k2==met_id1:
                                        base_reactant_indices_I[matched_cnt][k2]=imm.metaboliteMapping['base_met_indices'][cnt1];
                # update counter for matched input
                if base_found: matched_cnt+=1;
                # update met_mapping
                imm.update_trackedMetabolite_fromBaseMetabolites(model_id_I);
                if duplicates_found: 
                    for k2 in met_id_duplicate_found:
                        reactants_base_met_ids_cnt[k2]+=1;
                reactants_elements_tracked_O.append(imm.metaboliteMapping['met_elements']);
                reactants_positions_tracked_O.append(imm.metaboliteMapping['met_atompositions']);
                reactants_mapping_O.append(imm.convert_arrayMapping2StringMapping());
                reactants_stoichiometry_tracked_O.append(-1.0);
                reactants_ids_tracked_O.append(k);
                # copy out all of the base information
                imm_product.metaboliteMapping['base_met_ids'].extend(imm.metaboliteMapping['base_met_ids']);
                imm_product.metaboliteMapping['base_met_elements'].extend(imm.metaboliteMapping['base_met_elements']);
                imm_product.metaboliteMapping['base_met_atompositions'].extend(imm.metaboliteMapping['base_met_atompositions']);
                #imm_product.metaboliteMapping['base_met_symmetry_elements'].extend(imm.metaboliteMapping['base_met_symmetry_elements']);
                #imm_product.metaboliteMapping['base_met_symmetry_atompositions'].extend(imm.metaboliteMapping['base_met_symmetry_atompositions']);
                imm_product.metaboliteMapping['base_met_indices'].extend(imm.metaboliteMapping['base_met_indices']); 
                #
                reactants_metaboliteMappings_O.append(copy(imm.copy_metaboliteMapping()));  
                imm.clear_metaboliteMapping()
                reactant_ids_cnt[k]+=1
        # make the initial compound product mapping
        imm_product.update_trackedMetabolite_fromBaseMetabolites(model_id_I)
        # extract out the products from the compound product
        base_products = [];
        for cnt,row in enumerate(base_product_ids_elements_I):
            for k,v in row.iteritems():
                base_products.append(imm_product.extract_baseMetabolite_fromMetabolite(model_id_I,{k:v},base_reactant_indices_I[cnt][k]));
        # remove the base_products from the compound product
        for cnt,row in enumerate(base_product_ids_elements_I):
            for k,v in row.iteritems():
                imm_product.remove_baseMetabolite_fromMetabolite(model_id_I,{k:v},met_id_O=compound_product_id_I,met_index_I=base_reactant_indices_I[cnt][k]);
        # make the final products
        if compound_product_id_I: imm_final_products = [imm_product];
        else: imm_final_products = [];
        for d in base_products:
            imm_final_products.append(d);
        if compound_product_id_I: imm_final_products_ids = [compound_product_id_I];
        else: imm_final_products_ids = [];
        for id in base_product_ids_O:
            imm_final_products_ids.append(id);
        products_stoichiometry_tracked_O = [];
        products_ids_tracked_O = [];
        products_elements_tracked_O = [];
        products_positions_tracked_O = [];
        products_mapping_O = [];
        products_metaboliteMappings_O = [];
        for cnt,d in enumerate(imm_final_products):
            products_elements_tracked_O.append(d.metaboliteMapping['met_elements']);
            products_positions_tracked_O.append(d.metaboliteMapping['met_atompositions']);
            products_mapping_O.append(d.convert_arrayMapping2StringMapping());
            products_stoichiometry_tracked_O.append(1.0);
            products_ids_tracked_O.append(imm_final_products_ids[cnt]);
            products_metaboliteMappings_O.append(copy(d.copy_metaboliteMapping()));
        # save the reaction
        self.reactionMapping['reactants_stoichiometry_tracked'].extend(reactants_stoichiometry_tracked_O)
        self.reactionMapping['products_stoichiometry_tracked'].extend(products_stoichiometry_tracked_O)
        self.reactionMapping['reactants_ids_tracked'].extend(reactants_ids_tracked_O)
        self.reactionMapping['products_ids_tracked'].extend(products_ids_tracked_O)
        self.reactionMapping['reactants_elements_tracked'].extend(reactants_elements_tracked_O)
        self.reactionMapping['products_elements_tracked'].extend(products_elements_tracked_O)
        self.reactionMapping['reactants_positions_tracked'].extend(reactants_positions_tracked_O)
        self.reactionMapping['products_positions_tracked'].extend(products_positions_tracked_O)
        self.reactionMapping['reactants_mapping'].extend(reactants_mapping_O)
        self.reactionMapping['products_mapping'].extend(products_mapping_O)
        self.reactionMapping['reactants_metaboliteMappings'].extend(reactants_metaboliteMappings_O)
        self.reactionMapping['products_metaboliteMappings'].extend(products_metaboliteMappings_O)
    def add_reactionMapping(self,
            mapping_id_I=None,
            rxn_id_I=None,
            rxn_description_I=None,
            reactants_stoichiometry_tracked_I=[],
            products_stoichiometry_tracked_I=[],
            reactants_ids_tracked_I=[],
            products_ids_tracked_I=[],
            reactants_elements_tracked_I=[],
            products_elements_tracked_I=[],
            reactants_positions_tracked_I=[],
            products_positions_tracked_I=[],
            reactants_mapping_I=[],
            products_mapping_I=[],
            rxn_equation_I=None,
            used__I=None,
            comment__I=None):
        
        if mapping_id_I: self.reactionMapping['mapping_id']=mapping_id_I
        if rxn_id_I: self.reactionMapping['rxn_id']=rxn_id_I
        if rxn_description_I: self.reactionMapping['rxn_description']=rxn_description_I
        if reactants_stoichiometry_tracked_I: self.reactionMapping['reactants_stoichiometry_tracked']=reactants_stoichiometry_tracked_I
        if products_stoichiometry_tracked_I: self.reactionMapping['products_stoichiometry_tracked']=products_stoichiometry_tracked_I
        if reactants_ids_tracked_I: self.reactionMapping['reactants_ids_tracked']=reactants_ids_tracked_I
        if products_ids_tracked_I: self.reactionMapping['products_ids_tracked']=products_ids_tracked_I
        if reactants_elements_tracked_I: self.reactionMapping['reactants_elements_tracked']=reactants_elements_tracked_I
        if products_elements_tracked_I: self.reactionMapping['products_elements_tracked']=products_elements_tracked_I
        if reactants_positions_tracked_I: self.reactionMapping['reactants_positions_tracked']=reactants_positions_tracked_I
        if products_positions_tracked_I: self.reactionMapping['products_positions_tracked']=products_positions_tracked_I
        if reactants_mapping_I: self.reactionMapping['reactants_mapping']=reactants_mapping_I
        if products_mapping_I: self.reactionMapping['products_mapping']=products_mapping_I
        if rxn_equation_I: self.reactionMapping['rxn_equation']=rxn_equation_I
        if used__I: self.reactionMapping['used_']=used__I
        if comment__I: self.reactionMapping['comment_']=comment__I
        # add data to the database
        self.stage02_isotopomer_query.add_data_dataStage02IsotopomerAtomMappingReactions([self.reactionMapping])
    def add_productMapping(self,product_ids_I):
        '''Add newly made products to the atomMappingMetabolite table for future use'''
        for product in self.reactionMapping['products_metaboliteMappings']:
            if product.metaboliteMapping['met_id'] in product_ids_I:
                product.add_metaboliteMapping();
    def update_productMapping(self,product_ids_I):
        '''Update newly made products to the atomMappingMetabolite table for future use'''
        for product in self.reactionMapping['products_metaboliteMappings']:
            if product.metaboliteMapping['met_id'] in product_ids_I:
                product.update_metaboliteMapping();
    def update_reactionMapping(self,
            mapping_id_I=None,
            rxn_id_I=None,
            rxn_description_I=None,
            reactants_stoichiometry_tracked_I=[],
            products_stoichiometry_tracked_I=[],
            reactants_ids_tracked_I=[],
            products_ids_tracked_I=[],
            reactants_elements_tracked_I=[],
            products_elements_tracked_I=[],
            reactants_positions_tracked_I=[],
            products_positions_tracked_I=[],
            reactants_mapping_I=[],
            products_mapping_I=[],
            rxn_equation_I=None,
            used__I=None,
            comment__I=None):
        
        if mapping_id_I: self.reactionMapping['mapping_id']=mapping_id_I
        if rxn_id_I: self.reactionMapping['rxn_id']=rxn_id_I
        if rxn_description_I: self.reactionMapping['rxn_description']=rxn_description_I
        if reactants_stoichiometry_tracked_I: self.reactionMapping['reactants_stoichiometry_tracked']=reactants_stoichiometry_tracked_I
        if products_stoichiometry_tracked_I: self.reactionMapping['products_stoichiometry_tracked']=products_stoichiometry_tracked_I
        if reactants_ids_tracked_I: self.reactionMapping['reactants_ids_tracked']=reactants_ids_tracked_I
        if products_ids_tracked_I: self.reactionMapping['products_ids_tracked']=products_ids_tracked_I
        if reactants_elements_tracked_I: self.reactionMapping['reactants_elements_tracked']=reactants_elements_tracked_I
        if products_elements_tracked_I: self.reactionMapping['products_elements_tracked']=products_elements_tracked_I
        if reactants_positions_tracked_I: self.reactionMapping['reactants_positions_tracked']=reactants_positions_tracked_I
        if products_positions_tracked_I: self.reactionMapping['products_positions_tracked']=products_positions_tracked_I
        if reactants_mapping_I: self.reactionMapping['reactants_mapping']=reactants_mapping_I
        if products_mapping_I: self.reactionMapping['products_mapping']=products_mapping_I
        if rxn_equation_I: self.reactionMapping['rxn_equation']=rxn_equation_I
        if used__I: self.reactionMapping['used_']=used__I
        if comment__I: self.reactionMapping['comment_']=comment__I
        self.stage02_isotopomer_query.update_rows_dataStage02IsotopomerAtomMappingReactions([self.reactionMapping]);
    def get_reactionMapping(self,mapping_id_I,rxn_id_I):
        row = {};
        row = self.stage02_isotopomer_query.get_row_mappingIDAndRxnID_dataStage02IsotopomerAtomMappingReactions(mapping_id_I,rxn_id_I);
        self.reactionMapping = row;
        self.reactionMapping['reactants_metaboliteMappings']=[]
        self.reactionMapping['products_metaboliteMappings']=[]
    def clear_reactionMapping(self):
        self.reactionMapping = {};
    def checkAndCorrect_elementsAndPositions(self):
        '''Check that the reactant/product elements/positions are consistent with the
        reactants/products ids_tracked; if they are not, correct them'''
        # check that elements/positions are initialized
        if not self.reactionMapping['reactants_elements_tracked']:
            self.reactionMapping['reactants_elements_tracked']=[];
            for cnt,reactant_id in enumerate(self.reactionMapping['reactants_ids_tracked']):
                self.reactionMapping['reactants_elements_tracked'].append([]);
        if not self.reactionMapping['reactants_positions_tracked']:
            self.reactionMapping['reactants_positions_tracked']=[];
            for cnt,reactant_id in enumerate(self.reactionMapping['reactants_ids_tracked']):
                self.reactionMapping['reactants_positions_tracked'].append([]);
        # check that the length of the elements/positions match the length of the ids_tracked
        #TODO...
        # check each elements/positions
        for cnt,reactant_id in enumerate(self.reactionMapping['reactants_ids_tracked']):
            # get the metabolite data from the database
            met_data = {}
            met_data = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(self.reactionMapping['mapping_id'],reactant_id);
            if len(met_data['met_elements'])!=len(self.reactionMapping['reactants_elements_tracked'][cnt]):
                self.reactionMapping['reactants_elements_tracked'][cnt]=met_data['met_elements'];
            if len(met_data['met_atompositions'])!=len(self.reactionMapping['reactants_positions_tracked'][cnt]):
                self.reactionMapping['reactants_positions_tracked'][cnt]=met_data['met_atompositions'];
        # check that elements/positions are initialized
        if not self.reactionMapping['products_elements_tracked']:
            self.reactionMapping['products_elements_tracked']=[];
            for cnt,product_id in enumerate(self.reactionMapping['products_ids_tracked']):
                self.reactionMapping['products_elements_tracked'].append([]);
        if not self.reactionMapping['products_positions_tracked']:
            self.reactionMapping['products_positions_tracked']=[];
            for cnt,product_id in enumerate(self.reactionMapping['products_ids_tracked']):
                self.reactionMapping['products_positions_tracked'].append([]);
        # check that the length of the elements/positions match the length of the ids_tracked
        #TODO...
        # check each elements/positions
        for cnt,product_id in enumerate(self.reactionMapping['products_ids_tracked']):
            # get the metabolite data from the database
            met_data = {}
            met_data = self.stage02_isotopomer_query.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(self.reactionMapping['mapping_id'],product_id);
            if len(met_data['met_elements'])!=len(self.reactionMapping['products_elements_tracked'][cnt]):
                self.reactionMapping['products_elements_tracked'][cnt]=met_data['met_elements'];
            if len(met_data['met_atompositions'])!=len(self.reactionMapping['products_positions_tracked'][cnt]):
                self.reactionMapping['products_positions_tracked'][cnt]=met_data['met_atompositions'];
    #def checkAndCorrect_baseMetPositions(self,imm_I,base_reactant_indices_I):
    #    '''Check that the new base_met_id/index pairs are unique'''
    #    # Step 1:
    #    # get all reactants_base_met_ids and reactants_base_indices:
    #    reactants_base_met_ids = [];
    #    reactants_base_indices = [];
    #    for cnt,mm in enumerate(self.reactionMapping['reactants_metaboliteMappings']):
    #        reactants_base_met_ids.extend(mm.metaboliteMapping['base_met_ids'])
    #        reactants_base_indices.extend(self.reactionMapping['reactants_metaboliteMappings'][cnt].metaboliteMapping['base_met_indices'])
    #    reactants_base_met_ids_I = [];
    #    for row in base_reactant_indices_I:
    #        for k,v in row.iteritems():
    #            reactants_base_met_ids_I.append(k)
    #    # get unique reactants_base_met_ids
    #    reactants_base_met_ids_unique = list(set(reactants_base_met_ids+reactants_base_met_ids_I));
    #    reactants_base_met_ids_cnt = {};
    #    for base_met_id in reactants_base_met_ids_unique:
    #        reactants_base_met_ids_cnt[base_met_id]=0;
    #    # set reactants_base_met_indices to the next value
    #    for cnt,base_met_id in enumerate(reactants_base_met_ids):
    #        reactants_base_met_ids_cnt[base_met_id]=reactants_base_indices[cnt]+1
    #    # Step 2:
    #    # update reactants_base_met_ids_cnt to account for any new base_met_ids that are in the input metaboliteMapping
    #    base_met_ids_cnt_all_tmp=[];
    #    for cnt,base_met_id in enumerate(imm_I.metaboliteMapping['base_met_ids']):
    #        base_met_ids_cnt_all_tmp.append(base_met_id);
    #    base_met_ids_cnt_unqiue_tmp=list(set(base_met_ids_cnt_all_tmp));
    #    base_met_ids_cnt_tmp = {};
    #    for base_met_id in base_met_ids_cnt_unqiue_tmp:
    #        base_met_ids_cnt_tmp[base_met_id] = 0;
    #    for cnt,base_met_id in enumerate(imm_I.metaboliteMapping['base_met_ids']):
    #        if imm_I.metaboliteMapping['base_met_indices'][cnt]>=base_met_ids_cnt_tmp[base_met_id]:
    #            base_met_ids_cnt_tmp[base_met_id] = imm_I.metaboliteMapping['base_met_indices'][cnt]+1; 
    #    for cnt,base_met_id in enumerate(imm_I.metaboliteMapping['base_met_ids']):
    #        if not base_met_id in reactants_base_met_ids_cnt.keys():

        

'''Unit tests for stage02_isotopomer_metaboliteMapping:
from analysis.analysis_stage02_isotopomer.stage02_isotopomer_dependencies import stage02_isotopomer_metaboliteMapping
imm = stage02_isotopomer_metaboliteMapping()
imm.make_trackedMetabolite('full04','140407_iDM2014',{'f6p_c':'C'})
imm.clear_metaboliteMapping()
imm.make_compoundTrackedMetabolite('full04','140407_iDM2014',[{'f6p_c':'C'},{'f6p_c':'H'},{'f6p_c':'C'},{'f6p_c':'H'},{'ac_c':'C'},{'utp_c':'C'}],'uacgam_c')
imm.remove_baseMetabolite_fromMetabolite('140407_iDM2014',{'f6p_c':'C'})
imm.clear_metaboliteMapping()
imm.make_compoundTrackedMetabolite('full04','140407_iDM2014',[{'f6p_c':'C'},{'f6p_c':'H'},{'f6p_c':'C'},{'f6p_c':'H'},{'ac_c':'C'},{'utp_c':'C'}],'uacgam_c')
imm.remove_baseMetabolite_fromMetabolite('140407_iDM2014',{'f6p_c':'C'},met_index_I=2)
imm.clear_metaboliteMapping()
imm.make_compoundTrackedMetabolite('full04','140407_iDM2014',[{'f6p_c':'C'},{'f6p_c':'H'},{'f6p_c':'C'},{'f6p_c':'H'},{'ac_c':'C'},{'utp_c':'C'}],'uacgam_c')
imm.pop_baseMetabolite_fromMetabolite('140407_iDM2014',{'f6p_c':'C'})
imm.clear_metaboliteMapping()
imm.make_compoundTrackedMetabolite('full04','140407_iDM2014',[{'f6p_c':'C'},{'f6p_c':'H'},{'f6p_c':'C'},{'f6p_c':'H'},{'ac_c':'C'},{'utp_c':'C'}],'uacgam_c')
extracted_imm = imm.extract_baseMetabolite_fromMetabolite('140407_iDM2014',{'f6p_c':'C'},met_index_I=2)
imm.clear_metaboliteMapping()
'''

'''Unit tests for stage02_isotopomer_reactionMapping:
from analysis.analysis_stage02_isotopomer.stage02_isotopomer_dependencies import stage02_isotopomer_reactionMapping
irm = stage02_isotopomer_reactionMapping()
irm.make_trackedBinaryReaction('full04','140407_iDM2014','COFACTOR_7',[{'dxyl5p_c':'C'}],'h2mb4p_c')
irm.clear_reactionMapping()
irm.make_trackedBinaryReaction('full04','140407_iDM2014','COFACTOR_7',[{'dxyl5p_c':'C'},{'dxyl5p_c':'C'}],'h2mb4p_c')
irm.clear_reactionMapping()
irm.make_trackedUnitaryReactions('full04','140407_iDM2014','COFACTOR_7',[{'dxyl5p_c':'C'}],['h2mb4p_c'])
irm.clear_reactionMapping()
irm.make_trackedUnitaryReactions('full04','140407_iDM2014','COFACTOR_7',[{'dxyl5p_c':'C'},{'dxyl5p_c':'C'}],['h2mb4p_c','h2mb4p_c'])
irm.clear_reactionMapping()
'''