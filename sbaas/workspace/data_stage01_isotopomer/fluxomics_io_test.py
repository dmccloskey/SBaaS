from analysis import *

iobase = base_importData();
iobase.read_csv('data\\_input\\140415_13CFluxMRM.csv');

execute = stage00_execute();
#execute.execute_importStructureFile([{'met_id':'skm',
#                                      'file_directory':'data\\BIGG_mol',
#                                      'file_ext':'.mol'},
#                                     {'met_id':'udpg',
#                                      'file_directory':'data\\BIGG_mol',
#                                      'file_ext':'.mol'},
#                                      {'met_id':'chor',
#                                      'file_directory':'data\\BIGG_mol',
#                                      'file_ext':'.mol'}])
#execute.execute_updateFormulaAndMassFromStructure(['skm',
#                                                   'udpg',
#                                                   'chor'])
execute.execute_13CFluxMRM(iobase.data);
#execute.execute_scheduledMRMPro_quant(['atp'],'-')
