# ORMs
from models_base import *
from sqlalchemy.orm import relationship

# ORM classes
class data_stage02_isotopomer_experiment(Base):
    # redundant? (i.e. a view of isotopomer calcFragments and calcFluxes)
    __tablename__ = 'data_stage02_isotopomer_experiment'
    id = Column(Integer, Sequence('data_stage02_isotopomer_experiment_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self,experiment_id_I,
            model_id_I,mapping_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
            'model_id':self.model_id,
            'mapping_id':self.mapping_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_calcFragments(Base):
    __tablename__ = 'data_stage02_isotopomer_calcFragments'
    id = Column(Integer, Sequence('data_stage02_isotopomer_calcFragments_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    model_id = Column(String(50))
    mapping_id = Column(String(100), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    met_id = Column(String(100))
    fragment_name = Column(String(100), primary_key=True)
    fragment_formula = Column(String(500))
    fragment_mass = Column(Integer)
    idv_average = Column(Float);
    idv_stdev = Column(Float);
    idv_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self, experiment_id_I,
            model_id_I,mapping_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            met_id_I,
            fragment_name_I,
            fragment_formula_I,
            fragment_mass_I,
            idv_average_I,
            idv_stdev_I,
            idv_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.met_id=met_id_I
        self.fragment_name=fragment_name_I
        self.fragment_formula=fragment_formula_I
        self.fragment_mass=fragment_mass_I
        self.idv_average=idv_average_I
        self.idv_stdev=idv_stdev_I
        self.idv_units=idv_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                'mapping_id':self.mapping_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'met_id':self.met_id,
                'fragment_name':self.fragment_name,
                'fragment_formula':self.fragment_formula,
                'fragment_mass':self.fragment_mass,
                'idv_average':self.idv_average,
                'idv_stdev':self.idv_stdev,
                'idv_units':self.idv_units,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_calcFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_calcFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_calcFluxes_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    rxn_id = Column(String(100), primary_key=True)
    flux_average = Column(Float);
    flux_stdev = Column(Float);
    flux_lb = Column(Float); # based on 95% CI
    flux_ub = Column(Float);
    flux_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self,experiment_id_I,
            model_id_I,mapping_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            rxn_id_I,
            flux_average_I,
            flux_stdev_I,
            flux_lb_I,
            flux_ub_I,
            flux_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.flux_average=flux_average_I
        self.flux_stdev=flux_stdev_I
        self.flux_lb=flux_lb_I
        self.flux_ub=flux_ub_I
        self.flux_units=flux_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
            'model_id':self.model_id,
            'mapping_id':self.mapping_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
            'rxn_id':self.rxn_id,
            'flux_average':self.flux_average,
            'flux_stdev':self.flux_stdev,
            'flux_lb':self.flux_lb,
            'flux_ub':self.flux_ub,
            'flux_units':self.flux_units,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_tracers(Base):
    __tablename__ = 'data_stage02_isotopomer_tracers'
    id = Column(Integer, Sequence('data_stage02_isotopomer_tracers_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    met_id = Column(String(50), primary_key=True) # e.g glc_DASH_D_e
    met_name = Column(String(100), primary_key=True) # e.g. 1-13C Glucose
    isotopomer_formula = Column(postgresql.ARRAY(String(50))) # e.g. ['[13C]HO','CH2O','CH2O','CH2O','CH2O','CH3O']
    met_elements = Column(postgresql.ARRAY(String(3))) # the elements that are labeled (e.g. C,C,C)
    met_atompositions = Column(postgresql.ARRAY(Integer)) #the atoms positions that are labeled (e.g. 1,2,3) 
    ratio = Column(Float)
    supplier = Column(String(100))
    supplier_reference = Column(String(100))
    purity = Column(Float)
    comment_ = Column(Text);

    def __init__(self,experiment_id_I,
            met_id_I,
            met_name_I,
            isotopomer_formula_I,
            met_elements_I,
            met_atompositions_I,
            ratio_I,
            supplier_I,
            supplier_reference_I,
            purity_I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.met_id=met_id_I
        self.met_name=met_name_I
        self.isotopomer_formula=isotopomer_formula_I
        self.met_elements=met_elements_I
        self.met_atompositions=met_atompositions_I
        self.ratio=ratio_I
        self.supplier=supplier_I
        self.supplier_reference=supplier_reference_I
        self.purity=purity_I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                'met_id':self.met_id,
                'met_name':self.met_name,
                'isotopomer_formula':self.isotopomer_formula,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'ratio':self.ratio,
                'supplier':self.supplier,
                'supplier_reference':self.supplier_reference,
                'purity':self.purity,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage02_isotopomer_models(Base):
    __tablename__ = 'data_stage02_isotopomer_models'
    id = Column(Integer, Sequence('data_stage02_isotopomer_models_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    model_name = Column(String(100))
    model_description = Column(String(100))
    model_file = Column(Text)
    file_type = Column(String(50))
    date = Column(DateTime)

    def __init__(self,model_id_I,
            model_name_I,
            model_description_I,
            model_file_I,
            file_type_I,
            date_I):
        self.model_id=model_id_I
        self.model_name=model_name_I
        self.model_description=model_description_I
        self.model_file=model_file_I
        self.file_type=file_type_I
        self.date=date_I

    def __repr__dict__(self):
        return {'model_id':self.model_id,
                'model_name':self.model_name,
                'model_description':self.model_description,
                'file':self.file,
                'file_type':self.file_type,
                'date':self.date}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_modelReactions(Base):
    __tablename__ = 'data_stage02_isotopomer_modelReactions'
    id = Column(Integer, Sequence('data_stage02_isotopomer_modelReactions_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    rxn_id = Column(String(50), primary_key=True)
    rxn_name = Column(String(100))
    equation = Column(String(4000));
    subsystem = Column(String(255));
    gpr = Column(Text);
    genes = Column(postgresql.ARRAY(String(50)));
    reactants_stoichiometry = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites
    products_stoichiometry = Column(postgresql.ARRAY(Float)) 
    reactants_ids = Column(postgresql.ARRAY(String(50))) # list of met_ids that are in the reaction
    products_ids = Column(postgresql.ARRAY(String(50))) 
    lower_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    upper_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    objective_coefficient = Column(Float)
    flux_units = Column(String(50))
    fixed = Column(Boolean)
    free = Column(Boolean)
    reversibility = Column(Boolean)
    weight = Column(Float) #weighting given in the optimization problem
    used_ = Column(Boolean)
    comment_ = Column(Text);

    def __init__(self,model_id_I,
            rxn_id_I,
            equation_I,
            subsystem_I,
            gpr_I,
            genes_I,
            reactants_stoichiometry_I,
            products_stoichiometry_I,
            reactants_ids_I,
            products_ids_I,
            lower_bound_I,
            upper_bound_I,
            objective_coefficient_I,
            flux_units_I,
            fixed_I,
            free_I,
            reversibility_I,
            weight_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.rxn_id=rxn_id_I
        self.equation=equation_I
        self.subsystem=subsystem_I
        self.gpr=gpr_I
        self.genes=genes_I
        self.reactants_stoichiometry=reactants_stoichiometry_I
        self.products_stoichiometry=products_stoichiometry_I
        self.reactants_ids=reactants_ids_I
        self.products_ids=products_ids_I
        self.lower_bound=lower_bound_I
        self.upper_bound=upper_bound_I
        self.objective_coefficient=objective_coefficient_I
        self.flux_units=flux_units_I
        self.fixed=fixed_I
        self.free=free_I
        self.reversibility=reversibility_I
        self.weight=weight_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'model_id':self.model_id,
            'rxn_id':self.rxn_id,
            'equation':self.equation,
            'subsystem':self.subsystem,
            'gpr':self.gpr,
            'genes':self.genes,
            'reactants_stoichiometry':self.reactants_stoichiometry,
            'products_stoichiometry':self.products_stoichiometry,
            'reactants_ids':self.reactants_ids,
            'products_ids':self.products_ids,
            'lower_bound':self.lower_bound,
            'upper_bound':self.upper_bound,
            'objective_coefficient':self.objective_coefficient,
            'flux_units':self.flux_units,
            'fixed':self.fixed,
            'free':self.free,
            'reversibility':self.reversibility,
            'weight':self.weight,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage02_isotopomer_modelMetabolites(Base):
    __tablename__ = 'data_stage02_isotopomer_modelMetabolites'
    id = Column(Integer, Sequence('data_stage02_isotopomer_modelMetabolites_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    met_name = Column(String(500))
    met_id = Column(String(50), primary_key=True)
    formula = Column(String(100))
    charge = Column(Integer)
    compartment = Column(String(50))
    bound = Column(Float)
    constraint_sense = Column(String(5))
    used_ = Column(Boolean)
    comment_ = Column(Text);
    lower_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    upper_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    balanced = Column(Boolean)
    fixed = Column(Boolean)

    def __init__(self,model_id_I,
            met_name_I,
            met_id_I,
            formula_I,
            charge_I,
            compartment_I,
            bound_I,
            constraint_sense_I,
            lower_bound_I,
            upper_bound_I,
            balanced_I,
            fixed_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.met_name=met_name_I
        self.met_id=met_id_I
        self.formula=formula_I
        self.charge=charge_I
        self.compartment=compartment_I
        self.bound=bound_I
        self.constraint_sense=constraint_sense_I
        self.lower_bound=lower_bound_I
        self.upper_bound=upper_bound_I
        self.balanced=balanced_I
        self.fixed=fixed_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'model_id':self.model_id,
                'met_name':self.met_name,
                'met_id':self.met_id,
                'formula':self.formula,
                'charge':self.charge,
                'bound':self.bound,
                'constraint_sense':self.constraint_sense,
                'compartment':self.compartment,
                'lower_bound':self.lower_bound,
                'upper_bound':self.upper_bound,
                'balanced':self.balanced,
                'fixed':self.fixed,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_experimentalFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_experimentalFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_experimentalFluxes_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    rxn_id = Column(String(100))
    flux_average = Column(Float);
    flux_stdev = Column(Float);
    flux_lb = Column(Float); # based on 95% CI
    flux_ub = Column(Float);
    flux_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self,experiment_id_I,
            model_id_I,
            sample_name_abbreviation_I,
            #time_point_I,
            rxn_id_I,
            flux_average_I,
            flux_stdev_I,
            flux_lb_I,
            flux_ub_I,
            flux_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.flux_average=flux_average_I
        self.flux_stdev=flux_stdev_I
        self.flux_lb=flux_lb_I
        self.flux_ub=flux_ub_I
        self.flux_units=flux_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                    'model_id':self.model_id,
                    'sample_name_abbreviation':self.sample_name_abbreviation,
                    #'time_point':self.time_point,
                    'rxn_id':self.rxn_id,
                    'flux_average':self.flux_average,
                    'flux_stdev':self.flux_stdev,
                    'flux_lb':self.flux_lb,
                    'flux_ub':self.flux_ub,
                    'flux_units':self.flux_units,
                    'used_':self.used_,
                    'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage02_isotopomer_experimentalPools(Base):
    __tablename__ = 'data_stage02_isotopomer_experimentalPools'
    id = Column(Integer, Sequence('data_stage02_isotopomer_experimentalPools_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    met_id = Column(String(50))
    # Time-course simulations only:
    pool_size = Column(Float) # 0 if steady-state
    concentration_average = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_var = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_lb = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_ub = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_units = Column(String(50))
    used_ = Column(Boolean)
    comment_ = Column(Text);

    def __init__(self,experiment_id_I,
            model_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            met_id_I,
            pool_size_I,
            concentration_average_I,
            concentration_var_I,
            concentration_lb_I,
            concentration_ub_I,
            concentration_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.met_id=met_id_I
        self.pool_size=pool_size_I
        self.concentration_average=concentration_average_I
        self.concentration_var=concentration_var_I
        self.concentration_lb=concentration_lb_I
        self.concentration_ub=concentration_ub_I
        self.concentration_units=concentration_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                    'model_id':self.model_id,
                    'sample_name_abbreviation':self.sample_name_abbreviation,
                    'time_point':self.time_point,
                    'met_id':self.met_id,
                    'pool_size':self.pool_size,
                    'concentration_average':self.concentration_average,
                    'concentration_var':self.concentration_var,
                    'concentration_lb':self.concentration_lb,
                    'concentration_ub':self.concentration_ub,
                    'concentration_units':self.concentration_units,
                    'used_':self.used_,
                    'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_experimentalFragments(Base):
    __tablename__ = 'data_stage02_isotopomer_experimentalFragments'
    id = Column(Integer, Sequence('data_stage02_isotopomer_experimentalFragments_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    met_id = Column(String(100), primary_key=True)
    fragment_id = Column(String(100), primary_key=True)
    fragment_formula = Column(String(500), primary_key=True)
    #fragment_mass = Column(Integer, primary_key=True)
    #n_replicates = Column(Integer)
    intensity_normalized_average = Column(postgresql.ARRAY(Float))
    intensity_normalized_cv = Column(postgresql.ARRAY(Float))
    intensity_normalized_stdev = Column(postgresql.ARRAY(Float))
    intensity_normalized_units = Column(String(20))
    scan_type = Column(String(50), primary_key=True);
    met_elements = Column(postgresql.ARRAY(String(3))) # the elements that are tracked (e.g. C,C,C)
    met_atompositions = Column(postgresql.ARRAY(Integer)) #the atoms positions that are tracked (e.g. 1,2,3) 
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self, experiment_id_I, sample_name_abbreviation_I, 
                 time_point_I, met_id_I,fragment_id_I,
                    fragment_formula_I,
                    #fragment_mass_I,
                    #n_replicates_I,
                    intensity_normalized_average_I, intensity_normalized_cv_I,
                    intensity_normalized_stdev_I,
                    intensity_normalized_units_I, scan_type_I,
                    met_elements_I,
                    met_atompositions_I,used__I,comment__I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.met_id = met_id_I;
        self.fragment_id = fragment_id_I;
        self.fragment_formula = fragment_formula_I;
        #self.fragment_mass = fragment_mass_I;
        #self.n_replicates = n_replicates_I;
        self.intensity_normalized_average = intensity_normalized_average_I;
        self.intensity_normalized_cv = intensity_normalized_cv_I;
        self.intensity_normalized_stdev = intensity_normalized_stdev_I;
        self.intensity_normalized_units = intensity_normalized_units_I;
        self.scan_type = scan_type_I;
        self.met_elements=met_elements_I;
        self.met_atompositions=met_atompositions_I;
        self.used_=used__I;
        self.comment_=comment__I;

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'met_id':self.met_id,
                'fragment_id':self.fragment_id,
                'fragment_formula':self.fragment_formula,
                'intensity_normalized_average':self.intensity_normalized_average,
                'intensity_normalized_cv':self.intensity_normalized_cv,
                'intensity_normalized_stdev':self.intensity_normalized_stdev,
                'intensity_normalized_units':self.intensity_normalized_units,
                'scan_type':self.scan_type,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_atomMappingReactions(Base):
    __tablename__ = 'data_stage02_isotopomer_atomMappingReactions'
    id = Column(Integer, Sequence('data_stage02_isotopomer_atomMappingReactions_id_seq'), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    rxn_id = Column(String(50), primary_key=True)
    rxn_description = Column(String(500))
    reactants_stoichiometry_tracked = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites (e.g. ['-1','-1'])
    products_stoichiometry_tracked = Column(postgresql.ARRAY(Float))  
    reactants_ids_tracked = Column(postgresql.ARRAY(String(50))) # list of met_ids that are tracked (e.g. ['pyr_c','accoa_c'])
    products_ids_tracked = Column(postgresql.ARRAY(String(50)))
    reactants_elements_tracked = Column(postgresql.JSON) # list of elements that are tracked (e.g. ['C','C'])
    products_elements_tracked = Column(postgresql.JSON)
    reactants_positions_tracked = Column(postgresql.JSON) # list of elements that are tracked (e.g. ['C','C'])
    products_positions_tracked = Column(postgresql.JSON)
    reactants_mapping = Column(postgresql.ARRAY(String(5000))) # mappings of each atom for each met_id that are tracked (e.g. ['abc','de'])
    products_mapping = Column(postgresql.ARRAY(String(5000)))
    rxn_equation = Column(String(4000)) #formatted version of rxn_formula and rxn_mapping depending on the fluxomics software
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self,
            #id_I,
            mapping_id_I,
            rxn_id_I,
            rxn_description_I,
            reactants_stoichiometry_tracked_I,
            products_stoichiometry_tracked_I,
            reactants_ids_tracked_I,
            products_ids_tracked_I,
            reactants_elements_tracked_I,
            products_elements_tracked_I,
            reactants_positions_tracked_I,
            products_positions_tracked_I,
            reactants_mapping_I,
            products_mapping_I,
            rxn_equation_I,
            used__I,
            comment__I):
        #self.id=id_I
        self.mapping_id=mapping_id_I
        self.rxn_id=rxn_id_I
        self.rxn_description=rxn_description_I
        self.reactants_stoichiometry_tracked=reactants_stoichiometry_tracked_I
        self.products_stoichiometry_tracked=products_stoichiometry_tracked_I
        self.reactants_ids_tracked=reactants_ids_tracked_I
        self.products_ids_tracked=products_ids_tracked_I
        self.reactants_elements_tracked=reactants_elements_tracked_I
        self.products_elements_tracked=products_elements_tracked_I
        self.reactants_positions_tracked=reactants_positions_tracked_I
        self.products_positions_tracked=products_positions_tracked_I
        self.reactants_mapping=reactants_mapping_I
        self.products_mapping=products_mapping_I
        self.rxn_equation=rxn_equation_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'mapping_id':self.mapping_id,
                'rxn_id':self.rxn_id,
                'rxn_description':self.rxn_description,
                'reactants_stoichiometry_tracked':self.reactants_stoichiometry_tracked,
                'products_stoichiometry_tracked':self.products_stoichiometry_tracked,
                'reactants_ids_tracked':self.reactants_ids_tracked,
                'products_ids_tracked':self.products_ids_tracked,
                'reactants_elements_tracked':self.reactants_elements_tracked,
                'products_elements_tracked':self.products_elements_tracked,
                'reactants_positions_tracked':self.reactants_positions_tracked,
                'products_positions_tracked':self.products_positions_tracked,
                'reactants_mapping':self.reactants_mapping,
                'products_mapping':self.products_mapping,
                'rxn_equation':self.rxn_equation,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__());

class data_stage02_isotopomer_modelReactionsAtomMapping(Base):
    __tablename__ = 'data_stage02_isotopomer_modelReactionsAtomMapping'
    id = Column(Integer, Sequence('data_stage02_isotopomer_modelReactionsAtomMapping_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    rxn_id = Column(String(50), primary_key=True)
    rxn_name = Column(String(100))
    equation = Column(String(4000));
    subsystem = Column(String(255));
    gpr = Column(Text);
    genes = Column(postgresql.ARRAY(String(50)));
    reactants_stoichiometry = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites
    products_stoichiometry = Column(postgresql.ARRAY(Float)) 
    reactants_ids = Column(postgresql.ARRAY(String(50))) # list of met_ids that are in the reaction
    products_ids = Column(postgresql.ARRAY(String(50))) 
    reactants_stoichiometry_tracked = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites
    products_stoichiometry_tracked = Column(postgresql.ARRAY(Float))  
    reactants_ids_tracked = Column(postgresql.ARRAY(String(50))) # list of met_ids that are tracked
    products_ids_tracked = Column(postgresql.ARRAY(String(50)))
    reactants_elements_tracked = Column(postgresql.ARRAY(String(3))) # list of elements that are tracked (e.g. ['C','C'])
    products_elements_tracked = Column(postgresql.ARRAY(String(3)))
    reactants_mapping = Column(postgresql.ARRAY(String(50))) # mappings of each atom for each met_id that are tracked
    products_mapping = Column(postgresql.ARRAY(String(50)))
    rxn_equation = Column(String(1000)) #formatted version of rxn_formula and rxn_mapping depending on the fluxomics software
    lower_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    upper_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    objective_coefficient = Column(Float)
    flux_units = Column(String(50))
    fixed = Column(Boolean)
    free = Column(Boolean)
    reversibility = Column(Boolean)
    weight = Column(Float) #weighting given in the optimization problem
    used_ = Column(Boolean)
    comment_ = Column(Text);

    def __init__(self,model_id_I,
            mapping_id_I,
            rxn_id_I,
            equation_I,
            subsystem_I,
            gpr_I,
            genes_I,
            reactants_stoichiometry_I,
            products_stoichiometry_I,
            reactants_ids_I,
            products_ids_I,
            reactants_stoichiometry_tracked_I,
            products_stoichiometry_tracked_I,
            reactants_ids_tracked_I,
            products_ids_tracked_I,
            reactants_elements_tracked_I,
            products_elements_tracked_I,
            reactants_mapping_I,
            products_mapping_I,
            rxn_equation_I,
            lower_bound_I,
            upper_bound_I,
            objective_coefficient_I,
            flux_units_I,
            fixed_I,
            free_I,
            reversibility_I,
            weight_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.mapping_id=mapping_id_I
        self.rxn_id=rxn_id_I
        self.equation=equation_I
        self.subsystem=subsystem_I
        self.gpr=gpr_I
        self.genes=genes_I
        self.reactants_stoichiometry=reactants_stoichiometry_I
        self.products_stoichiometry=products_stoichiometry_I
        self.reactants_ids=reactants_ids_I
        self.products_ids=products_ids_I
        self.reactants_stoichiometry_tracked=reactants_stoichiometry_tracked_I
        self.products_stoichiometry_tracked=products_stoichiometry_tracked_I
        self.reactants_ids_tracked=reactants_ids_tracked_I
        self.products_ids_tracked=products_ids_tracked_I
        self.reactants_elements_tracked=reactants_elements_tracked_I
        self.products_elements_tracked=products_elements_tracked_I
        self.reactants_mapping=reactants_mapping_I
        self.products_mapping=products_mapping_I
        self.rxn_equation=rxn_equation_I
        self.lower_bound=lower_bound_I
        self.upper_bound=upper_bound_I
        self.objective_coefficient=objective_coefficient_I
        self.flux_units=flux_units_I
        self.fixed=fixed_I
        self.free=free_I
        self.reversibility=reversibility_I
        self.weight=weight_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'model_id':self.model_id,
            'rxn_id':self.rxn_id,
            'equation':self.equation,
            'subsystem':self.subsystem,
            'gpr':self.gpr,
            'genes':self.genes,
            'reactants_stoichiometry':self.reactants_stoichiometry,
            'products_stoichiometry':self.products_stoichiometry,
            'reactants_ids':self.reactants_ids,
            'products_ids':self.products_ids,
            'reactants_stoichiometry_tracked':self.reactants_stoichiometry_tracked,
            'products_stoichiometry_tracked':self.products_stoichiometry_tracked,
            'reactants_ids_tracked':self.reactants_ids_tracked,
            'products_ids_tracked':self.products_ids_tracked,
            'reactants_elements_tracked':self.reactants_elements_tracked,
            'products_elements_tracked':self.products_elements_tracked,
            'reactants_mapping':self.reactants_mapping,
            'products_mapping':self.products_mapping,
            'rxn_equation':self.rxn_equation,
            'lower_bound':self.lower_bound,
            'upper_bound':self.upper_bound,
            'objective_coefficient':self.objective_coefficient,
            'flux_units':self.flux_units,
            'fixed':self.fixed,
            'free':self.free,
            'reversibility':self.reversibility,
            'weight':self.weight,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_modelMetabolitesAtomMapping(Base):
    __tablename__ = 'data_stage02_isotopomer_modelMetabolitesAtomMapping'
    id = Column(Integer, Sequence('data_stage02_isotopomer_modelMetabolitesAtomMapping_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    met_name = Column(String(500))
    met_id = Column(String(50), primary_key=True)
    formula = Column(String(100))
    charge = Column(Integer)
    compartment = Column(String(50))
    bound = Column(Float)
    constraint_sense = Column(String(5))
    lower_bound = Column(Float)
    upper_bound = Column(Float)
    met_elements = Column(postgresql.JSON) # the elements that are tracked (e.g. C,C,C)
    met_atompositions = Column(postgresql.JSON) #the atoms positions that are tracked (e.g. 1,2,3) 
    balanced = Column(Boolean)
    met_symmetry_elements = Column(postgresql.JSON) #symmetric molecules can alternatively be indicated in the reaction mapping
    met_symmetry_atompositions = Column(postgresql.JSON) #maps the symmetric atom positions
    used_ = Column(Boolean)
    comment_ = Column(Text);

    def __init__(self,model_id_I,
            mapping_id_I,
            met_name_I,
            met_id_I,
            formula_I,
            charge_I,
            compartment_I,
            bound_I,
            constraint_sense_I,
            met_elements_I,
            met_atompositions_I,
            balanced_I,
            met_symmetry_elements_I,
            met_symmetry_atompositions_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.mapping_id=mapping_id_I
        self.met_name=met_name_I
        self.met_id=met_id_I
        self.formula=formula_I
        self.charge=charge_I
        self.bound=bound_I
        self.constraint_sense=constraint_sense_I
        self.met_elements=met_elements_I
        self.met_atompositions=met_atompositions_I
        self.compartment=compartment_I
        self.balanced=balanced_I
        self.met_symmetry_elements=met_symmetry_elements_I
        self.met_symmetry_atompositions=met_symmetry_atompositions_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'model_id':self.model_id,
                'met_name':self.met_name,
                'met_id':self.met_id,
                'formula':self.formula,
                'charge':self.charge,
                'compartment':self.compartment,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'balanced':self.balanced,
                'met_symmetry_elements':self.met_symmetry_elements,
                'met_symmetry_atompositions':self.met_symmetry_atompositions,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_atomMappingMetabolites(Base):
    __tablename__ = 'data_stage02_isotopomer_atomMappingMetabolites'
    id = Column(Integer, Sequence('data_stage02_isotopomer_atomMappingMetabolites_id_seq'), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    #met_name = Column(String(500))
    met_id = Column(String(50), primary_key=True)
    #formula = Column(String(100))
    met_elements = Column(postgresql.ARRAY(String(3))) # the elements that are tracked (e.g. C,C,C)
    met_atompositions = Column(postgresql.ARRAY(Integer)) #the atoms positions that are tracked (e.g. 1,2,3) 
    met_symmetry_elements = Column(postgresql.ARRAY(String(3))) #symmetric molecules can alternatively be indicated in the reaction mapping
    met_symmetry_atompositions = Column(postgresql.ARRAY(Integer)) #maps the symmetric atom positions
    used_ = Column(Boolean)
    comment_ = Column(Text);
    met_mapping=Column(postgresql.JSON())
    #met_mapping=Column(postgresql.ARRAY(String(5000)))
    base_met_ids=Column(postgresql.ARRAY(String(50)))
    base_met_elements=Column(postgresql.JSON())
    #base_met_elements=Column(postgresql.ARRAY(String(3)))
    base_met_atompositions=Column(postgresql.JSON())
    #base_met_atompositions=Column(postgresql.ARRAY(Integer))
    base_met_symmetry_elements=Column(postgresql.JSON())
    #base_met_symmetry_elements=Column(postgresql.ARRAY(String(3)))
    base_met_symmetry_atompositions=Column(postgresql.JSON())
    #base_met_symmetry_atompositions=Column(postgresql.ARRAY(Integer))
    base_met_indices=Column(postgresql.ARRAY(Integer))

    def __init__(self,
            mapping_id_I,
            #met_name_I,
            met_id_I,
            #formula_I,
            met_elements_I,
            met_atompositions_I,
            met_symmetry_elements_I,
            met_symmetry_atompositions_I,
            used__I,
            comment__I,
            met_mapping_I=None,
            base_met_ids_I=None,
            base_met_elements_I=None,
            base_met_atompositions_I=None,
            base_met_symmetry_elements_I=None,
            base_met_symmetry_atompositions_I=None,
            base_met_indices_I=None):
        self.mapping_id=mapping_id_I
        #self.met_name=met_name_I
        self.met_id=met_id_I
        #self.formula=formula_I
        self.met_elements=met_elements_I
        self.met_atompositions=met_atompositions_I
        self.met_symmetry_elements=met_symmetry_elements_I
        self.met_symmetry_atompositions=met_symmetry_atompositions_I
        self.used_=used__I
        self.comment_=comment__I
        self.met_mapping=met_mapping_I;
        self.base_met_ids=base_met_ids_I;
        self.base_met_elements=base_met_elements_I;
        self.base_met_atompositions=base_met_atompositions_I;
        self.base_met_symmetry_elements=base_met_symmetry_elements_I;
        self.base_met_symmetry_atompositions=base_met_symmetry_atompositions_I;
        self.base_met_indices = base_met_indices_I;

    def __repr__dict__(self):
        return {'mapping_id':self.mapping_id,
                #'met_name':self.met_name,
                'met_id':self.met_id,
                #'formula':self.formula,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'met_symmetry_elements':self.met_symmetry_elements,
                'met_symmetry_atompositions':self.met_symmetry_atompositions,
                'used_':self.used_,
                'comment_':self.comment_,
                'met_mapping':self.met_mapping,
                'base_met_ids':self.base_met_ids,
                'base_met_elements':self.base_met_elements,
                'base_met_atompositions':self.base_met_atompositions,
                'base_met_symmetry_elements':self.base_met_symmetry_elements,
                'base_met_symmetry_atompositions':self.base_met_symmetry_atompositions,
                'base_met_indices':self.base_met_indices}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())