from analysis import *

def data_stage00():
    
    '''acqusition method import'''
    method_io = stage00_io();

def data_stage01():
    
    ma = stage01_ale_execute();
    ma.initialize_dataStage01();

    '''exeriment data imports'''
    data_io = stage01_ale_io();
    #data_io.import_dataStage01AleTrajectories_matlab('ALEsKOs01',
    #      'C:\\Users\\dmccloskey-sbrg\\Documents\\MATLAB\\ALEsKOs\\ALEsKOs_trajectories.mat'); #TODO

    '''data analysis'''
    #ma.execute_findJumps('ALEsKOs01'); #TODO

    '''experiment data exports'''
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04pgiEvo01EcoliGlc',
                                                'OxicEvo04pgiEvo02EcoliGlc',
                                                'OxicEvo04pgiEvo03EcoliGlc',
                                                'OxicEvo04pgiEvo04EcoliGlc',
                                                'OxicEvo04pgiEvo05EcoliGlc',
                                                'OxicEvo04pgiEvo06EcoliGlc',
                                                'OxicEvo04pgiEvo07EcoliGlc',
                                                'OxicEvo04pgiEvo08EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\pgi.js');
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04ptsHIcrrEvo01EcoliGlc',
                                                'OxicEvo04ptsHIcrrEvo02EcoliGlc',
                                                'OxicEvo04ptsHIcrrEvo03EcoliGlc',
                                                'OxicEvo04ptsHIcrrEvo04EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\ptsHIcrr.js');
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04tpiAEvo01EcoliGlc',
                                                'OxicEvo04tpiAEvo02EcoliGlc',
                                                'OxicEvo04tpiAEvo03EcoliGlc',
                                                'OxicEvo04tpiAEvo04EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\tpiA.js');
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04pgiEvo01EcoliGlc',
                                                'OxicEvo04pgiEvo02EcoliGlc',
                                                'OxicEvo04pgiEvo03EcoliGlc',
                                                'OxicEvo04pgiEvo04EcoliGlc',
                                                'OxicEvo04pgiEvo05EcoliGlc',
                                                'OxicEvo04pgiEvo06EcoliGlc',
                                                'OxicEvo04pgiEvo07EcoliGlc',
                                                'OxicEvo04pgiEvo08EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\pgi.js');
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04gndEvo01EcoliGlc',
                                                'OxicEvo04gndEvo02EcoliGlc',
                                                'OxicEvo04gndEvo03EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\gnd.js');
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04sdhCadhBEvo01EcoliGlc',
                                                'OxicEvo04sdhCadhBEvo02EcoliGlc',
                                                'OxicEvo04sdhCadhBEvo03EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\sdhCB.js');
    data_io.export_dataStage01AleTrajectories_d3('ALEsKOs01',
                        sample_name_abbreviations_I=['OxicEvo04Evo01EcoliGlc',
                                                'OxicEvo04Evo02EcoliGlc'],
                        fit_func_I='lowess',
                        json_var_name='data',
                        filename='visualization\\data\\ALEsKOs01\\ale\\scatterlineplot\\evo04.js');

