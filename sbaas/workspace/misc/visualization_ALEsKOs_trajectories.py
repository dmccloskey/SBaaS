import matplotlib.pyplot as pp
from scipy import linspace, sin
from scipy.io import loadmat
from scipy.interpolate import splrep, splev
import numpy
import json

from resources.cookb_signalsmooth import smooth
from resources.legendre_smooth import legendre_smooth
from Bio.Statistics import lowess

def load_matlab_data(matlab_data,filename):
    # load matlab data
    ale_ids = loadmat(matlab_data)['ALEsKOs']['ale_id'][0];
    time = loadmat(matlab_data)['ALEsKOs']['time'][0];
    growth_rate = loadmat(matlab_data)['ALEsKOs']['growth_rate'][0];
    # export json file
    ALEsKOs_trajectories = {};
    for i,id in enumerate(ale_ids):
        ALEsKOs_trajectories[id[0]] = {'time':[j for j in time[i][0]],
                                       'growth_rate':[j for j in growth_rate[i][0]]};
    with open(filename, 'w') as outfile:
        json.dump(ALEsKOs_trajectories, outfile, indent=4);

def fit_growth_rate(filename,ALEsKOs_order,ALEsKOs_textLabels):
    # import json file
    ALEsKOs_trajectories = json.load(open(filename))
    # fit spline to data
    ALEsKOs_trajectories_fitted = {};
    # Create a Figure object.
    fig = pp.figure();
    #fig.set_size_inches(11,8.5)
    cnt = 1;
    for k in ALEsKOs_order:
        x = ALEsKOs_trajectories[k['sample_name_abbreviation']]['time']
        y = ALEsKOs_trajectories[k['sample_name_abbreviation']]['growth_rate']
        ##spline
        #tck = splrep(x,y,k=3) #no smoothing factor
        #x2_spline = linspace(min(x),max(x),500)
        #y2_spline = splev(x2,tck)
        ##moving window filer
        #x2 = numpy.array(x);
        #y2 = smooth(numpy.array(y),window_len=10, window='hanning');
        ##legendre smoothing optimization
        #smooth = legendre_smooth(len(x),1,1e-4,25)
        #x2 = numpy.array(x);
        #y2 = smooth.fit(numpy.array(y))
        #lowess
        x2 = numpy.array(x);
        y2 = lowess.lowess(x2,numpy.array(y),f=0.1,iter=100)
        # Create an Axes object.
        #ax = fig.add_subplot(1,1,1) # one row, one column, first plot
        ax = fig.add_subplot(6,4,cnt) # one row, one column, first plot
        # Add a title.
        ax.set_title(k['sample_label'])
        # Set the axis
        pp.axis([0,40,0,max(y)+0.1]);
        # Add axis labels.
        if cnt in [21,22,23,24]:
            ax.set_xlabel('Time [days]')
        if cnt in [1,5,9,13,17,21]:
            ax.set_ylabel('GR [hr-1]')
        # Modify xtick labels
        if cnt not in [21,22,23,24]:
            ax.set_xticklabels([]); #remove xticklabels
        # Label data points
        tck = splrep(x,y,k=3,s=1.); #spline fit with very high smoothing factor
        x_days = ALEsKOs_textLabels[k['sample_name_abbreviation']]['day']
        y_days = splev(x_days,tck)
        for i,txt in enumerate(ALEsKOs_textLabels[k['sample_name_abbreviation']]['dataType']):
            ax.annotate(txt, (x_days[i],y_days[i]-.15))
        # Create the plot
        pp.plot(x_days,y_days,'rx',x,y,'b.',x2,y2,'g')
        #record
        ALEsKOs_trajectories_fitted[k['sample_name_abbreviation']] = {'time':x2,'growth_rate':y2};
        cnt += 1;
    #display the plot
    pp.show()
    return ALEsKOs_trajectories, ALEsKOs_trajectories_fitted

