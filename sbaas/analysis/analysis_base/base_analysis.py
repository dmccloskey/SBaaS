'''Base class for metabolomics analysis'''

from math import log, sqrt, exp
import csv
from sys import exit
import numpy
#from numpy import zeros, average, array

from models import *
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

class base_analysis():
    def __init__(self):
        self.session = Session();

    
