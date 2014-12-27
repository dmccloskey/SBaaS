from analysis.analysis_stage02_isotopomer.analyze13Cflux import *
from analysis.analysis_base.base_exportData import base_exportData

def extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list,
                             isotopomerMeasured_1_filename_list=[],isotopomerMeasured_2_filename_list=[]):
    '''extract and compare matlab data'''
    for i in range(len(isotopomer_1_filename_list)):
        # extract out matlab data
        if isotopomerMeasured_1_filename_list:
            isotopomer_1 = load_isotopomer_matlab(isotopomer_1_filename_list[i],isotopomerMeasured_1_filename_list[i]);
        else:
            isotopomer_1 = load_isotopomer_matlab(isotopomer_1_filename_list[i]);
        ci_1 = load_confidenceIntervals_matlab(ci_1_filename_list[i],cobra_model_1_filename_list[i],cobra_model_1_name_list[i]);
        if isotopomerMeasured_2_filename_list:
            isotopomer_2 = load_isotopomer_matlab(isotopomer_2_filename_list[i],isotopomerMeasured_2_filename_list[i]);
        else:
            isotopomer_2 = load_isotopomer_matlab(isotopomer_2_filename_list[i]);
        ci_2 = load_confidenceIntervals_matlab(ci_2_filename_list[i],cobra_model_2_filename_list[i],cobra_model_2_name_list[i]);
        # compare extracted matlab data
        isotopomer_comparison,isotopomer_comparison_stats = compare_isotopomers_calculated(isotopomer_1, isotopomer_2);
        ci_comparison,cirange_1_sum,cirange_2_sum,cirange_1_combined_sum,cirange_2_combined_sum = compare_ci_calculated(ci_1,ci_2);
        # write isotopomer_comparison to file:
        export = base_exportData(isotopomer_comparison);
        export.write_dict2csv(isotopomer_comparison_filename_list[i]);
        # write ci_comparison to file:
        export = base_exportData(ci_comparison);
        export.write_dict2csv(ci_comparison_filename_list[i]);
        # visualize isotopomer_comparison
        plot_ci_calculated(ci_2);

def proteogenicAAcomparison():
    # all files to analyze
    nCompare = 3;
    isotopomer_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\iDM2014_113C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\iDM2014_613C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\iDM2014_U12C80_U13C20_WT.mat'];
    ci_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\ci_iDM2014_113C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\ci_iDM2014_613C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\ci_iDM2014_U12C80_U13C20_WT.mat'];
    cobra_model_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140430_iDMisotopomer_proteogenicAAcomparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140430_iDMisotopomer_proteogenicAAcomparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140430_iDMisotopomer_proteogenicAAcomparison_WT.mat'];
    cobra_model_1_name_list = ['iDM2014_proteogenicAAcomparison_WT',
                               'iDM2014_proteogenicAAcomparison_WT',
                               'iDM2014_proteogenicAAcomparison_WT'];

    isotopomer_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\iJS2012_113C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\iJS2012_613C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\iJS2012_U12C80_U13C20_WT.mat'];
    ci_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\ci_iJS2012_113C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\ci_iJS2012_613C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison\\ci_iJS2012_U12C80_U13C20_WT.mat'];
    cobra_model_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat'];
    cobra_model_2_name_list = ['iJS2012',
                               'iJS2012',
                               'iJS2012'];

    isotopomer_comparison_filename_list = ['data\\iDM2014_validation\\isotopomer_comparison_113C_WT.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_613C_WT.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C80_U13C20_WT.csv']
    ci_comparison_filename_list = ['data\\iDM2014_validation\\ci_comparison_113C_WT.csv',
                                   'data\\iDM2014_validation\\ci_comparison_613C_WT.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C80_U13C20_WT.csv']
    
    extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list);

