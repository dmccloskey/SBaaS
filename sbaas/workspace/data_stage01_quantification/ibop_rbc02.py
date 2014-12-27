from analysis import *

# analyze calibrators
stage00 = stage00_QMethod();
stage00.execute_quantitationMethodUpdate();

# update data
data = base_importData();
update = stage01_quantification_update();
data.read_csv('ibop_update01.csv');
data.format_data();
update.update_data_stage01_quantification_MQResultsTable(data.data);
data.clear_data();
data.read_csv('ibop_update02.csv');
data.format_data();
update.update_data_stage01_quantification_MQResultsTable(data.data);
data.clear_data();

# analyze the data
ma = stage01_quantification_execute();
ma.execute_checkLLOQAndULOQ('ibop_rbc02');
ma.execute_analyzeQCs('ibop_rbc02');
ma.execute_checkCV_QCs('ibop_rbc02'); #need to test
ma.execute_analyzeDilutions('ibop_rbc02');
ma.execute_checkCV_dilutions('ibop_rbc02');
ma.execute_normalizeSamples2Biomass('ibop_rbc02');
ma.execute_removeDuplicateDilutions('ibop_rbc02',
                                    ["fum.fum_1.Light","succ.succ_1.Light",
                                     "gln-L.gln-L_1.Light","glu-L.glu-L_1.Light",
                                     "atp.atp_1.Light","23dpg.23dpg_1.Light"]);
ma.execute_analyzeReplicates('ibop_rbc02');
ma.execute_analyzeAverages('ibop_rbc02');
ma.execute_checkCVAndExtracelluar_averages('ibop_rbc02');