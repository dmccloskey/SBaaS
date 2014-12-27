import json
from analysis.analysis_base import base_exportData

data = {"name":'MetabolomicsWorkflow',
        "children":[{
    "name":'Genomics',
    "children":[
        {"name":'Define the reaction network based on the genotype'}
        ]},
    {"name":'Phenomics',
    "children":[
        {"name":'Determine substrate input/output rates'},
        {"name":'Determine growth rate'}
        ]},
    {"name":'Model reduction',
    "children":[
        {"name":'Retain core modules based on coverage of anticipated data'},
        {"name":'Determine conditionally essential/optimal reactions outside of core modules'},
        {"name":'Lump conditionally essential/optimal reactions outside core modules'},
        {"name":'Modify biomass composition accordingly'}
        ]},
    {"name":'Fluxomics',
    "children":[
        {"name":'Determine atom mapping'},
        {"name":'Determine isotopomer distributions'},
        {"name":'Fit isotopomer distributions to model predictions'},
        {"name":'Check residuals of the fit'},
        {"name":'Determine flux confidence intervals'},
        {"name":'Determine statistically significant flux changes'},
        {"name":'Incorporate flux constraints'}
        ]},
    {"name":'Metabolomics',
    "children":[
        {"name":'Determine absolute metabolite concentrations'},
        {"name":'Check physiological ratios'},
        {"name":'Perform statistical and correlation analyses'},
        {"name":'Remove outliers'},
        {"name":'Determine statistically significant metabolite changes'},
        {"name":'Determine data correlations'}
        ]},
    {"name":'Thermodynamics',
    "children":[
        {"name":'Calculate dG0_f values not available in the literature'},
        {"name":'Adjust dG_f values to in vivo ionic strength, pH, and temperature'},
        {"name":'Determine dG0_r values from dG_f values'},
        {"name":'Determine dG_r values from dG0_r values and metabolomics data'},
        {"name":'Check reaction and pathway thermodynamic feasibility'},
        {"name":'Sample infeasible dG_r values'},
        {"name":'Sample thermodynamically feasible fluxes'},
        {"name":'Sample missing metabolite concentrations'},
        {"name":'Determine and compare thermodynamic disequilibriums'}
        ]},
    {"name":'Expression/proteomics',
    "children":[
        {"name":'Expand the model to explicitly include proteins and enzymes'},
        {"name":'Estimate enzyme levels based on expression and/or proteomics data'},
        {"name":'Sample thermodynamically valid enzyme levels that are missing'}
        ]},
    {"name":'Kinetics',
    "children":[
        {"name":'Sample PERCs'},
        {"name":'Check ensemble model/data combination stability'},
        {"name":'Perform time-scale decomposition'},
        {"name":'Determine aggregate pools'},
        {"name":'Abstract to a functional operating diagram'}
        ]},
    {"name":'Functional operating diagram'}
    ]};

def _main_():
    '''Write data to json file'''
    export = base_exportData(data)
    export.write_dict2json('visualization\\ReingoldTilford Tree\\data.json')