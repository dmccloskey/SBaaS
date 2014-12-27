####atomMapping scripts####
from analysis.analysis_base import *
from analysis.analysis_stage02_isotopomer.stage02_isotopomer_io import stage02_isotopomer_io
import copy
from sqlalchemy import or_
def part1():
    session = Session();
    try:
        data = session.query(data_stage02_isotopomer_atomMappingReactions1);
        data_O = []
        if data:
            for i,d in enumerate(data):
                print d.id
                reactants_elements_tracked = [];
                reactants_positions_tracked = [];
                if d.reactants_mapping[0]:
                    for r_cnt,r in enumerate(d.reactants_mapping):
                        element = d.reactants_elements_tracked[r_cnt];
                        elements_tracked = [];
                        positions_tracked = [];
                        for e_cnt, e in enumerate(r):
                            elements_tracked.append(element);
                            positions_tracked.append(e_cnt);
                        reactants_elements_tracked.append(elements_tracked);
                        reactants_positions_tracked.append(positions_tracked);
                #else:
                #    reactants_elements_tracked.append([]);
                #    reactants_positions_tracked.append([]);

                products_elements_tracked = [];
                products_positions_tracked = [];
                if d.products_mapping[0]:
                    for r_cnt,r in enumerate(d.products_mapping):
                        element = d.products_elements_tracked[r_cnt];
                        elements_tracked = [];
                        positions_tracked = [];
                        for e_cnt, e in enumerate(r):
                            elements_tracked.append(element);
                            positions_tracked.append(e_cnt);
                        products_elements_tracked.append(elements_tracked);
                        products_positions_tracked.append(positions_tracked);
                #else:
                #    products_elements_tracked.append([]);
                #    products_positions_tracked.append([]);

                data_O.append({'mapping_id':d.mapping_id,
                                'rxn_id':d.rxn_id,
                                'rxn_description':d.rxn_description,
                                'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                                'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                                'reactants_ids_tracked':d.reactants_ids_tracked,
                                'products_ids_tracked':d.products_ids_tracked,
                                'reactants_mapping':d.reactants_mapping,
                                'products_mapping':d.products_mapping,
                                'rxn_equation':d.rxn_equation,
                                'products_elements_tracked':products_elements_tracked,
                                'products_positions_tracked':products_positions_tracked,
                                'reactants_elements_tracked':reactants_elements_tracked,
                                'reactants_positions_tracked':reactants_positions_tracked,
                                'used_':d.used_,
                                'comment_':d.comment_,
                                'id':d.id});
        io = base_exportData(data_O);
        io.write_dict2csv('data\\140923_data_stage02_isotopomer_atomMappingReactions03.csv');
        io.write_dict2json('data\\140923_data_stage02_isotopomer_atomMappingReactions03.json');

        io2 = stage02_isotopomer_io();
        io2.add_data_stage02_isotopomer_atomMappingReactions(data_O);

    except SQLAlchemyError as e:
        print(e);
def part2():
    io0 = base_importData();
    io0.read_csv('data\\140923_data_stage02_isotopomer_atomMappingReactions01.csv')
    io1 = base_exportData(io0.data);
    io1.write_dict2json('data\\140923_data_stage02_isotopomer_atomMappingReactions01.json')
def part3():
    io2 = stage02_isotopomer_io();
    io2.import_data_stage02_isotopomer_atomMappingReactions_update('data\\140923_data_stage02_isotopomer_atomMappingReactions01.json');
