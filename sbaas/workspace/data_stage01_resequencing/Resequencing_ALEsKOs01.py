from analysis import *

def strain_lineages():
    strain_lineages_O = {"evo04pgievo01":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo01J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo01J02EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo02":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo02J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo02J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo03":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo03J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo03J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo03J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo04":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo04J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo04J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo04J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo05":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo05J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo05J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo05J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo06":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo06J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo06J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo06J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo07":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo07J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo07J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo07J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1"},
                                        "evo04pgievo08":{0:"140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04pgiEvo08J01EcoliGlcM9_Broth-1",2:"140702_2_OxicEvo04pgiEvo08J02EcoliGlcM9_Broth-1",3:"140702_3_OxicEvo04pgiEvo08J03EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1"},
                                        "evo04ptsHIcrrevo01":{0:"140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04ptsHIcrrEvo01J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04ptsHIcrrEvo01J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1"},
                                        "evo04ptsHIcrrevo02":{0:"140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04ptsHIcrrEvo02J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04ptsHIcrrEvo02J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1"},
                                        "evo04ptsHIcrrevo03":{0:"140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04ptsHIcrrEvo03J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04ptsHIcrrEvo03J03EcoliGlcM9_Broth-1",3:"140702_4_OxicEvo04ptsHIcrrEvo03J04EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1"},
                                        "evo04ptsHIcrrevo04":{0:"140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04ptsHIcrrEvo04J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04ptsHIcrrEvo04J03EcoliGlcM9_Broth-1",3:"140702_4_OxicEvo04ptsHIcrrEvo04J04EcoliGlcM9_Broth-1",4:"140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1"},
                                        "evo04tpiAevo01":{0:"140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04tpiAEvo01J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04tpiAEvo01J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1"},
                                        "evo04tpiAevo02":{0:"140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04tpiAEvo02J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04tpiAEvo02J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1"},
                                        "evo04tpiAevo03":{0:"140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04tpiAEvo03J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04tpiAEvo03J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1"},
                                        "evo04tpiAevo04":{0:"140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04tpiAEvo04J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04tpiAEvo04J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1"},
                                        "evo04evo01":{0:"140401_0_OxicEvo04EcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1"},
                                        "evo04evo02":{0:"140401_0_OxicEvo04EcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1"},
                                        "evo04gndevo01":{0:"140401_0_OxicEvo04gndEcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1"},
                                        "evo04gndevo02":{0:"140401_0_OxicEvo04gndEcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1"},
                                        "evo04gndevo03":{0:"140401_0_OxicEvo04gndEcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1"},
                                        "evo04sdhevo01":{0:"140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1"},
                                        "evo04sdhevo02":{0:"140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1"},
                                        "evo04sdhevo03":{0:"140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1",1:"140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1"}};
    return strain_lineages_O;
def initial_final_pairs():
    initial_final_O = ["140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04EcoliGlcM9_Broth-1","140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04EcoliGlcM9_Broth-1","140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04gndEcoliGlcM9_Broth-1","140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04gndEcoliGlcM9_Broth-1","140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04gndEcoliGlcM9_Broth-1","140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1","140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1","140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1","140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1"];
    return initial_final_O;
def initial_final():
    initial_final_O = ["140401_0_OxicEvo04pgiEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04ptsHIcrrEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04EcoliGlcM9_Broth-1","140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04gndEcoliGlcM9_Broth-1","140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1",
                    "140401_0_OxicEvo04sdhCBEcoliGlcM9_Broth-1","140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1",
                    "140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1"];
    return initial_final_O;
def reduce_groupNames():
    reduce_group_names_O = {"evo04pgievoEP":["140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1",
										"140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1"],
                        "evo04ptsHIcrrevoEP":["140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1"],
                        "evo04tpiAevoEP":["140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1"],
                        "evo04evoEP":["140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1"],
                        "evo04gndevoEP":["140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1"],
                        "evo04sdhevoEP":["140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1",
                                        "140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1"]};
    return reduce_group_names_O;

def data_stage00():
    
    '''data import'''
    execute00 = stage00_execute();
    execute00.execute_makeExperimentFromSampleFile('data\\_input\\140823_Resequencing_ALEsKOs01_sampleFile01.csv',0,0);

