import json
from analysis.analysis_base import base_exportData

data = {"name":'AnalysisPipeline',
        "children":[{
    "name":'Database',
    "children":[
        {"name":'LC-MS/MS',
        "children":[
            {"name":'LCParameters'},
            {"name":'MSParameters'},
            {"name":'AutosamplerParams'}]},
        {"name":'Samples',
        "children":[
            {"name":'Storage'},
            {"name":'ExperimentConditions'},
            {"name":'PhysiologicalData'},
            {"name":'AcquisitionData'}]},
        {"name":'Standards',
        "children":[
            {"name":'Identifiers'},
            {"name":'Storage'},
            {"name":'Ordering'},
            {"name":'Chem/PhysProperties'},
            {"name":'AcquisitionData'}]},
        {"name":'Calibrators',
        "children":[
            {"name":'Mixes'},
            {"name":'Storage'},
            {"name":'LLO/ULOQ'},
            {"name":'RegressionParameters'},
            {"name":'AcquisitionData'}]}
        ]},
    {"name":'Analysis',
    "children":[
        {"name":'Quantification',
        "children":[
            {"name":'QC/QA'},
            {"name":'MissingValueHandling'},
            {"name":'Statistics'},
            {"name":'Correlation'},
            {"name":'Thermodynamics'},
            {"name":'Kinetics'}]},
        {"name":'MetabolicLabeling',
        "children":[
            {"name":'SpectraFiltering'},
            {"name":'PeakDeconvolution'},
            {"name":'IsotopomerDistCalc'},
            {"name":'DistributionFitting'},
            {"name":'FluxCalculations'},
            {"name":'ErrorEstimation'}]}
        ]},
    {"name":'Visualization',
    "children":[
        {"name":'BiochemicalMap'},
        {"name":'Plots/Charts',
        "children":[
            {"name":'Scatter'},
            {"name":'Bar'},
            {"name":'HeatMap'},
            {"name":'LinkageGraph'}]},
        {"name":'Tables'}
        ]}
    ]};

def _main_():
    '''Write data to json file'''
    export = base_exportData(data)
    export.write_dict2json('visualization\\ReingoldTilford Tree\\data.json')