def part4():
    session = Session();
    try:
        data_O = []
        data = None;
        data = session.query(data_stage02_isotopomer_atomMappingReactions).filter(data_stage02_isotopomer_atomMappingReactions.mapping_id.like('central02')).all();
        if data:
            for i,d in enumerate(data):
                data_O.append({'mapping_id':'central03',
                                'rxn_id':d.rxn_id,
                                'rxn_description':d.rxn_description,
                                'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                                'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                                'reactants_ids_tracked':d.reactants_ids_tracked,
                                'products_ids_tracked':d.products_ids_tracked,
                                'reactants_mapping':d.reactants_mapping,
                                'products_mapping':d.products_mapping,
                                'rxn_equation':d.rxn_equation,
                                'products_elements_tracked':d.products_elements_tracked,
                                'products_positions_tracked':d.products_positions_tracked,
                                'reactants_elements_tracked':d.reactants_elements_tracked,
                                'reactants_positions_tracked':d.reactants_positions_tracked,
                                'used_':d.used_,
                                'comment_':d.comment_,
                                'id':d.id});
        data = None;
        data = session.query(data_stage02_isotopomer_atomMappingReactions).filter(data_stage02_isotopomer_atomMappingReactions.mapping_id.like('full01')).all();
        if data:
            for i,d in enumerate(data):
                data_O.append({'mapping_id':'full02',
                                'rxn_id':d.rxn_id,
                                'rxn_description':d.rxn_description,
                                'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                                'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                                'reactants_ids_tracked':d.reactants_ids_tracked,
                                'products_ids_tracked':d.products_ids_tracked,
                                'reactants_mapping':d.reactants_mapping,
                                'products_mapping':d.products_mapping,
                                'rxn_equation':d.rxn_equation,
                                'products_elements_tracked':d.products_elements_tracked,
                                'products_positions_tracked':d.products_positions_tracked,
                                'reactants_elements_tracked':d.reactants_elements_tracked,
                                'reactants_positions_tracked':d.reactants_positions_tracked,
                                'used_':d.used_,
                                'comment_':d.comment_,
                                'id':d.id});

        io2 = stage02_isotopomer_io();
        io2.add_data_stage02_isotopomer_atomMappingReactions(data_O);

    except SQLAlchemyError as e:
        print(e);
