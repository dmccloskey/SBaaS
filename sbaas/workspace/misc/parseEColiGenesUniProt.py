from analysis.analysis_base.base_importData import base_importData
from analysis.analysis_base.base_exportData import base_exportData
import json

def parse_data():
    bi = base_importData()
    bi.read_csv('resources\\ecoli_genes_UniProt_140903.csv')
    ecoligenes = [];
    for d in bi.data:
        for gene in d['gene_name'].split():
            tmp = {};
            tmp['biologicalmaterial_id']=d['biologicalmaterial_id']
            tmp['ordered_locus_name']=d['ordered_locus_name']
            tmp['ordered_locus_name2']=d['ordered_locus_name2']
            tmp['swissprot_entry_name']=d['swissprot_entry_name']
            tmp['ac']=d['ac']
            tmp['ecogene_accession_number']=d['ecoGene_accession_number']
            tmp['gene_name']=gene;
            ecoligenes.append(tmp); 
    return ecoligenes;

def export_data(ecoligenes):
    bo = base_exportData(ecoligenes);
    bo.write_dict2csv('data\\_input\\140910_biologicalmaterial_genereferences.csv');

from analysis.analysis_base import *

def add_newTables():
    try:
        biologicalMaterial_geneReferences.__table__.create(engine,True);
    except SQLAlchemyError as e:
        print(e);

from analysis.analysis_stage00.stage00_io import stage00_io

def add_data():
    io = stage00_io();
    io.import_biologicalMaterialGeneReferences_add('data\\_input\\140910_biologicalmaterial_genereferences.csv')

def _main_():
    #add_newTables();
    #add_data();

    #from Bio import SeqIO
    #from Bio import Entrez
    #Entrez.email = 'dmccloskey87@gmail.com'
    #handle = Entrez.efetch(db="nucleotide",id="49175990",rettype='gb',retmode='text')
    #record_genbank = SeqIO.read(handle,'genbank')
    #handle.close()

    print 'done'