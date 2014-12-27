from fluxomics.isotopomer import convert_ids

def _main_():
    #cids = convert_ids('data\\Schellenberger2011_metmapping.csv','data\\Schellenberger2011_metsoriginal.csv');
    #cids.convert_ctrack();
    #cids.write_ctrack_converted('data\\Schellenberger2011_metsupdated.csv');

    cids = convert_ids('data\\Schellenberger2011_metmapping.csv','data\\Schellenberger2012_metsOriginal.csv');
    cids.convert_ctrack();
    cids.write_ctrack_converted('data\\Schellenberger2012_metsUpdated.csv');

    cids = convert_ids('data\\Schellenberger2011_metmapping.csv','data\\Schellenberger2012_isotopomersOriginal.csv');
    cids.convert_ctrack();
    cids.write_ctrack_converted('data\\Schellenberger2012_isotopomersUpdated.csv');