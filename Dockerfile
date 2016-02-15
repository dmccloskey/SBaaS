# Dockerfile to build SBaaS container images
# Based on Ubuntu

# Set the base image
FROM python3cobrapy:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com

# Install SBaaS modules from github
WORKDIR /usr/local/
RUN mkdir SBaaS
WORKDIR /usr/local/SBaaS/

# component-contribution
RUN wget https://github.com/dmccloskey/component-contribution/archive/master.zip
RUN unzip master.zip
RUN mv component-contribution-master component-contribution

# ddt_python
RUN wget https://github.com/dmccloskey/ddt_python/archive/master.zip
RUN unzip master.zip
RUN mv ddt_python-master ddt_python

# genomeScale_MFA
RUN wget https://github.com/dmccloskey/genomeScale_MFA/archive/master.zip
RUN unzip master.zip
RUN mv genomeScale_MFA-master genomeScale_MFA

# genomeScale_MFA_INCA
RUN wget https://github.com/dmccloskey/genomeScale_MFA_INCA/archive/master.zip
RUN unzip master.zip
RUN mv genomeScale_MFA_INCA-master genomeScale_MFA_INCA

# genomeScale_MFA_model
RUN wget https://github.com/dmccloskey/genomeScale_MFA_model/archive/master.zip
RUN unzip master.zip
RUN mv genomeScale_MFA_model-master genomeScale_MFA_model

# io_utilities
RUN wget https://github.com/dmccloskey/io_utilities/archive/master.zip
RUN unzip master.zip
RUN mv io_utilities-master io_utilities

# listDict
RUN wget https://github.com/dmccloskey/listDict/archive/master.zip
RUN unzip master.zip
RUN mv listDict-master listDict

# matplotlib_utilities
RUN wget https://github.com/dmccloskey/matplotlib_utilities/archive/master.zip
RUN unzip master.zip
RUN mv matplotlib_utilities-master matplotlib_utilities

# MDV_utilities
RUN wget https://github.com/dmccloskey/MDV_utilities/archive/master.zip
RUN unzip master.zip
RUN mv MDV_utilities-master MDV_utilities

# molmass
RUN wget https://github.com/dmccloskey/molmass/archive/master.zip
RUN unzip master.zip
RUN mv molmass-master molmass

# MS_utilities
RUN wget https://github.com/dmccloskey/MS_utilities/archive/master.zip
RUN unzip master.zip
RUN mv MS_utilities-master MS_utilities

# physiology_analysis
RUN wget https://github.com/dmccloskey/physiology_analysis/archive/master.zip
RUN unzip master.zip
RUN mv physiology_analysis-master physiology_analysis

# python_statistics
RUN wget https://github.com/dmccloskey/python_statistics/archive/master.zip
RUN unzip master.zip
RUN mv python_statistics-master python_statistics

# quantification_analysis
RUN wget https://github.com/dmccloskey/quantification_analysis/archive/master.zip
RUN unzip master.zip
RUN mv quantification_analysis-master quantification_analysis

# r_statistics
RUN wget https://github.com/dmccloskey/r_statistics/archive/master.zip
RUN unzip master.zip
RUN mv r_statistics-master r_statistics

# SBaaS_ale
RUN wget https://github.com/dmccloskey/SBaaS_ale/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_ale-master SBaaS_ale

# SBaaS_base
RUN wget https://github.com/dmccloskey/SBaaS_base/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_base-master SBaaS_base

# SBaaS_COBRA
RUN wget https://github.com/dmccloskey/SBaaS_COBRA/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_COBRA-master SBaaS_COBRA

# SBaaS_database
RUN wget https://github.com/dmccloskey/SBaaS_database/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_database-master SBaaS_database

# SBaaS_dataPreProcessing
RUN wget https://github.com/dmccloskey/SBaaS_dataPreProcessing/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_dataPreProcessing-master SBaaS_dataPreProcessing

# SBaaS_isotopomer
RUN wget https://github.com/dmccloskey/SBaaS_isotopomer/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_isotopomer-master SBaaS_isotopomer

# SBaaS_LIMS
RUN wget https://github.com/dmccloskey/SBaaS_LIMS/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_LIMS-master SBaaS_LIMS

# SBaaS_MFA
RUN wget https://github.com/dmccloskey/SBaaS_MFA/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_MFA-master SBaaS_MFA

# SBaaS_models
RUN wget https://github.com/dmccloskey/SBaaS_models/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_models-master SBaaS_models

# SBaaS_physiology
RUN wget https://github.com/dmccloskey/SBaaS_physiology/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_physiology-master SBaaS_physiology

# SBaaS_quantification
RUN wget https://github.com/dmccloskey/SBaaS_quantification/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_quantification-master SBaaS_quantification

# SBaaS_resequencing
RUN wget https://github.com/dmccloskey/SBaaS_resequencing/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_resequencing-master SBaaS_resequencing

# SBaaS_rnasequencing
RUN wget https://github.com/dmccloskey/SBaaS_rnasequencing/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_rnasequencing-master SBaaS_rnasequencing

# SBaaS_statistics
RUN wget https://github.com/dmccloskey/SBaaS_statistics/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_statistics-master SBaaS_statistics

# SBaaS_thermodynamics
RUN wget https://github.com/dmccloskey/SBaaS_thermodynamics/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_thermodynamics-master SBaaS_thermodynamics

# SBaaS_visualization
RUN wget https://github.com/dmccloskey/SBaaS_visualization/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_visualization-master SBaaS_visualization

# SBaaS_webServer
RUN wget https://github.com/dmccloskey/SBaaS_webServer/archive/master.zip
RUN unzip master.zip
RUN mv SBaaS_webServer-master SBaaS_webServer

# sequencing_analysis
RUN wget https://github.com/dmccloskey/sequencing_analysis/archive/master.zip
RUN unzip master.zip
RUN mv sequencing_analysis-master sequencing_analysis

# sequencing_utilities
RUN wget https://github.com/dmccloskey/sequencing_utilities/archive/master.zip
RUN unzip master.zip
RUN mv sequencing_utilities-master sequencing_utilities

# thermodynamics
RUN wget https://github.com/dmccloskey/thermodynamics/archive/master.zip
RUN unzip master.zip
RUN mv thermodynamics-master thermodynamics


