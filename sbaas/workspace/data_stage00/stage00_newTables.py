from analysis.analysis_base import *

def add_newTables():
    try:
        metabolomics_characterization.__table__.create(engine,True);
    except SQLAlchemyError as e:
        print(e);