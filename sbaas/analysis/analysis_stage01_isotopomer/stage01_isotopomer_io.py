from sbaas.analysis.analysis_base import *
from .stage01_isotopomer_query import stage01_isotopomer_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from MDV_utilities.mass_isotopomer_distributions import mass_isotopomer_distributions

class stage01_isotopomer_io(base_analysis):
    def __init__(self,session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage01_isotopomer_query = stage01_isotopomer_query(self.session);

    def export_compareAveragesSpectrumToTheoretical(self, experiment_id_I, filename, sample_name_abbreviations_I=None,scan_types_I=None,met_ids_I = None):
        '''export a comparison of calculated spectrum to theoretical spectrum'''
        # query the data
        data = [];
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Averages(experiment_id_I);
        for tp in time_points:
            print('Reporting average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                # query sample types from sample name abbreviations and time-point from _dataStage01Averages
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Averages(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Reporting average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Averages(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Averages(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Reporting average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Averages( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Reporting average precursor and product spectrum for metabolite ' + met);
                        data_tmp = [];
                        data_tmp = self.stage01_isotopomer_query.get_dataPrecursorFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01Averages(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
                        data_tmp = [];
                        data_tmp = self.stage01_isotopomer_query.get_dataProductFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01Averages(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
        # write the comparison to file
        headerL1 = ['sample_name_abbreviation','time_point','met_id','fragment_formula','C_pos','scan_type','theoretical'] + ['' for i in range(49)]\
            + ['measured'] + ['' for i in range(49)]\
            + ['measured_cv'] + ['' for i in range(49)]\
            + ['abs_difference'] + ['' for i in range(49)];
        headerL2 = ['' for i in range(6)] + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)];
        header = [];
        header.append(headerL1);
        header.append(headerL2);
        export = base_exportData(data);
        export.write_headersAndElements2csv(header,filename);
    def export_compareAveragesNormSumSpectrumToTheoretical(self, experiment_id_I, filename, sample_name_abbreviations_I=None,scan_types_I=None,met_ids_I = None):
        '''export a comparison of calculated spectrum to theoretical spectrum'''
        # query the data
        data = [];
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01AveragesNormSum(experiment_id_I);
        for tp in time_points:
            print('Reporting average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                # query sample types from sample name abbreviations and time-point from data_stage01_isotopomer_normalized
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Reporting average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Reporting average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Reporting average precursor and product spectrum for metabolite ' + met);
                        data_tmp = [];
                        data_tmp = self.stage01_isotopomer_query.get_dataPrecursorFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
                        data_tmp = [];
                        data_tmp = self.stage01_isotopomer_query.get_dataProductFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
        # write the comparison to file
        headerL1 = ['sample_name_abbreviation','time_point','met_id','fragment_formula','C_pos','scan_type','theoretical'] + ['' for i in range(49)]\
            + ['measured'] + ['' for i in range(49)]\
            + ['measured_cv'] + ['' for i in range(49)]\
            + ['abs_difference'] + ['' for i in range(49)]\
            + ['average_accuracy'];
        headerL2 = ['' for i in range(6)] + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + [''];
        header = [];
        header.append(headerL1);
        header.append(headerL2);
        export = base_exportData(data);
        export.write_headersAndElements2csv(header,filename);

    def import_dataStage01MQResultsTable_add(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01MQResultsTable(data.data);
        data.clear_data();

    def add_dataStage01MQResultsTable(self,data_I):
        '''add rows of data_stage01_isotopomer_MQResultsTable'''
        if data_I:
            cnt = 0;
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_MQResultsTable(d['Index'],
                            d['Sample Index'],
                            d['Original Filename'],
                            d['Sample Name'],
                            d['Sample ID'],
                            d['Sample Comment'],
                            d['Sample Type'],
                            d['Acquisition Date & Time'],
                            d['Rack Number'],
                            d['Plate Number'],
                            d['Vial Number'],
                            d['Dilution Factor'],
                            d['Injection Volume'],
                            d['Operator Name'],
                            d['Acq. Method Name'],
                            d['IS'],
                            d['Component Name'],
                            d['Component Index'],
                            d['Component Comment'],
                            d['IS Comment'],
                            d['Mass Info'],
                            d['IS Mass Info'],
                            d['IS Name'],
                            d['Component Group Name'],
                            d['Conc. Units'],
                            d['Failed Query'],
                            d['IS Failed Query'],
                            d['Peak Comment'],
                            d['IS Peak Comment'],
                            d['Actual Concentration'],
                            d['IS Actual Concentration'],
                            d['Concentration Ratio'],
                            d['Expected RT'],
                            d['IS Expected RT'],
                            d['Integration Type'],
                            d['IS Integration Type'],
                            d['Area'],
                            d['IS Area'],
                            d['Corrected Area'],
                            d['IS Corrected Area'],
                            d['Area Ratio'],
                            d['Height'],
                            d['IS Height'],
                            d['Corrected Height'],
                            d['IS Corrected Height'],
                            d['Height Ratio'],
                            d['Area / Height'],
                            d['IS Area / Height'],
                            d['Corrected Area/Height'],
                            d['IS Corrected Area/Height'],
                            d['Region Height'],
                            d['IS Region Height'],
                            d['Quality'],
                            d['IS Quality'],
                            d['Retention Time'],
                            d['IS Retention Time'],
                            d['Start Time'],
                            d['IS Start Time'],
                            d['End Time'],
                            d['IS End Time'],
                            d['Total Width'],
                            d['IS Total Width'],
                            d['Width at 50%'],
                            d['IS Width at 50%'],
                            d['Signal / Noise'],
                            d['IS Signal / Noise'],
                            d['Baseline Delta / Height'],
                            d['IS Baseline Delta / Height'],
                            d['Modified'],
                            d['Relative RT'],
                            d['Used'],
                            d['Calculated Concentration'],
                            d['Accuracy'],
                            d['Comment'],
                            d['Use_Calculated_Concentration']);
                    self.session.add(data_add);
                    cnt = cnt + 1;
                    if cnt > 1000: 
                        self.session.commit();
                        cnt = 0;
                except SQLAlchemyError as e:
                    print(e);
                    self.session.rollback();
            self.session.commit();
    
    def import_dataStage01MQResultsTable_update(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01MQResultsTable(data.data);
        data.clear_data();

    def update_dataStage01MQResultsTable(self,data_I):
        '''update rows of data_stage01_isotopomer_MQResultsTable'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_isotopomer_MQResultsTable).filter(
                            data_stage01_isotopomer_MQResultsTable.component_name.like(d['Component Name']),
                            data_stage01_isotopomer_MQResultsTable.sample_name.like(d['Sample Name'])).update(
                            {'index_':d['Index'],
                            'sample_index':d['Sample Index'],
                            'original_filename':d['Original Filename'],
                            'sample_name':d['Sample Name'],
                            'sample_id':d['Sample ID'],
                            'sample_comment':d['Sample Comment'],
                            'sample_type':d['Sample Type'],
                            'acquisition_date_and_time':d['Acquisition Date & Time'],
                            'rack_number':d['Rack Number'],
                            'plate_number':d['Plate Number'],
                            'vial_number':d['Vial Number'],
                            'dilution_factor':d['Dilution Factor'],
                            'injection_volume':d['Injection Volume'],
                            'operator_name':d['Operator Name'],
                            'acq_method_name':d['Acq. Method Name'],
                            'is_':d['IS'],
                            'component_name':d['Component Name'],
                            'component_index':d['Component Index'],
                            'component_comment':d['Component Comment'],
                            'is_comment':d['IS Comment'],
                            'mass_info':d['Mass Info'],
                            'is_mass':d['IS Mass Info'],
                            'is_name':d['IS Name'],
                            'component_group_name':d['Component Group Name'],
                            'conc_units':d['Conc. Units'],
                            'failed_query':d['Failed Query'],
                            'is_failed_query':d['IS Failed Query'],
                            'peak_comment':d['Peak Comment'],
                            'is_peak_comment':d['IS Peak Comment'],
                            'actual_concentration':d['Actual Concentration'],
                            'is_actual_concentration':d['IS Actual Concentration'],
                            'concentration_ratio':d['Concentration Ratio'],
                            'expected_rt':d['Expected RT'],
                            'is_expected_rt':d['IS Expected RT'],
                            'integration_type':d['Integration Type'],
                            'is_integration_type':d['IS Integration Type'],
                            'area':d['Area'],
                            'is_area':d['IS Area'],
                            'corrected_area':d['Corrected Area'],
                            'is_corrected_area':d['IS Corrected Area'],
                            'area_ratio':d['Area Ratio'],
                            'height':d['Height'],
                            'is_height':d['IS Height'],
                            'corrected_height':d['Corrected Height'],
                            'is_corrected_height':d['IS Corrected Height'],
                            'height_ratio':d['Height Ratio'],
                            'area_2_height':d['Area / Height'],
                            'is_area_2_height':d['IS Area / Height'],
                            'corrected_area2height':d['Corrected Area/Height'],
                            'is_corrected_area2height':d['IS Corrected Area/Height'],
                            'region_height':d['Region Height'],
                            'is_region_height':d['IS Region Height'],
                            'quality':d['Quality'],
                            'is_quality':d['IS Quality'],
                            'retention_time':d['Retention Time'],
                            'is_retention_time':d['IS Retention Time'],
                            'start_time':d['Start Time'],
                            'is_start_time':d['IS Start Time'],
                            'end_time':d['End Time'],
                            'is_end_time':d['IS End Time'],
                            'total_width':d['Total Width'],
                            'is_total_width':d['IS Total Width'],
                            'width_at_50':d['Width at 50%'],
                            'is_width_at_50':d['IS Width at 50%'],
                            'signal_2_noise':d['Signal / Noise'],
                            'is_signal_2_noise':d['IS Signal / Noise'],
                            'baseline_delta_2_height':d['Baseline Delta / Height'],
                            'is_baseline_delta_2_height':d['IS Baseline Delta / Height'],
                            'modified_':d['Modified'],
                            'relative_rt':d['Relative RT'],
                            'used_':d['Used'],
                            'calculated_concentration':d['Calculated Concentration'],
                            'accuracy_':d['Accuracy'],
                            'comment_':d['Comment'],
                            'use_calculated_concentration':d['Use_Calculated_Concentration']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_peakData_add(self, filename, experiment_id, samplename, precursor_formula, met_id,
                            mass_units_I='Da',intensity_units_I='cps', scan_type_I='EPI', header_I=True,
                            add_data_I=True):
        '''table adds'''
        data = base_importData();
        try:
            data.read_tab_fieldnames(filename,['Mass/Charge','Intensity'],header_I);
            #data.read_tab_fieldnames(filename,['mass','intensity','intensity_percent'],header_I);
            data.format_data();
            if add_data_I:
                self.add_peakData(data.data, experiment_id, samplename, precursor_formula, met_id,
                              mass_units_I,intensity_units_I, scan_type_I);
            data.clear_data();
        except IOError as e:
            print(e);

    def add_peakData(self, data_I, experiment_id, samplename, precursor_formula, met_id,
                          mass_units_I,intensity_units_I, scan_type_I):
        '''add rows of data_stage01_isotopomer_peakData'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_peakData(experiment_id,
                            samplename,
                            met_id,
                            precursor_formula,
                            d['Mass/Charge'],
                            #d['mass'],
                            mass_units_I,
                            d['Intensity'],
                            #d['intensity'],
                            intensity_units_I,
                            scan_type_I,
                            True);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_peakList_add(self, filename, experiment_id, samplename, precursor_formula, met_id,
                            mass_units_I='Da',intensity_units_I='cps', 
                            centroid_mass_units_I='Da', peak_start_units_I='Da',
                            peak_stop_units_I='Da', resolution_I=None, scan_type_I='EPI'):
        '''table adds'''
        data = base_importData();
        data.read_tab_fieldnames(filename,['mass','centroid_mass','intensity','peak_start','peak_end','width','intensity_percent']);
        data.format_data();
        self.add_peakList(data.data, experiment_id, samplename, met_id,
                          mass_units_I,intensity_units_I, scan_type_I);
        data.clear_data();

    def add_peakList(self, data_I, experiment_id, samplename, precursor_formula, met_id,
                            mass_units_I='Da',intensity_units_I='cps',
                            centroid_mass_units_I='Da', peak_start_units_I='Da',
                            peak_stop_units_I='Da', resolution_I=None, scan_type_I='EPI'):
        '''add rows of data_stage01_isotopomer_peakList'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_peakList(experiment_id,
                            samplename,
                            met_id,
                            precursor_formula,
                            d['mass'],
                            mass_units_I,
                            d['intensity'],
                            intensity_units_I,
                            d['centroid_mass'],
                            centroid_mass_units_I,
                            d['peak_start'],
                            peak_start_units_I,
                            d['peak_stop'],
                            peak_stop_units_I,
                            resolution_I,
                            scan_type_I);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01PeakSpectrum_add(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01PeakSpectrum(data.data);
        data.clear_data();

    def add_dataStage01PeakSpectrum(self,data_I):
        '''add rows of data_stage01_isotopomer_peakSpectrum'''
        if data_I:
            #cnt = 0;
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_peakSpectrum(d['experiment_id'],
                                    d['sample_name'],
                                    d['sample_name_abbreviation'],
                                    d['sample_type'],
                                    d['time_point'],
                                    d['replicate_number'],
                                    d['met_id'],
                                    d['precursor_formula'],
                                    d['precursor_mass'],
                                    d['product_formula'],
                                    d['product_mass'],
                                    d['intensity'],
                                    d['intensity_units'],
                                    d['intensity_corrected'],
                                    d['intensity_corrected_units'],
                                    d['intensity_normalized'],
                                    d['intensity_normalized_units'],
                                    d['intensity_theoretical'],
                                    d['abs_devFromTheoretical'],
                                    d['scan_type'],
                                    d['used_'],
                                    d['comment_']);
                    self.session.add(data_add);
                    #cnt = cnt + 1;
                    #if cnt > 1000: 
                    #    self.session.commit();
                    #    cnt = 0;
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def import_dataStage01PeakSpectrum_update(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01PeakSpectrum(data.data);
        data.clear_data();

    def update_dataStage01PeakSpectrum(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_peakSpectrum
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(
                        data_stage01_isotopomer_peakSpectrum.id == d['id']).update(
                        #data_stage01_isotopomer_peakSpectrum.experiment_id.like(d['experiment_id']),
                        #data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        #data_stage01_isotopomer_peakSpectrum.time_point.like(d['time_point']),
                        #data_stage01_isotopomer_peakSpectrum.sample_type.like(d['sample_type']),
                        #data_stage01_isotopomer_peakSpectrum.replicate_number == d['replicate_number'],
                        #data_stage01_isotopomer_peakSpectrum.met_id.like(d['met_id']),
                        #data_stage01_isotopomer_peakSpectrum.precursor_formula.like(d['precursor_formula']),
                        #data_stage01_isotopomer_peakSpectrum.precursor_mass == d['precursor_mass'],
                        #data_stage01_isotopomer_peakSpectrum.product_formula.like(d['product_formula']),
                        #data_stage01_isotopomer_peakSpectrum.product_mass == d['product_mass']).update(		
                        {'intensity':d['intensity'],
                        'intensity_units':d['intensity_units'],
                        'intensity_corrected':d['intensity_corrected'],
                        'intensity_corrected_units':d['intensity_corrected_units'],
                        'intensity_normalized':d['intensity_normalized'],
                        'intensity_normalized_units':d['intensity_normalized_units'],
                        'scan_type':d['scan_type'],
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def import_dataStage01Normalized_update(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01Normalized(data.data);
        data.clear_data();

    def update_dataStage01Normalized(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                        data_stage01_isotopomer_normalized.id == d['id']).update(
                        #data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                        #data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        #data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                        #data_stage01_isotopomer_normalized.dilution == d['dilution'],
                        #data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                        #data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                        #data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                        #data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                        #data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass']).update(		
                        {
                        'experiment_id':d['experiment_id'],
                        'sample_name_abbreviation':d['sample_name_abbreviation'],
                        'time_point':d['time_point'],
                        'dilution':d['dilution'],
                        'sample_type':d['sample_type'],
                        'replicate_number':d['replicate_number'],
                        'met_id':d['met_id'],
                        'fragment_formula':d['fragment_formula'],
                        'fragment_mass':d['fragment_mass'],
                        'intensity':d['intensity'],
                        'intensity_units':d['intensity_units'],
                        'intensity_corrected':d['intensity_corrected'],
                        'intensity_corrected_units':d['intensity_corrected_units'],
                        'intensity_normalized':d['intensity_normalized'],
                        'intensity_normalized_units':d['intensity_normalized_units'],
                        'scan_type':d['scan_type'],
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def import_dataStage01Normalized_updateUsedAndComment(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.updateUsedAndComment_dataStage01Normalized(data.data);
        data.clear_data();

    def updateUsedAndComment_dataStage01Normalized(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                        data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                        data_stage01_isotopomer_normalized.dilution == d['dilution'],
                        data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                        data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                        data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                        data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
                        {
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def import_dataStage01Normalized_add(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01Normalized(data.data);
        data.clear_data();

    def add_dataStage01Normalized(self,dataListUpdated_I):
        # add to data_stage01_isotopomer_normalized
        for d in dataListUpdated_I:
            try:
                data_update = data_stage01_isotopomer_normalized(d['experiment_id'],
                        d['sample_name_abbreviation'],
                        d['time_point'],
                        d['dilution'],
                        d['sample_type'],
                        d['replicate_number'],
                        d['met_id'],
                        d['fragment_formula'],
                        d['fragment_mass'],
                        d['intensity'],
                        d['intensity_units'],
                        d['intensity_corrected'],
                        d['intensity_corrected_units'],
                        d['intensity_normalized'],
                        d['intensity_normalized_units'],
                        d['scan_type'],
                        d['used_'],
                        d['comment_']);
                self.session.add(data_add);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def import_dataStage01Averages_updateUsedAndComment(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01Averages_usedAndComment(data.data);
        data.clear_data();

    def update_dataStage01Averages_usedAndComment(self,dataListUpdated_I):
        # update used and comment fields of the data_stage01_isotopomer_averages
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_averages).filter(
                        data_stage01_isotopomer_averages.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_averages.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_averages.time_point.like(d['time_point']),
                        data_stage01_isotopomer_averages.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_averages.met_id.like(d['met_id']),
                        data_stage01_isotopomer_averages.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_averages.fragment_mass == int(d['fragment_mass']),
                        data_stage01_isotopomer_averages.scan_type.like(d['scan_type'])
                        ).update(		
                        {
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def import_dataStage01AveragesNormSum_updateUsedAndComment(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01AveragesNormSum_usedAndComment(data.data);
        data.clear_data();

    def update_dataStage01AveragesNormSum_usedAndComment(self,dataListUpdated_I):
        # update used and comment fields of the data_stage01_isotopomer_averagesNormSum
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(
                        data_stage01_isotopomer_averagesNormSum.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_averagesNormSum.time_point.like(d['time_point']),
                        data_stage01_isotopomer_averagesNormSum.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_averagesNormSum.met_id.like(d['met_id']),
                        data_stage01_isotopomer_averagesNormSum.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_averagesNormSum.fragment_mass == int(d['fragment_mass']),
                        data_stage01_isotopomer_averagesNormSum.scan_type.like(d['scan_type'])
                        ).update(		
                        {
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def export_dataStage01IsotopomerNormalized_js(self,experiment_id_I,sample_names_I=[],sample_name_abbreviations_I=[],time_points_I=[],scan_types_I=[],met_ids_I=[],data_dir_I="tmp",
                                                  single_plot_I = True):
        """Export data_stage01_isotopomer_normalized to js file"""

        mids = mass_isotopomer_distributions();

        # get the data
        
        data_O = [];
        sample_names_O = [];
        sample_name_abbreviations_O = [];
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Plotting precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_name_abbreviations_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
                # query sample types from sample name abbreviations and time-point from data_stage01_isotopomer_normalized 
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Normalized(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Plotting precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Plotting precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting precursor and product spectrum for metabolite ' + met);
                        if sample_names_I:
                            sample_names = sample_names_I;
                        else:
                            sample_names,replicate_numbers,sample_types = [],[],[];
                            sample_names,replicate_numbers,sample_types = self.stage01_isotopomer_query.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndMetIDAndTimePointAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,met,tp,scan_type);
                        if not(replicate_numbers): continue; #no replicates found
                        for rep in replicate_numbers:
                        #if not(sample_names): continue; #no replicates found
                        #for sn_cnt,sn in enumerate(sample_names):
                            print('Plotting precursor and product spectrum for replicate_number ' + str(rep));
                            #print('Plotting precursor and product spectrum for sample_name ' + sn);
                            #sample_names_O.append(sn);
                            sample_name_abbreviations_O.append(sna);
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            #peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndSampleName_dataStage01Normalized( \
                            #    experiment_id_I,sna,tp,scan_type,met,sn);
                            if peakData_I:
                                fragment_formulas = list(peakData_I.keys());
                                peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                    peakData_I, fragment_formulas, True);
                                for fragment_formula in fragment_formulas:
                                    for fragment_mass,intensity_normalized in peakSpectrum_normalized[fragment_formula].items():
                                        sample_name = sna + "_" + str(rep);
                                        sample_names_O.append(sample_name);
                                        fragment_id = mids.make_fragmentID(met,fragment_formula,fragment_mass);
                                        intensity = 0.0;
                                        if intensity_normalized:
                                            intensity = intensity_normalized;
                                        data_tmp = {
                                                    'experiment_id':experiment_id_I,
                                                    'sample_name':sample_name,
                                                    #'sample_name':sn,
                                                    'sample_name_abbreviation':sna,
                                                    'sample_type':sample_types_lst[sna_cnt],
                                                    'time_point':tp,
                                                    #'dilution':dil,
                                                    'replicate_number':rep,
                                                    'met_id':met,
                                                    'fragment_formula':fragment_formula,
                                                    'fragment_mass':fragment_mass,
                                                    'intensity_normalized':intensity,
                                                    'intensity_normalized_units':"normMax",
                                                    'scan_type':scan_type,
                                                    'fragment_id':fragment_id};
                                        data_O.append(data_tmp);

        # record the unique sample names:
        sample_names_unique = list(set(sample_names_O));
        sample_names_unique.sort();
        #sample_name_abbreviations_unique = list(set(sample_name_abbreviations_O));
        #sample_name_abbreviations_unique.sort();
        #sample_names_dict = {};
        #for sna in sample_name_abbreviations_unique:
        #    sample_names_dict[sna]=[];
        #    for sn in sample_names_O:
        #        if sna==sn[1] and not sn[0] in sample_names_dict[sna]:
        #            sample_names_dict[sna].append(sn[0]);

        # get the table data
        data_table_O = [];
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Tabulting precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            dataListUpdated = [];
            # get dilutions
            dilutions = [];
            dilutions = self.stage01_isotopomer_query.get_sampleDilution_experimentIDAndTimePoint_dataStage01Normalized(experiment_id_I,tp);
            for dil in dilutions:
                print('Tabulting precursor and product spectrum from isotopomer normalized for dilution ' + str(dil));
                if sample_names_I:
                    sample_abbreviations = [];
                    sample_types = ['Unknown','QC'];
                    for sn in sample_names_I:
                        for st in sample_types:
                            sample_abbreviations_tmp = [];
                            sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilutionAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,dil,sn);
                            sample_abbreviations.extend(sample_abbreviations_tmp);
                elif sample_name_abbreviations_I:
                    sample_abbreviations = sample_name_abbreviations_I;
                else:
                    # get sample names and sample name abbreviations
                    sample_abbreviations = [];
                    sample_types = ['Unknown','QC'];
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution_dataStage01Normalized(experiment_id_I,st,tp,dil);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                for sna_cnt,sna in enumerate(sample_abbreviations):
                    print('Tabulting precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                    # get the scan_types
                    if scan_types_I:
                        scan_types = scan_types_I;
                    else:
                        scan_types = [];
                        scan_types = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndDilutionAndSampleAbbreviations_dataStage01Normalized(experiment_id_I,tp,dil,sna);
                    for scan_type in scan_types:
                        print('Tabulting precursor and product spectrum for scan type ' + scan_type)
                        # met_ids
                        if not met_ids_I:
                            met_ids = [];
                            met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanType_dataStage01Normalized( \
                                    experiment_id_I,sna,tp,dil,scan_type);
                        else:
                            met_ids = met_ids_I;
                        if not(met_ids): continue #no component information was found
                        for met in met_ids:
                            # get the data
                            data = [];
                            data = self.stage01_isotopomer_query.get_rows_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanTypeAndMetID_dataStage01Normalized( \
                                    experiment_id_I,sna,tp,dil,scan_type,met);
                            for d in data:
                                d['sample_name'] = d['sample_name_abbreviation']+"_"+str(d['replicate_number']);
                                d['fragment_id'] = mids.make_fragmentID(d['met_id'],d['fragment_formula'],d['fragment_mass']);
                            data_table_O.extend(data);
        # visualization parameters
        data1_keys = ['sample_name','sample_name_abbreviation',
                      'sample_type',
                      'met_id','time_point','fragment_formula','fragment_mass','scan_type','fragment_id'];
        data1_nestkeys = [
            #'fragment_id',
            'fragment_mass'
            ];
        data1_keymap = {
                #'xdata':'fragment_id',
                'xdata':'fragment_mass',
                'ydata':'intensity_normalized',
                'serieslabel':'sample_name',
                #'featureslabel':'fragment_id',
                'featureslabel':'fragment_mass',
                'ydata_lb':None,
                'ydata_ub':None};

        # initialize the ddt objects
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};

        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        dataobject_O.append({"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(formtileparameters_O);
        tile2datamap_O.update({"filtermenu1":[0]});
        if not single_plot_I:
            rowcnt = 1;
            colcnt = 1;
            for cnt,sn in enumerate(sample_names_unique):
                svgtileid = "tilesvg"+str(cnt);
                svgid = 'svg'+str(cnt);
                iter=cnt+1; #start at 1
                if (cnt % 2 == 0): 
                    rowcnt = rowcnt+1;#even 
                    colcnt = 1;
                else:
                    colcnt = colcnt+1;
                # make the svg object
                svgparameters1_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                    #'svgid':'svg1',
                    'svgid':'svg'+str(cnt),
                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":500,"svgheight":350,"svgy1axislabel":"intensity (norm)",
                    "svgfilters":{'sample_name':[sn]}               
                        };
                svgtileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'svg',
                    #'tileid':"tile2",
                    'tileid':svgtileid,
                    #'rowid':"row1",
                    'rowid':"row"+str(rowcnt),
                    #'colid':"col1",
                    'colid':"col"+str(colcnt),
                    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
                svgtileparameters1_O.update(svgparameters1_O);
                parametersobject_O.append(svgtileparameters1_O);
                tile2datamap_O.update({svgtileid:[0]});
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svgparameters1_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                #'svgid':'svg1',
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,"svgheight":350,"svgy1axislabel":"intensity (norm)",
                "svgfilters":{'sample_name':[sn]}               
                    };
            svgtileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'svg',
                #'tileid':"tile2",
                'tileid':svgtileid,
                #'rowid':"row1",
                #'colid':"col1",
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
            svgtileparameters1_O.update(svgparameters1_O);
            parametersobject_O.append(svgparameters1_O);
            tile2datamap_O.update({svgtileid:[0]});

        # make the table object
        tableparameters1_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    #"tableheaders":[],
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'tile1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'table','tileid':"tabletile1",
            'rowid':"row100",
            'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters1_O.update(tableparameters1_O);
        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(tabletileparameters1_O);
        tile2datamap_O.update({"tabletile1":[1]})

        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = settings.visualization_data + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = settings.visualization_data + '/project/' + analysis_id_I + '_data_stage01_isotopomer_normalized' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);