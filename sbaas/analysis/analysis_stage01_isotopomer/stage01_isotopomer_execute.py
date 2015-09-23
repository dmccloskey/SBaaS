'''quantitative metabolomics analysis class'''

from sbaas.analysis.analysis_base import *
from .stage01_isotopomer_query import *
from .stage01_isotopomer_io import *

from sbaas.resources.molmass import Formula
from sbaas.resources.matplot import matplot
import re,copy

from scipy.stats import mode
from scipy.io import savemat

class stage01_isotopomer_execute():
    '''class for quantitative metabolomics analysis'''
    def __init__(self, session_I=None):
        if session_I: self.session = session_I;
        else: self.session = Session();
        self.stage01_isotopomer_query = stage01_isotopomer_query(self.session);
        self.calculate = base_calculate();
        self.isotopomer_13C_fragments_validated = {'23dpg':['C3H7O10P2-'],
                                '6pgc':['C6H12O10P-','C6H10O9P-','C5H12O7P-'],
                                'accoa':['C23H37N7O17P3S-','C23H36N7O14P2S-','C13H23N2O10P2S-','C10H14N5O10P2-','C10H12N5O9P2-','C10H11N5O6P-'],
                                'acon-C':['C6H5O6-','C6H3O5-','C5H5O4-'],
                                'akg':['C5H5O5-','C4H5O3-','C2HO3-'],
                                'amp':['C5H4N5-','C10H13N5O7P-'],
                                'asp-L':['C4H6NO4-','C4H6NO2-','C4H3O4-','C3H6NO2-'],
                                'atp':['C10H15N5O13P3-','C10H14N5O10P2-','C10H12N5O9P2-','C10H11N5O6P-'],
                                'dhap':['C3H6O6P-'],
                                'fad':['C27H32N9O15P2-','C17H18N4O8P-','C10H13N5O7P-'],
                                'fdp':['C6H13O12P2-','C6H10O8P-'],
                                'g1p':['C6H12O9P-'],
                                'g6p':['C6H12O9P-','C4H8O7P-'],
                                'glu-L':['C5H8NO4-','C5H6NO3-'],
                                'glyc3p':['C3H8O6P-'],
                                'glyclt':['CH3O2-','C2H3O3-'],
                                'icit':['C6H7O7-','C6H5O6-','C5H3O3-'],
                                'mal-L':['C4H5O5-','C4H3O4-'],
                                'met-L':['CH3S-','C5H10NO2S-'],
                                'pep':['C3H4O6P-'],
                                'phe-L':['C9H7O2-','C9H10NO2-'],
                                'phpyr':['C9H7O3-','C8H7O','C7H7-'],
                                'Pool_2pg_3pg':['C3H6O7P-'],
                                'prpp':['C5H9O10P2-','C5H12O14P3-'],
                                'pyr':['C3H3O3-'],
                                'ru5p-D':['C5H10O8P-'],
                                's7p':['C7H14O10P-'],
                                'skm':['C7H9O5-','C6H5O-'],
                                'succ':['C4H5O4-','C4H3O3-'],
                                'thr-L':['C4H8NO3-'],
                                'ump':['C9H9N2O6-','C9H12N2O9P-','C4H3N2O2-']};

    #analyses not tested:
    def execute_removeDuplicateDilutions(self,experiment_id_I,component_names_dil_I = []):
        '''remove duplicate dilutions from data_stage01_isotopomer_normalized
        NOTE: rows are not removed, but the used value is changed to false
        NOTE: priority is given to the 1x dilution (i.e. 10x dilutions are removed
              if a 1x and 10x are both used'''
        # Input:
        #   experiment_id_I = experiment
        #   component_names_dil_I = component names for which the dilution will be prioritized
        
        print('execute_removeDuplicateDilutions...')
        # get sample names
        sample_ids = [];
        sample_ids = self.stage01_isotopomer_query.get_sampleIDs_experimentID_dataStage01Normalized(experiment_id_I);
        for si in sample_ids:
            # get component names
            component_names = [];
            component_names = self.stage01_isotopomer_query.get_componentsNames_experimentIDAndSampleID_dataStage01Normalized(experiment_id_I,si);
            for cn in component_names:
                # get dilutions
                sample_dilutions = [];
                sample_dilutions = self.stage01_isotopomer_query.get_sampleDilutions_experimentIDAndSampleIDAndComponentName_dataStage01Normalized(experiment_id_I,si,cn);
                if len(sample_dilutions)<2: continue;
                # find the minimum and maximum dilution
                min_sample_dilution = min(sample_dilutions);
                max_sample_dilution = max(sample_dilutions);
                for sd in sample_dilutions:
                    # prioritize undiluted samples if not in the dilution list
                    # i.e. diluted samples used_ are set to FALSE
                    if not(cn in component_names_dil_I) and not(sd == min_sample_dilution):
                        # get the sample name
                        sample_name = self.stage01_isotopomer_query.get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(experiment_id_I,si,sd);
                        try:
                            data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                                    data_stage01_isotopomer_normalized.sample_name.like(sample_name),
                                    data_stage01_isotopomer_normalized.component_name.like(cn)).update(
                                    {'used_': False},synchronize_session=False);
                        except SQLAlchemyError as e:
                            print(e);
                    # prioritize diluted samples if in the dilution list
                    # i.e. undiluted samples used_ are set to FALSE
                    if (cn in component_names_dil_I) and not(sd == max_sample_dilution):
                        # get the sample name
                        sample_name = self.stage01_isotopomer_query.get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(experiment_id_I,si,sd);
                        try:
                            data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                                    data_stage01_isotopomer_normalized.sample_name.like(sample_name),
                                    data_stage01_isotopomer_normalized.component_name.like(cn)).update(
                                    {'used_': False},synchronize_session=False);
                        except SQLAlchemyError as e:
                            print(e);
        self.session.commit();
    def execute_removeDuplicateComponents(self,experiment_id_I):
        '''remove duplicate components from data_stage01_isotopomer_normalized
        NOTE: rows are not removed, but the used value is changed to false
        NOTE: priority is given to the primary transition'''
        return
    #analyses tested:
    def execute_buildSpectrumFromMRMs(self,experiment_id_I,ms_methodtype_I='isotopomer_13C',sample_name_abbreviations_I=[],sample_names_I=[],met_ids_I=[]):
        '''Extract peak spectrum for each fragment from MRMs'''
        # Input:
        #   experiment_id
        #   sample_names = (optional) list of specific samples
        # Output:
        #   sample_name
        #   sample_id
        #   component_group_name
        #   component_name
        #   calculated_concentration
        #   calculated_concentration_units
        #   used_

        # assumptions:
        #   1. there is only spectrum of MRMs for each components 

        mids = mass_isotopomer_distributions();
        
        print('build_precursorSpectrumFromMRMs...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID(experiment_id_I);
        for tp in time_points:
            print('Building precursor and product spectrum from MRMs for time-point ' + str(tp));
            # get dilutions
            dilutions = self.stage01_isotopomer_query.get_sampleDilution_experimentIDAndTimePoint(experiment_id_I,tp);
            for dil in dilutions:
                print('Building precursor and product spectrum from MRMs for dilution ' + str(dil));
                if sample_names_I:
                    sample_abbreviations = [];
                    for sn in sample_names_I:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleName(experiment_id_I,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                elif sample_name_abbreviations_I:
                    sample_abbreviations = sample_name_abbreviations_I;
                else:
                    # get sample names and sample name short
                    sample_abbreviations = [];
                    sample_types = ['Unknown','QC'];
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution(experiment_id_I,st,tp,dil);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                for sna_cnt,sna in enumerate(sample_abbreviations):
                    print('Building precursor and product spectrum from MRMs for sample name abbreviation ' + sna);
                    ##BUG alert:
                    ##there is a potential bug whereby if the entire spectra per compound is not returned
                    ##e.g. one of the samples is not returned because "used_" is set to false in isotopomer_MQResultsTable
                    ##the spectra could potentially be shifted
                    ##get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilution has been adjusted to
                    ##return all component_names even if the sample from which it came is not "used_" as a temporary fix
                    ##this works for C12 validation experiments, but
                    ##the results of normalization will need to be monitored until a more robust method is established

                    ##UPDATE to BUG:
                    ##'met_cnt_max = len(component_names)-1' changed to 'met_cnt_max = len(component_names)' and 
                    ##get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndTimePointAndDilution added
                    ##so that the last component is included in the met/fragment spectra even when not all component names have "used_"
                    ##set to true in isotopomer_MQResultsTable 

                    # component names, group names, fragment formula, and fragment mass
                    if met_ids_I:
                        component_names,component_group_names,\
                            precursor_formulas_O, precursor_masses_O,\
                            product_formulas_O, product_masses_O = [],[],[],[],[],[];
                        for met in met_ids_I:
                            component_names_tmp,component_group_names_tmp,\
                                precursor_formulas_tmp, precursor_masses_tmp,\
                                product_formulas_tmp, product_masses_tmp = [],[],[],[],[],[];
                            component_names_tmp,component_group_names_tmp,\
                                precursor_formulas_tmp, precursor_masses_tmp,\
                                product_formulas_tmp, product_masses_tmp = \
                                self.stage01_isotopomer_query.get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilutionAndMetID( \
                                experiment_id_I,sna,ms_methodtype_I,tp,dil,met);
                            if not(component_names_tmp): continue #no component information was found
                            component_names.extend(component_names_tmp)
                            component_group_names.extend(component_group_names_tmp)
                            precursor_formulas_O.extend(precursor_formulas_tmp)
                            precursor_masses_O.extend(precursor_masses_tmp)
                            product_formulas_O.extend(product_formulas_tmp)
                            product_masses_O.extend(product_masses_tmp)
                    else:
                        component_names,component_group_names,\
                            precursor_formulas_O, precursor_masses_O,\
                            product_formulas_O, product_masses_O = [],[],[],[],[],[];
                        component_names,component_group_names,\
                            precursor_formulas_O, precursor_masses_O,\
                            product_formulas_O, product_masses_O = \
                            self.stage01_isotopomer_query.get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilution( \
                            experiment_id_I,sna,ms_methodtype_I,tp,dil);
                    if not(component_names): continue #no component information was found
                    # extract unique met ids and precursor formula id
                    met_ids_unique = [];
                    met_ids = [];
                    #precursor_formulas_unique = [];
                    #product_formulas_unique = [];
                    met_id = '';
                    met_id_old = '';
                    # algorithm works because lists are ordered by component_names
                    for i,cn in enumerate(component_names):
                        met_id = cn.split('.')[0];
                        met_ids.append(met_id);
                        if met_id != met_id_old:
                            met_id_old = met_id;
                            met_ids_unique.append(met_id);
                            #precursor_formulas_unique.append(precursor_formulas_O[i]);
                            #product_formulas_unique.append(product_formulas_O[i]);
                    # get precursor and productformulas for each unique met id:
                    precursor_formulas_unique = [];
                    product_formulas_unique = [];
                    for met in met_ids_unique:
                        precursor_formula,product_formula = None,None;
                        precursor_formula,product_formula = self.stage01_isotopomer_query.get_precursorFormulaAndProductFormula_metID(met,'-','isotopomer_13C')
                        precursor_formulas_unique.append(precursor_formula);
                        product_formulas_unique.append(product_formula);
                    # build precursor and spectrum for each met
                    met_all_cnt = 0;
                    met_cnt_max = len(component_names); # for use in a while loop
                    for i,met in enumerate(met_ids_unique):
                        print('Building precursor and product spectrum from MRMs for metabolite ' + met);
                        # get filtrate samples
                        precursorFiltrate_measured = {};
                        productFiltrate_measured = {};

                        #precursorFiltrate_measured[precursor_formulas_unique[i]] = None; #keep track of all met_ids

                        precursorFiltrate = {};
                        productFiltrate = {};
                        met_cnt = met_all_cnt;
                        # iterate through mets/fragments then sample names in order to calculate the average for each component_name (fragment/mass)
                        while met_cnt < met_cnt_max and met==met_ids[met_cnt]:
                            # get filtrate sample names
                            sample_names = [];
                            replicate_numbers = [];
                            sample_description = 'Filtrate';
                            sample_names,replicate_numbers,sample_types = self.stage01_isotopomer_query.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePointAndDilution(experiment_id_I,sna,sample_description,component_names[met_cnt],tp,dil);
                            intensities = [];
                            for sn_cnt,sn in enumerate(sample_names):
                                # get intensities
                                intensity = None;
                                intensity = self.stage01_isotopomer_query.get_peakHeight_sampleNameAndComponentName(sn,component_names[met_cnt]);
                                if not(intensity): continue
                                intensities.append(intensity);
                            n_replicates = len(intensities);
                            intensities_average_filtrate = 0.0;
                            intensities_var_filtrate = 0.0;
                            # calculate average and CV of the intensities
                            if (not(intensities)): intensities_average_filtrate = 0.0;
                            elif n_replicates<2: intensities_average_filtrate = intensities[0];
                            else: 
                                #intensities_average_filtrate, intensities_var_filtrate = self.calculate.calculate_ave_var_R(intensities);
                                intensities_average_filtrate = numpy.mean(numpy.array(intensities));
                                intensities_var_filtrate = numpy.var(numpy.array(intensities));
                            # append value to dictionary
                            precursorFiltrate[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensities_average_filtrate;
                            productFiltrate[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensities_average_filtrate;
                            met_cnt += 1;
                        precursorFiltrate_measured[precursor_formulas_unique[i]] = precursorFiltrate
                        productFiltrate_measured[product_formulas_unique[i]] = productFiltrate
                        # get broth samples
                        sample_names = [];
                        sample_description = 'Broth';
                        sample_names,replicate_numbers,sample_types = self.stage01_isotopomer_query.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndTimePointAndDilution(experiment_id_I,sna,sample_description,tp,dil);
                        #sample_names,replicate_numbers,sample_types = self.stage01_isotopomer_query.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePointAndDilution(experiment_id_I,sna,sample_description,component_names[met_cnt],tp,dil);
                        # iterate through sample names then mets/fragments in order to calculate the spectrum for each sample and component
                        for sn_cnt,sn in enumerate(sample_names):
                            print('Building precursor and product spectrum from MRMs for sample ' + sn);
                            precursorPeakSpectrum_measured = {};
                            precursorPeakSpectrum_corrected = {};
                            productPeakSpectrum_measured = {};
                            productPeakSpectrum_corrected = {};
                            #precursorPeakSpectrum_measured[precursor_formulas_unique[i]] = None; #keep track of all met_ids
                            #precursorPeakSpectrum_corrected[precursor_formulas_unique[i]] = None; #keep track of all met_ids
                            precursorMeasured = {};
                            precursorCorrected = {};
                            productMeasured = {};
                            productCorrected = {};
                            met_cnt = met_all_cnt;
                            while met_cnt < met_cnt_max and met==met_ids[met_cnt]:
                                # get intensities
                                intensity = None;
                                intensity = self.stage01_isotopomer_query.get_peakHeight_sampleNameAndComponentName(sn,component_names[met_cnt]);
                                if not(intensity):
                                    precursorMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = 0.0;
                                    productMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = 0.0;
                                else:
                                    precursorMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensity;
                                    productMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensity;
                                #if precursorFiltrate_measured[precursor_formulas_unique[i]][(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] < 0.5*intensity: 
                                #    corrected_intensity = intensity - precursorFiltrate_measured[precursor_formulas_unique[i]][(precursor_masses_O[met_cnt],product_masses_O[met_cnt])];
                                #else: corrected_intensity = 0.0;
                                #precursorCorrected[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = corrected_intensity;
                                met_cnt += 1;
                            precursorPeakSpectrum_measured[precursor_formulas_unique[i]] = precursorMeasured;
                            productPeakSpectrum_measured[product_formulas_unique[i]] = productMeasured;

                            # generate normalized spectrum for the precursor:
                            precursorPeakSpectrum_measured, precursorPeakSpectrum_corrected, precursorPeakSpectrum_normalized \
                                = mids.build_precursorSpectrumFromMRMs(precursorPeakSpectrum_measured,precursorFiltrate_measured);
                            peakSpectrum_stats_O,precursorPeakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([precursorPeakSpectrum_normalized],True);
                            # update data_stage01_isotopomer_normalized
                            if precursorPeakSpectrum_theoretical[precursor_formulas_unique[i]]:
                                for k,v in precursorPeakSpectrum_theoretical[precursor_formulas_unique[i]].items():
                                    row1 = None;
                                    row1 = data_stage01_isotopomer_normalized(experiment_id_I,sn,sna,sample_types[sn_cnt],tp,dil,replicate_numbers[sn_cnt],
                                                                             met,precursor_formulas_unique[i],int(numpy.round(k)),
                                                                             precursorPeakSpectrum_measured[precursor_formulas_unique[i]][k],'cps',
                                                                             precursorPeakSpectrum_corrected[precursor_formulas_unique[i]][k],'cps',
                                                                             precursorPeakSpectrum_normalized[precursor_formulas_unique[i]][k],'normMax',
                                                                             v,peakSpectrum_stats_O[precursor_formulas_unique[i]][k]['absDev'],'MRM',True,None);
                                    self.session.add(row1);

                            # generate normalized spectrum for the product:
                            productPeakSpectrum_measured, productPeakSpectrum_corrected, productPeakSpectrum_normalized \
                                = mids.build_productSpectrumFromMRMs(productPeakSpectrum_measured,productFiltrate_measured);
                            peakSpectrum_stats_O,productPeakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([productPeakSpectrum_normalized],True);
                            # update data_stage01_isotopomer_normalized
                            if productPeakSpectrum_theoretical[product_formulas_unique[i]]:
                                for k,v in productPeakSpectrum_theoretical[product_formulas_unique[i]].items():
                                    row2 = None;
                                    row2 = data_stage01_isotopomer_normalized(experiment_id_I,sn,sna,sample_types[sn_cnt],tp,dil,replicate_numbers[sn_cnt],
                                                                             met,product_formulas_unique[i],int(numpy.round(k)),
                                                                             productPeakSpectrum_measured[product_formulas_unique[i]][k],'cps',
                                                                             productPeakSpectrum_corrected[product_formulas_unique[i]][k],'cps',
                                                                             productPeakSpectrum_normalized[product_formulas_unique[i]][k],'normMax',
                                                                             v,peakSpectrum_stats_O[product_formulas_unique[i]][k]['absDev'],'MRM',True,None);
                                    self.session.add(row2);

                        met_all_cnt = met_cnt
            self.session.commit();
    def execute_updateNormalizedSpectrum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''re-calculate intensity_normalized from intensity_corrected and used'''

        mids = mass_isotopomer_distributions();
        
        print('execute_updateNormalizedSpectrum...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Building precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            dataListUpdated = [];
            # get dilutions
            dilutions = [];
            dilutions = self.stage01_isotopomer_query.get_sampleDilution_experimentIDAndTimePoint_dataStage01Normalized(experiment_id_I,tp);
            for dil in dilutions:
                print('Building precursor and product spectrum from isotopomer normalized for dilution ' + str(dil));
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
                    print('Building precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                    # get the scan_types
                    if scan_types_I:
                        scan_types = scan_types_I;
                    else:
                        scan_types = [];
                        scan_types = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndDilutionAndSampleAbbreviations_dataStage01Normalized(experiment_id_I,tp,dil,sna);
                    for scan_type in scan_types:
                        print('Building precursor and product spectrum for scan type ' + scan_type)
                        # met_ids
                        if not met_ids_I:
                            met_ids = [];
                            met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanType_dataStage01Normalized( \
                                    experiment_id_I,sna,tp,dil,scan_type);
                        else:
                            met_ids = met_ids_I;
                        if not(met_ids): continue #no component information was found
                        for met in met_ids:
                            print('Building precursor and product spectrum from isotopomer normalized for metabolite ' + met);
                            # get sample names
                            sample_names = [];
                            sample_names,replicate_numbers,sample_types = self.stage01_isotopomer_query.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndMetIDAndTimePointAndDilutionAndScanType_dataStage01Normalized(experiment_id_I,sna,met,tp,dil,scan_type);
                            # iterate through sample names then mets/fragments in order to calculate the spectrum for each sample and component
                            for sn_cnt,sn in enumerate(sample_names):
                                print('Building precursor and product spectrum from isotopomer normalized for sample ' + sn);
                                # get peak data for the sample/met_id/scan_type
                                peak_data = [];
                                peak_data = self.stage01_isotopomer_query.get_data_experimentIDAndSampleNameAndMetIDAndAndScanType_normalized(experiment_id_I,sn,met,scan_type);
                                fragment_formulas = list(peak_data.keys());
                                peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                    peak_data, fragment_formulas, True);
                                peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                                # update data_stage01_isotopomer_normalized
                                for frag,spec in peakSpectrum_theoretical.items():
                                    if spec:
                                        fragment_str = re.sub('[+-]', '', frag);
                                        fragment_mass =  Formula(fragment_str).isotope.mass;
                                        for k,v in peakSpectrum_theoretical[frag].items():
                                            dataListUpdated.append({'experiment_id':experiment_id_I,
                                                            'sample_name':sn,
                                                            'sample_name_abbreviation':sna,
                                                            'sample_type':sample_types[sn_cnt],
                                                            'time_point':tp,
                                                            'dilution':dil,
                                                            'replicate_number':replicate_numbers[sn_cnt],
                                                            'met_id':met,
                                                            'fragment_formula':frag,
                                                            'fragment_mass':int(numpy.round(k)),
                                                            'intensity_corrected':peakSpectrum_corrected[frag][k],
                                                            'intensity_corrected_units':'cps',
                                                            'intensity_normalized':peakSpectrum_normalized[frag][k],
                                                            'intensity_normalized_units':'normMax',
                                                            'intensity_theoretical':v,
                                                            'abs_devFromTheoretical':peakSpectrum_stats[frag][k]['absDev'],
                                                            'scan_type':scan_type});
            self.stage01_isotopomer_query.update_data_stage01_isotopomer_normalized(dataListUpdated);
    def execute_recombineNormalizedSpectrum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None):
        '''recombine intensity_normalized from a lower and higher dilution'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();

        print('execute_recombineNormalizedSpectrum...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentIDAndComment_dataStage01Normalized(experiment_id_I,'Recombine');
        for tp in time_points:
            print('recombining spectrum for time-point ' + str(tp));
            dataListUpdated = [];
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAndComment_dataStage01Normalized(experiment_id_I,st,tp,sn,'Recombine');
                        sample_abbreviations.extend(sample_abbreviations_tmp);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndComment_dataStage01Normalized(experiment_id_I,st,tp,'Recombine');
                    sample_abbreviations.extend(sample_abbreviations_tmp);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('recombining spectrum for sample name abbreviation ' + sna);
                # get the scan_types
                scan_types = [];
                scan_types = self.stage01_isotopomer_query.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndComment_dataStage01Normalized(experiment_id_I,tp,sna,'Recombine');
                for scan_type in scan_types:
                    print('recombining spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndComment_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,'Recombine');
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('recombining spectrum for metabolite ' + met);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        for rep in replicate_numbers:
                            print('recombining spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_data_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            peakData_O,peakData_O_false,peakData_intensities_O = mids.recombine_dilutionsMRMs(peakData_I);
                            peakSpectrum_stats = mids.compare_peakSpectrum_normMax([peakData_intensities_O]);
                            # update data_stage01_isotopomer_normalized
                            for frag,spec in peakSpectrum_stats.items():
                                if spec:
                                    fragment_str = re.sub('[+-]', '', frag);
                                    fragment_mass =  Formula(fragment_str).isotope.mass;
                                    for k,v in peakSpectrum_stats[frag].items():
                                        if int(numpy.round(k)) in peakData_O[frag]:
                                            dataListUpdated.append({'experiment_id':experiment_id_I,
                                                        'sample_name_abbreviation':sna,
                                                        'time_point':tp,
                                                        'dilution':peakData_O[frag][int(numpy.round(k))]['dilution'],
                                                        'replicate_number':rep,
                                                        'met_id':met,
                                                        'fragment_formula':frag,
                                                        'fragment_mass':int(numpy.round(k)),
                                                        'intensity_normalized':peakData_O[frag][int(numpy.round(k))]['intensity'],
                                                        'intensity_normalized_units':'normMax',
                                                        'abs_devFromTheoretical':v['absDev'],
                                                        'scan_type':scan_type,
                                                        'used_':peakData_O[frag][int(numpy.round(k))]['used_'],
                                                        'comment_':peakData_O[frag][int(numpy.round(k))]['comment_']});
                            # update data_stage01_isotopomer_normalized (rows changed to false)
                            for frag,spec in peakData_O_false.items():
                                if spec:
                                    fragment_str = re.sub('[+-]', '', frag);
                                    fragment_mass =  Formula(fragment_str).isotope.mass;
                                    for k,v in peakData_O_false[frag].items():
                                        if v:
                                            dataListUpdated.append({'experiment_id':experiment_id_I,
                                                        'sample_name_abbreviation':sna,
                                                        'time_point':tp,
                                                        'dilution':v['dilution'],
                                                        'replicate_number':rep,
                                                        'met_id':met,
                                                        'fragment_formula':frag,
                                                        'fragment_mass':int(numpy.round(k)),
                                                        'intensity_normalized':v['intensity'],
                                                        'intensity_normalized_units':'normMax',
                                                        'abs_devFromTheoretical':None,
                                                        'scan_type':scan_type,
                                                        'used_':v['used_'],
                                                        'comment_':v['comment_']});
            self.stage01_isotopomer_query.update_data_stage01_isotopomer_normalized(dataListUpdated);
    def execute_analyzeAverages(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for MRM samples'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();
        print('execute_analyzeAverages...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
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
                print('Calculating average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Calculating average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating average precursor and product spectrum for metabolite ' + met);
                        ## get fragment formulas and masses
                        #fragment_formulas, fragment_masses = [],[];
                        #fragment_formulas,fragment_masses = self.stage01_isotopomer_query.get_fragmentFormulasAndMass_experimentIDAndSampleAbbreviationAndTimePointAndAndSampleTypeAndScanTypeAndMetID_dataStage01Normalized(experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        #for mass_cnt,mass in enumerate(fragment_masses):
                        #    print 'Calculating average precursor and product spectrum for fragment/mass ' + fragment_formulas[mass_cnt] + '/' + str(mass);
                        #    # get data
                        #    intensities = [];
                        #    intensities = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(experiment_id_I,sna,tp,sample_types_lst[sna_cnt],met,fragment_formulas[mass_cnt],mass,scan_type);
                        #    # calculate the average and cv
                        #    n_replicates = len(intensities);
                        #    intensities_average = 0.0;
                        #    intensities_var = 0.0;
                        #    intensities_cv = 0.0;
                        #    # calculate average and CV of intensities
                        #    if (not(intensities)): 
                        #        #continue
                        #        intensities_average = 0.0;
                        #        intensities_var = 0.0;
                        #        intensities_cv = 0.0;
                        #    elif n_replicates<2: # require at least 2 replicates
                        #        #continue
                        #        intensities_average = 0.0;
                        #        intensities_var = 0.0;
                        #        intensities_cv = 0.0;
                        #    else: 
                        #        intensities_average = numpy.mean(numpy.array(intensities));
                        #        intensities_var = numpy.var(numpy.array(intensities));
                        #        if (intensities_average <= 0.0): intensities_cv = 0.0;
                        #        else: intensities_cv = sqrt(intensities_var)/intensities_average*100;
                        #    # calculate the theoretical spectrum for the pecursor/mass
                        #    peakSpectrum_theoretical = mids.report_fragmentSpectrum_normMax([fragment_formulas[mass_cnt]],True);
                        #    # calculate the absolute deviation from the theoretical
                        #    intensity_theoretical = peakSpectrum_theoretical[fragment_formulas[mass_cnt]][mass];
                        #    if intensity_theoretical > 0.0:abs_devFromTheoretical = abs(intensity_theoretical-intensities_average)/intensity_theoretical*100;
                        #    else: abs_devFromTheoretical = None;
                        #    # add to data_stage01_isotopomer_averages
                        #    row = [];
                        #    row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,fragment_formulas[mass_cnt], mass,
                        #                                           n_replicates, intensities_average, intensities_cv,
                        #                                           'normMax', intensity_theoretical, abs_devFromTheoretical, scan_type, True)
                        #    self.session.add(row);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating average precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax(peakSpectrum_normalized_lst,True);
                        # update data_stage01_isotopomer_averages
                        for frag,spec in peakSpectrum_theoretical.items():
                            if spec:
                                fragment_str = re.sub('[+-]', '', frag);
                                fragment_mass =  Formula(fragment_str).isotope.mass;
                                for k,v in peakSpectrum_theoretical[frag].items():
                                    if v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normMax', v, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    elif v and k not in peakSpectrum_stats[frag]:
                                        intensities_cv = None;
                                        row = [];
                                        row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   None, None, intensities_cv,
                                                                   'normMax', v, None, scan_type, True);
                                    elif not v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normMax', None, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    self.session.add(row);
            self.session.commit();
    def execute_buildSpectrumFromPeakData(self,experiment_id_I,ms_methodtype_I='isotopomer_13C',sample_name_abbreviations_I = None,met_ids_I = None):
        '''Build spectrum from raw peak data'''

        '''Assumptions:
        Only 1 precursur:spectrum per sample name and
        only 1 precursor:spectrum per dilution
        (i.e. the best/most representative precursor:spectrum was chose from the
        available EPI scans and dilutions of that particular precursor)
        '''

        mids = mass_isotopomer_distributions();

        # extract out the peakSpectrum
        # get sample names for the experiment
        print('execute_buildSpectrumFromPeakData...')
        if sample_name_abbreviations_I:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for sna in sample_name_abbreviations_I:
                for st in sample_types:
                    sample_names_tmp = [];
                    sample_names_tmp = self.stage01_isotopomer_query.get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakData(experiment_id_I,st,sna);
                    sample_names.extend(sample_names_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        else:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.stage01_isotopomer_query.get_sampleNames_experimentIDAndSampleType_peakData(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        # create database table
        for sn_cnt,sn in enumerate(sample_names):
            print('building spectrum for sample ' + sn);
            # get other information about the sample for later use
            sample_name_abbreviation,time_point,replicate_numbers = None,None,None;
            sample_name_abbreviation,time_point,replicate_numbers = self.stage01_isotopomer_query.get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakData(experiment_id_I,sn);
            # get met_id and precursor_formula for each sample
            scan_type = [];
            scan_type = self.stage01_isotopomer_query.get_scanType_experimentIDAndSampleName_peakData(experiment_id_I,sn);
            for scantype in scan_type:
                print('building spectrum for scan type ' + scantype);
                # get met_id and precursor formula for each sample
                if met_ids_I:
                    met_id, precursor_formula = [], [];
                    for met in met_ids_I:
                        met_id_tmp, precursor_formula_tmp = [], []
                        met_id_tmp, precursor_formula_tmp = self.stage01_isotopomer_query.get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanTypeAndMetID_peakData(experiment_id_I,sn,scantype,met);
                        met_id.extend(met_id_tmp);
                        precursor_formula.extend(precursor_formula_tmp);
                else:
                    met_id, precursor_formula = [], [];
                    met_id, precursor_formula = self.stage01_isotopomer_query.get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakData(experiment_id_I,sn,scantype);
                for precursor_cnt, precursor in enumerate(precursor_formula):
                    print('building spectrum for met_id/precursor ' + met_id[precursor_cnt] + '/' + precursor);
                    precursor_str = re.sub('[+-]', '', precursor);
                    precursor_mass =  Formula(precursor_str).isotope.mass
                    # get all product fragments for the met_id/precursor
                    precursor_formulas_monoisotopic, product_formulas = [], [];
                    precursor_formulas_monoisotopic, product_formulas = self.stage01_isotopomer_query.get_precursorAndProductFormulas_metID(met_id[precursor_cnt],'-','tuning');
                    product_formulas.append(precursor_formulas_monoisotopic[0]); # add precursor to list of fragments
                    # get peak data for the sample/met_id/precursor_formula
                    peak_data = [];
                    peak_data = self.stage01_isotopomer_query.get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakData(experiment_id_I,sn,met_id[precursor_cnt],precursor,scantype);
                    peakSpectrum_measured,\
                        peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakData_normMax(\
                        peak_data, product_formulas, 0.3, True);
                    peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                    # update data_stage01_isotopomer_normalized
                    for frag,spec in peakSpectrum_theoretical.items():
                        if spec:
                            product_str = re.sub('[+-]', '', frag);
                            product_mass =  Formula(product_str).isotope.mass;
                            for k,v in peakSpectrum_theoretical[frag].items():
                                row1 = None;
                                row1 = data_stage01_isotopomer_peakSpectrum(experiment_id_I,sn,sample_name_abbreviation,
                                        sample_types_lst[sn_cnt],time_point,replicate_numbers,
                                        met_id[precursor_cnt],precursor,int(numpy.round(precursor_mass)),
                                        frag,int(numpy.round(k)),
                                        peakSpectrum_measured[frag][k],'cps',
                                        peakSpectrum_corrected[frag][k],'cps',
                                        peakSpectrum_normalized[frag][k],'normMax',
                                        v,peakSpectrum_stats[frag][k]['absDev'],scantype,True,None);
                                self.session.add(row1);
        self.session.commit();
    def execute_updatePeakSpectrum(self,experiment_id_I,sample_name_abbreviations_I = None):
        '''re-calculate intensity_normalized from intensity_corrected and used'''

        mids = mass_isotopomer_distributions();

        # extract out the peakSpectrum
        dataListUpdated = [];
        # get sample names for the experiment
        print('execute_updatePeakSpectrum...')
        if sample_name_abbreviations_I:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for sna in sample_name_abbreviations_I:
                for st in sample_types:
                    sample_names_tmp = [];
                    sample_names_tmp = self.stage01_isotopomer_query.get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakSpectrum(experiment_id_I,st,sna);
                    sample_names.extend(sample_names_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        else:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.stage01_isotopomer_query.get_sampleNames_experimentIDAndSampleType_peakSpectrum(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        # create database table
        for sn_cnt,sn in enumerate(sample_names):
            print('updating peak spectrum for sample ' + sn);
            # get other information about the sample for later use
            sample_name_abbreviation,time_point,replicate_numbers = None,None,None;
            sample_name_abbreviation,time_point,replicate_numbers = self.stage01_isotopomer_query.get_sampleNameAbbreviationsAndTimePointAndReplicateNumber_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            # get met_id and precursor_formula for each sample
            scan_type = [];
            scan_type = self.stage01_isotopomer_query.get_scanType_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            for scantype in scan_type:
                print('building spectrum for scan type ' + scantype);
                # get met_id and precursor formula for each sample
                met_id, precursor_formula = [], [];
                met_id, precursor_formula = self.stage01_isotopomer_query.get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakSpectrum(experiment_id_I,sn,scantype);
                for precursor_cnt, precursor in enumerate(precursor_formula):
                    print('updating peak spectrum for met_id/precursor ' + met_id[precursor_cnt] + '/' + precursor);
                    precursor_str = re.sub('[+-]', '', precursor);
                    precursor_mass =  Formula(precursor_str).isotope.mass
                    # get all product fragments for the met_id/precursor
                    precursor_formulas_monoisotopic, product_formulas = [], [];
                    precursor_formulas_monoisotopic, product_formulas = self.stage01_isotopomer_query.get_precursorAndProductFormulas_metID(met_id[precursor_cnt],'-','tuning');
                    product_formulas.append(precursor_formulas_monoisotopic[0]); # add precursor to list of fragments
                    # get peak data for the sample/met_id/precursor_formula
                    peak_data = [];
                    peak_data = self.stage01_isotopomer_query.get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(experiment_id_I,sn,met_id[precursor_cnt],precursor,scantype);
                    peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                        peak_data, product_formulas,True);
                    peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                    # update data_stage01_isotopomer_peakSpectrum
                    for frag,spec in peakSpectrum_theoretical.items():
                        if spec:
                            product_str = re.sub('[+-]', '', frag);
                            product_mass =  Formula(product_str).isotope.mass;
                            for k,v in peakSpectrum_theoretical[frag].items():
                                dataListUpdated.append({'experiment_id':experiment_id_I,
                                                'sample_name':sn,
                                                'sample_name_abbreviation':sample_name_abbreviation,
                                                'sample_type':sample_types_lst[sn_cnt],
                                                'time_point':time_point,
                                                'replicate_number':replicate_numbers,
                                                'met_id':met_id[precursor_cnt],
                                                'precursor_formula':precursor,
                                                'precursor_mass':int(numpy.round(precursor_mass)),
                                                'product_formula':frag,
                                                'product_mass':int(numpy.round(k)),
                                                'intensity_corrected':peakSpectrum_corrected[frag][k],
                                                'intensity_corrected_units':'cps',
                                                'intensity_normalized':peakSpectrum_normalized[frag][k],
                                                'intensity_normalized_units':'normMax',
                                                'intensity_theoretical':v,
                                                'abs_devFromTheoretical':peakSpectrum_stats[frag][k]['absDev'],
                                                'scan_type':scantype});
        self.stage01_isotopomer_query.update_data_stage01_isotopomer_peakSpectrum(dataListUpdated);
    def execute_filterValidatedFragments(self,experiment_id_I):
        '''Filter fragments that have been validated by a U12C reference experiment'''

        print('filtering validated met/fragment pairs...')
        dataUpdate_O = [];
        for k,v in self.isotopomer_13C_fragments_validated.items():
            for frag in v:
                dataUpdate_O.append({'experiment_id':experiment_id_I,'met_id':k,'product_formula':frag});
        self.stage01_isotopomer_query.update_validFragments_stage01_isotopomer_peakSpectrum(dataUpdate_O);
    def execute_normalizeSpectrumFromReference(self,experiment_id_I,sample_name_abbreviations_I = None, use_mrm_ref = True, met_ids_I = None):
        # 1. import used peak spectrum to normalized table after multiplying by measured
        #       scaling factor calculated from used MRM spectrum
        # 2. be sure that the MRMs in the normalized table have been finalized
        
        '''NOTES:
        cannot follow the forloop pattern used in buildSpectrumFromPeakData (i.e. starting with sample name)
        must use the forloop pattern similar to updateNormalizedSpectrum, but without a forloop for dilutions
        (i.e. time-point to sample name abbreviations to scan types to mets)
        buildSpectrumFromPeakData and updatePeakSpectrum methods process one product:spectrum from a single precursor at a time;
        each precursor:product:spectrum is associated with only one sample name
        However, because the entire range of precursor:product:spectrum for a given met can encompass multiple dilutions and therefore different 
        sample names, a more generic approach must be used'''

        '''Assumptions:
        only a single precursor:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();

        # extract out the peakSpectrum
        print('execute_normalizeSpectrumFromReference...')        
        # get time points
        time_points = [];
        time_points = self.stage01_isotopomer_query.get_timePoints_experimentID_peakSpectrum(experiment_id_I);
        for tp in time_points:
            print('normalizing peak spectrum from reference for time-point ' + tp);
            # get sample name abbreviations
            if sample_name_abbreviations_I:
                sample_name_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_name_abbreviations_tmp = [];
                    sample_name_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_peakSpectrum(experiment_id_I,st,tp);
                    sample_name_abbreviations.extend([sna for sna in sample_name_abbreviations_tmp if sna in sample_name_abbreviations_I]);
                    sample_types_lst.extend([st for sna in sample_name_abbreviations_tmp if sna in sample_name_abbreviations_I]);
            else:
                sample_name_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_name_abbreviations_tmp = [];
                    sample_name_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_peakSpectrum(experiment_id_I,st,tp);
                    sample_name_abbreviations.extend(sample_name_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_name_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_name_abbreviations):
                print('normalizing peak spectrum from reference for sample name abbreviation ' + sna);
                # get scan types
                scan_type = [];
                scan_type = self.stage01_isotopomer_query.get_scanType_experimentIDAndTimePointSampleNameAbbreviation_peakSpectrum(experiment_id_I,tp,sna);
                for scantype in scan_type:
                    print('normalizing peak spectrum from reference for scan type ' + scantype);
                    # get replicates
                    replicate_numbers = [];
                    replicate_numbers = self.stage01_isotopomer_query.get_replicateNumber_experimentIDAndTimePointAndSampleNameAbbreviationAndScanType_peakSpectrum(experiment_id_I,tp,sna,scantype);
                    for rep in replicate_numbers:
                        print('normalizing peak spectrum from reference for replicate ' + str(rep));
                        # get other information about the sample for later use
                        sample_name, dilution = None,None;
                        sample_name,dilution = self.stage01_isotopomer_query.get_sampleNameAndDilution_experimentIDAndTimePointAndSampleNameAbbreviationAndScanType_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep);
                        # get met_id
                        if met_ids_I:
                            met_id = met_ids_I;
                        else:
                            med_id = [];
                            met_id = self.stage01_isotopomer_query.get_metID_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicate_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep);
                        for met_cnt,met in enumerate(met_id):
                            print('normalizing peak spectrum from reference for met_id ' + met);
                            # get precursor formula and mass
                            precursor_formula, precursor_mass = [], [];
                            precursor_formula, precursor_mass = self.stage01_isotopomer_query.get_precursorFormulaAndMass_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetID_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep,met);
                            peak_data_all = {};
                            scaling_factors_all = {};
                            for precursor_cnt, precursor in enumerate(precursor_formula):
                                peak_data_all[precursor] = None;
                                scaling_factors_all[precursor] = None;
                                print('normalizing peak spectrum from reference for precursor ' + precursor);
                                precursor_str = re.sub('[+-]', '', precursor);
                                # get all product fragments for the met_id/precursor
                                product_formulas = [];
                                product_formulas = self.stage01_isotopomer_query.get_productFormulas_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetIDAndPrecursorFormula_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep,met,precursor);
                                # get the m+0 precursor_formula
                                precursor_formula_monoisotopic = self.stage01_isotopomer_query.get_precursorFormula_metID(met,'-','tuning');
                                precursor_monoisotopic_str = re.sub('[+-]', '', precursor_formula_monoisotopic);
                                precursor_monoisotpoic_mass = int(numpy.round(Formula(precursor_monoisotopic_str).isotope.mass));
                                # get peakSpectrum data
                                peak_data = {};
                                peak_data = self.stage01_isotopomer_query.get_data_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetIDAndPrecursorFormula_peakSpectrum(\
                                    experiment_id_I,tp,sna,scantype,rep,met,precursor);
                                peak_data_all[precursor] = peak_data;
                                if scantype == 'ER': 
                                    scaling_factors_all[precursor] = 1.0; # there is no need to scale ER or other precursor ion scans
                                else:
                                    if use_mrm_ref:
                                        # get reference MRM spectrum scaling factor for the sample
                                        #scaling_factor,scaling_factor_cv = None,None; # will need to incorporate propogation of error
                                        #scaling_factor,scaling_factor_cv = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Averages(experiment_id_I,sample_name_abbreviation,time_point,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                        scaling_factor = None; # does not require the propogation of error
                                        scaling_factor = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(experiment_id_I,sna,tp,rep,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                        if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                        else:
                                            scaling_factors_all[precursor] = 0.0;
                                            ## substitute with reference spectrum
                                            #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                            #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                            #scaling_factors_all[precursor] = scaling_factor;
                                    else:
                                        # get reference ER spectrum scaling factor for the sample
                                        scaling_factor = None;
                                        scaling_factor = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndPrecursorFormulaAndMassAndScanType_peakSpectrum(experiment_id_I,sna,tp,rep,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'ER');
                                        if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                        else:
                                            scaling_factors_all[precursor] = 0.0;
                                            ## substitute with reference spectrum
                                            #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                            #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                            #scaling_factors_all[precursor] = scaling_factor;
                            # normalize spectrum to reference MRM for each precursor (m+0,m+1,...)
                            peakSpectrum_normalized = mids.normalize_peakSpectrum_normMax(peak_data_all,scaling_factors_all);
                            peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                            # update data_stage01_isotopomer_peakSpectrum
                            for frag,spec in peakSpectrum_theoretical.items():
                                if spec:
                                    product_str = re.sub('[+-]', '', frag);
                                    product_mass =  Formula(product_str).isotope.mass;
                                    for k,v in peakSpectrum_theoretical[frag].items():
                                        if k in peakSpectrum_normalized[frag]:
                                            row = None;
                                            row = data_stage01_isotopomer_normalized(experiment_id_I,sample_name,sna,sample_types_lst[sna_cnt],tp,dilution,rep,
                                                                                         met,frag,int(numpy.round(k)),
                                                                                         #None,'cps',None,'cps',
                                                                                         None,'cps',peakSpectrum_normalized[frag][k],'normMax', #allows for spectrum updates
                                                                                         peakSpectrum_normalized[frag][k],'normMax',
                                                                                         v,peakSpectrum_stats[frag][k]['absDev'],scantype,True,None);
                                            self.session.add(row);
        self.session.commit();
    def execute_normalizeSpectrumFromReference_v1(self,experiment_id_I,sample_name_abbreviations_I = None,use_mrm_ref = True):
        # 1. import used peak spectrum to normalized table after multiplying by measured
        #       scaling factor calculated from used MRM spectrum
        # 2. be sure that the MRMs in the normalized table have been finalized
        
        '''NOTES: Broken for the following reason:
        cannot follow the forloop pattern used in buildSpectrumFromPeakData (i.e. starting with sample name)
        must use the forloop pattern used in updateNormalizedSpectrum (i.e. time-point to dilutions to sample name abbreviations to scan types to mets)
        buildSpectrumFromPeakData and updatePeakSpectrum methods process one product:spectrum from a single precursor at a time;
        each precursor:product:spectrum is associated with only one sample name
        However, because the entire range of precursor:product:spectrum for a given met can encompass multiple dilutions and therefore different 
        sample names, a more generic approach must be used
        Please use current version'''

        mids = mass_isotopomer_distributions();
        
        # extract out the peakSpectrum
        # get sample name for the experiment
        print('execute_normalizeSpectrumFromReference...')
        if sample_name_abbreviations_I:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for sna in sample_name_abbreviations_I:
                for st in sample_types:
                    sample_names_tmp = [];
                    sample_names_tmp = self.stage01_isotopomer_query.get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakSpectrum(experiment_id_I,st,sna);
                    sample_names.extend(sample_names_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        else:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.stage01_isotopomer_query.get_sampleNames_experimentIDAndSampleType_peakSpectrum(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        for sn_cnt,sn in enumerate(sample_names):
            print('normalizing peak spectrum for sample ' + sn);
            # get other information about the sample for later use
            sample_name_abbreviation,time_point,dilution,replicate_numbers = None,None,None,None;
            sample_name_abbreviation,time_point,dilution,replicate_numbers = self.stage01_isotopomer_query.get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            # get met_id and precursor_formula for each sample
            scan_type = [];
            scan_type = self.stage01_isotopomer_query.get_scanType_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            for scantype in scan_type:
                print('normalizing spectrum for scan type ' + scantype);
                # get met_id
                med_id = [];
                met_id = self.stage01_isotopomer_query.get_metID_experimentIDAndSampleNameAndScanType_peakSpectrum(experiment_id_I,sn,scantype);
                for met in met_id:
                    print('normalizing peak spectrum for met_id ' + met);
                    # get precursor formula and mass
                    precursor_formula, precursor_mass = [], [];
                    precursor_formula, precursor_mass = self.stage01_isotopomer_query.get_precursorFormulaAndMass_experimentIDAndSampleNameAndMetIDAndScanType_peakSpectrum(experiment_id_I,sn,met,scantype);
                    peak_data_all = {};
                    scaling_factors_all = {};
                    for precursor_cnt, precursor in enumerate(precursor_formula):
                        peak_data_all[precursor] = None;
                        scaling_factors_all[precursor] = None;
                        print('normalizing peak spectrum for precursor ' + precursor);
                        precursor_str = re.sub('[+-]', '', precursor);
                        # get all product fragments for the met_id/precursor
                        product_formulas = [];
                        product_formulas = self.stage01_isotopomer_query.get_productFormulas_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(experiment_id_I,sn,met,precursor,scantype);
                        # get the m+0 precursor_formula
                        precursor_formula_monoisotopic = self.stage01_isotopomer_query.get_precursorFormula_metID(met,'-','tuning');
                        precursor_monoisotopic_str = re.sub('[+-]', '', precursor_formula_monoisotopic);
                        precursor_monoisotpoic_mass = int(numpy.round(Formula(precursor_monoisotopic_str).isotope.mass));
                        # get peakSpectrum data
                        peak_data = {};
                        #Change to sna+rep+timepoint:peak_data = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(experiment_id_I,sn,met,precursor,scantype);
                        peak_data_all[precursor] = peak_data;
                        if scantype == 'ER': 
                            scaling_factors_all[precursor] = 1.0; # there is no need to scale ER or other precursor ion scans
                        else:
                            if use_mrm_ref:
                                # get reference MRM spectrum scaling factor for the sample
                                #scaling_factor,scaling_factor_cv = None,None; # will need to incorporate propogation of error
                                #scaling_factor,scaling_factor_cv = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Averages(experiment_id_I,sample_name_abbreviation,time_point,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                scaling_factor = None; # does not require the propogation of error
                                scaling_factor = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(experiment_id_I,sample_name_abbreviation,time_point,replicate_numbers,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                else:
                                    scaling_factors_all[precursor] = 0.0;
                                    ## substitute with reference spectrum
                                    #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                    #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                    #scaling_factors_all[precursor] = scaling_factor;
                            else:
                                # get reference ER spectrum scaling factor for the sample
                                scaling_factor = None;
                                scaling_factor = self.stage01_isotopomer_query.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndPrecursorFormulaAndMassAndScanType_peakSpectrum(experiment_id_I,sample_name_abbreviation,time_point,replicate_numbers,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'ER');
                                if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                else:
                                    scaling_factors_all[precursor] = 0.0;
                                    ## substitute with reference spectrum
                                    #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                    #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                    #scaling_factors_all[precursor] = scaling_factor;
                    # normalize spectrum to reference MRM for each precursor (m+0,m+1,...)
                    peakSpectrum_normalized = mids.normalize_peakSpectrum_normMax(peak_data_all,scaling_factors_all);
                    peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                    # update data_stage01_isotopomer_peakSpectrum
                    for frag,spec in peakSpectrum_theoretical.items():
                        if spec:
                            product_str = re.sub('[+-]', '', frag);
                            product_mass =  Formula(product_str).isotope.mass;
                            for k,v in peakSpectrum_theoretical[frag].items():
                                if k in peakSpectrum_normalized[frag]:
                                    row = None;
                                    row = data_stage01_isotopomer_normalized(experiment_id_I,sn,sample_name_abbreviation,sample_types_lst[sn_cnt],time_point,dilution,replicate_numbers,
                                                                                 met,frag,int(numpy.round(k)),
                                                                                 None,'cps',None,'cps',
                                                                                 peakSpectrum_normalized[frag][k],'normMax',
                                                                                 v,peakSpectrum_stats[frag][k]['absDev'],scantype,True);
                                    self.session.add(row);
        self.session.commit();
    def execute_analyzeAveragesNormSum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for all samples and scan types'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();
        
        print('execute_analyzeAveragesNormSum...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
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
                print('Calculating average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Calculating average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating average precursor and product spectrum for metabolite ' + met);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating average precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normSum(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normSum(peakSpectrum_normalized_lst,True);
                        # update data_stage01_isotopomer_normalized
                        for frag,spec in peakSpectrum_theoretical.items():
                            if spec:
                                fragment_str = re.sub('[+-]', '', frag);
                                fragment_mass =  Formula(fragment_str).isotope.mass;
                                for k,v in peakSpectrum_theoretical[frag].items():
                                    if v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averagesNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normSum', v, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    elif v and k not in peakSpectrum_stats[frag]:
                                        intensities_cv = None;
                                        row = [];
                                        row = data_stage01_isotopomer_averagesNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   None, None, intensities_cv,
                                                                   'normSum', v, None, scan_type, True);
                                    elif not v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averagesNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normSum', None, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    self.session.add(row);
            self.session.commit();
    def execute_analyzeSpectrumAccuracy(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average spectrum accuracy'''

        mids = mass_isotopomer_distributions();
        
        print('execute_analyzeSpectrumAccuracy...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating spectrum accuracy from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
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
                print('Calculating spectrum accuracy from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Calculating spectrum accuracy for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating spectrum accuracy for metabolite ' + met);
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating spectrum accuracy for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_accuracy = mids.calculate_fragmentSpectrumAccuracy(peakSpectrum_normalized_lst);
                        # update data_stage01_isotopomer_spectrumAccuracy
                        for frag,accuracy in peakSpectrum_accuracy.items():
                            if accuracy:
                                row = [];
                                row = data_stage01_isotopomer_spectrumAccuracy(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, accuracy, scan_type, True);
                                self.session.add(row);
            self.session.commit();
    def execute_analyzeSpectrumAccuracyNormSum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average spectrum accuracy'''

        mids = mass_isotopomer_distributions();
        
        print('execute_analyzeSpectrumAccuracy...')
        # get time points
        time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating spectrum accuracy from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
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
                print('Calculating spectrum accuracy from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Calculating spectrum accuracy for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating spectrum accuracy for metabolite ' + met);
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating spectrum accuracy for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normSum(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_accuracy = mids.calculate_fragmentSpectrumAccuracy_normSum(peakSpectrum_normalized_lst);
                        # update data_stage01_isotopomer_spectrumAccuracy
                        for frag,accuracy in peakSpectrum_accuracy.items():
                            if accuracy:
                                row = [];
                                row = data_stage01_isotopomer_spectrumAccuracyNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, accuracy, scan_type, True);
                                self.session.add(row);
            self.session.commit();
    def execute_makeIsotopomerSimulation_cobraMat(self,csource_name_I, csource_I, csource_mix_I, experiment_id_I, sample_name_abbreviations_I = None, time_points_I = None, met_ids_I = None, scan_types_I = None):
        '''export a fluxomics experimental data for simulation using the cobra 2.0 fluxomics module'''

        # TODO:
        #   1. move to analysis_stage02
        #   2. query csource_name, csourse, and csource_mix from database

        # calculate the emu for the input_met:
        # make carbon input for the experiment:
        # 80/20 1-13C/U-13C
        #inputfrag = isoexecute.make_CSourceMix([['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
        #                      ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O']],
        #                      [0.8,0.2]);
        # 30/20/50 1-13C/U-13C/U-12C
        #inputfrag = isoexecute.make_CSourceMix([['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
        #                      ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O'],
        #                      ['CHO','CH2O','CH2O','CH2O','CH2O','CH3O']],
        #                      [0.3,0.2,0.5]);
        # 80/20 1-13C/U-13C
        #inputfrag = isoexecute.make_CSourceMix([['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O']],
        #                      [1.0]);
        inputfrag = self.make_CSourceMix(csource_I,csource_mix_I);
        # get experiment information:
        met_id_conv_dict = {'Hexose_Pool_fru_glc-D':'glc-D',
                            'Pool_2pg_3pg':'3pg',
                            '23dpg':'13dpg'};
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
                # Matlab script file to make the structures
                experiment_name = 'Isotopomer_' + re.sub('[.\/]','',experiment_id_I) + '_' + re.sub(' ','',sna) + '_' + re.sub(' ','',str(tp));
                filename = 'data/_output/' + 'isotopomer_' + re.sub('[.\/]','',experiment_id_I) + '_' + re.sub(' ','',sna) + '_' + re.sub(' ','',str(tp)) + '.m';
                filename_dict = 'data/_output/' + 'isotopomer_' + re.sub('[.\/]','',experiment_id_I) + '_' + re.sub(' ','',sna) + '_' + re.sub(' ','',str(tp)) + '.json';
                #filename_mat = 'data/_output/' + 'isotopomer_' + re.sub('[.\/]','',experiment_id_I) + '_' + re.sub(' ','',sna) + '_' + re.sub(' ','',str(tp)) + '.mat';
                mat_script = '';
                experiment = {};
                struct_data = {};
                experiment_stdev = [];
                #struct_mat_data = {};
                #struct_mat_data_list = [];
                #struct_mat_dtype_list = [];
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
                        # format the metabolite
                        if met in list(met_id_conv_dict.keys()):
                            met_formatted = met_id_conv_dict[met];
                        else: met_formatted = met;
                        met_formatted = re.sub('-','_DASH_',met_formatted)
                        met_formatted = re.sub('[(]','_LPARANTHES_',met_formatted)
                        met_formatted = re.sub('[)]','_RPARANTHES_',met_formatted)
                        # fragments
                        fragment_formulas = [];
                        fragment_formulas = self.stage01_isotopomer_query.get_fragmentFormula_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        # frag c map
                        frag_cmap = {};
                        frag_cmap = self.stage01_isotopomer_query.get_precursorFormulaAndProductFormulaAndCMaps_metID(met,'-','tuning');
                        for frag in fragment_formulas:
                            # data
                            data_mat = [];
                            data_mat_cv = [];
                            data_mat, data_mat_cv = self.stage01_isotopomer_query.get_spectrum_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetIDAndFragmentFormula_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met,frag);
                            # combine into a structure
                            frag_tmp_int = [];
                            frag_tmp_str = [];
                            for f in frag_cmap[frag]:
                                if f: 
                                    frag_tmp_int.append(1);
                                    frag_tmp_str.append('1');
                                else: 
                                    frag_tmp_int.append(0);
                                    frag_tmp_str.append('0');
                            fieldname = 'x' + met_formatted+'_'+ re.sub('[-+]','',frag);
                            #struct_mat_data['x'+met_formatted+'_c'+''.join(frag_tmp_str)] = {'met':'x'+met_formatted+'_c',
                            #                                                                 'fragment':frag_tmp_int,
                            #                                                                 'data':data_mat,
                            #                                                                 'metfrag':'x'+met_formatted+'_c'+''.join(frag_tmp_str)};
                            mat_script = mat_script + ("%s.fragments.%s.met = '%s';\n" %(experiment_name,fieldname,'x'+met_formatted+'_c'));
                            mat_script = mat_script + ("%s.fragments.%s.fragment = %s';\n" %(experiment_name,fieldname,frag_tmp_int));
                            mat_script = mat_script + ("%s.fragments.%s.data = %s';\n" %(experiment_name,fieldname,data_mat));
                            mat_script = mat_script + ("%s.fragments.%s.metfrag = '%s';\n" %(experiment_name,fieldname,'x'+met_formatted+'_c'+''.join(frag_tmp_str)));

                            data_names = [];
                            data_stdev = [];
                            for i,d in enumerate(data_mat):
                                stdev = 0.0;
                                if data_mat_cv[i]: stdev = data_mat[i]*data_mat_cv[i]/100;
                                data_names.append(fieldname+str(i));
                                data_stdev.append(stdev);
                                experiment_stdev.append(stdev);
                            struct_data[fieldname] = {'met':'x'+met_formatted+'_c','fragment':frag_tmp_int,
                                                      'data_names':data_names,'data_ave':data_mat,'data_cv':data_mat_cv,
                                                      'data_stdev':data_stdev,'metfrag':'x'+met_formatted+'_c'+''.join(frag_tmp_str)};

                            #data_mat_reshape = numpy.array(data_mat).reshape((len(data_mat),1));
                            #frag_tmp_int_reshape = numpy.array(frag_tmp_int).reshape((len(frag_tmp_int),1));
                            #struct_mat_data = numpy.array([(['x'+met_formatted+'_c'],frag_tmp_int_reshape,data_mat_reshape,['x'+met_formatted+'_c'+''.join(frag_tmp_str)])], dtype=[('met', 'O'), ('fragment', 'O'), ('data', 'O'), ('metfrag', 'O')]);
                            #struct_mat_dtype = (fieldname.encode('ascii','ignore'),'O');
                            #struct_mat_data_list.append(struct_mat_data);
                            #struct_mat_dtype_list.append(struct_mat_dtype);
                ## dump the experiment to a matlab file
                #experiment['input']=[];
                ##experiment['fragments']=struct_mat_data;
                #experiment['fragments']=numpy.array([tuple(struct_mat_data_list)],dtype=struct_mat_dtype_list);
                #experiment['ignored']=[];
                #experiment['inputfrag']=inputfrag;
                #experiment['std2']=0.015;
                #experiment_mat = numpy.array([(experiment['fragments'],experiment['inputfrag'],experiment['std2'])],
                #                             dtype = [('fragments','O'),('inputfrag','O'),('std2','O')]);
                #savemat(filename_mat,{experiment_name:experiment_mat});
                # dump the experiment to a matlab script to generate the matlab file in matlab
                mat_script = mat_script + ("%s.input = [];\n" %experiment_name);
                mat_script = mat_script + ("%s.ignored = [];\n" %experiment_name);
                for k,v in inputfrag.items():
                    mat_script = mat_script + ("%s.inputfrag.%s = %s;\n" %(experiment_name,k,v));
                mat_script = mat_script + ("%s.std2=0.015;\n" %experiment_name);
                mat_script = mat_script + ("save('%s','%s');\n" %(experiment_name+'.mat',experiment_name));
                with open(filename,'w') as f:
                    f.write(mat_script);
                # dump the experiment to a json file
                experiment['fragments']=struct_data;
                experiment['inputfrag']={csource_name_I:inputfrag};
                experiment['stdev']=numpy.mean(numpy.array(experiment_stdev));
                with open(filename_dict,'w') as f:
                    json.dump(experiment,f,indent=4);
    #table updates:
    def update_dataStage01NormalizedFromAverages(self,experiment_id_I):
        '''update data_stage01_normalized from data_stage01_averages'''

        # get row information for all samples
        row = [];
        row = self.stage01_isotopomer_query.get_row_experimentID_dataStage01Averages(experiment_id_I); 
        # update entries that match the corresponding experiment_id/sample_name_abbreviation/sample_type/time_point/met_id/fragment_formula/fragment_mass
        # with used_ and comment_
        self.stage01_isotopomer_query.update_usedAndComment_stage01_isotopomer_normalized(row);
    #table initializations:
    def drop_dataStage01(self):
        try:
            #data_stage01_isotopomer_MQResultsTable.__table__.drop(engine,True);
            data_stage01_isotopomer_peakData.__table__.drop(engine,True);
            data_stage01_isotopomer_peakList.__table__.drop(engine,True);
            data_stage01_isotopomer_peakSpectrum.__table__.drop(engine,True);
            data_stage01_isotopomer_normalized.__table__.drop(engine,True);
            data_stage01_isotopomer_averages.__table__.drop(engine,True);
            data_stage01_isotopomer_averagesNormSum.__table__.drop(engine,True);
            data_stage01_isotopomer_spectrumAccuracy.__table__.drop(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01(self):
        try:
            data_stage01_isotopomer_MQResultsTable.__table__.create(engine,True);
            data_stage01_isotopomer_peakSpectrum.__table__.create(engine,True);
            data_stage01_isotopomer_peakList.__table__.create(engine,True);
            data_stage01_isotopomer_peakData.__table__.create(engine,True);
            data_stage01_isotopomer_normalized.__table__.create(engine,True);
            data_stage01_isotopomer_averages.__table__.create(engine,True);
            data_stage01_isotopomer_averagesNormSum.__table__.create(engine,True);
            data_stage01_isotopomer_spectrumAccuracy.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_peakList).filter(data_stage01_isotopomer_peakList.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_peakData).filter(data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_normalized).filter(data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_averages).filter(data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_spectrumAccuracy).filter(data_stage01_isotopomer_spectrumAccuracy.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_isotopomer_peakSpectrum).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_peakList).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_peakData).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_normalized).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_averages).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_averagesNormSum).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_spectrumAccuracy).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage01_isotopomer_averages(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_averages).filter(data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage01_isotopomer_peakData(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_peakData).filter(data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    #plotting methods:
    def plot_normalizedSpectrum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''plot the normalized spectrum'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''
        mids = mass_isotopomer_distributions();
        print('plot_normalizedSpectrum...')
        plot = matplot();
        # get time points
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
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        fragment_formulas_lst = [];
                        if not(replicate_numbers): continue; #no replicates found
                        for rep in replicate_numbers:
                            print('Plotting precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            if peakData_I:
                                fragment_formulas = list(peakData_I.keys());
                                fragment_formulas_lst.extend(fragment_formulas)
                                peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                    peakData_I, fragment_formulas, True);
                                peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                                
                        # plot spectrum data for all replicates and fragments
                        fragment_formulas_unique = list(set(fragment_formulas_lst));
                        for fragment in fragment_formulas_unique:
                            panelLabels = [];
                            xticklabels = [];
                            mean = [];
                            xlabel = 'm/z'
                            ylabel = 'intensity'
                            for rep,spectrum in enumerate(peakSpectrum_normalized_lst):
                                panelLabels_tmp = sna+'_'+met+'_'+fragment+'_'+str(rep+1)
                                xticklabels_tmp = [];
                                mean_tmp = [];
                                if fragment not in spectrum: 
                                    print('no spectrum found for fragment ' + fragment);
                                    continue;
                                for mass,intensity in spectrum[fragment].items():
                                    intensity_tmp = intensity;
                                    if not intensity_tmp: intensity_tmp=0.0
                                    mean_tmp.append(intensity_tmp);
                                    xticklabels_tmp.append(mass);
                                panelLabels.append(panelLabels_tmp);
                                xticklabels.append(xticklabels_tmp);
                                mean.append(mean_tmp);
                            plot.multiPanelBarPlot('',xticklabels,xlabel,ylabel,panelLabels,mean);
    def plot_normalizedSpectrumNormSum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for all samples and scan types'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''
        mids = mass_isotopomer_distributions();
        
        print('plot_normalizedSpectrumNormSum...')
        plot = matplot();
        # get time points
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
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
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
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.stage01_isotopomer_query.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Plotting precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.stage01_isotopomer_query.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normSum(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        # plot spectrum data for all replicates and fragments
                        fragment_formulas_unique = list(set(fragment_formulas_lst));
                        for fragment in fragment_formulas_unique:
                            panelLabels = [];
                            xticklabels = [];
                            mean = [];
                            xlabel = 'm/z'
                            ylabel = 'intensity'
                            for rep,spectrum in enumerate(peakSpectrum_normalized_lst):
                                panelLabels_tmp = sna+'_'+met+'_'+fragment+'_'+str(rep+1)
                                xticklabels_tmp = [];
                                mean_tmp = [];
                                for mass,intensity in spectrum[fragment].items():
                                    intensity_tmp = intensity;
                                    if not intensity_tmp: intensity_tmp=0.0
                                    mean_tmp.append(intensity_tmp);
                                    xticklabels_tmp.append(mass);
                                panelLabels.append(panelLabels_tmp);
                                xticklabels.append(xticklabels_tmp);
                                mean.append(mean_tmp);
                            plot.multiPanelBarPlot('',xticklabels,xlabel,ylabel,panelLabels,mean);
    def plot_averageSpectrumNormSum(self,experiment_id_I, time_points_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for all samples and scan types'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''
        mids = mass_isotopomer_distributions();
        
        print('plot_averagesNormSum...')
        plot = matplot();
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.stage01_isotopomer_query.get_timePoint_experimentID_dataStage01AveragesNormSum(experiment_id_I);
        for tp in time_points:
            print('Plotting product and precursor for time-point ' + str(tp));
            # get sample names and sample name abbreviations
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
            else:
                sample_abbreviations = [];
                sample_types = ['Unknown'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.stage01_isotopomer_query.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Plotting product and precursor for sample name abbreviation ' + sna);
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
                    print('Plotting product and precursor for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.stage01_isotopomer_query.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting product and precursor for metabolite ' + met);
                        # fragments
                        fragment_formulas = [];
                        fragment_formulas = self.stage01_isotopomer_query.get_fragmentFormula_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        for frag in fragment_formulas:
                            print('Plotting product and precursor for fragment ' + frag);
                            # data
                            data_mat = [];
                            data_mat_cv = [];
                            data_masses = [];
                            data_mat,data_mat_cv,data_masses = self.stage01_isotopomer_query.get_spectrum_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetIDAndFragmentFormula_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met,frag);
                            data_stdev = [];
                            for i,d in enumerate(data_mat):
                                stdev = 0.0;
                                stderr = 0.0;
                                if data_mat_cv[i]: 
                                    stdev = data_mat[i]*data_mat_cv[i]/100;
                                data_stdev.append(stdev);
                            title = sna+'_'+met+'_'+frag;
                            plot.barPlot(title,data_masses,'intensity','m/z',data_mat,var_I=None,se_I=data_stdev,add_labels_I=True)
    # data_stage01_isotopomer deletes
    def execute_deleteExperimentFromMQResultsTable(self,experiment_id_I,sample_types_I = ['Quality Control','Unknown']):
        '''delete rows in data_stage01_MQResultsTable by sample name and sample type 
        (default = Quality Control and Unknown) from the experiment'''
        
        print('deleting rows in data_stage01_MQResultsTable by sample_name and sample_type...');
        dataDeletes = [];
        # get sample_names
        sample_names = [];
        for st in sample_types_I:
            sample_names_tmp = [];
            sample_names_tmp = self.stage01_isotopomer_query.get_allSampleNames_experimentIDAndSampleType(experiment_id_I,st);
            sample_names.extend(sample_names_tmp);
        for sn in sample_names:
            # format into a dictionary list
            print('deleting sample_name ' + sn);
            dataDeletes.append({'sample_name':sn});
        # delete rows based on sample_names
        self.stage01_isotopomer_query.delete_row_sampleName(dataDeletes);
