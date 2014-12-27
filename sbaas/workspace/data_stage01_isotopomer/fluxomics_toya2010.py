from analysis.analysis_base.base_importData import base_importData
from analysis.analysis_stage01_isotopomer import stage01_isotopomer_query
from analysis.analysis_stage01_isotopomer import stage01_isotopomer_execute
from resources.molmass import Formula
from math import fabs
import re
from models.models_stage01_isotopomer import data_stage01_isotopomer_averagesNormSum
from models.models_base import Session

def import_Toya2011(filename_I=None):
    '''import fluxomics data from Toya2010 ('10.1002/btpr.420')'''
    filename_I = 'data\\Toya2010_LCMS_Data.csv';
    session = Session();
    isoquery = stage01_isotopomer_query();
    # JS ids
    toya2js = {'F16P':'fdp','DHAP':'dhap','3PG':'3pg',
                'PEP':'pep','PYR':'pyr','Ru5P':'ru5pD',
                'R5P':'r5p','S7P':'s7p','MAL':'malL'};
    # iJO1366 ids
    #toya2ijo = {'F16P':'fdp_c','DHAP':'dhap_c','3PG':'3pg_c',
    #            'PEP':'pep_c','PYR':'pyr_c','Ru5P':'ru5p_DASH_D_c',
    #            'R5P':'r5p_c','S7P':'s7p_c','MAL':'mal_DASH_L_c'};
    toya2ijo = {'F16P':'fdp','DHAP':'dhap','3PG':'3pg',
                'PEP':'pep','PYR':'pyr','Ru5P':'ru5p-D',
                'R5P':'r5p','S7P':'s7p','MAL':'mal-L'};

    # import raw data as a dictionary
    bi = base_importData();
    bi.read_csv(filename_I);
    bi.format_data();
    # process exp data
    dataTable = [];
    dataTable_js = [];
    update_exp,update_sim = False,False;
    for d in bi.data:
        # covert id    
        met_id = toya2ijo[d['met']];
        fragment = isoquery.get_precursorFormula_metID(met_id,'-','tuning');
        fragment_str = re.sub('[+-]', '', fragment);
        mass = Formula(fragment_str).isotope.massnumber

        if d['data']=='Exp':
            update_exp = True;
            intensity = [];
            intensity_sd = [];
            if d['m0']:
                m = d['m0'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m1']:
                m = d['m1'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m2']:
                m = d['m2'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m3']:
                m = d['m3'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m4']:
                m = d['m4'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m5']:
                m = d['m5'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m6']:
                m = d['m6'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
            if d['m7']:
                m = d['m7'].split(';');
                intensity.append(m[0]);
                intensity_sd.append(m[1]);
        elif d['data']=='Sim':
            update_sim = True;
            theoretical = [];
            if d['m0']:
                m = d['m0'];
                theoretical.append(m);
            if d['m1']:
                m = d['m1'];
                theoretical.append(m);
            if d['m2']:
                m = d['m2'];
                theoretical.append(m);
            if d['m3']:
                m = d['m3'];
                theoretical.append(m);
            if d['m4']:
                m = d['m4'];
                theoretical.append(m);
            if d['m5']:
                m = d['m5'];
                theoretical.append(m);
            if d['m6']:
                m = d['m6'];
                theoretical.append(m);
            if d['m7']:
                m = d['m7'];
                theoretical.append(m);
        if update_exp and update_sim:
            for i,v in enumerate(intensity):
                # convert string input to float
                intensity_f = [];
                intensity_sd_f = [];
                theoretical_f = [];
                cv_f = None;
                abs_dev_f = None;
                intensity_f = float(intensity[i])
                intensity_sd_f = float(intensity_sd[i])
                theoretical_f = float(theoretical[i]);
                if intensity_f > 0:
                    cv_f = intensity_sd_f/intensity_f*100;
                    abs_dev_f = fabs(intensity_f-theoretical_f);
                else:
                    cv_f = None;
                    abs_dev_f = None;
                # create datatable row
                row1 = {};
                #row1['experiment_id'] = 'Toya2011_10.1002/btpr.420';
                row1['experiment_id'] = '10.1002/btpr.420';
                row1['sample_name_abbreviation'] = d['strain'];
                row1['sample_type'] = 'Unknown';
                row1['time_point'] = d['time'];
                row1['met_id'] = toya2ijo[d['met']];
                row1['fragment_formula'] = fragment;
                row1['fragment_mass'] = mass+i;
                row1['n_replicates'] = 3;
                row1['intensity_normalized_average'] = intensity_f;
                row1['intensity_normalized_cv'] = cv_f;
                row1['intensity_normalized_units'] = 'normSum';
                row1['intensity_theoretical'] = theoretical_f;
                row1['abs_devFromTheoretical'] = abs_dev_f;
                row1['scan_type'] = 'MRM';
                row1['used_'] = True;
                row1['comment_'] = 'Published data';
                dataTable.append(row1);
                # repeat for JS2011
                row2 = {};
                #row2['experiment_id'] = 'Toya2011_10.1002/btpr.420';
                row2['experiment_id'] = '10.1002/btpr.420';
                row2['sample_name_abbreviation'] = d['strain'];
                row2['sample_type'] = 'Unknown';
                row2['time_point'] = d['time'];
                row2['met_id'] = toya2js[d['met']];
                row2['fragment_formula'] = fragment;
                row2['fragment_mass'] = mass+i;
                row2['n_replicates'] = 3;
                row2['intensity_normalized_average'] = intensity_f;
                row2['intensity_normalized_cv'] = cv_f;
                row2['intensity_normalized_units'] = 'normSum';
                row2['intensity_theoretical'] = theoretical_f;
                row2['abs_devFromTheoretical'] = abs_dev_f;
                row2['scan_type'] = 'MRM';
                row2['used_'] = True;
                row2['comment_'] = 'Published data';
                dataTable_js.append(row2);
                # reset values:
                update_exp,update_sim = False,False;
                # upload data to database (if desired)
                row = data_stage01_isotopomer_averagesNormSum(row1['experiment_id'], row1['sample_name_abbreviation'], row1['sample_type'], row1['time_point'],
                                                                     row1['met_id'],row1['fragment_formula'],row1['fragment_mass'],row1['n_replicates'],
                                                                     row1['intensity_normalized_average'],row1['intensity_normalized_cv'],row1['intensity_normalized_units'],
                                                                     row1['intensity_theoretical'],row1['abs_devFromTheoretical'],row1['scan_type'],row1['used_'],row1['comment_']);
                session.add(row);
    session.commit();

def _main_():
    # import data from literature:
    #import_Toya2011();

    # make carbon input for the experiment:
    # 80/20 1-13C/U-13C
    #emu_O = isoexecute.make_CSourceMix([['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
    #                      ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O']],
    #                      [0.8,0.2]);
    # 30/20/50 1-13C/U-13C/U-12C
    #emu_O = isoexecute.make_CSourceMix([['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
    #                      ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O'],
    #                      ['CHO','CH2O','CH2O','CH2O','CH2O','CH3O']],
    #                      [0.3,0.2,0.5]);
    # 80/20 1-13C/U-13C

    # make experiment
    csource = [['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O'],
                          ['[13C]HO','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H2O','[13C]H3O'],
                          ['CHO','CH2O','CH2O','CH2O','CH2O','CH3O']];
    csource_mix = [0.3,0.2,0.5];
    isoexecute = stage01_isotopomer_execute();
    isoexecute.execute_makeIsotopomerExperiment_cobraMat('xglc_DASH_D_e',csource,csource_mix,'10.1002/btpr.420');