def part5():
    session = Session();
    try:
        data_O = []
        data = None;
        data = session.query(data_stage02_isotopomer_atomMappingReactions).filter(data_stage02_isotopomer_atomMappingReactions.mapping_id.like('central03')).all();
        if data:
            for i,d in enumerate(data):
                if d.reactants_ids_tracked:
                    for reactant_cnt,reactant in enumerate(d.reactants_ids_tracked):
                        print d.mapping_id,d.rxn_id,reactant
                        if len(d.reactants_elements_tracked)!=len(d.reactants_ids_tracked):
                            print 'reactants tracked do not match the elements tracked'
                            raw_input("Press enter to continue")
                        if len(d.reactants_positions_tracked)!=len(d.reactants_ids_tracked):
                            print 'reactants tracked do not match the positions tracked'
                            raw_input("Press enter to continue")
                        if len(d.reactants_stoichiometry_tracked)!=len(d.reactants_ids_tracked):
                            print 'reactants tracked do not match the stoichiometry tracked'
                            raw_input("Press enter to continue")
                        data_O.append({
                                'mapping_id':d.mapping_id,
                                #'met_name':self.met_name,
                                'met_id':reactant,
                                #'formula':self.formula,
                                'met_elements':d.reactants_elements_tracked[reactant_cnt],
                                'met_atompositions':d.reactants_positions_tracked[reactant_cnt],
                                'met_symmetry_elements':None,
                                'met_symmetry_atompositions':None,
                                'used_':True,
                                'comment_':None})
                if d.products_ids_tracked:
                    for product_cnt,product in enumerate(d.products_ids_tracked):
                        print d.mapping_id,d.rxn_id,product
                        if len(d.products_elements_tracked)!=len(d.products_ids_tracked):
                            print 'products tracked do not match the elements tracked'
                            raw_input("Press enter to continue")
                        if len(d.products_positions_tracked)!=len(d.products_ids_tracked):
                            print 'products tracked do not match the positions tracked'
                            raw_input("Press enter to continue")
                        if len(d.products_stoichiometry_tracked)!=len(d.products_ids_tracked):
                            print 'products tracked do not match the stoichiometry tracked'
                            raw_input("Press enter to continue")
                        data_O.append({
                                'mapping_id':d.mapping_id,
                                #'met_name':self.met_name,
                                'met_id':product,
                                #'formula':self.formula,
                                'met_elements':d.products_elements_tracked[product_cnt],
                                'met_atompositions':d.products_positions_tracked[product_cnt],
                                'met_symmetry_elements':None,
                                'met_symmetry_atompositions':None,
                                'used_':True,
                                'comment_':None})

        data = None;
        data = session.query(data_stage02_isotopomer_atomMappingReactions).filter(data_stage02_isotopomer_atomMappingReactions.mapping_id.like('full02')).all();
        if data:
            for i,d in enumerate(data):
                if d.reactants_ids_tracked:
                    for reactant_cnt,reactant in enumerate(d.reactants_ids_tracked):
                        print d.mapping_id,d.rxn_id,reactant
                        if len(d.reactants_elements_tracked)!=len(d.reactants_ids_tracked):
                            print 'reactants tracked do not match the elements tracked'
                            raw_input("Press enter to continue")
                        if len(d.reactants_positions_tracked)!=len(d.reactants_ids_tracked):
                            print 'reactants tracked do not match the positions tracked'
                            raw_input("Press enter to continue")
                        if len(d.reactants_stoichiometry_tracked)!=len(d.reactants_ids_tracked):
                            print 'reactants tracked do not match the stoichiometry tracked'
                            raw_input("Press enter to continue")
                        if len(d.reactants_elements_tracked[reactant_cnt])!=len(d.reactants_positions_tracked[reactant_cnt]):
                            print 'reactants elements tracked do not match the positions tracked'
                            raw_input("Press enter to continue")
                        if len(d.reactants_elements_tracked[reactant_cnt])!=len(d.reactants_mapping[reactant_cnt]):
                            print 'reactants elements tracked do not match the mappings'
                            raw_input("Press enter to continue")
                        if len(d.reactants_mapping[reactant_cnt])!=len(d.reactants_positions_tracked[reactant_cnt]):
                            print 'reactants mappings do not match the positions tracked'
                            raw_input("Press enter to continue")
                        data_O.append({
                                'mapping_id':d.mapping_id,
                                #'met_name':self.met_name,
                                'met_id':reactant,
                                #'formula':self.formula,
                                'met_elements':d.reactants_elements_tracked[reactant_cnt],
                                'met_atompositions':d.reactants_positions_tracked[reactant_cnt],
                                'met_symmetry_elements':None,
                                'met_symmetry_atompositions':None,
                                'used_':True,
                                'comment_':None})
                if d.products_ids_tracked:
                    for product_cnt,product in enumerate(d.products_ids_tracked):
                        print d.mapping_id,d.rxn_id,product
                        if len(d.products_elements_tracked)!=len(d.products_ids_tracked):
                            print 'products tracked do not match the elements tracked'
                            raw_input("Press enter to continue")
                        if len(d.products_positions_tracked)!=len(d.products_ids_tracked):
                            print 'products tracked do not match the positions tracked'
                            raw_input("Press enter to continue")
                        if len(d.products_stoichiometry_tracked)!=len(d.products_ids_tracked):
                            print 'products tracked do not match the stoichiometry tracked'
                            raw_input("Press enter to continue")
                        if len(d.products_elements_tracked[product_cnt])!=len(d.products_positions_tracked[product_cnt]):
                            print 'products elements tracked do not match the positions tracked'
                            raw_input("Press enter to continue")
                        if len(d.products_elements_tracked[product_cnt])!=len(d.products_mapping[product_cnt]):
                            print 'products elements tracked do not match the mappings'
                            raw_input("Press enter to continue")
                        if len(d.products_mapping[product_cnt])!=len(d.products_positions_tracked[product_cnt]):
                            print 'products mappings do not match the positions tracked'
                            raw_input("Press enter to continue")
                        data_O.append({
                                'mapping_id':d.mapping_id,
                                #'met_name':self.met_name,
                                'met_id':product,
                                #'formula':self.formula,
                                'met_elements':d.products_elements_tracked[product_cnt],
                                'met_atompositions':d.products_positions_tracked[product_cnt],
                                'met_symmetry_elements':None,
                                'met_symmetry_atompositions':None,
                                'used_':True,
                                'comment_':None})

        duplicate_ind = [];
        for d1_cnt,d1 in enumerate(data_O):
            for d2_cnt in range(d1_cnt+1,len(data_O)):
                if d1['mapping_id'] == data_O[d2_cnt]['mapping_id'] and \
                d1['met_id'] == data_O[d2_cnt]['met_id'] and \
                d1['met_elements'] == data_O[d2_cnt]['met_elements'] and \
                d1['met_atompositions'] == data_O[d2_cnt]['met_atompositions']:
                    duplicate_ind.append(d2_cnt);
        duplicate_ind_unique=list(set(duplicate_ind));
        data_O_O = [];
        for d1_cnt,d1 in enumerate(data_O):
            if d1_cnt in duplicate_ind_unique:
                continue;
            else:
                data_O_O.append(d1);

        met_ids = [x['met_id'] for x in data_O_O];
        met_ids_unique = list(set(met_ids));
        data_mets_cnt = {};
        for met in met_ids_unique:
            data_mets_cnt[met] = 0;
        for d in data_O_O:
            data_mets_cnt[d['met_id']] += 1;
        print 'done'

        #io2 = stage02_isotopomer_io();
        #io2.add_data_stage02_isotopomer_atomMappingMetabolites(data_O_O);

    except SQLAlchemyError as e:
        print(e);