def proteogenicAAcomparison_centralMets():
    # all files to analyze
    nCompare = 3;
    isotopomer_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\iDM2014_113C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\iDM2014_613C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\iDM2014_U12C80_U13C20_WT.mat'];
    ci_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\ci_iDM2014_113C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\ci_iDM2014_613C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\ci_iDM2014_U12C80_U13C20_WT.mat'];
    cobra_model_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_proteogenicAAcomparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_proteogenicAAcomparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_proteogenicAAcomparison_WT.mat'];
    cobra_model_1_name_list = ['iDM2014_proteogenicAAcomparison_WT',
                               'iDM2014_proteogenicAAcomparison_WT',
                               'iDM2014_proteogenicAAcomparison_WT'];

    isotopomer_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\iJS2012_113C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\iJS2012_613C_WT.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\iJS2012_U12C80_U13C20_WT.mat'];
    ci_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\ci_iJS2012_113C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\ci_iJS2012_613C_WT.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\proteogenicAAcomparison_centralMets\\ci_iJS2012_U12C80_U13C20_WT.mat'];
    cobra_model_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012_centralMets.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012_centralMets.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012_centralMets.mat'];
    cobra_model_2_name_list = ['iJS2012',
                               'iJS2012',
                               'iJS2012'];

    isotopomer_comparison_filename_list = ['data\\iDM2014_validation\\isotopomer_comparison_113C_WT_centralMets.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_613C_WT_centralMets.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C80_U13C20_WT_centralMets.csv']
    ci_comparison_filename_list = ['data\\iDM2014_validation\\ci_comparison_113C_WT_centralMets.csv',
                                   'data\\iDM2014_validation\\ci_comparison_613C_WT_centralMets.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C80_U13C20_WT_centralMets.csv']
    
    extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list);

def Toya2010comparison():
    # all files to analyze
    nCompare = 3;
    isotopomer_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Wildtype_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Wildtype_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Wildtype_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iDM2014_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    ci_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Wildtype_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Wildtype_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Wildtype_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iDM2014_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    cobra_model_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140430_iDMisotopomer_Toya2010comparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140423_iDMisotopomer_Toya2010comparison_PGI.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140423_iDMisotopomer_Toya2010comparison_PYK.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140430_iDMisotopomer_Toya2010comparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140423_iDMisotopomer_Toya2010comparison_PGI.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140423_iDMisotopomer_Toya2010comparison_PYK.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140430_iDMisotopomer_Toya2010comparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140423_iDMisotopomer_Toya2010comparison_PGI.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140423_iDMisotopomer_Toya2010comparison_PYK.mat'];
    cobra_model_1_name_list = ['iDM2014_Toya2010comparison_WT',
                               'iDM2014_Toya2010comparison_PGI',
                               'iDM2014_Toya2010comparison_PYK',
                               'iDM2014_Toya2010comparison_WT',
                               'iDM2014_Toya2010comparison_PGI',
                               'iDM2014_Toya2010comparison_PYK',
                               'iDM2014_Toya2010comparison_WT',
                               'iDM2014_Toya2010comparison_PGI',
                               'iDM2014_Toya2010comparison_PYK'];

    isotopomer_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Wildtype_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Wildtype_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Wildtype_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\iJS2012_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    ci_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Wildtype_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Wildtype_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Wildtype_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison\\ci_iJS2012_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    cobra_model_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat'];
    cobra_model_2_name_list = ['iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012'];

    isotopomer_comparison_filename_list = ['data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Wildtype_5h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pgimutant_5h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pykmutant_5h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Wildtype_6h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pgimutant_6h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pykmutant_6h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Wildtype_7h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pgimutant_7h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pykmutant_7h.csv']
    ci_comparison_filename_list = ['data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Wildtype_5h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pgimutant_5h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pykmutant_5h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Wildtype_6h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pgimutant_6h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pykmutant_6h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Wildtype_7h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pgimutant_7h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pykmutant_7h.csv']
    
    extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list);

def Toya2010comparison_centralMets():
    # all files to analyze
    nCompare = 3;
    isotopomer_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Wildtype_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Wildtype_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Wildtype_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iDM2014_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    ci_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Wildtype_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Wildtype_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Wildtype_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iDM2014_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    cobra_model_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_PGI.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_PYK.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_PGI.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_PYK.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_WT.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_PGI.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_Toya2010comparison_PYK.mat'];
    cobra_model_1_name_list = ['iDM2014_Toya2010comparison_WT',
                               'iDM2014_Toya2010comparison_PGI',
                               'iDM2014_Toya2010comparison_PYK',
                               'iDM2014_Toya2010comparison_WT',
                               'iDM2014_Toya2010comparison_PGI',
                               'iDM2014_Toya2010comparison_PYK',
                               'iDM2014_Toya2010comparison_WT',
                               'iDM2014_Toya2010comparison_PGI',
                               'iDM2014_Toya2010comparison_PYK'];

    isotopomer_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Wildtype_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Wildtype_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Wildtype_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                                  'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\iJS2012_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    ci_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Wildtype_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Pgimutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Pykmutant_5h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Wildtype_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Pgimutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Pykmutant_6h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Wildtype_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Pgimutant_7h.mat',
                          'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\Toya2010comparison_centralMets\\ci_iJS2012_U12C50_113C30_U13C20_Pykmutant_7h.mat'];
    cobra_model_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat',
                                   'C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat'];
    cobra_model_2_name_list = ['iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012',
                               'iJS2012'];

    isotopomer_comparison_filename_list = ['data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Wildtype_5h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pgimutant_5h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pykmutant_5h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Wildtype_6h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pgimutant_6h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pykmutant_6h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Wildtype_7h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pgimutant_7h.csv',
                                           'data\\iDM2014_validation\\isotopomer_comparison_U12C50_113C30_U13C20_Pykmutant_7h.csv']
    ci_comparison_filename_list = ['data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Wildtype_5h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pgimutant_5h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pykmutant_5h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Wildtype_6h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pgimutant_6h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pykmutant_6h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Wildtype_7h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pgimutant_7h.csv',
                                   'data\\iDM2014_validation\\ci_comparison_U12C50_113C30_U13C20_Pykmutant_7h.csv']
    
    extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list);

def WTEColi_113C80_U13C20_01():
    # all files to analyze
    ncompare = 1;
    isotopomer_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01\\iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    ci_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01\\ci_iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    cobra_model_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140527_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    cobra_model_1_name_list = ['iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc'];

    isotopomer_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01\\iJS2012_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    ci_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01\\ci_iJS2012_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    cobra_model_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012.mat'];
    cobra_model_2_name_list = ['iJS2012'];
    
    isotopomer_comparison_filename_list = ['data\\iDM2014_validation\\isotopomer_comparison_WTEColi_113C80_U13C20_01_centralMets.csv'];
    ci_comparison_filename_list = ['data\\iDM2014_validation\\ci_comparison_WTEColi_113C80_U13C20_01_centralMets.csv'];
    
    extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list);

def WTEColi_113C80_U13C20_01_centralMets():
    # all files to analyze
    ncompare = 1;
    isotopomer_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01_centralMets\\iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    isotopomerMeasured_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01_centralMets\\isotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc_0.json'];
    ci_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01_centralMets\\ci_iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    cobra_model_1_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iteration3_140601_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    cobra_model_1_name_list = ['iDM2014_WTEColi_113C80_U13C20_01_OxicWtGlc'];

    isotopomer_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01_centralMets_WTALE\\iJS2012_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    isotopomerMeasured_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01_centralMets_WTALE\\isotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc_0.json'];
    ci_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\WTEColi_113C80_U13C20_01_centralMets_WTALE\\ci_iJS2012_WTEColi_113C80_U13C20_01_OxicWtGlc.mat'];
    cobra_model_2_filename_list = ['C:\\Users\dmccloskey-sbrg\\Documents\\MATLAB\\fluxomics_DM\\iJS2012_centralMets.mat'];
    cobra_model_2_name_list = ['iJS2012'];
    
    isotopomer_comparison_filename_list = ['data\\iDM2014_validation\\isotopomer_comparison_WTEColi_113C80_U13C20_01_centralMets.csv'];
    ci_comparison_filename_list = ['data\\iDM2014_validation\\ci_comparison_WTEColi_113C80_U13C20_01_centralMets.csv'];
    
    extractAndCompare_matlab(isotopomer_1_filename_list,ci_1_filename_list,cobra_model_1_filename_list,cobra_model_1_name_list,
                             isotopomer_2_filename_list,ci_2_filename_list,cobra_model_2_filename_list,cobra_model_2_name_list,
                             isotopomer_comparison_filename_list, ci_comparison_filename_list,
                             isotopomerMeasured_1_filename_list, isotopomerMeasured_2_filename_list);

    # export selected flux data with a specific model for later use
    cobra_model_filename = 'data\\iteration3_140601_centralMets\\iteration3_140601_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.xml'
    cobra_model_O_filename = 'data\\iDM2014_validation\\140601_iDMisotopomer_WTEColi_113C80_U13C20_01_OxicWtGlc.xml'
    ci_1 = load_confidenceIntervals_matlab(ci_1_filename_list[0],cobra_model_1_filename_list[0],cobra_model_1_name_list[0])
    ci_2 = load_confidenceIntervals_matlab(ci_2_filename_list[0],cobra_model_2_filename_list[0],cobra_model_2_name_list[0])
    ci_1_mod = {};
    for k,v in ci_1.iteritems():
        if not k in ci_2.keys():
            ci_1_mod[k] = v;
    export_modelWithFlux(cobra_model_filename,[ci_2,ci_1_mod],cobra_model_O_filename);