def data_stage01():

    ma = stage01_resequencing_execute();
    #ma.drop_dataStage01();
    ma.initialize_dataStage01();

    '''data import'''
    io = stage01_resequencing_io();
    ## import resequencing data from breseq
    #iobase = base_importData();
    #iobase.read_csv('data\\_input\\140823_Resequencing_ALEsKOs01_fileList01.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'importing resequencing data for sample ' + file['sample_name']
    #    io.import_resequencingData_add(file['filename'],file['experiment_id'],file['sample_name']);
    #iobase.clear_data();
    #iobase.read_csv('data\\_input\\140823_Resequencing_ALEsKOs01_fileList02.csv');
    #fileList = iobase.data;
    ## read in each data file
    #for file in fileList:
    #    print 'importing resequencing data for sample ' + file['sample_name']
    #    io.import_resequencingData_add(file['filename'],file['experiment_id'],file['sample_name']);
    ## updates
    #io.import_dataStage01ResequencingLineage_update('data\\_input\\140823_Resequencing_ALEsKOs01_lineage_update01.csv');

    '''data analysis'''
    #ma.reset_dataStage01_filtered('ALEsKOs01');
    #ma.execute_filterMutations_population('ALEsKOs01');
    #ma.reset_dataStage01_lineage('ALEsKOs01')
    #ma.execute_analyzeLineage_population('ALEsKOs01',
    #                                     strain_lineages());
    #ma.execute_annotateMutations_lineage('ALEsKOs01');
    #ma.reset_dataStage01_endpoints('ALEsKOs01')
    #ma.execute_analyzeEndpointReplicates_population('ALEsKOs01',
    #                                     {"evo04pgi":["140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1",
    #                                                  "140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1",
    #                                                  "140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1"],
    #                                    "evo04ptsHIcrr":["140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1",
    #                                                     "140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1"],
    #                                    "evo04tpiA":["140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1",
    #                                                 "140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1"],
    #                                    "evo04":["140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1"],
    #                                    "evo04gnd":["140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1",
    #                                                "140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1"],
    #                                    "evo04sdh":["140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1",
    #                                                "140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1"]});
    #ma.execute_annotateMutations_endpoints('ALEsKOs01');
    #ma.execute_annotateFilteredMutations('ALEsKOs01');

    '''data export'''
    mutation_id_base = ['MOB_insA-/-uspC_1977510',
                        'SNP_ylbE_547694',
                        'SNP_yifN_3957957',
                        'DEL_corA_3999668',
                        'MOB_tdk_1292255',
                        'SNP_rpoB_4182566',
                        'INS__4294403',
                        'DEL_pyrE-/-rph_3813882',
                        'SNP_wcaA_2130811']
    io.export_dataStage01ResequencingLineage_d3('ALEsKOs01',
                                                ['evo04pgievo01','evo04pgievo02','evo04pgievo03','evo04pgievo04','evo04pgievo05','evo04pgievo06','evo04pgievo07','evo04pgievo08'],
                                                filename='visualization\\data\\ALEsKOs01\\resequencing\\heatmap\\pgi.js',
                                                mutation_id_exclusion_list = mutation_id_base);
    io.export_dataStage01ResequencingLineage_d3('ALEsKOs01',
                                                ['evo04ptsHIcrrevo01','evo04ptsHIcrrevo02','evo04ptsHIcrrevo03','evo04ptsHIcrrevo04'],
                                                filename='visualization\\data\\ALEsKOs01\\resequencing\\heatmap\\ptsHIcrr.js',
                                                mutation_id_exclusion_list = mutation_id_base);
    io.export_dataStage01ResequencingLineage_d3('ALEsKOs01',
                                                ['evo04tpiAevo01','evo04tpiAevo02','evo04tpiAevo03','evo04tpiAevo04'],
                                                filename='visualization\\data\\ALEsKOs01\\resequencing\\heatmap\\tpiA.js',
                                                mutation_id_exclusion_list = mutation_id_base);
    io.export_dataStage01ResequencingLineage_d3('ALEsKOs01',
                                                ['evo04gndevo01','evo04gndevo02','evo04gndevo03'],
                                                filename='visualization\\data\\ALEsKOs01\\resequencing\\heatmap\\gnd.js',
                                                mutation_id_exclusion_list = mutation_id_base);
    io.export_dataStage01ResequencingLineage_d3('ALEsKOs01',
                                                ['evo04sdhevo01','evo04sdhevo02','evo04sdhevo03'],
                                                filename='visualization\\data\\ALEsKOs01\\resequencing\\heatmap\\sdhCB.js',
                                                mutation_id_exclusion_list = mutation_id_base);
    io.export_dataStage01ResequencingLineage_d3('ALEsKOs01',
                                                ['evo04evo01','evo04evo02'],
                                                filename='visualization\\data\\ALEsKOs01\\resequencing\\heatmap\\evo04.js',
                                                mutation_id_exclusion_list = mutation_id_base);

    #io.export_dataStage01ResequencingMutationsAnnotated_d3('ALEsKOs01',
    #                                     strain_lineages(),
    #                                            mutation_id_exclusion_list = ['insA-/-uspC_MOB_1977510',
    #                    'ylbE_SNP_547694',
    #                    'yifN_SNP_3957957',
    #                    'corA_DEL_3999668',
    #                    'tdk_MOB_1292255',
    #                    'rpoB_SNP_4182566',
    #                    '_INS_4294403',
    #                    'pyrE-/-rph_DEL_3813882',
    #                    'wcaA_SNP_2130811']);

def data_stage02():
    
    ex02 = stage02_resequencing_execute();
    #ex02.drop_dataStage02();
    ex02.initialize_dataStage02();

    '''data import'''
    io02 = stage02_resequencing_io();

    '''data analysis'''
    #ex02.reset_dataStage02('ALEsKOs01');
    #ex02.execute_mapResequencingPhysiology_population('ALEsKOs01',sample_names_I=initial_final())
    #ex02.reset_dataStage02_reduceResequencingPhysiology('ALEsKOs01')
    #ex02.execute_reduceResequencingPhysiology_population('ALEsKOs01',reduce_groupNames())
    #ex02.execute_reduceResequencingPhysiology_population('ALEsKOs01',{"evo04ptsHIcrrevoEP":["140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1",
    #                                    "140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1",
    #                                    "140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1",
    #                                    "140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1"]});

    io02.export_dataStage02ResequencingLineage_d3('ALEsKOs01');