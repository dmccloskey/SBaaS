from analysis import *

stage00 = stage00_execute()

# import structure files into metabolomics_standards
data = [
        {'met_id':'12ppd-R','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'2392410','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'23dpg','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'2h3mb','file_directory':'data\\BIGG_mol\\','file_ext':'.sdf'},
{'met_id':'2h3mv','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'2hic','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'2mcit','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'2obut','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'2pg','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'34hpp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'35cgmp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'3mob','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'3pg','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'4hdxbutn','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'4mop','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'5oxpro','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'6pgc','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'6pgl','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ac','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'acac','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'accoa','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'acon-C','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'actp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ade','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'adn','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'adp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'adpglc','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'AICAr','file_directory':'data\\BIGG_mol\\','file_ext':'.sdf'},
{'met_id':'akg','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ala-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ala-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'amp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'anserine','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'arg-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'argsuc','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'asn-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'asp-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'atp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'btal','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'btn','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'camp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cbp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cdp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'chor','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cit','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'citr-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cmp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'coa','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ctp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cys-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cyst-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'cytd','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dadp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'damp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'datp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dcdp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dcmp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dctp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dgdp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dgmp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dgtp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dhap','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dimp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ditp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dtdpglu','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dtmp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dttp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dump','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'dutp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'e4p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'f1p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'f6p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'fad','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'fdp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'fol','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'for','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'fum','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'G_2mcit','file_directory':'data\\BIGG_mol\\','file_ext':'.sdf'},
{'met_id':'G_phlac','file_directory':'data\\BIGG_mol\\','file_ext':'.sdf'},
{'met_id':'g1p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'g3p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'g6p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gal1p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gam6p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gdp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glc-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glcn','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gln-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glu-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glutacon','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glx','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gly','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glyald','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glyc3p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'glyclt','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gmp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gsn','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gthox','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gthrd','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gtp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'gua','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'hcys-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'his-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'hxan','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'icit','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'idp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ile-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'imp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'inost','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ins','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'itp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'L2aadp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'lac-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'lac-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'Lcystin','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'leu-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'Lhcystin','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'lys-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'mal-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'malcoa','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'man','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'man1p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'man6p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'met-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'mev-R','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'mmal','file_directory':'data\\BIGG_mol\\','file_ext':'.sdf'},
{'met_id':'Nacasp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'Nacser','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'nad','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'nadh','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'nadp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'nadph','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'Ntigly','file_directory':'data\\BIGG_mol\\','file_ext':'.sdf'},
{'met_id':'oaa','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'orn','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'orot','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'oxa','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'pep','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'phe-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'phpyr','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ppal','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'pro-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'prpp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'pser-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ptrc','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'pyr','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'r5p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'rbl-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'rib-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ribflv','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ru5p-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'s7p','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ser-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'skm','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'spmd','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'sprm','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'succ','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'succoa','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'taur','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'thf','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'THF-2-ol','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'thr-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'thym','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'trp-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'tyr-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'udp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'udpg','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'udpgal','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'udpglcur','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ump','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'ura','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'urate','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'uri','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'utp','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'val-L','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'xan','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'xu5p-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'xyl-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
{'met_id':'xylu-D','file_directory':'data\\BIGG_mol\\','file_ext':'.mol'},
        ]
stage00.execute_importStructureFile(data)

# update formula, mass, and exact mass from structure files
met_ids = ['12ppd-R','2392410','23dpg','2h3mb','2h3mv','2hic',
           '2mcit','2obut','2pg','34hpp','35cgmp','3mob','3pg',
           '4hdxbutn','4mop','5oxpro','6pgc','6pgl','ac','acac',
           'accoa','acon-C','actp','ade','adn','adp','adpglc',
           'AICAr','akg','ala-D','ala-L','amp','anserine','arg-L',
           'argsuc','asn-L','asp-L','atp','btal','btn','camp',
           'cbp','cdp','chor','cit','citr-L','cmp','coa','ctp',
           'cys-L','cyst-L','cytd','dadp','damp','datp','dcdp',
           'dcmp','dctp','dgdp','dgmp','dgtp','dhap','dimp','ditp',
           'dtdpglu','dtmp','dttp','dump','dutp','e4p','f1p','f6p',
           'fad','fdp','fol','for','fum','G_2mcit','G_phlac','g1p',
           'g3p','g6p','gal1p','gam6p','gdp','glc-D','glcn',
           'gln-L','glu-L','glutacon','glx','gly','glyald','glyc3p',
           'glyclt','gmp','gsn','gthox','gthrd','gtp','gua',
           'hcys-L','his-L','hxan','icit','idp','ile-L','imp',
           'inost','ins','itp','L2aadp','lac-D','lac-L','Lcystin',
           'leu-L','Lhcystin','lys-L','mal-L','malcoa','man',
           'man1p','man6p','met-L','mev-R','mmal','Nacasp','Nacser',
           'nad','nadh','nadp','nadph','Ntigly','oaa','orn',
           'orot','oxa','pep','phe-L','phpyr','ppal','pro-L',
           'prpp','pser-L','ptrc','pyr','r5p','rbl-L','rib-D',
           'ribflv','ru5p-D','s7p','ser-L','skm','spmd','sprm',
           'succ','succoa','taur','thf','THF-2-ol','thr-L',
           'thym','trp-L','tyr-L','udp','udpg','udpgal',
           'udpglcur','ump','ura','urate','uri','utp','val-L',
           'xan','xu5p-D','xyl-D','xylu-D'];
stage00.execute_updateFormulaAndMassFromStructure(met_ids)

# update precursor formula and exact mass from structure files
stage00.execute_updatePrecursorFormulaAndMass(met_ids);