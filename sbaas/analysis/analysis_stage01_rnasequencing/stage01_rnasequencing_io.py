from sbaas.analysis.analysis_base import *
from .stage01_rnasequencing_query import stage01_rnasequencing_query
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import json
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_analysis.genes_fpkm_tracking import genes_fpkm_tracking
from sequencing_analysis.gene_exp_diff import gene_exp_diff

class stage01_rnasequencing_io(base_analysis):
    '''class for rnasequencing analysis'''
    def __init__(self,session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage01_rnasequencing_query = stage01_rnasequencing_query(self.session);
        self.calculate = base_calculate();

    def import_dataStage01RNASequencingAnalysis_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01RNASequencingAnalysis(data.data);
        data.clear_data();

    def add_dataStage01RNASequencingAnalysis(self, data_I):
        '''add rows of data_stage01_rnasequencing_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_rnasequencing_analysis(d['analysis_id'],
                            d['experiment_id'],
                            d['sample_name_abbreviation'],
                            d['sample_name'],
                            d['time_point'],
                            d['analysis_type'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingAnalysis_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingAnalysis(data.data);
        data.clear_data();

    def update_dataStage01RNASequencingAnalysis(self,data_I):
        '''update rows of data_stage01_rnasequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_analysis).filter(
                           data_stage01_rnasequencing_analysis.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'sample_name':d['sample_name'],
                            'time_point':d['time_point'],
                            'analysis_type':d['analysis_type'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingGenesFpkmTracking_add(self,filename,experiment_id,sample_name):
        '''table adds'''
        genesfpkmtracking = genes_fpkm_tracking();
        genesfpkmtracking.import_genesFpkmTracking(filename_I=filename,experiment_id_I = experiment_id,sample_name_I = sample_name);
        self.add_dataStage01RNASequencingGenesFpkmTracking(genesfpkmtracking.genesFpkmTracking);

    def add_dataStage01RNASequencingGenesFpkmTracking(self, data_I):
        '''add rows of data_stage01_rnasequencing_fpkmTracking'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_rnasequencing_genesFpkmTracking(d['experiment_id'],
                            d['sample_name'],
                            d['tracking_id'],
                            d['class_code'],
                            d['nearest_ref_id'],
                            d['gene_id'],
                            d['gene_short_name'],
                            d['tss_id'],
                            d['locus'],
                            d['length'],
                            d['coverage'],
                            d['FPKM'],
                            d['FPKM_conf_lo'],
                            d['FPKM_conf_hi'],
                            d['FPKM_status'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingGenesFpkmTracking_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingGenesFpkmTracking(data.data);
        data.clear_data();

    def update_dataStage01RNASequencingGenesFpkmTracking(self,data_I):
        '''update rows of data_stage01_rnasequencing_genesFpkmTracking'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(
                           data_stage01_rnasequencing_genesFpkmTracking.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'tracking_id':d['tracking_id'],
                            'class_code':d['class_code'],
                            'nearest_ref_id':d['nearest_ref_id'],
                            'gene_id':d['gene_id'],
                            'gene_short_name':d['gene_short_name'],
                            'tss_id':d['tss_id'],
                            'locus':d['locus'],
                            'length':d['length'],
                            'coverage':d['coverage'],
                            'FPKM':d['FPKM'],
                            'FPKM_conf_lo':d['FPKM_conf_lo'],
                            'FPKM_conf_hi':d['FPKM_conf_hi'],
                            'FPKM_status':d['FPKM_status'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingGeneExpDiff_add(self, filename,experiment_id_1,experiment_id_2,sample_name_abbreviation_1,sample_name_abbreviation_2):
        '''table adds'''
        geneexpdiff = gene_exp_diff();
        geneexpdiff.import_geneExpDiff(filename_I=filename,experiment_id_1_I = experiment_id_1,experiment_id_2_I = experiment_id_2,
                        sample_name_abbreviation_1_I = sample_name_abbreviation_1,sample_name_abbreviation_2_I = sample_name_abbreviation_2);
        self.add_dataStage01RNASequencingGeneExpDiff(geneexpdiff.geneExpDiff);

    def add_dataStage01RNASequencingGeneExpDiff(self, data_I):
        '''add rows of data_stage01_rnasequencing_geneExpDiff'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_rnasequencing_geneExpDiff(
                            d['experiment_id_1'],
                            d['experiment_id_2'],
                            d['sample_name_abbreviation_1'],
                            d['sample_name_abbreviation_2'],
                            d['test_id'],
                            d['gene_id'],
                            d['gene'],
                            d['sample_1'],
                            d['sample_2'],
                            d['status'],
                            d['value_1'],
                            d['value_2'],
                            d['fold_change_log2'],
                            d['test_stat'],
                            d['p_value'],
                            d['q_value'],
                            d['significant'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01RNASequencingGeneExpDiff_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingGeneExpDiff(data.data);
        data.clear_data();

    def update_dataStage01RNASequencingGeneExpDiff(self,data_I):
        '''update rows of data_stage01_rnasequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_geneExpDiff).filter(
                           data_stage01_rnasequencing_geneExpDiff.id==d['id']).update(
                            {'experiment_id_1':d['experiment_id_1'],
                            'experiment_id_2':d['experiment_id_2'],
                            'sample_name_abbreviation_1':d['sample_name_abbreviation_1'],
                            'sample_name_abbreviation_2':d['sample_name_abbreviation_2'],
                            'test_id':d['test_id'],
                            'gene_id':d['gene_id'],
                            'gene':d['gene'],
                            'sample_1':d['sample_1'],
                            'sample_2':d['sample_2'],
                            'status':d['status'],
                            'value_1':d['value_1'],
                            'value_2':d['value_2'],
                            'fold_change_log2':d['fold_change_log2'],
                            'test_stat':d['test_stat'],
                            'p_value':d['p_value'],
                            'q_value':d['q_value'],
                            'significant':d['significant'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def export_dataStage01RNASequencingHeatmap_js(self,analysis_id_I,data_dir_I="tmp"):
        """export heatmap to js file"""

        #get the heatmap data for the analysis
        # TODO
        data_O = self.stage01_rnasequencing_query.get_rows_analysisID_dataStage01RNASequencingHeatmap(analysis_id_I);
        # dump chart parameters to a js files
        data1_keys = [
            'analysis_id',
                      'row_label','col_label','row_index','col_index','row_leaves','col_leaves',
                'col_pdist_metric','row_pdist_metric','col_linkage_method','row_linkage_method',
                'value_units']
        data1_nestkeys = ['analysis_id'];
        data1_keymap = {'xdata':'row_leaves','ydata':'col_leaves','zdata':'value',
                'rowslabel':'row_label','columnslabel':'col_label',
                'rowsindex':'row_index','columnsindex':'col_index',
                'rowsleaves':'row_leaves','columnsleaves':'col_leaves'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        svgparameters_O = {"svgtype":'heatmap2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                             'svgcellsize':18,'svgmargin':{ 'top': 200, 'right': 50, 'bottom': 100, 'left': 200 },
                            'svgcolorscale':'quantile',
                            'svgcolorcategory':'heatmap10',
                            'svgcolordomain':[0,1],
                            'svgcolordatalabel':'value',
                            'svgdatalisttileid':'tile1'};
        svgtileparameters_O = {'tileheader':'heatmap','tiletype':'svg','tileid':"tile2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_O.update(svgparameters_O);
        formtileparameters_O = {'tileheader':'filter menu','tiletype':'html','tileid':"tile1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"
            
            };
        formparameters_O = {'htmlid':'datalist1','htmltype':'datalist_01','datalist': [{'value':'hclust','text':'by cluster'},
                            {'value':'probecontrast','text':'by row and column'},
                            {'value':'probe','text':'by row'},
                            {'value':'contrast','text':'by column'},
                            {'value':'custom','text':'by value'}]}
        formtileparameters_O.update(formparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O];
        tile2datamap_O = {"tile1":[0],"tile2":[0]};
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_rnasequencing_heatmap' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
        
    def export_dataStage01RNASequencingGeneExpDiff_js(self,analysis_id_I,data_dir_I='tmp'):
        '''Export data for a volcano plot'''
        
        #get the data for the analysis
        data_O = [];
        data_O = self.geneExpDiff
        # make the data parameters
        data1_keys = ['experiment_id_1','experiment_id_2','sample_name_abbreviation_1','sample_name_abbreviation_2','gene','log2(fold_change)','p_value'
                    ];
        data1_nestkeys = ['experiment_id_1'];
        data1_keymap = {'ydata':'p_value',
                        'xdata':'log2(fold_change)',
                        'serieslabel':'',
                        'featureslabel':'gene'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'volcanoplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 50, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":'Fold Change [log2(FC)]',"svgy1axislabel":'Probability [-log10(P)]',
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Volcano plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'pairWiseTest','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_rnasequencing_heatmap' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    def export_dataStage01RNASequencingGenesFpkmTracking_js(self,analysis_id_I,data_dir_I='tmp'):
        '''Export data for a box and whiskers plot'''

        #get the analysis information
        analysis_info = [];
        #TODO
        #analysis_info = genesFpkmTracking
        #get the data for the analysis
        data_O = [];
        #TODO
        #data_O = self.stage02_quantification_query.get_rows_analysisID_dataStage02QuantificationDescriptiveStats(analysis_id_I);
        # dump chart parameters to a js files
        data1_keys = ['analysis_id','experiment_id','sample_name','gene'
                    ];
        data1_nestkeys = ['gene'];
        data1_keymap = {'xdata':'gene',
                        'ydata':'FPKM',
                        'ydatalb':'FPKM_conf_lo',
                        'ydataub':'FPKM_conf_hi',
                        'serieslabel':'sample_name',
                        'featureslabel':'gene'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"gene","svgy1axislabel":"FPKM",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Custom box and whiskers plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'FPKM','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_rnasequencing_heatmap' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);

    