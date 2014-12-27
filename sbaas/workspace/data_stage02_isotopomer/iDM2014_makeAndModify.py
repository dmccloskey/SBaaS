from analysis.analysis_stage02_isotopomer.iterations import isotopomer_model_iteration3

def make_WT():
    ## WT
    isotopomer_model_iteration3(\
    'data\\iteration2_140407_ijo1366_netrxn_irreversible.xml',\
    'data\\iteration3_140407_iDMisotopomer.xml',\
    'data\\iteration3_140407_iDMisotopomer.mat',\
    'data\\iteration3_140407_iDMisotopomer.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    []);

def make_proteogenicAAcomparison():
    # proteogenicAAcomparison
    # WT 
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.44,'ub':0.44};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':3.5,'ub':3.5};
    #flux_dict['EX_lac_DASH_L_LPAREN_e_RPAREN_'] = {'lb':0.4,'ub':0.4}; #breaks the model
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':14.9,'ub':14.9};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-9.0,'ub':-9.0};
    #flux_dict['ATPM'] = {'lb':7.6,'ub':7.6};
    isotopomer_model_iteration3(\
    'data\\iteration3\\iteration3_140407_iDMisotopomer.xml',\
    'data\\iteration3_140430_iDMisotopomer_proteogenicAAcomparison_WT.xml',\
    'data\\iteration3_140430_iDMisotopomer_proteogenicAAcomparison_WT.mat',\
    'data\\iteration3_140430_iDMisotopomer_proteogenicAAcomparison_WT.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_proteogenicAAcomparison_WT');

def make_proteogenicAAcomparison_centralMets():
    # proteogenicAAcomparison
    # WT 
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.44,'ub':0.44};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':3.5,'ub':3.5};
    #flux_dict['EX_lac_DASH_L_LPAREN_e_RPAREN_'] = {'lb':0.4,'ub':0.4}; #breaks the model
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':14.9,'ub':14.9};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-9.0,'ub':-9.0};
    #flux_dict['ATPM'] = {'lb':7.6,'ub':7.6};
    isotopomer_model_iteration3(\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_proteogenicAAcomparison_WT.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_proteogenicAAcomparison_WT.mat',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_proteogenicAAcomparison_WT.csv',\
    'data\\iteration3_140601_centralMets\\isotopomer_mapping_140528_centralMets.csv',\
    ko_list,flux_dict,'iDM2014_proteogenicAAcomparison_WT');

def make_Toya2010comparison():
    # Toya2010comparison
    # WT 
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.7,'ub':0.7};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':3.0,'ub':3.0};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-11.0,'ub':-11.0};
    isotopomer_model_iteration3(\
    'data\\iteration3\\iteration3_140407_iDMisotopomer.xml',\
    'data\\iteration3_140430_iDMisotopomer_Toya2010comparison_WT.xml',\
    'data\\iteration3_140430_iDMisotopomer_Toya2010comparison_WT.mat',\
    'data\\iteration3_140430_iDMisotopomer_Toya2010comparison_WT.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_Toya2010comparison_WT');
    # delta_PGI
    ko_list = ['PGI','PGI_reverse'];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.2,'ub':0.2};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':0.25,'ub':0.25};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-3.5,'ub':-3.5};
    isotopomer_model_iteration3(\
    'data\\iteration3\\iteration3_140407_iDMisotopomer.xml',\
    'data\\iteration3_140423_iDMisotopomer_Toya2010comparison_PGI.xml',\
    'data\\iteration3_140423_iDMisotopomer_Toya2010comparison_PGI.mat',\
    'data\\iteration3_140423_iDMisotopomer_Toya2010comparison_PGI.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_Toya2010comparison_PGI');
    # delta_PYK
    ko_list = ['PYK'];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.7,'ub':0.7};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':3.0,'ub':3.0};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-11.0,'ub':-11.0};
    isotopomer_model_iteration3(\
    'data\\iteration3\\iteration3_140407_iDMisotopomer.xml',\
    'data\\iteration3_140423_iDMisotopomer_Toya2010comparison_PYK.xml',\
    'data\\iteration3_140423_iDMisotopomer_Toya2010comparison_PYK.mat',\
    'data\\iteration3_140423_iDMisotopomer_Toya2010comparison_PYK.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_Toya2010comparison_PYK');

