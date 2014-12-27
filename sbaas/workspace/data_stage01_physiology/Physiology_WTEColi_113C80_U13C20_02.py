from analysis import *

def data_stage00():
    
    '''acqusition method import'''
    execute00 = stage00_execute();
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\141216_WTEColi_113C80_U13C20_02_biomass01.csv',0,[]); # todo

def data_stage01():

    ma = stage01_physiology_execute();
    ma.initialize_dataStage01();

    '''data import'''
    io = stage01_physiology_io();
    io.import_dataStage01PhysiologyData_add('data\\_input\\141216_WTEColi_113C80_U13C20_02_biomass01.csv',0,[]); # todo

    '''data analysis'''
    #functions to return sample names
    def sample_names_short_calculateGrowthRates_isotopomer01a():
        return ['OxicWtGlc_Broth-1',
'OxicWtGlc_Broth-2',
'OxicWtGlc_Broth-3'
];
    def sample_names_abbreviation_calculateRatesAverages_isotopomer01a():
        return ['OxicWtGlc'
];
    def sample_names_interpolateBiomassFromReplicates_isotopomer01a():
        return ['141209_0_OxicWTEcoli13CGlcM9_Broth-1',
'141209_0_OxicWTEcoli13CGlcM9_Broth-2',
'141209_0_OxicWTEcoli13CGlcM9_Broth-3',
'141209_0_OxicWTEcoli13CGlcM9_Broth-4',
'141209_0_OxicWTEcoli13CGlcM9_Broth-5',
'141209_0_OxicWTEcoli13CGlcM9_Broth-6'];
    def sample_names_interpolateBiomassFromAverages_isotopomer01a():
        return['141209_0_OxicWTEcoli13CGlcM9_Broth-1',
'141209_0_OxicWTEcoli13CGlcM9_Broth-2',
'141209_0_OxicWTEcoli13CGlcM9_Broth-3',
'141209_0_OxicWTEcoli13CGlcM9_Broth-4',
'141209_0_OxicWTEcoli13CGlcM9_Broth-5',
'141209_0_OxicWTEcoli13CGlcM9_Broth-6'];
    def sample_names_calculateBiomassFromBrothAverage_isotopomer01a():
        return ['141209_0_OxicWTEcoli13CGlcM9_Broth-1',
'141209_0_OxicWTEcoli13CGlcM9_Broth-2',
'141209_0_OxicWTEcoli13CGlcM9_Broth-3',
'141209_0_OxicWTEcoli13CGlcM9_Broth-4',
'141209_0_OxicWTEcoli13CGlcM9_Broth-5',
'141209_0_OxicWTEcoli13CGlcM9_Broth-6'];
    def sample_names_updatePhysiologicalParametersFromOD600_isotopomer01a():
        return ['141209_0_OxicWTEcoli13CGlcM9_Broth-1',
'141209_0_OxicWTEcoli13CGlcM9_Broth-2',
'141209_0_OxicWTEcoli13CGlcM9_Broth-3',
'141209_0_OxicWTEcoli13CGlcM9_Broth-4',
'141209_0_OxicWTEcoli13CGlcM9_Broth-5',
'141209_0_OxicWTEcoli13CGlcM9_Broth-6'];

    #Isotopomer growth rates and physiological parameter updates
    ma.execute_calculateGrowthRates('WTEColi_113C80_U13C20_02',sample_names_short_calculateGrowthRates_isotopomer01a()); # todo
    ma.execute_calculateRatesAverages('WTEColi_113C80_U13C20_02',sample_names_abbreviation_calculateRatesAverages_isotopomer01a()); # todo
    #Isotopomer biomass interpolations
    ma.execute_interpolateBiomassFromReplicates('WTEColi_113C80_U13C20_02',sample_names_interpolateBiomassFromReplicates_isotopomer01a()); # todo
    #ma.execute_interpolateBiomassFromAverages('WTEColi_113C80_U13C20_02',sample_names_interpolateBiomassFromAverages_isotopomer01a()); # not needed
    #ma.execute_calculateBiomassFromBrothAverage('WTEColi_113C80_U13C20_02',sample_names_calculateBiomassFromBrothAverage_isotopomer01a()) # not needed
    
    #Isotopomer physiological parameter updates
    ma.execute_updatePhysiologicalParametersFromOD600('WTEColi_113C80_U13C20_02'); # todo