def _main_():
    ALEsKOs_trajectories = {};
    ALEsKOs_trajectories_fitted = {};
    ALEsKOs_trajectories_filename = 'data\\visualization\\ALEsKOs_trajectories.json';
    ALEsKOs_trajectories_filename_matlab = 'C:\\Users\\dmccloskey-sbrg\\Documents\\MATLAB\\ALEsKOs\\ALEsKOs_trajectories.mat'

    ALEsKOs_startdate = 7.3574e05; #t0 [datenum]
    ALEsKOs_jumps = [0,
                     4.90295451390557,8.13420451397542,11.8321211806033,
                     15.8571211806266,18.9397600694792,20.4700000000000,
                     23.8793434028514,26.6071211805567,29.4967045139521,
                     32.4890656250529,
                     36.6057322917506]; #days relative to t0
    ALEsKOs_order = [{'sample_name_abbreviation':'OxicEvo04pgiEvo01EcoliGlc','sample_label':'pgi_e1'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo02EcoliGlc','sample_label':'pgi_e2'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo03EcoliGlc','sample_label':'pgi_e3'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo04EcoliGlc','sample_label':'pgi_e4'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo05EcoliGlc','sample_label':'pgi_e5'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo06EcoliGlc','sample_label':'pgi_e6'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo07EcoliGlc','sample_label':'pgi_e7'},
                    {'sample_name_abbreviation':'OxicEvo04pgiEvo08EcoliGlc','sample_label':'pgi_e8'},
                    {'sample_name_abbreviation':'OxicEvo04ptsHIcrrEvo01EcoliGlc','sample_label':'pts_e1'},
                    {'sample_name_abbreviation':'OxicEvo04ptsHIcrrEvo02EcoliGlc','sample_label':'pts_e2'},
                    {'sample_name_abbreviation':'OxicEvo04ptsHIcrrEvo03EcoliGlc','sample_label':'pts_e3'},
                    {'sample_name_abbreviation':'OxicEvo04ptsHIcrrEvo04EcoliGlc','sample_label':'pts_e4'},
                    {'sample_name_abbreviation':'OxicEvo04tpiAEvo01EcoliGlc','sample_label':'tpi_e1'},
                    {'sample_name_abbreviation':'OxicEvo04tpiAEvo02EcoliGlc','sample_label':'tpi_e2'},
                    {'sample_name_abbreviation':'OxicEvo04tpiAEvo03EcoliGlc','sample_label':'tpi_e3'},
                    {'sample_name_abbreviation':'OxicEvo04tpiAEvo04EcoliGlc','sample_label':'tpi_e4'},
                    {'sample_name_abbreviation':'OxicEvo04sdhCadhBEvo01EcoliGlc','sample_label':'sdh_e1'},
                    {'sample_name_abbreviation':'OxicEvo04sdhCadhBEvo02EcoliGlc','sample_label':'sdh_e2'},
                    {'sample_name_abbreviation':'OxicEvo04sdhCadhBEvo03EcoliGlc','sample_label':'sdh_e3'},
                    {'sample_name_abbreviation':'OxicEvo04gndEvo01EcoliGlc','sample_label':'gnd_e1'},
                    {'sample_name_abbreviation':'OxicEvo04gndEvo02EcoliGlc','sample_label':'gnd_e2'},
                    {'sample_name_abbreviation':'OxicEvo04gndEvo03EcoliGlc','sample_label':'gnd_e3'},
                    {'sample_name_abbreviation':'OxicEvo04Evo01EcoliGlc','sample_label':'e4wt_e1'},
                    {'sample_name_abbreviation':'OxicEvo04Evo02EcoliGlc','sample_label':'e4wt_e2'}]
    ALEsKOs_textLabels = {
        #d = dna resequencing
        #r = rna resequencing
        #f = fluxomics
        #m = metabolomics
        #p = phenomics
                    'OxicEvo04pgiEvo01EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[11]]},
                    'OxicEvo04pgiEvo02EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04pgiEvo03EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04pgiEvo04EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04pgiEvo05EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04pgiEvo06EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04pgiEvo07EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[10]]}, #stock 10 is the endpoint
                    'OxicEvo04pgiEvo08EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[2],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04ptsHIcrrEvo01EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04ptsHIcrrEvo02EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04ptsHIcrrEvo03EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[4],ALEsKOs_jumps[11]]},
                    'OxicEvo04ptsHIcrrEvo04EcoliGlc':{'dataType':['drfmp','dm','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[4],ALEsKOs_jumps[11]]},
                    'OxicEvo04tpiAEvo01EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04tpiAEvo02EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04tpiAEvo03EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04tpiAEvo04EcoliGlc':{'dataType':['drfmp','dm','dm','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[1],ALEsKOs_jumps[3],ALEsKOs_jumps[11]]},
                    'OxicEvo04sdhCadhBEvo01EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04sdhCadhBEvo02EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04sdhCadhBEvo03EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04gndEvo01EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04gndEvo02EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04gndEvo03EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04Evo01EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]},
                    'OxicEvo04Evo02EcoliGlc':{'dataType':['drfmp','drfmp'],
                                                       'day':[ALEsKOs_jumps[0],ALEsKOs_jumps[11]]}};

    ALEsKOs_trajectories_groups = {"evo04pgi":['OxicEvo04pgiEvo01EcoliGlc',
                                                'OxicEvo04pgiEvo02EcoliGlc',
                                                'OxicEvo04pgiEvo03EcoliGlc',
                                                'OxicEvo04pgiEvo04EcoliGlc',
                                                'OxicEvo04pgiEvo05EcoliGlc',
                                                'OxicEvo04pgiEvo06EcoliGlc',
                                                'OxicEvo04pgiEvo07EcoliGlc',
                                                'OxicEvo04pgiEvo08EcoliGlc'],
                                "evo04ptsHIcrr":['OxicEvo04ptsHIcrrEvo01EcoliGlc',
                                                'OxicEvo04ptsHIcrrEvo02EcoliGlc',
                                                'OxicEvo04ptsHIcrrEvo03EcoliGlc',
                                                'OxicEvo04ptsHIcrrEvo04EcoliGlc'],
                                "evo04tpiA":['OxicEvo04tpiAEvo01EcoliGlc',
                                                'OxicEvo04tpiAEvo02EcoliGlc',
                                                'OxicEvo04tpiAEvo03EcoliGlc',
                                                'OxicEvo04tpiAEvo04EcoliGlc'],
                                "evo04":['OxicEvo04Evo01EcoliGlc',
                                                'OxicEvo04Evo02EcoliGlc'],
                                "evo04gnd":['OxicEvo04gndEvo01EcoliGlc',
                                                'OxicEvo04gndEvo02EcoliGlc',
                                                'OxicEvo04gndEvo03EcoliGlc'],
                                "evo04sdh":['OxicEvo04sdhCadhBEvo01EcoliGlc',
                                                'OxicEvo04sdhCadhBEvo02EcoliGlc',
                                                'OxicEvo04sdhCadhBEvo03EcoliGlc']};
                                                    

    load_matlab_data(ALEsKOs_trajectories_filename_matlab,ALEsKOs_trajectories_filename);
    ALEsKOs_trajectories, ALEsKOs_trajectories_fitted = fit_growth_rate(ALEsKOs_trajectories_filename,ALEsKOs_order,ALEsKOs_textLabels);