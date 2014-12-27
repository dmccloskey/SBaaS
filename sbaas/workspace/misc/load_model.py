# Dependencies
import operator, json, csv
# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file
from cobra.io.sbml import write_cobra_model_to_sbml_file
from cobra.io.mat import save_matlab_model
from cobra.manipulation.modify import convert_to_irreversible, revert_to_reversible
from cobra.flux_analysis.objective import update_objective
from cobra.core.Reaction import Reaction
from cobra.core.Metabolite import Metabolite


def load_ALEWt(anoxic = False):
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
    ammoniaExcess = ['GLUDy'];
    aerobic = ['RNDR1', 'RNDR2', 'RNDR3', 'RNDR4', 'DHORD2', 'ASPO6','LCARR'];
    anaerobic = ['RNTR1c2', 'RNTR2c2', 'RNTR3c2', 'RNTR4c2', 'DHORD5', 'ASPO5'];
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
    fattyAcidSynthesis = ['ACCOAC', 'ACOATA', 'HACD1', 'HACD2', 'HACD3', 'HACD4', 'HACD5', 'HACD6', 'HACD7', 'HACD8', 'KAS14', 'KAS15', 'MACPD', 'MCOATA', '3OAR100', '3OAR120', '3OAR121', '3OAR140', '3OAR141', '3OAR160', '3OAR161', '3OAR180', '3OAR181', '3OAR40', '3OAR60', '3OAR80']
    fattyAcidOxidation = ['ACACT1r', 'ACACT2r', 'ACACT3r', 'ACACT4r', 'ACACT5r', 'ACACT6r', 'ACACT7r', 'ACACT8r', 'ACOAD1f', 'ACOAD2f', 'ACOAD3f', 'ACOAD4f', 'ACOAD5f', 'ACOAD6f', 'ACOAD7f', 'ACOAD8f', 'CTECOAI6', 'CTECOAI7', 'CTECOAI8', 'ECOAH1', 'ECOAH2', 'ECOAH3', 'ECOAH4', 'ECOAH5', 'ECOAH6', 'ECOAH7', 'ECOAH8']
    ndpk = ['NDPK1','NDPK2','NDPK3','NDPK4','NDPK5','NDPK7','NDPK8'];
    rxnList = fattyAcidSynthesis + fattyAcidOxidation;
    for rxn in rxnList:
        cobra_model.reactions.get_by_id(rxn).lower_bound = 0.0;
        cobra_model.reactions.get_by_id(rxn).upper_bound = 1000.0;

    return cobra_model;