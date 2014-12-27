'''isotopomer distribution analysis class'''

from math import log, sqrt
import csv

from models import *
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
session = Session();

from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

from analysis import analysis

class analysis_isotopomer(analysis):
    '''Class for isotopomer analysis'''

    # ORM classes
    class analysis_isotopomer(Base):
        __tablename__ = 'analysis_isotopomer'
        id = Column(Integer, Sequence('analysis_isotopomer_id_seq'), primary_key=True)
        sample_name = Column(String(100))
        component_group_name = Column(String(100))
        component_name = Column(String(500))
        height = Column(Float)
        intensity = Column(Float)

        def __init__(self,sample_name_I, component_group_name_I, component_name_I, 
                                        height_I, intensity_I):
            self.sample_name = sample_name_I;
            self.component_group_name = component_group_name_I;
            self.component_name = component_name_I;
            self.height = height_I;
            self.intensity = intensity_I;
    class analysis_isotopomerReplicates_analytical(Base):
        __tablename__ = 'analysis_isotopomerReplicates_analytical'
        id = Column(Integer, Sequence('analysis_isotopomerReplicates_analytical_id_seq'), primary_key=True)
        sample_id = Column(String(100))
        component_group_name = Column(String(100))
        component_name = Column(String(500))
        n_replicates = Column(Integer)
        height_average = Column(Float)
        height_CV = Column(Float)
        intensity_average = Column(Float)
        intensity_CV = Column(Float)

        def __init__(self,sample_id_I, component_group_name_I, component_name_I, n_replicates_I,
                     height_average_I, height_CV_I, intensity_average_I, intensity_CV_I):
            self.sample_id = sample_id_I;
            self.component_group_name = component_group_name_I;
            self.component_name = component_name_I;
            self.n_replicates = n_replicates_I;
            self.height_average = height_average_I;
            self.height_CV = height_CV_I;
            self.intensity_average = intensity_average_I;
            self.intensity_CV = intensity_CV_I;
    class analysis_isotopomerReplicates_biological(Base):
        __tablename__ = 'analysis_isotopomerReplicates_biological'
        id = Column(Integer, Sequence('analysis_isotopomerReplicates_biological_id_seq'), primary_key=True)
        sample_id = Column(String(100))
        component_group_name = Column(String(100))
        component_name = Column(String(500))
        n_replicates = Column(Integer)
        height_average = Column(Float)
        height_CV = Column(Float)
        intensity_average = Column(Float)
        intensity_CV = Column(Float)

        def __init__(self,sample_id_I, component_group_name_I, component_name_I, n_replicates_I,
                     height_average_I, height_CV_I, intensity_average_I, intensity_CV_I):
            self.sample_id = sample_id_I;
            self.component_group_name = component_group_name_I;
            self.component_name = component_name_I;
            self.n_replicates = n_replicates_I;
            self.height_average = height_average_I;
            self.height_CV = height_CV_I;
            self.intensity_average = intensity_average_I;
            self.intensity_CV = intensity_CV_I;

    # table initializations
    def createTable_isotopomerAnalysis(self):
        try:
            self.analysis_isotopomer.__table__.drop(engine,True);
            self.analysis_isotopomer.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def createTable_isotopomerReplicates_analytical(self):
        try:
            self.analysis_isotopomerReplicates_analytical.__table__.drop(engine,True);
            self.analysis_isotopomerReplicates_analytical.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def createTable_isotopomerReplicates_biological(self):
        try:
            self.analysis_isotopomerReplicates_biological.__table__.drop(engine,True);
            self.analysis_isotopomerReplicates_biological.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);

    # table updates
    def update_isotopomerAnalysis(self, sample_name_I, component_group_name_I, component_name_I, 
                                  height_I, intensity_I):
        '''Update the analysis_isotopomer table'''
        # Input: sample_name_I, component_group_name_I, component_name_I, 
        #                          height_I, intensity_I
        # Output: row to database
        try:
            row = self.analysis_isotopomer(sample_name_I, component_group_name_I, component_name_I, 
                                  height_I, intensity_I);
            self.session.add(row);
             # commit changes to the database     
            self.session.commit()
        except SQLAlchemyError as e:
            print(e);
    def update_isotopomerReplicates_analytical(self,sample_id_I, component_group_name_I, component_name_I, 
                     n_replicates_I, height_average_I, height_CV_I, intensity_average_I, intensity_CV_I):
        '''Update the analysis_isotopomer table'''
        # Input: self,sample_id_I, component_group_name_I, component_name_I, 
        #            height_average_I, height_CV_I, intensity_average_I, intensity_CV_I
        # Output: row to database
        try:
            row = self.analysis_isotopomerReplicates_analytical(sample_id_I, component_group_name_I, component_name_I, 
                     n_replicates_I, height_average_I, height_CV_I, intensity_average_I, intensity_CV_I);
            self.session.add(row);
             # commit changes to the database     
            self.session.commit()
        except SQLAlchemyError as e:
            print(e);
    def update_isotopomerReplicates_biological(self,sample_name_abbreviation_I, component_group_name_I, component_name_I, 
                     n_replicates_I, height_average_I, height_CV_I, intensity_average_I, intensity_CV_I):
        '''Update the analysis_isotopomer table'''
        # Input: self, sample_name_abbreviation_I, component_group_name_I, component_name_I, 
        #            height_average_I, height_CV_I, intensity_average_I, intensity_CV_I
        # Output: row to database
        try:
            row = self.analysis_isotopomerReplicates_biological(sample_name_abbreviation_I, component_group_name_I, component_name_I, 
                     n_replicates_I, height_average_I, height_CV_I, intensity_average_I, intensity_CV_I);
            self.session.add(row);
             # commit changes to the database     
            self.session.commit()
        except SQLAlchemyError as e:
            print(e);

    # Analyses:
    #   1: isotopomer analysis
    #   2: analyzeReplicates (analytical and/or biological)
    def execute_isotopomerAnalysis(self,experiment_id_I):
        # Input:
        #   experiment_id
        # Output:
        #   sample_name
        #   component_group_name
        #   component_name
        #   height
        #   height_normalized

        # get sample names
        sample_names = [];
        sample_types = ['Unknown','Quality Control'];
        for st in sample_types:
            sample_names_tmp = [];
            sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
            sample_names.extend(sample_names_tmp);
        # create database table
        self.createTable_isotopomerAnalysis();
        for sn in sample_names:
            # get component group names
            component_group_names = [];
            component_group_names = self.get_componentGroupNames_sampleName(sn);
            for cgn in component_group_names:
                # get component names, heights
                component_names = [];
                heights = [];
                component_names, heights = self.get_data_heights(sn,cgn);
                # normalize component_heights
                heights_normalized = [];
                heights_normalized = self.calculate_normalizedHeight(heights);
                for i in range(len(component_names)):
                    # add data to the session
                    self.update_isotopomerAnalysis(sn,cgn,component_names[i],heights[i],heights_normalized[i]);
    def execute_analyzeReplicates_analytical(self,experiment_id_I):
        '''calculate the average and coefficient of variation for analytical
        replicates
        NOTE: analytical replicates are those samples with the same 
        sample_id (but different sample_name)
        NOTE: analysis_isotopomer table must be populated'''
        # Input:
        #   experiment_id
        # Output:
        #   sample_name
        #   component_group_name
        #   component_name
        #   n_replicates
        #   height_average
        #   height_CV
        #   height_normalized_average
        #   height_normalized_CV

        # get sample names
        sample_ids = [];
        sample_types = ['Unknown','QC'];
        for st in sample_types:
            sample_ids_tmp = [];
            sample_ids_tmp = self.get_sampleIDs_experimentIDAndSampleType(experiment_id_I,st);
            sample_ids.extend(sample_ids_tmp);
        # create database table
        self.createTable_isotopomerReplicates_analytical();
        for si in sample_ids:
            # get sample names
            sample_names = [];
            sample_names = self.get_sampleNames_experimentIDAndSampleID(experiment_id_I,si);
            # get component names
            component_names = [];
            component_names = self.get_componentsNames_experimentIDAndSampleID(experiment_id_I,si);
            for cn in component_names:
                heights = [];
                intensities = [];
                for sn in sample_names:
                    # get heights, intensities
                    height, intensity = self.get_dataFromIsotopomerAnalysis(sn,cn);
                    if not(height and intensity): continue
                    component_group_name = self.get_componentGroupFromIsotopomerAnalysis(cn);
                    heights.append(height);
                    intensities.append(intensity);
                n_replicates = len(heights);
                # calculate average and CV of heights and intensities
                if not(heights and intensity): continue
                heights_average, heights_CV = self.calculate_ave_CV_R(heights);
                intensities_average, intensities_CV = self.calculate_ave_CV_R(intensities);

                # add data to the session
                self.update_isotopomerReplicates_analytical(si,component_group_name,cn,n_replicates, heights_average,
                                                           heights_CV,intensities_average,intensities_CV);                
    def execute_analyzeReplicates_biological(self,experiment_id_I):
        '''calculate the average and coefficient of variation for biological
        replicates
        NOTE: analytical replicates are those samples with the same 
        sample_id (but different sample_name)
        NOTE: analysis_isotopomer table must be populated'''
        # Input:
        #   experiment_id
        # Output:
        #   sample_name
        #   component_group_name
        #   component_name
        #   n_replicates
        #   height_average
        #   height_CV
        #   height_normalized_average
        #   height_normalized_CV

        # get sample_name_abbreviations
        sample_name_abbreviations = [];
        sample_types = ['Unknown'];
        for st in sample_types:
            sample_name_abbreviations_tmp = [];
            sample_name_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleType(experiment_id_I,st);
            sample_name_abbreviations.extend(sample_name_abbreviations_tmp);
        # create database table
        self.createTable_isotopomerReplicates_biological();
        for sna in sample_name_abbreviations:
            # get broth sample names
            sample_names = [];
            sample_description = 'Broth';
            sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescription(experiment_id_I,sna,sample_description);
            # get component data
            component_names = [];
            component_names = self.get_componentsNames_experimentIDAndSampleNameAbbreviation(experiment_id_I,sna);
            for cn in component_names:
                heights = [];
                intensities = [];
                for sn in sample_names:
                    # get heights, intensities
                    height, intensity = self.get_dataFromIsotopomerAnalysis(sn,cn);
                    if not(height and intensity): continue
                    component_group_name = self.get_componentGroupFromIsotopomerAnalysis(cn);
                    heights.append(height);
                    intensities.append(intensity);
                n_replicates = len(heights);
                # calculate average and CV of heights and intensities
                if not(heights and intensity): continue
                heights_average, heights_CV = self.calculate_ave_CV_R(heights);
                intensities_average, intensities_CV = self.calculate_ave_CV_R(intensities);

                # add data to the session
                self.update_isotopomerReplicates_biological(sna,component_group_name,cn,n_replicates, heights_average,
                                                           heights_CV,intensities_average,intensities_CV);
    # optional execution straight to csv (deprecated)
    def execute_isotopomerAnalysis_csv(self,experiment_id_I):
        # Input:
        #   experiment_id
        # Output:
        #   sample_name
        #   component_group_name
        #   component_name
        #   height
        #   height_normalized

        # get sample names
        sample_names = [];
        sample_types = ['Unknown','Quality Control'];
        for st in sample_types:
            sample_names_tmp = [];
            sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
            sample_names.extend(sample_names_tmp);
        with open('isotopomerAnalysis.csv', 'wb') as csvfile: #change to database!
            # write header to file
            csv_writer = csv.writer(csvfile)
            columns = [];
            column_names = ['Sample_name','component_group','component_name','height','heights_normalized'];
            for c in column_names:
                columns.append(c);
            csv_writer.writerow(columns);
            for sn in sample_names:
                # get component group names
                component_group_names = [];
                component_group_names = self.get_componentGroupNames_sampleName(sn);
                for cgn in component_group_names:
                    # get component names, heights
                    component_names = [];
                    heights = [];
                    component_names, heights = self.get_data_heights(sn,cgn);
                    # normalize component_heights
                    heights_normalized = [];
                    heights_normalized = self.calculate_normalizedHeight(heights);
                    # TODO: make method
                    for i in range(len(component_names)):
                        # copy data to self.data
                        # write data to file 
                        row = [];
                        row.append(sn);
                        row.append(cgn);
                        row.append(component_names[i]);
                        row.append(heights[i]);
                        row.append(heights_normalized[i]);
                        csv_writer.writerow(row);

    # isotopomer analysis:
    def get_data_heights(self,sample_name_I,component_group_name_I):
        '''Querry component names and data (i.e. height) that are used from
        the experiment
        NOTE: intended to be used within a for loop'''
        try:
            components = session.query(data_stage01_MQResultsTable.component_name,
                    data_stage01_MQResultsTable.height).filter(
                    data_stage01_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_MQResultsTable.component_group_name.like(component_group_name_I),
                    data_stage01_MQResultsTable.used_.is_(True)).order_by(
                    data_stage01_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            heights_O = [];
            for cn in components: 
                if cn.component_name:
                    component_names_O.append(cn.component_name);
                if cn.height:
                    heights_O.append(cn.height);
                else: 
                    heights_O.append(0.0);
            return component_names_O, heights_O;
        except SQLAlchemyError as e:
            print(e);
    def calculate_normalizedHeight(self,heights_I):
        '''normalize heights to the max height in the isotope
        distribution'''
        if heights_I:
            heights_normalized_O = [];
            maxHeight = max(heights_I);
            for h in heights_I:
                heights_normalized_O.append(h/maxHeight*100);
            return heights_normalized_O;

    # analyze replicates (all):
    def get_dataFromIsotopomerAnalysis(self, sample_name_I, component_name_I):
        try:
            data_analysis_isotopomer = session.query(self.analysis_isotopomer.height, self.analysis_isotopomer.intensity).filter(
                    self.analysis_isotopomer.sample_name.like(sample_name_I),
                    self.analysis_isotopomer.component_name.like(component_name_I)).all();
            if data_analysis_isotopomer:
                if data_analysis_isotopomer[0][0]: height_O = data_analysis_isotopomer[0][0];
                else: height_O = None;
                if data_analysis_isotopomer[0][1]: intensity_O = data_analysis_isotopomer[0][1];
                else: intensity_O = None;
                return height_O, intensity_O;
            else:
                return None,None;
        except SQLAlchemyError as e:
            print(e);
    def get_componentGroupFromIsotopomerAnalysis(self, component_name_I):
        try:
            component_group_name = session.query(self.analysis_isotopomer.component_group_name).filter(
                       self.analysis_isotopomer.component_name.like(component_name_I)).group_by(
                       self.analysis_isotopomer.component_group_name).all();
            component_group_name_O = component_group_name[0][0];
            return component_group_name_O;
        except SQLAlchemyError as e:
            print(e);