def make_Toya2010comparison_centralMets():
    # Toya2010comparison
    # WT 
    ko_list = [];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.7,'ub':0.7};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':3.0,'ub':3.0};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-11.0,'ub':-11.0};
    isotopomer_model_iteration3(\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_WT.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_WT.mat',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_WT.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_Toya2010comparison_WT');
    # delta_PGI
    ko_list = ['PGI','PGI_reverse'];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.2,'ub':0.2};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':0.25,'ub':0.25};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-3.5,'ub':-3.5};
    isotopomer_model_iteration3(\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_PGI.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_PGI.mat',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_PGI.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_Toya2010comparison_PGI');
    # delta_PYK
    ko_list = ['PYK'];
    flux_dict = {};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.7,'ub':0.7};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':3.0,'ub':3.0};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-11.0,'ub':-11.0};
    isotopomer_model_iteration3(\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_PYK.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_PYK.mat',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_Toya2010comparison_PYK.csv',\
    'data\\iteration3\\isotopomer_mapping_140415.csv',\
    ko_list,flux_dict,'iDM2014_Toya2010comparison_PYK');

def make_WTEColi_113C80_U13C20_01():
    # WTEColi_113C80_U13C20_01
    # WT 
    ko_list = [];
    flux_dict = {};
    #flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.61*0.9,'ub':0.61*1.1};
    #flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.721-0.5,'ub':2.721+0.5};
    #flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    #flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.54-1.23,'ub':-7.54+1.23};
    #flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.696,'ub':0.712};
    #flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':1.63,'ub':2.63};
    #flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    #flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.6,'ub':-7.2};
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.4*1.1,'ub':-7.4*0.9};
    isotopomer_model_iteration3(\
    'data\\iteration3\\iteration3_140407_iDMisotopomer.xml',\
    'data\\iteration3_140527_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.xml',\
    'data\\iteration3_140527_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.mat',\
    'data\\iteration3_140527_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.csv',\
    'data\\iteration3\\isotopomer_mapping_140528.csv',\
    ko_list,flux_dict,'iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc');

def make_WTEColi_113C80_U13C20_01_centralMets():
    # WTEColi_113C80_U13C20_01
    # WT 
    ko_list = [];
    flux_dict = {};
    #flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.61*0.9,'ub':0.61*1.1};
    #flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.721-0.5,'ub':2.721+0.5};
    #flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    #flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.54-1.23,'ub':-7.54+1.23};
    #flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.696,'ub':0.712};
    #flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':1.63,'ub':2.63};
    #flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    #flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.6,'ub':-7.2};
    ##Water bath data
    #flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.59,'ub':0.63};
    #flux_dict['EX_succ_LPAREN_e_RPAREN_'] = {'lb':0.04,'ub':0.08};
    #flux_dict['EX_for_LPAREN_e_RPAREN_'] = {'lb':0.57,'ub':1.07};
    #flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.48,'ub':2.96};
    #flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    #flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-8.1,'ub':-6.08};
    #flux_dict['EX_etoh_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    #flux_dict['EX_fum_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    #flux_dict['EX_lac_DASH_L_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    #flux_dict['EX_pyr_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    #ALE WT data
    flux_dict['Ec_biomass_iJO1366_WT_53p95M'] = {'lb':0.704*0.9,'ub':0.704*1.1};
    flux_dict['EX_ac_LPAREN_e_RPAREN_'] = {'lb':2.13*0.9,'ub':2.13*1.1};
    flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
    flux_dict['EX_glc_LPAREN_e_RPAREN_'] = {'lb':-7.4*1.1,'ub':-7.4*0.9};
    flux_dict['EX_succ_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    flux_dict['EX_for_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    flux_dict['EX_etoh_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    flux_dict['EX_fum_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    flux_dict['EX_lac_DASH_L_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    flux_dict['EX_pyr_LPAREN_e_RPAREN_'] = {'lb':0,'ub':0};
    isotopomer_model_iteration3(\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDM2014.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.xml',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.mat',\
    'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.csv',\
    'data\\iteration3_140601_centralMets\\isotopomer_mapping_140528_centralMets.csv',\
    ko_list,flux_dict,'iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc');