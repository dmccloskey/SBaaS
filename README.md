SBaaS
============
Systems Biochemistry as a Service
============
Douglas McCloskey
============

Analysis pipelines currently supported:
1.	Quantification (i.e., Metabolomics)
2.	Isotopomer (i.e., Fluxomics)
3.	Physiology (i.e., Phenomics)
4.	ALE (i.e., ALE experiment growth rate trajectories)
5.	Resequencing (i.e., DNA population resequencing)

Project organization:
metabolomics.py: driver file
analysis/: code to support the analysis pipelines
data/: raw data, biochemical models, database dumps, compound .mol files, etc.
models/: data models of the database written in the ORM (i.e., sqlalchemy)
resources/: open-source and 3rd party dependencies and classes utilized in various analyses
sql/: sql queries not implemented or not supported by the ORM (i.e., sqlalchemy)
visualization/: webserver files used for data visualization
workspace/: scripts utilized to upload data, run analyses, and visualize data contained in the database

Dependencies:
Python 2.7+
R 2.12+
Postgresql 9.0+

Python-dependencies:
#TODO

Analysis Pipeline software needs:
1.	Fluxomics package written as a module for cobrapy
2.	Peak viewing and peak integration software written outside of the vendor-specific/proprietary domain
3.	Direct integration with breseq
4.	Web-UI for data analysis beyond only data visualization