from analysis.analysis_base import *
from analysis.analysis_stage00.stage00_query import stage00_query

def print_sampleStorage(experiment_id_I,exp_type_id_I):
    #Input:
    #   experiment_id_I = e.g. 'ALEsKOs01'
    #   exp_type_id_I = e.g. '5'
    query00 = stage00_query();
    sampleLocations = query00.get_sampleLabelAndBoxAndPos_experimentIDAndExperimentTypeID_sampleStorage(experiment_id_I,exp_type_id_I)
    for sample in sampleLocations:
        print sample['sample_label'] + '\t' + str(sample['box']) + '\t' + str(sample['pos'])