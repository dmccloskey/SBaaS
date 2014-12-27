from analysis.analysis_base import *
from stage02_quantification_query import stage02_quantification_query
from resources.matplot import matplot
from resources.heatmap import heatmap

class stage02_quantification_io(base_analysis):
    def __init__(self):
        self.session = Session();
        self.stage02_quantification_query = stage02_quantification_query();
        self.matplot = matplot();
        self.calculate = base_calculate();
    
    def export_volcanoPlot_d3(self,experiment_id_I,time_points_I=[],concentration_units_I=[],
                                json_var_name='data',
                                filename=['visualization\\data\\','\\quantification\\scatterplot\\','volcanoplot\\']):
        '''generate a volcano plot from pairwiseTest table'''

        print 'exporting volcanoPlot...'
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02pairWiseTest(experiment_id_I);
        filter_O = {};
        filter_O['time_point'] = [];
        filter_O['concentration_unit'] = [];
        filter_O['sample'] = [];
        for tp in time_points:
            filter_tp_str = 'time_point/'+tp;
            filter_O['time_point'].append(filter_tp_str);
            print 'generating a volcano plot for time_point ' + tp;
            data_transformed = [];
            # get concentration units...
            if concentration_units_I:
                concentration_units = concentration_units_I;
            else:
                concentration_units = [];
                concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02pairWiseTest(experiment_id_I,tp);
            #concentration_units = ['mM_glog_normalized']
            for cu in concentration_units:
                filter_cu_str = 'time_point/'+tp+'/concentration_unit/'+cu;
                filter_O['concentration_unit'].append(filter_cu_str);
                print 'exporting a volcano plot for concentration_units ' + cu;
                # get sample_name_abbreviations:
                sample_name_abbreviations = [];
                sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_experimentIDAndTimePointAndUnits_dataStage02pairWiseTest(experiment_id_I, tp, cu)
                for sna_1 in sample_name_abbreviations:
                    for sna_2 in sample_name_abbreviations:
                        if sna_1 != sna_2:
                            filter_sna_str = 'time_point/'+tp+'/concentration_unit/'+cu+'/sample/'+sna_1 + '_' + sna_2;
                            filter_O['sample'].append(filter_sna_str);
                            print 'exporting a volcano plot for sample_name_abbreviation ' + sna_1 + ' vs. ' + sna_2;
                            # get data:
                            data_1 = [];
                            data_1 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndSampleNameAbbreviations_dataStage02pairWiseTest(experiment_id_I,tp,cu,sna_1,sna_2);
                            # plot the data
                            title = sna_1 + ' vs. ' + sna_2;
                            xlabel = 'Fold Change [log2(FC)]';
                            ylabel = 'Probability [-log10(P)]';
                            x_data = [d['fold_change_log2'] for d in data_1];
                            y_data = [d['pvalue_corrected_negLog10'] for d in data_1];
                            text_labels = [t['component_group_name'] for t in data_1];
                            #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                            # initialize js variables
                            json_O = {};
                            options_O = {};
                            options_O['x_axis_label'] = 'Fold Change [log2(FC)]';
                            options_O['y_axis_label'] = 'Probability [-log10(P)]';
                            options_O['feature_name'] = 'component_group_name';
                            options_O['legend'] = False;
                            options_O['text_labels'] = True;
                            options_O['filter_by'] = 'labels';
                            # assign data to the js variables
                            data_O = [];
                            for d in data_1:
                                tmp = {};
                                tmp['x_data']=d['fold_change_log2'];
                                tmp['y_data']=d['pvalue_corrected_negLog10'];
                                tmp['text_labels']=d['component_group_name'];
                                tmp['samples']=title;
                                data_O.append(tmp);
                            json_O['data'] = data_O;
                            json_O['options'] = options_O;
                            # dump the data to a json file
                            json_str = 'var ' + json_var_name + ' = ' + json.dumps(json_O);
                            filename_str = filename[0] + experiment_id_I + filename[1] + filename[2] + tp + '_' + cu + '_' + sna_1 + '_' + sna_2 + '.js';
                            with open(filename_str,'w') as file:
                                file.write(json_str);
        # dump the filter data to a json file
        json_str = 'var ' + 'data_filter' + ' = ' + json.dumps(filter_O);
        filename_str = filename[0] + experiment_id_I + filename[1] + filename[2] + 'filter.js'
        with open(filename_str,'w') as file:
            file.write(json_str);
    def export_pcaPlot_d3(self,experiment_id_I,time_points_I=[],concentration_units_I=[],
                            json_var_name='data',
                            filename=['visualization\\data\\','\\quantification\\scatterplot\\','pcaplot\\']):
        '''generate a pca plot'''

        print 'export_pcaPlot...'
        # query metabolomics data from pca_scores and pca_loadings
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02Scores(experiment_id_I);
        filter_O = {};
        filter_O['time_point'] = [];
        filter_O['concentration_unit'] = [];
        filter_O['component'] = [];
        filter_O['score_loading'] = [];
        for tp in time_points:
            filter_tp_str = 'time_point/'+tp;
            filter_O['time_point'].append(filter_tp_str);
            print 'exporting pca for time_point ' + tp;
            data_transformed = [];
            # get concentration units...
            if concentration_units_I:
                concentration_units = concentration_units_I;
            else:
                concentration_units = [];
                concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02Scores(experiment_id_I,tp);
            for cu in concentration_units:
                filter_cu_str = 'time_point/'+tp+'/concentration_unit/'+cu;
                filter_O['concentration_unit'].append(filter_cu_str);
                print 'exporting pca for concentration_units ' + cu;
                # get data:
                data_scores,data_loadings = [],[];
                data_scores,data_loadings = self.stage02_quantification_query.get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage02ScoresLoadings(experiment_id_I,tp,cu);
                # plot the data:
                PCs = [[1,2],[1,3],[2,3]];
                for PC in PCs:
                    filter_sna_str = 'time_point/'+tp+'/concentration_unit/'+cu+'/component/'+str(PC[0]) + '_' + str(PC[1]);
                    filter_O['component'].append(filter_sna_str);
                    # scores
                    filter_sl_str = 'time_point/'+tp+'/concentration_unit/'+cu+'/component/'+str(PC[0]) + '_' + str(PC[1])+'/score_loading/'+'scores';
                    filter_O['score_loading'].append(filter_sl_str);
                    title,xlabel,ylabel,x_data,y_data,text_labels,samples = self.matplot._extractPCAScores(data_scores,PC[0],PC[1]);
                    #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                    json_O = {};
                    options_O = {};
                    options_O['x_axis_label'] = xlabel;
                    options_O['y_axis_label'] = ylabel;
                    options_O['feature_name'] = 'Sample name';
                    options_O['legend'] = True;
                    options_O['text_labels'] = True;
                    options_O['filter_by'] = 'samples';
                    data_O = [];
                    for i in range(len(x_data)):
                        tmp = {};
                        tmp['x_data']=x_data[i];
                        tmp['y_data']=y_data[i];
                        tmp['text_labels']=text_labels[i];
                        tmp['samples']=samples[i];
                        data_O.append(tmp);
                    json_O['data'] = data_O;
                    json_O['options'] = options_O;
                    # dump the data to a json file
                    json_str = 'var ' + json_var_name + ' = ' + json.dumps(json_O);
                    filename_str = filename[0] + experiment_id_I + filename[1] + filename[2] + tp + '_' + cu + '_' + str(PC[0]) + '_' + str(PC[1]) + '_' +'scores' + '.js';
                    with open(filename_str,'w') as file:
                        file.write(json_str);
                    # loadings
                    filter_sl_str = 'time_point/'+tp+'/concentration_unit/'+cu+'/component/'+str(PC[0]) + '_' + str(PC[1])+'/score_loading/'+'loadings';
                    filter_O['score_loading'].append(filter_sl_str);
                    title,xlabel,ylabel,x_data,y_data,text_labels = self.matplot._extractPCALoadings(data_loadings,PC[0],PC[1]);
                    #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                    json_O = {};
                    options_O = {};
                    options_O['x_axis_label'] = xlabel;
                    options_O['y_axis_label'] = ylabel;
                    options_O['feature_name'] = 'Component name';
                    options_O['legend'] = False;
                    options_O['text_labels'] = False;
                    options_O['filter_by'] = 'labels';
                    data_O = [];
                    for i in range(len(x_data)):
                        tmp = {};
                        tmp['x_data']=x_data[i];
                        tmp['y_data']=y_data[i];
                        tmp['text_labels']=text_labels[i];
                        tmp['samples']=title;
                        data_O.append(tmp);
                    json_O['data'] = data_O;
                    json_O['options'] = options_O;
                    # dump the data to a json file
                    json_str = 'var ' + json_var_name + ' = ' + json.dumps(json_O);
                    filename_str = filename[0] + experiment_id_I + filename[1] + filename[2] + tp + '_' + cu + '_' + str(PC[0]) + '_' + str(PC[1]) + '_' +'loadings' +'.js';
                    with open(filename_str,'w') as file:
                        file.write(json_str);
        # dump the filter data to a json file
        json_str = 'var ' + 'data_filter' + ' = ' + json.dumps(filter_O);
        filename_str = filename[0] + experiment_id_I + filename[1] + filename[2] + 'filter.js'
        with open(filename_str,'w') as file:
            file.write(json_str);

    def export_heatmap_d3(self, experiment_id_I,include_dataStage01ReplicatesMI_I = False,
                          time_points_I=[],concentration_units_I=[],
                          sample_name_shorts_I=[],component_group_names_I=[],
                        json_var_name='data',
                        filename=['visualization\\data\\','\\quantification\\heatmap\\','hcluster\\']):
        '''Export data for viewing using d3'''
        #Input:
        #   experiment_id
        #Output:
        #   

        print 'exporting heatmap...'
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        filter_O = {};
        filter_O['time_point'] = [];
        filter_O['concentration_unit'] = [];
        for tp in time_points:
            filter_tp_str = 'time_point/'+tp;
            filter_O['time_point'].append(filter_tp_str);
            print 'generating a heatmap for time_point ' + tp;
            data_transformed = [];
            # get concentration units...
            if concentration_units_I:
                concentration_units = concentration_units_I;
            else:
                concentration_units = [];
                concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            if include_dataStage01ReplicatesMI_I:
                concentration_units_add = [];
                concentration_units_add = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,tp);
                concentration_units.extend(concentration_units_add);
            #concentration_units = ['mM_glog_normalized']
            for cu in concentration_units:
                filter_cu_str = 'time_point/'+tp+'/concentration_unit/'+cu;
                filter_O['concentration_unit'].append(filter_cu_str);
                print 'exporting a heatmap for concentration_units ' + cu;
                # get data for the time-point and concentration_units
                if include_dataStage01ReplicatesMI_I and cu in concentration_units_add:
                    data = [];
                    data = self.stage02_quantification_query.get_data_experimentIDAndTimePointAndUnits_dataStage01ReplicatesMI(experiment_id_I,tp,cu);
                else:
                    data = [];
                    data = self.stage02_quantification_query.get_data_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I,tp,cu);
                # find unique
                component_group_names = [x['component_group_name'] for x in data];
                component_group_names_unique = list(set(component_group_names));
                component_group_names_unique.sort();
                sample_name_shorts = [x['sample_name_short'] for x in data];
                sample_name_short_unique = list(set(sample_name_shorts));
                sample_name_short_unique.sort();
                # generate the frequency matrix data structure (sample x met)
                data_O = numpy.zeros((len(sample_name_short_unique),len(component_group_names_unique)));
                labels_O = {};
                labels_O['lineage']=[];
                col_cnt = 0;
                # order 2: groups each lineage by met (sample x met)
                for sample_name_short_cnt,sample_name_short in enumerate(sample_name_short_unique): #all lineages for sample j / met i
                    labels_O['lineage'].append(sample_name_short);
                    for component_group_name_cnt,component_group_name in enumerate(component_group_names_unique): #all mets i for sample j
                        for row in data:
                            if row['sample_name_short'] == sample_name_short and row['component_group_name'] == component_group_name:
                                data_O[sample_name_short_cnt,component_group_name_cnt] = row['calculated_concentration'];
                    col_cnt+=1;
                # generate the clustering for the heatmap
                json_O = {};
                json_O = self.calculate.heatmap(data_O,sample_name_short_unique,component_group_names_unique);
                options_O = {};
                options_O['row_axis_label'] = 'sample_id';
                options_O['col_axis_label'] = 'met_id';
                options_O['value_label'] = 'normalized_concentration';
                options_O['domain'] = '1';
                ##No clustering:
                #labels_O = {};
                #labels_O['row_labels']=[];
                #labels_O['col_labels']=[];
                #labels_O['hcrow']=[];
                #labels_O['hccol']=[];
                #labels_O['lineage']=[];
                #labels_O['maxval']=None;
                #labels_O['minval']=None;
                #col_cnt = 0;
                ## order 2: groups each lineage by met (sample x met)
                #for sample_name_short_cnt,sample_name_short in enumerate(sample_name_short_unique): #all lineages for sample j / met i
                #    labels_O['row_labels'].append(sample_name_short); # corresponding label from hierarchical clustering (in this case, arbitrary)
                #    labels_O['hcrow'].append(col_cnt+1); # ordering from hierarchical clustering (in this case, arbitrary)
                #    for component_group_name_cnt,component_group_name in enumerate(component_group_names_unique): #all mets i for sample j
                #        if sample_name_short_cnt==0: # record only once
                #            labels_O['col_labels'].append(component_group_name); # corresponding label from hierarchical clustering (in this case, arbitrary)
                #            labels_O['lineage'].append(sample_name_short);
                #            labels_O['hccol'].append(component_group_name_cnt+1); # ordering from hierarchical clustering (in this case, arbitrary)
                #        data_tmp = {};
                #        data_tmp['col'] = component_group_name_cnt+1;
                #        data_tmp['row'] = col_cnt+1;
                #        data_tmp['value'] = 0.0;
                #        for row in group_data:
                #            if row['sample_name_short'] == sample_name_short and row['component_group_name'] == component_group_name:
                #                data_tmp['value'] = row['calculated_concentration'];
                #        data_O.append(data_tmp);
                #    col_cnt+=1;
                #labels_O['maxval']=max([x['value'] for x in data_O]);
                #labels_O['minval']=min([x['value'] for x in data_O]);
                #json_O['heatmap_data']=data_O;

                json_O.update(labels_O);
                json_O['options'] = options_O;
                # dump the data to a json file
                json_str = 'var ' + json_var_name + ' = ' + json.dumps(json_O);
                filename_str = filename[0] + experiment_id_I + filename[1]+ filename[2] + tp + '_' + cu +'.js'
                with open(filename_str,'w') as file:
                    file.write(json_str);
        # dump the filter data to a json file
        json_str = 'var ' + 'data_filter' + ' = ' + json.dumps(filter_O);
        filename_str = filename[0] + experiment_id_I + filename[1] + filename[2] + 'filter.js'
        with open(filename_str,'w') as file:
            file.write(json_str);