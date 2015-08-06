'''quantitative metabolomics analysis class'''

from sbaas.analysis.analysis_base import *
from .stage02_quantification_query import stage02_quantification_query
from calculate_utilities.r import r_calculate
from sbaas.resources.matplot import matplot
from math import sqrt
import copy

class stage02_quantification_execute(base_analysis):
    '''class for quantitative metabolomics analysis'''
    def __init__(self,session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage02_quantification_query = stage02_quantification_query(self.session);
        self.calculate = base_calculate();
        self.r_calc = r_calculate();
        self.matplot = matplot();
    # analyses:
    def execute_glogNormalization_v1(self,experiment_id_I,concentration_units_I=[],time_course_I=False
                                  ):
        '''glog normalize concentration values using R'''

        print('execute_glogNormalization...')
        
        # get the analysis information

        # query metabolomics data from the experiment
        #if time_course_I:
        #    # get the concentration units
        #    data_transformed = [];
        #    if concentration_units_I:
        #        concentration_units = concentration_units_I;
        #    else:
        #        concentration_units = [];
        #        concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,tp);
        #    for cu in concentration_units:
        #        print 'calculating glogNormalization for concentration_units ' + cu;
        #        data = [];
        #        # get the time-points
        #        time_points = [];
        #        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        #        for tp in time_points:
        #            print 'calculating glogNormalization for time_point ' + tp;
        #            data_tmp = [];
        #            data = self.stage02_quantification_query.get_RExpressionData_experimentIDAndTimePointAndUnitsAndSampleNameShort_dataStage01ReplicatesMI(experiment_id_I, tp, cu);
        #            data.extend(data_tmp)
        #        # call R
        #        data_transformed = [];
        #        concentrations = None;
        #        concentrations_glog = None;
        #        data_glog, concentrations, concentrations_glog = self.r_calc.calculate_glogNormalization(data)
        #        ## plot original values:
        #        self.matplot.densityPlot(concentrations);
        #        self.matplot.densityPlot(concentrations_glog);
        #        # upload data
        #        for d in data:
        #            row = data_stage02_quantification_glogNormalized(experiment_id_I,experiment_id_I, d['sample_name_short'],
        #                                                        d['time_point'],d['component_group_name'],
        #                                                        d['component_name'],d['calculated_concentration'],
        #                                                        d['calculated_concentration_units'] + '_glog_normalized',
        #                                                        True,None);
        #            self.session.add(row);
        #        data_transformed.extend(data_glog);
        #    # commit data to the session every timepoint
        #    self.session.commit();
        #    self.stage02_quantification_query.update_concentrations_dataStage02GlogNormalized(experiment_id_I,experiment_id_I, tp, data_transformed)
        #else:
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        for tp in time_points:
            print('calculating glogNormalization for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            if concentration_units_I:
                concentration_units = concentration_units_I;
            else:
                concentration_units = [];
                concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,tp);
            for cu in concentration_units:
                print('calculating glogNormalization for concentration_units ' + cu);
                data = [];
                data = self.stage02_quantification_query.get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage01ReplicatesMI(experiment_id_I, tp, cu);
                # call R
                data_transformed = [];
                concentrations = None;
                concentrations_glog = None;
                data_glog, concentrations, concentrations_glog = self.r_calc.calculate_glogNormalization(data)
                ## plot original values:
                self.matplot.densityPlot(concentrations);
                self.matplot.densityPlot(concentrations_glog);
                # upload data
                for d in data:
                    row = data_stage02_quantification_glogNormalized(experiment_id_I,experiment_id_I, d['sample_name_short'],
                                                                d['time_point'],d['component_group_name'],
                                                                d['component_name'],d['calculated_concentration'],
                                                                d['calculated_concentration_units'] + '_glog_normalized',
                                                                True,None);
                    self.session.add(row);
                data_transformed.extend(data_glog);
            # commit data to the session every timepoint
            self.session.commit();
            self.stage02_quantification_query.update_concentrations_dataStage02GlogNormalized(experiment_id_I,experiment_id_I, tp, data_transformed)
    def execute_componentNameSpecificNormalization(self,experiment_id_I,sample_name_abbreviations_I=[],cn_normalize_I='glu-L.glu_L_1.Light'):
        '''normalize concentration values to a specific component'''

        print('execute_componentGroupNameSpecificNormalization...')
        
        # query metabolomics data from the experiment
        # get sample name abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I;
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        for sna in sample_name_abbreviations:
            # get time points
            time_points = [];
            time_points = self.stage02_quantification_query.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,sna);
            for tp in time_points:
                print('calculating componentGroupNameSpecificNormalization for time_point ' + tp);
                # get sample_name_shorts
                sample_name_shorts = [];
                sample_name_shorts = self.stage02_quantification_query.get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,sna,tp);
                for sns in sample_name_shorts:
                    data_transformed = [];
                    # get data for componentGroupName to be normalized to
                    cn_conc,cn_conc_units = None, None;
                    cn_conc,cn_conc_units = self.stage02_quantification_query.get_concentrationAndUnits_experimentIDAndTimePointAndSampleNameShortAndComponentName_dataStage01ReplicatesMI(experiment_id_I,tp,sns,cn_normalize_I);
                    # get concentration units...
                    concentration_units = [];
                    concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePointAndSampleNameShort_dataStage01ReplicatesMI(experiment_id_I,tp,sns)
                    for cu in concentration_units:
                        normalize_units = cu + '*' + cn_conc_units + '_' + cn_normalize_I + '-1';
                        print('calculating componentGroupNameSpecificNormalization for concentration_units ' + cu);
                        data = [];
                        data = self.stage02_quantification_query.get_data_experimentIDAndTimePointAndSampleNameShortAndUnits_dataStage01ReplicatesMI(experiment_id_I, tp, sns, cu);
                        # normalize the data
                        concentrations = [];
                        concentrations_norm = [];
                        for i,d in enumerate(data):
                            concentrations.append(d['calculated_concentration']);
                            concentrations_norm.append(d['calculated_concentration']/cn_conc*100);
                            data[i].update({'calculated_concentration_normalized':d['calculated_concentration']/cn_conc*100});
                            data[i].update({'calculated_concentration_units_normalized':normalize_units});
                        ## plot original values:
                        #self.matplot.densityPlot(concentrations);
                        #self.matplot.densityPlot(concentrations_norm);
                        # upload data
                        for d in data:
                            row = data_stage02_quantification_glogNormalized(experiment_id_I, d['sample_name_short'],
                                                                        d['time_point'],d['component_group_name'],
                                                                        d['component_name'],d['calculated_concentration_normalized'],
                                                                        d['calculated_concentration_units_normalized'],
                                                                        True,None);
                            self.session.add(row);
                        data_transformed.extend(data);
            # commit data to the session every sample_name_abbreviation
            self.session.commit();
    def execute_glogNormalization_update_v1(self,experiment_id_I):
        '''glog normalize concentration values using R'''

        print('execute_glogNormalization...')
        
        # query metabolomics data from the experiment
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        for tp in time_points:
            print('calculating glogNormalization for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            for cu in concentration_units:
                print('calculating glogNormalization for concentration_units ' + cu);
                data = [];
                data = self.stage02_quantification_query.get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I, tp, cu);
                # call R
                data_transformed = [];
                concentrations = None;
                concentrations_glog = None;
                data_glog, concentrations, concentrations_glog = self.r_calc.calculate_glogNormalization(data)
                ## plot original values:
                self.matplot.densityPlot(concentrations);
                self.matplot.densityPlot(concentrations_glog);
                # upload data
                data_transformed.extend(data_glog);
            # commit data to the session every timepoint
            self.session.commit();
            self.stage02_quantification_query.update_concentrations_dataStage02GlogNormalized(experiment_id_I, tp, data_transformed)
    def execute_anova_v1(self,experiment_id_I):
        '''execute anova using R'''

        print('execute_anova...')

        # query metabolomics data from glogNormalization
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        for tp in time_points:
            print('calculating anova for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            for cu in concentration_units:
                print('calculating anova for concentration_units ' + cu);
                # get component_names:
                component_names, component_group_names = [],[];
                component_names, component_group_names = self.stage02_quantification_query.get_componentNames_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I, tp, cu);
                for cnt_cn,cn in enumerate(component_names):
                    print('calculating anova for component_names ' + cn);
                    # get data:
                    data = [];
                    data = self.stage02_quantification_query.get_RDataFrame_experimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(experiment_id_I,tp,cu,cn);
                    # call R
                    data_anova,data_pairwise = [],[];
                    data_anova,data_pairwise = self.r_calc.calculate_anova(data);
                    # add data to database
                    for d in data_anova:
                        row1 = data_stage02_quantification_anova(experiment_id_I,experiment_id_I,
                                d['sample_name_abbreviation'],
                                tp,
                                component_group_names[cnt_cn],
                                d['component_name'],
                                d['test_stat'],
                                d['test_description'],
                                d['pvalue'],
                                d['pvalue_corrected'],
                                d['pvalue_corrected_description'],
                                cu,
                                True,None);
                        self.session.add(row1);
                    for d in data_pairwise:
                        row2 = data_stage02_quantification_pairWiseTest(experiment_id_I,
                                d['sample_name_abbreviation_1'],
                                d['sample_name_abbreviation_2'],
                                tp,tp,
                                component_group_names[cnt_cn],
                                d['component_name'],
                                d['mean'],
                                d['test_stat'],
                                d['test_description'],
                                d['pvalue'],
                                d['pvalue_corrected'],
                                d['pvalue_corrected_description'],
                                d['ci_lb'],
                                d['ci_ub'],
                                d['ci_level'],
                                d['fold_change'],
                                cu,
                                True,None);
                        self.session.add(row2);
        self.session.commit();
    def execute_pairwiseTTest_v1(self,experiment_id_I):
        '''execute pairwiseTTest using R'''

        print('execute_pairwiseTTest...')

        # query metabolomics data from glogNormalization
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        for tp in time_points:
            print('calculating pairwiseTTest for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            ## get original concentration units
            #concentration_units_original = [];
            #concentration_units_original = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,tp);
            concentration_units_original = [x.split('_glog_normalized')[0] for x in concentration_units];
            for cu_cnt, cu in enumerate(concentration_units):
                print('calculating pairwiseTTest for concentration_units ' + cu);
                # get component_names:
                component_names, component_group_names = [],[];
                component_names, component_group_names = self.stage02_quantification_query.get_componentNames_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I, tp, cu);
                for cnt_cn,cn in enumerate(component_names):
                    print('calculating pairwiseTTest for component_names ' + cn);
                    # get sample_name_abbreviations:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_experimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(experiment_id_I, tp, cu, cn)
                    for sna_1 in sample_name_abbreviations:
                        for sna_2 in sample_name_abbreviations:
                            print('calculating pairwiseTTest for sample_name_abbreviations ' + sna_1 + ' vs. ' + sna_2);
                            if sna_1 != sna_2:
                            # get data:
                                all_1,all_2 = [],[];
                                data_1,data_2 = [],[];
                                all_1,data_1 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(experiment_id_I,tp,cu,cn,sna_1);
                                all_2,data_2 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(experiment_id_I,tp,cu,cn,sna_2);
                                # call R
                                data_pairwiseTTest = {};
                                if len(data_1)==len(data_2):
                                    data_pairwiseTTest = self.r_calc.calculate_twoSampleTTest(data_1, data_2, alternative_I = "two.sided", mu_I = 0, paired_I="TRUE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                                else:
                                    data_pairwiseTTest = self.r_calc.calculate_twoSampleTTest(data_1, data_2, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                                # Query the original concentration values to calculate the fold change
                                all_1,all_2 = [],[];
                                data_1,data_2 = [],[];  
                                all_1,data_1 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,tp,concentration_units_original[cu_cnt],cn,sna_1);
                                all_2,data_2 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,tp,concentration_units_original[cu_cnt],cn,sna_2);
                                foldChange = numpy.array(data_2).mean()/numpy.array(data_1).mean();
                                # add data to database
                                row2 = data_stage02_quantification_pairWiseTest(experiment_id_I,
                                        sna_1,sna_2,tp,tp,component_group_names[cnt_cn],cn,
                                        data_pairwiseTTest['mean'],
                                        data_pairwiseTTest['test_stat'],
                                        data_pairwiseTTest['test_description'],
                                        data_pairwiseTTest['pvalue'],
                                        data_pairwiseTTest['pvalue_corrected'],
                                        data_pairwiseTTest['pvalue_corrected_description'],
                                        data_pairwiseTTest['ci_lb'],
                                        data_pairwiseTTest['ci_ub'],
                                        data_pairwiseTTest['ci_level'],
                                        foldChange,
                                        cu,True,None);
                                self.session.add(row2);
        self.session.commit();
    def execute_descriptiveStats_v1(self,experiment_id_I):
        '''execute descriptiveStats using R'''

        print('execute_descriptiveStats...')

        # query metabolomics data from glogNormalization
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        for tp in time_points:
            print('calculating descriptiveStats for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            for cu in concentration_units:
                print('calculating descriptiveStats for concentration_units ' + cu);
                # get component_names:
                component_names, component_group_names = [],[];
                component_names, component_group_names = self.stage02_quantification_query.get_componentNames_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I, tp, cu);
                for cnt_cn,cn in enumerate(component_names):
                    print('calculating descriptiveStats for component_names ' + cn);
                    data_plot_mean = [];
                    data_plot_var = [];
                    data_plot_ci = [];
                    data_plot_sna = [];
                    data_plot_component_names = [];
                    data_plot_calculated_concentration_units = [];
                    data_plot_data = [];
                    # get sample_name_abbreviations:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_experimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(experiment_id_I, tp, cu, cn)
                    for sna in sample_name_abbreviations:
                        print('calculating descriptiveStats for sample_name_abbreviations ' + sna);
                        # get data:
                        all_1,all_2 = [],[];
                        all_1,data_1 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(experiment_id_I,tp,cu,cn,sna);
                        # call R
                        data_TTest = {};
                        data_TTest = self.r_calc.calculate_oneSampleTTest(data_1, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                        #TODO:
                        # calculate the interquartile range
                        min_O, max_O, median_O, iq_1_O, iq_2_O=self.calculate.calculate_interquartiles(data_1);
                        # record data for plotting
                        data_plot_mean.append(data_TTest['mean']);
                        data_plot_var.append(data_TTest['var']);
                        data_plot_ci.append([data_TTest['ci_lb'],data_TTest['ci_lb']]);
                        data_plot_data.append(data_1);
                        data_plot_sna.append(sna);
                        data_plot_component_names.append(cn);
                        data_plot_calculated_concentration_units.append(cu);
                        # add data to database
                        row2 = data_stage02_quantification_descriptiveStats(experiment_id_I,
                                sna,tp,component_group_names[cnt_cn],cn,
                                data_TTest['mean'],
                                data_TTest['var'],
                                data_TTest['cv'],
                                data_TTest['n'],
                                data_TTest['test_stat'],
                                data_TTest['test_description'],
                                data_TTest['pvalue'],
                                data_TTest['pvalue_corrected'],
                                data_TTest['pvalue_corrected_description'],
                                data_TTest['ci_lb'],
                                data_TTest['ci_ub'],
                                data_TTest['ci_level'],
                                cu,True,None);
                        self.session.add(row2);
                    ## visualize the stats:
                    #self.matplot.barPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_mean,data_plot_var);
                    #self.matplot.boxAndWhiskersPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_data,data_plot_mean,data_plot_ci);
        self.session.commit();
    def execute_pca_v1(self,experiment_id_I):
        '''execute pca using R'''

        print('execute_pca...')

        # query metabolomics data from glogNormalization
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        for tp in time_points:
            print('calculating pca for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            for cu in concentration_units:
                print('calculating pca for concentration_units ' + cu);
                # get data:
                data = [];
                data = self.stage02_quantification_query.get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I,tp,cu);
                # call R
                data_scores,data_loadings = [],[];
                data_scores,data_loadings = self.r_calc.calculate_pca_prcomp(data, retx_I = "TRUE", center_I = "FALSE", na_action_I='na.omit',scale_I="TRUE");
                ## plot the data:
                ## scores
                #title,xlabel,ylabel,x_data,y_data,text_labels,samples = self.matplot._extractPCAScores(data_scores);
                #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                ## loadings
                #title,xlabel,ylabel,x_data,y_data,text_labels = self.matplot._extractPCALoadings(data_loadings);
                #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                # add data to database
                for d in data_scores:
                    row1 = data_stage02_quantification_pca_scores(experiment_id_I,
                            d['sample_name_short'],
                            tp,
                            d['score'],
                            d['axis'],
                            d['var_proportion'],
                            d['var_cumulative'],
                            cu,
                            True,None);
                    self.session.add(row1);
                for d in data_loadings:
                    row2 = data_stage02_quantification_pca_loadings(experiment_id_I,
                            tp,
                            d['component_group_name'],
                            d['component_name'],
                            d['loadings'],
                            d['axis'],
                            cu,
                            True,None);
                    self.session.add(row2);
        self.session.commit();
    def execute_volcanoPlot_v1(self,experiment_id_I):
        '''generate a volcano plot from pairwiseTest table'''

        print('execute_volcanoPlot...')
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02pairWiseTest(experiment_id_I);
        for tp in time_points:
            print('generating a volcano plot for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02pairWiseTest(experiment_id_I,tp);
            #concentration_units = ['mM_glog_normalized']
            for cu in concentration_units:
                print('generating a volcano plot for concentration_units ' + cu);
                # get sample_name_abbreviations:
                sample_name_abbreviations = [];
                sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_experimentIDAndTimePointAndUnits_dataStage02pairWiseTest(experiment_id_I, tp, cu)
                for sna_1 in sample_name_abbreviations:
                    for sna_2 in sample_name_abbreviations:
                        if sna_1 != sna_2:
                            print('generating a volcano plot for sample_name_abbreviation ' + sna_1 + ' vs. ' + sna_2);
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
                            self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
    def execute_pcaPlot_v1(self,experiment_id_I):
        '''generate a pca plot'''

        print('execute_pcaPlot...')
        # query metabolomics data from pca_scores and pca_loadings
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02Scores(experiment_id_I);
        for tp in time_points:
            print('plotting pca for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02Scores(experiment_id_I,tp);
            for cu in concentration_units:
                if cu=='height_ratio_glog_normalized': continue; # skip for now...
                print('plotting pca for concentration_units ' + cu);
                # get data:
                data_scores,data_loadings = [],[];
                data_scores,data_loadings = self.stage02_quantification_query.get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage02ScoresLoadings(experiment_id_I,tp,cu);
                # plot the data:
                PCs = [[1,2],[1,3],[2,3]];
                for PC in PCs:
                    # scores
                    title,xlabel,ylabel,x_data,y_data,text_labels,samples = self.matplot._extractPCAScores(data_scores,PC[0],PC[1]);
                    self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                    # loadings
                    title,xlabel,ylabel,x_data,y_data,text_labels = self.matplot._extractPCALoadings(data_loadings,PC[0],PC[1]);
                    self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
    def execute_boxAndWhiskersPlot_v1(self,experiment_id_I,component_names_I=[]):
        '''generate a boxAndWhiskers plot from descriptiveStats table'''

        print('execute_boxAndWhiskersPlot...')
        # query metabolomics data from glogNormalization
        # get time points
        time_points = [];
        time_points = self.stage02_quantification_query.get_timePoint_experimentID_dataStage02GlogNormalized(experiment_id_I);
        for tp in time_points:
            print('calculating descriptiveStats for time_point ' + tp);
            data_transformed = [];
            # get concentration units...
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage02GlogNormalized(experiment_id_I,tp);
            for cu in concentration_units:
                print('calculating descriptiveStats for concentration_units ' + cu);
                # get component_names:
                component_names, component_group_names = [],[];
                component_names, component_group_names = self.stage02_quantification_query.get_componentNames_experimentIDAndTimePointAndUnits_dataStage02GlogNormalized(experiment_id_I, tp, cu);
                if component_names_I:
                    component_names_ind = [i for i,x in enumerate(component_names) if x in component_names_I];
                    component_names_cpy = copy.copy(component_names);
                    component_group_names = copy.copy(component_group_names);
                    component_names = [x for i,x in enumerate(component_names) if i in component_names_ind]
                    component_group_names = [x for i,x in enumerate(component_group_names) if i in component_names_ind]
                for cnt_cn,cn in enumerate(component_names):
                    print('calculating descriptiveStats for component_names ' + cn);
                    data_plot_mean = [];
                    data_plot_var = [];
                    data_plot_ci = [];
                    data_plot_sna = [];
                    data_plot_component_names = [];
                    data_plot_calculated_concentration_units = [];
                    data_plot_data = [];
                    # get sample_name_abbreviations:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_experimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(experiment_id_I, tp, cu, cn)
                    for sna in sample_name_abbreviations:
                        print('calculating descriptiveStats for sample_name_abbreviations ' + sna);
                        # get data:
                        all_1,data_1 = [],[];
                        all_1,data_1 = self.stage02_quantification_query.get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(experiment_id_I,tp,cu,cn,sna);
                        # call R
                        data_TTest = {};
                        data_TTest = self.r_calc.calculate_oneSampleTTest(data_1, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                        # record data for plotting
                        data_plot_mean.append(data_TTest['mean']);
                        data_plot_var.append(data_TTest['var']);
                        data_plot_ci.append([data_TTest['ci_lb'],data_TTest['ci_lb']]);
                        data_plot_data.append(data_1);
                        data_plot_sna.append(sna);
                        data_plot_component_names.append(cn);
                        data_plot_calculated_concentration_units.append(cu);
                    # visualize the stats:
                    #self.matplot.barPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_mean,data_plot_var);
                    self.matplot.boxAndWhiskersPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_data,data_plot_mean,data_plot_ci);
    # data_stage02_quantification initializations
    def drop_dataStage02_quantification(self):
        try:
            data_stage02_quantification_glogNormalized.__table__.drop(engine,True);
            data_stage02_quantification_anova.__table__.drop(engine,True);
            data_stage02_quantification_pairWiseTest.__table__.drop(engine,True);
            data_stage02_quantification_descriptiveStats.__table__.drop(engine,True);
            data_stage02_quantification_pca_scores.__table__.drop(engine,True);
            data_stage02_quantification_pca_loadings.__table__.drop(engine,True);
            data_stage02_quantification_heatmap.__table__.drop(engine,True);
            data_stage02_quantification_dendrogram.__table__.drop(engine,True);
            #data_stage02_quantification_svm.__table__.drop(engine,True);
            data_stage02_quantification_analysis.__table__.drop(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_glogNormalized).filter(data_stage02_quantification_glogNormalized.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_anova).filter(data_stage02_quantification_anova.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_pairWiseTest).filter(data_stage02_quantification_pairWiseTest.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_descriptiveStats).filter(data_stage02_quantification_descriptiveStats.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_pca_scores).filter(data_stage02_quantification_pca_scores.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_pca_loadings).filter(data_stage02_quantification_pca_loadings.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                #reset = self.session.query(data_stage02_quantification_svm).filter(data_stage02_quantification_svm.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                #reset = self.session.query(data_stage02_quantification_analysis).filter(data_stage02_quantification_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_heatmap).filter(data_stage02_quantification_heatmap.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_dendrogram).filter(data_stage02_quantification_dendrogram.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_glogNormalized).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_anova).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_pairWiseTest).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_descriptiveStats).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_pca_scores).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_pca_loadings).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_heatmap).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_quantification_dendrogram).delete(synchronize_session=False);
                #reset = self.session.query(data_stage02_quantification_svm).delete(synchronize_session=False);
                #reset = self.session.query(data_stage02_quantification_analysis).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_glogNormalized(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_glogNormalized).filter(data_stage02_quantification_glogNormalized.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_glogNormalized).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_pairWiseTest(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_pairWiseTest).filter(data_stage02_quantification_pairWiseTest.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_pairWiseTest).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_descriptiveStats(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_descriptiveStats).filter(data_stage02_quantification_descriptiveStats.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_descriptiveStats).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_anova(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_anova).filter(data_stage02_quantification_anova.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_anova).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_pca_scores(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_pca_scores).filter(data_stage02_quantification_pca_scores.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_pca_scores).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_pca_loadings(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_pca_loadings).filter(data_stage02_quantification_pca_loadings.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_pca_loadings).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_heatmap(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_heatmap).filter(data_stage02_quantification_heatmap.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_heatmap).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_quantification_dendrogram(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_quantification_dendrogram).filter(data_stage02_quantification_dendrogram.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_quantification_dendrogram).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage02_quantification(self):
        try:
            data_stage02_quantification_glogNormalized.__table__.create(engine,True);
            data_stage02_quantification_anova.__table__.create(engine,True);
            data_stage02_quantification_pairWiseTest.__table__.create(engine,True);
            data_stage02_quantification_descriptiveStats.__table__.create(engine,True);
            data_stage02_quantification_pca_scores.__table__.create(engine,True);
            data_stage02_quantification_pca_loadings.__table__.create(engine,True);
            data_stage02_quantification_heatmap.__table__.create(engine,True);
            data_stage02_quantification_dendrogram.__table__.create(engine,True);
            #data_stage02_quantification_svm.__table__.create(engine,True);
            data_stage02_quantification_analysis.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    #TODO
    def execute_svm(self,experiment_id_I):
        '''execute svm using R'''

        print('execute_svm...')

    def execute_glogNormalization(self,analysis_id_I,concentration_units_I=[]):
        '''glog normalize concentration values using R'''

        print('execute_glogNormalization...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data_transformed = [];
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            for row in analysis_info:
                concentration_units_tmp = []
                concentration_units_tmp = self.stage02_quantification_query.get_concentrationUnits_experimentID_dataStage01ReplicatesMI(row['experiment_id']);
                concentration_units.extend(concentration_units_tmp)
            concentration_units = list(set(concentration_units));
        for cu in concentration_units:
            print('calculating glogNormalization for concentration_units ' + cu);
            data = [];
            # get all of the samples in the simulation
            for row in analysis_info:
                data_tmp = [];
                data_tmp = self.stage02_quantification_query.get_RExpressionData_AnalysisIDAndExperimentIDAndTimePointAndUnitsAndSampleNameShort_dataStage01ReplicatesMI(analysis_id_I,row['experiment_id'], row['time_point'], cu, row['sample_name_short']);
                data.extend(data_tmp)
            # call R
            concentrations = None;
            concentrations_glog = None;
            data_glog, concentrations, concentrations_glog = self.r_calc.calculate_glogNormalization(data)
            for i,d in enumerate(data_glog):
                data_glog[i]['calculated_concentration_units']=cu+'_glog_normalized'
            ## plot original values:
            #self.matplot.densityPlot(concentrations);
            #self.matplot.densityPlot(concentrations_glog);
            # upload data
            for d in data:
                row = None;
                row = data_stage02_quantification_glogNormalized(analysis_id_I,d['experiment_id'], d['sample_name_short'],
                                                            d['time_point'],d['component_group_name'],
                                                            d['component_name'],d['calculated_concentration'],
                                                            d['calculated_concentration_units'] + '_glog_normalized',
                                                            True,None);
                self.session.add(row);
            data_transformed.extend(data_glog);
        # commit data to the session every timepoint
        self.session.commit();
        self.stage02_quantification_query.update_concentrations_dataStage02GlogNormalized(analysis_id_I, data_transformed)
    def execute_pca(self,analysis_id_I,experiment_ids_I=[],time_points_I=[],concentration_units_I=[]):
        '''execute pca using R'''

        print('execute_pca...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from glogNormalization
        # get concentration units
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02GlogNormalized(analysis_id_I);
        for cu in concentration_units:
            print('calculating pca for concentration_units ' + cu);
            data = [];
            # get data:
            data = self.stage02_quantification_query.get_RExpressionData_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I,cu);
            # call R
            data_scores,data_loadings = [],[];
            data_scores,data_loadings = self.r_calc.calculate_pca_prcomp(data, retx_I = "TRUE", center_I = "FALSE", na_action_I='na.omit',scale_I="TRUE");
            ## plot the data:
            ## scores
            #title,xlabel,ylabel,x_data,y_data,text_labels,samples = self.matplot._extractPCAScores(data_scores);
            #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
            ## loadings
            #title,xlabel,ylabel,x_data,y_data,text_labels = self.matplot._extractPCALoadings(data_loadings);
            #self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
            # add data to database
            for d in data_scores:
                row1 = data_stage02_quantification_pca_scores(analysis_id_I,
                        #d['experiment_id'],
                        d['sample_name_short'],
                        #d['time_point'],
                        d['score'],
                        d['axis'],
                        d['var_proportion'],
                        d['var_cumulative'],
                        cu,
                        True,None);
                self.session.add(row1);
            for d in data_loadings:
                row2 = data_stage02_quantification_pca_loadings(analysis_id_I,
                        #d['experiment_id'],
                        #d['time_point'],
                        d['component_group_name'],
                        d['component_name'],
                        d['loadings'],
                        d['axis'],
                        cu,
                        True,None);
                self.session.add(row2);
        self.session.commit();
    def execute_pcaPlot(self,analysis_id_I,experiment_ids_I=[],time_points_I=[],concentration_units_I=[]):
        '''generate a pca plot'''

        print('execute_pcaPlot...')
        # query metabolomics data from pca_scores and pca_loadings
        # get concentration units...
        concentration_units = [];
        concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02Scores(analysis_id_I);
        for cu in concentration_units:
            if cu=='height_ratio_glog_normalized' or cu=='height_ratio': continue; # skip for now...
            print('plotting pca for concentration_units ' + cu);
            # get data:
            data_scores,data_loadings = [],[];
            data_scores,data_loadings = self.stage02_quantification_query.get_RExpressionData_analysisIDAndUnits_dataStage02ScoresLoadings(analysis_id_I,cu);
            # plot the data:
            PCs = [[1,2],[1,3],[2,3]];
            for PC in PCs:
                # scores
                title,xlabel,ylabel,x_data,y_data,text_labels,samples = self.matplot._extractPCAScores(data_scores,PC[0],PC[1]);
                self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
                # loadings
                title,xlabel,ylabel,x_data,y_data,text_labels = self.matplot._extractPCALoadings(data_loadings,PC[0],PC[1]);
                self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
    def execute_descriptiveStats(self,analysis_id_I,experiment_ids_I=[],time_points_I=[],concentration_units_I=[],component_names_I=[]):
        '''execute descriptiveStats using R'''

        #print 'execute_descriptiveStats...'
        
        # get the experiment ids
        if experiment_ids_I:
            experiment_ids = experiment_ids_I;
        else:
            experiment_ids = [];
            experiment_ids = self.stage02_quantification_query.get_experimentID_analysisID_dataStage02GlogNormalized(analysis_id_I);
        for experiment_id in experiment_ids:
            # get time points
            if time_points_I:
                time_points=time_points_I;
            else:
                time_points = [];
                time_points = self.stage02_quantification_query.get_timePoint_analysisIDAndExperimentID_dataStage02GlogNormalized(analysis_id_I,experiment_id);
            for tp in time_points:
                print('calculating descriptiveStats for time_point ' + tp);
                data_transformed = [];
                # get concentration units...
                if concentration_units_I:
                    concentration_units = concentration_units_I;
                else:
                    concentration_units = [];
                    concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisIDAndExperimentIDAndTimePoint_dataStage02GlogNormalized(analysis_id_I,experiment_id,tp);
                for cu in concentration_units:
                    print('calculating descriptiveStats for concentration_units ' + cu);
                    # get component_names:
                    component_names, component_group_names = [],[];
                    component_names, component_group_names = self.stage02_quantification_query.get_componentNames_analysisIDAndExperimentIDAndTimePointAndUnits_dataStage02GlogNormalized(analysis_id_I,experiment_id, tp, cu);
                    if component_names_I:
                        component_names_ind = [i for i,x in enumerate(component_names) if x in component_names_I];
                        component_names_cpy = copy.copy(component_names);
                        component_group_names = copy.copy(component_group_names);
                        component_names = [x for i,x in enumerate(component_names) if i in component_names_ind]
                        component_group_names = [x for i,x in enumerate(component_group_names) if i in component_names_ind]
                    for cnt_cn,cn in enumerate(component_names):
                        print('calculating descriptiveStats for component_names ' + cn);
                        data_plot_mean = [];
                        data_plot_var = [];
                        data_plot_ci = [];
                        data_plot_sna = [];
                        data_plot_component_names = [];
                        data_plot_calculated_concentration_units = [];
                        data_plot_data = [];
                        # get sample_name_abbreviations:
                        sample_name_abbreviations = [];
                        sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_analysisIDAndExperimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(analysis_id_I,experiment_id, tp, cu, cn)
                        for sna in sample_name_abbreviations:
                            print('calculating descriptiveStats for sample_name_abbreviations ' + sna);
                            # get data:
                            all_1,data_1 = [],[];
                            all_1,data_1 = self.stage02_quantification_query.get_RDataList_analysisIDAndExperimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(analysis_id_I,experiment_id,tp,cu,cn,sna);
                            if len(data_1)<2: continue
                            # call R
                            data_TTest = {};
                            data_TTest = self.r_calc.calculate_oneSampleTTest(data_1, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                            #TODO:
                            # calculate the interquartile range
                            min_O, max_O, median_O, iq_1_O, iq_3_O=self.calculate.calculate_interquartiles(data_1);
                            # record data for plotting
                            data_plot_mean.append(data_TTest['mean']);
                            data_plot_var.append(data_TTest['var']);
                            data_plot_ci.append([data_TTest['ci_lb'],data_TTest['ci_lb']]);
                            data_plot_data.append(data_1);
                            data_plot_sna.append(sna);
                            data_plot_component_names.append(cn);
                            data_plot_calculated_concentration_units.append(cu);
                            # add data to database
                            row2 = data_stage02_quantification_descriptiveStats(analysis_id_I,
                                    experiment_id,
                                    sna,tp,component_group_names[cnt_cn],cn,
                                    data_TTest['mean'],
                                    data_TTest['var'],
                                    data_TTest['cv'],
                                    data_TTest['n'],
                                    data_TTest['test_stat'],
                                    data_TTest['test_description'],
                                    data_TTest['pvalue'],
                                    data_TTest['pvalue_corrected'],
                                    data_TTest['pvalue_corrected_description'],
                                    data_TTest['ci_lb'],
                                    data_TTest['ci_ub'],
                                    data_TTest['ci_level'],
                                    min_O,max_O,median_O,iq_1_O,iq_3_O,
                                    cu,True,None);
                            self.session.add(row2);
                        ## visualize the stats:
                        #self.matplot.barPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_mean,data_plot_var);
                        #self.matplot.boxAndWhiskersPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_data,data_plot_mean,data_plot_ci);
        self.session.commit();
    def execute_anova(self,analysis_id_I,concentration_units_I=[],component_names_I=[]):
        '''execute anova using R'''

        print('execute_anova...')
        
        # query metabolomics data from glogNormalization
        # get concentration units
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02GlogNormalized(analysis_id_I);
        for cu in concentration_units:
            print('calculating anova for concentration_units ' + cu);
            ## get the experiment_ids
            #if experiment_ids_I:
            #    experiment_ids = experiment_ids_I;
            #else:
            #    experiment_ids = [];
            #    experiment_ids = self.stage02_quantification_query.get_experimentID_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I,cu);
            #for experiment_id in experiment_ids:
            #    print 'calculating anova for experiment_ids ' + experiment_id;
            #    # get the time_points
            #    if time_points_I:
            #        time_points=time_points_I;
            #    else:
            #        time_points = [];
            #        time_points = self.stage02_quantification_query.get_timePoint_analysisIDAndExperimentIDAndUnits_dataStage02GlogNormalized(analysis_id_I,experiment_id,cu);
            #    for tp in time_points:
            #        print 'calculating anova for time_points ' + tp;
            #        # get component_names:
            #        if component_names_I:
            #            data = [];
            #            component_names = [cn[0] for cn in component_names_I]
            #            component_group_names = [cn[1] for cn in component_names_I]
            #        else:
            #            component_names, component_group_names = [],[];
            #            component_names, component_group_names = self.stage02_quantification_query.get_componentNames_analysisIDAndExperimentIDAndTimePointAndUnits_dataStage02GlogNormalized(analysis_id_I,experiment_id, tp, cu);
            #        for cnt_cn,cn in enumerate(component_names):
            #            print 'calculating anova for component_names ' + cn;
            #            # get data:
            #            data_tmp = [];
            #            data_tmp = self.stage02_quantification_query.get_RDataFrame_analysisIDAndExperimentIDAndTimePointAndUnitsAndComponentNames_dataStage02GlogNormalized(analysis_id_I,experiment_id,tp,cu,cn);
            #            data.extend(data_tmp);
            # get component_names:
            component_names, component_group_names = [],[];
            component_names, component_group_names = self.stage02_quantification_query.get_componentNames_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I, cu);
            if component_names_I:
                component_names_ind = [i for i,x in enumerate(component_names) if x in component_names_I];
                component_names_cpy = copy.copy(component_names);
                component_group_names = copy.copy(component_group_names);
                component_names = [x for i,x in enumerate(component_names) if i in component_names_ind]
                component_group_names = [x for i,x in enumerate(component_group_names) if i in component_names_ind]
            for cnt_cn,cn in enumerate(component_names):
                print('calculating anova for component_names ' + cn);
                # get data:
                data = [];
                data = self.stage02_quantification_query.get_RDataFrame_analysisIDAndUnitsAndComponentNames_dataStage02GlogNormalized(analysis_id_I,cu,cn);
                # call R
                data_anova,data_pairwise = [],[];
                data_anova,data_pairwise = self.r_calc.calculate_anova(data);
                # add data to database
                for d in data_anova:
                    row1 = data_stage02_quantification_anova(analysis_id_I,
                            d['sample_name_abbreviation'],
                            component_group_names[cnt_cn],
                            d['component_name'],
                            d['test_stat'],
                            d['test_description'],
                            d['pvalue'],
                            d['pvalue_corrected'],
                            d['pvalue_corrected_description'],
                            cu,
                            True,None);
                    self.session.add(row1);
                for d in data_pairwise:
                    row2 = data_stage02_quantification_pairWiseTest(analysis_id_I,
                            d['sample_name_abbreviation_1'],
                            d['sample_name_abbreviation_2'],
                            component_group_names[cnt_cn],
                            d['component_name'],
                            d['mean'],
                            d['test_stat'],
                            d['test_description'],
                            d['pvalue'],
                            d['pvalue_corrected'],
                            d['pvalue_corrected_description'],
                            d['ci_lb'],
                            d['ci_ub'],
                            d['ci_level'],
                            d['fold_change'],
                            cu,
                            True,None);
                    self.session.add(row2);
        self.session.commit();
    def execute_pairwiseTTest(self,analysis_id_I,concentration_units_I=[],component_names_I=[],redundancy_I=True):
        '''execute pairwiseTTest using R'''

        print('execute_pairwiseTTest...')

        # query metabolomics data from glogNormalization
        # get concentration units
        if concentration_units_I:
            concentration_units = concentration_units_I;
            concentration_units_original = [x.split('_glog_normalized')[0] for x in concentration_units];
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02GlogNormalized(analysis_id_I);
            ## get original concentration units
            #concentration_units_original = [];
            #concentration_units_original = self.stage02_quantification_query.get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,tp);
            concentration_units_original = [x.split('_glog_normalized')[0] for x in concentration_units];
        for cu_cnt,cu in enumerate(concentration_units):
            print('calculating pairwiseTTest for concentration_units ' + cu);
            data = [];
            # get component_names:
            component_names, component_group_names = [],[];
            component_names, component_group_names = self.stage02_quantification_query.get_componentNames_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I, cu);
            if component_names_I:
                component_names_ind = [i for i,x in enumerate(component_names) if x in component_names_I];
                component_names_cpy = copy.copy(component_names);
                component_group_names = copy.copy(component_group_names);
                component_names = [x for i,x in enumerate(component_names) if i in component_names_ind]
                component_group_names = [x for i,x in enumerate(component_group_names) if i in component_names_ind]
            for cnt_cn,cn in enumerate(component_names):
                print('calculating pairwiseTTest for component_names ' + cn);
                # get sample_name_abbreviations:
                sample_name_abbreviations = [];
                sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_analysisIDAndUnitsAndComponentNames_dataStage02GlogNormalized(analysis_id_I,cu, cn)
                for sna_1_cnt,sna_1 in enumerate(sample_name_abbreviations):
                    if redundancy_I: list_2 = sample_name_abbreviations;
                    else: list_2 = sample_name_abbreviations[sna_1+1:];
                    for cnt,sna_2 in enumerate(list_2):
                        if redundancy_I: sna_2_cnt = cnt;
                        else: sna_2_cnt = sna_1_cnt+cnt+1;
                        if sna_1 != sna_2:
                            print('calculating pairwiseTTest for sample_name_abbreviations ' + sna_1 + ' vs. ' + sna_2);
                            # get data:
                            all_1,all_2 = [],[];
                            data_1,data_2 = [],[];
                            all_1,data_1 = self.stage02_quantification_query.get_RDataList_analysisIDAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(analysis_id_I,cu,cn,sna_1);
                            all_2,data_2 = self.stage02_quantification_query.get_RDataList_analysisIDAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(analysis_id_I,cu,cn,sna_2);
                            # call R
                            data_pairwiseTTest = {};
                            if len(data_1)==len(data_2):
                                data_pairwiseTTest = self.r_calc.calculate_twoSampleTTest(data_1, data_2, alternative_I = "two.sided", mu_I = 0, paired_I="TRUE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                            else:
                                data_pairwiseTTest = self.r_calc.calculate_twoSampleTTest(data_1, data_2, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                            # Query the original concentration values to calculate the fold change
                            all_1,all_2 = [],[];
                            data_1,data_2 = [],[];  
                            all_1,data_1 = self.stage02_quantification_query.get_RDataList_analysisIDAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage01ReplicatesMI(analysis_id_I,concentration_units_original[cu_cnt],cn,sna_1);
                            all_2,data_2 = self.stage02_quantification_query.get_RDataList_analysisIDAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage01ReplicatesMI(analysis_id_I,concentration_units_original[cu_cnt],cn,sna_2);
                            foldChange = numpy.array(data_2).mean()/numpy.array(data_1).mean();
                            # add data to database
                            row2 = data_stage02_quantification_pairWiseTest(
                                    analysis_id_I,
                                    sna_1,sna_2,
                                    component_group_names[cnt_cn],cn,
                                    data_pairwiseTTest['mean'],
                                    data_pairwiseTTest['test_stat'],
                                    data_pairwiseTTest['test_description'],
                                    data_pairwiseTTest['pvalue'],
                                    data_pairwiseTTest['pvalue_corrected'],
                                    data_pairwiseTTest['pvalue_corrected_description'],
                                    data_pairwiseTTest['ci_lb'],
                                    data_pairwiseTTest['ci_ub'],
                                    data_pairwiseTTest['ci_level'],
                                    foldChange,
                                    cu,True,None);
                            self.session.add(row2);
        self.session.commit();
    def execute_volcanoPlot(self,analysis_id_I,concentration_units_I=[]):
        '''generate a volcano plot from pairwiseTest table'''

        print('execute_volcanoPlot...')
        # query metabolomics data from glogNormalization
        # get concentration units
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02pairWiseTest(analysis_id_I);
        for cu in concentration_units:
            print('generating a volcano plot for concentration_units ' + cu);
            data = [];
            # get sample_name_abbreviations:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_analysisIDAndUnits_dataStage02pairWiseTest(analysis_id_I, cu)
            for sna_1_cnt,sna_1 in enumerate(sample_name_abbreviations):
                for sna_2_cnt,sna_2 in enumerate(sample_name_abbreviations[sna_1_cnt:]):
                    if sna_1 != sna_2:
                        print('generating a volcano plot for sample_name_abbreviation ' + sna_1 + ' vs. ' + sna_2);
                        # get data:
                        data_1 = [];
                        data_1 = self.stage02_quantification_query.get_RDataList_analysisIDAndUnitsAndSampleNameAbbreviations_dataStage02pairWiseTest(analysis_id_I,cu,sna_1,sna_2);
                        # plot the data
                        title = sna_1 + ' vs. ' + sna_2;
                        xlabel = 'Fold Change [log2(FC)]';
                        ylabel = 'Probability [-log10(P)]';
                        x_data = [d['fold_change_log2'] for d in data_1];
                        y_data = [d['pvalue_corrected_negLog10'] for d in data_1];
                        text_labels = [t['component_group_name'] for t in data_1];
                        self.matplot.volcanoPlot(title,xlabel,ylabel,x_data,y_data,text_labels);
    def execute_boxAndWhiskersPlot(self,analysis_id_I,concentration_units_I=[],component_names_I=[]):
        '''generate a boxAndWhiskers plot from descriptiveStats table'''

        # get concentration units...
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02GlogNormalized(analysis_id_I);
        for cu in concentration_units:
            print('calculating descriptiveStats for concentration_units ' + cu);
            # get component_names:
            component_names, component_group_names = [],[];
            component_names, component_group_names = self.stage02_quantification_query.get_componentNames_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I, cu);
            if component_names_I:
                component_names_ind = [i for i,x in enumerate(component_names) if x in component_names_I];
                component_names_cpy = copy.copy(component_names);
                component_group_names = copy.copy(component_group_names);
                component_names = [x for i,x in enumerate(component_names) if i in component_names_ind]
                component_group_names = [x for i,x in enumerate(component_group_names) if i in component_names_ind]
            for cnt_cn,cn in enumerate(component_names):
                print('calculating descriptiveStats for component_names ' + cn);
                data_plot_mean = [];
                data_plot_var = [];
                data_plot_ci = [];
                data_plot_sna = [];
                data_plot_component_names = [];
                data_plot_calculated_concentration_units = [];
                data_plot_data = [];
                # get sample_name_abbreviations:
                sample_name_abbreviations = [];
                sample_name_abbreviations = self.stage02_quantification_query.get_sampleNameAbbreviations_analysisIDAndUnitsAndComponentNames_dataStage02GlogNormalized(analysis_id_I, cu, cn)
                for sna in sample_name_abbreviations:
                    print('calculating descriptiveStats for sample_name_abbreviations ' + sna);
                    # get data:
                    all_1,data_1 = [],[];
                    all_1,data_1 = self.stage02_quantification_query.get_RDataList_analysisIDAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage02GlogNormalized(analysis_id_I,cu,cn,sna);
                    # call R
                    data_TTest = {};
                    data_TTest = self.r_calc.calculate_oneSampleTTest(data_1, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                    # record data for plotting
                    data_plot_mean.append(data_TTest['mean']);
                    data_plot_var.append(data_TTest['var']);
                    data_plot_ci.append([data_TTest['ci_lb'],data_TTest['ci_lb']]);
                    data_plot_data.append(data_1);
                    data_plot_sna.append(sna);
                    data_plot_component_names.append(cn);
                    data_plot_calculated_concentration_units.append(cu);
                # visualize the stats:
                #self.matplot.barPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_mean,data_plot_var);
                self.matplot.boxAndWhiskersPlot(data_plot_component_names[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_data,data_plot_mean,data_plot_ci);
    def execute_heatmap(self, analysis_id_I,concentration_units_I=[],
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete'):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');
        # get the analysis information
        analysis_info = [];
        analysis_info = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data_transformed = [];
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02GlogNormalized(analysis_id_I);
        for cu in concentration_units:
            print('generating a heatmap for concentration_units ' + cu);
            # get the data
            data = [];
            data = self.stage02_quantification_query.get_RExpressionData_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I,cu);
            # find unique
            component_group_names = [x['component_group_name'] for x in data];
            component_group_names_unique = list(set(component_group_names));
            component_group_names_unique.sort();
            sample_name_shorts = [x['sample_name_short'] for x in data];
            sample_name_short_unique = list(set(sample_name_shorts));
            sample_name_short_unique.sort();
            # generate the frequency matrix data structure (sample x met)
            data_O = numpy.zeros((len(sample_name_short_unique),len(component_group_names_unique)));
            col_cnt = 0;
            # order 2: groups each lineage by met (sample x met)
            for sample_name_short_cnt,sample_name_short in enumerate(sample_name_short_unique): #all lineages for sample j / met i
                for component_group_name_cnt,component_group_name in enumerate(component_group_names_unique): #all mets i for sample j
                    for row in data:
                        if row['sample_name_short'] == sample_name_short and row['component_group_name'] == component_group_name:
                            data_O[sample_name_short_cnt,component_group_name_cnt] = row['calculated_concentration'];
                col_cnt+=1;
            # generate the clustering for the heatmap
            heatmap_O = [];
            dendrogram_col_O = {};
            dendrogram_row_O = {};
            heatmap_O,dendrogram_col_O,dendrogram_row_O = self.calculate.heatmap(data_O,sample_name_short_unique,component_group_names_unique,
                    row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                    col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I);
            # add data to to the database for the heatmap
            for d in heatmap_O:
                row = None;
                row = data_stage02_quantification_heatmap(
                    analysis_id_I,
                    d['col_index'],
                    d['row_index'],
                    d['value'],
                    d['col_leaves'],
                    d['row_leaves'],
                    d['col_label'],
                    d['row_label'],
                    d['col_pdist_metric'],
                    d['row_pdist_metric'],
                    d['col_linkage_method'],
                    d['row_linkage_method'],
                    cu, True, None);
                self.session.add(row);
            # add data to the database for the dendrograms
            row = None;
            row = data_stage02_quantification_dendrogram(
                analysis_id_I,
                dendrogram_col_O['leaves'],
                dendrogram_col_O['icoord'],
                dendrogram_col_O['dcoord'],
                dendrogram_col_O['ivl'],
                dendrogram_col_O['colors'],
                dendrogram_col_O['pdist_metric'],
                dendrogram_col_O['pdist_metric'],
                cu, True, None);
            self.session.add(row);
            row = None;
            row = data_stage02_quantification_dendrogram(
                analysis_id_I,
                dendrogram_row_O['leaves'],
                dendrogram_row_O['icoord'],
                dendrogram_row_O['dcoord'],
                dendrogram_row_O['ivl'],
                dendrogram_row_O['colors'],
                dendrogram_row_O['pdist_metric'],
                dendrogram_row_O['pdist_metric'],
                cu, True, None);
            self.session.add(row);
        self.session.commit();
    # TODO: test
    def execute_glogNormalization_update(self,analysis_id_I):
        '''glog normalize concentration values using R'''

        print('execute_glogNormalization...')
        
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data_transformed = [];
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            concentration_units = self.stage02_quantification_query.get_concentrationUnits_analysisID_dataStage02GlogNormalized(analysis_id_I);
        for cu in concentration_units:
            print('calculating glogNormalization for concentration_units ' + cu);
            data = [];
            # get all of the samples in the analysis
            data = self.stage02_quantification_query.get_RExpressionData_analysisIDAndUnits_dataStage02GlogNormalized(analysis_id_I, cu);
            # call R
            data_transformed = [];
            concentrations = None;
            concentrations_glog = None;
            data_glog, concentrations, concentrations_glog = self.r_calc.calculate_glogNormalization(data)
            ## plot original values:
            self.matplot.densityPlot(concentrations);
            self.matplot.densityPlot(concentrations_glog);
            # upload data
            data_transformed.extend(data_glog);
        # commit data to the session every timepoint
        self.session.commit();
        self.stage02_quantification_query.update_concentrations_dataStage02GlogNormalized(analysis_id_I, data_transformed)
    def execute_getDataStage01ReplicatesMI(self,analysis_id_I,concentration_units_I=[]):
        '''glog normalize concentration values using R'''

        print('execute_getDataStage01ReplicatesMI...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data_transformed = [];
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            for row in analysis_info:
                concentration_units_tmp = [];
                concentration_units_tmp = self.stage02_quantification_query.get_concentrationUnits_experimentID_dataStage01ReplicatesMI(row['experiment_id']);
                concentration_units.extend(concentration_units_tmp);
            concentration_units = list(set(concentration_units));
        for cu in concentration_units:
            print('calculating glogNormalization for concentration_units ' + cu);
            data = [];
            # get all of the samples in the simulation
            for row in analysis_info:
                data_tmp = [];
                data_tmp = self.stage02_quantification_query.get_RExpressionData_AnalysisIDAndExperimentIDAndTimePointAndUnitsAndSampleNameShort_dataStage01ReplicatesMI(analysis_id_I,row['experiment_id'], row['time_point'], cu, row['sample_name_short']);
                data.extend(data_tmp)
            # upload data
            for d in data:
                row = None;
                row = data_stage02_quantification_glogNormalized(analysis_id_I,d['experiment_id'], d['sample_name_short'],
                                                            d['time_point'],d['component_group_name'],
                                                            d['component_name'],d['calculated_concentration'],
                                                            d['calculated_concentration_units'],
                                                            True,None);
                self.session.add(row);
        self.session.commit();
    def execute_getDataStage01PhysiologicalRatios(self,analysis_id_I):
        '''glog normalize concentration values using R'''

        print('execute_getDataStage01ReplicatesMI...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data = [];
        # get all of the samples in the simulation
        for row in analysis_info:
            data_tmp = [];
            data_tmp = self.stage02_quantification_query.get_RExpressionData_AnalysisIDAndExperimentIDAndSampleNameShortAndTimePoint_dataStage01PhysiologicalRatiosReplicates(analysis_id_I,row['experiment_id'], row['sample_name_short'], row['time_point']);
            data.extend(data_tmp)
        # upload data
        for d in data:
            row = None;
            row = data_stage02_quantification_glogNormalized(analysis_id_I,d['experiment_id'], d['sample_name_short'],
                                                        d['time_point'],d['physiologicalratio_id'],
                                                        d['physiologicalratio_name'],d['physiologicalratio_value'],
                                                        'ratio',
                                                        True,d['physiologicalratio_description']);
            self.session.add(row);
        self.session.commit();