def part6():
    session = Session();
    try:
        data_O = []
        data = None;
        data = session.query(data_stage02_isotopomer_atomMappingReactions).filter(
            or_(data_stage02_isotopomer_atomMappingReactions.mapping_id.like('central02'),
                 data_stage02_isotopomer_atomMappingReactions.mapping_id.like('central03'),
                 data_stage02_isotopomer_atomMappingReactions.mapping_id.like('full01'),
                 data_stage02_isotopomer_atomMappingReactions.mapping_id.like('full02')),
            data_stage02_isotopomer_atomMappingReactions.rxn_id.like('Ec_biomass_iJO1366_WT_53p95M%')).all();
        if data:
            for i,d in enumerate(data):
                reactants_elements_tracked = [];
                reactants_positions_tracked = [];
                reactants_mapping = []
                for r_cnt,r in enumerate(d.reactants_ids_tracked):
                    if r in ['utp_c','dctp_c','ctp_c']:
                        elements_tracked=['C','C','C','C','C','C','C','C','C'];
                        positions_tracked=[0,1,2,3,4,5,6,7,8];
                        reactant_mapping=d.reactants_mapping[r_cnt][:-1];
                    else:
                        elements_tracked=d.reactants_elements_tracked[r_cnt];
                        positions_tracked=d.reactants_positions_tracked[r_cnt];
                        reactant_mapping=d.reactants_mapping[r_cnt];
                    reactants_elements_tracked.append(elements_tracked);
                    reactants_positions_tracked.append(positions_tracked);
                    reactants_mapping.append(reactant_mapping);
                products_elements_tracked = [];
                products_positions_tracked = [];
                products_mapping = []
                for r_cnt,r in enumerate(d.products_ids_tracked):
                    if r in ['utp_c','dctp_c','ctp_c']:
                        elements_tracked=['C','C','C','C','C','C','C','C','C'];
                        positions_tracked=[0,1,2,3,4,5,6,7,8];
                        product_mapping=d.products_mapping[r_cnt][:-1];
                    else:
                        elements_tracked.append(d.products_elements_tracked[r_cnt]);
                        positions_tracked.append(d.products_positions_tracked[r_cnt]);
                        product_mapping=d.products_mapping[r_cnt];
                    products_elements_tracked.append(elements_tracked);
                    products_positions_tracked.append(positions_tracked);
                    products_mapping.append(product_mapping);
                

                data_O.append({'mapping_id':d.mapping_id,
                                'rxn_id':d.rxn_id,
                                'rxn_description':d.rxn_description,
                                'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                                'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                                'reactants_ids_tracked':d.reactants_ids_tracked,
                                'products_ids_tracked':d.products_ids_tracked,
                                'reactants_mapping':reactants_mapping,
                                'products_mapping':products_mapping,
                                'rxn_equation':d.rxn_equation,
                                'products_elements_tracked':products_elements_tracked,
                                'products_positions_tracked':products_positions_tracked,
                                'reactants_elements_tracked':reactants_elements_tracked,
                                'reactants_positions_tracked':reactants_positions_tracked,
                                'used_':d.used_,
                                'comment_':d.comment_,
                                'id':d.id});

        io2 = stage02_isotopomer_io();
        io2.update_data_stage02_isotopomer_atomMappingReactions(data_O);

    except SQLAlchemyError as e:
        print(e);
#part1();
#part2();
#part3();
#part4();
#part6();
#part5();