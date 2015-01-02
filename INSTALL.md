SBaaS
============
Systems Biochemistry as a Service
============
Douglas McCloskey
-----------------

Getting started:
----------------
1.	Install python, postgresql, R, and other dependencies

2.	Build the sbaas database using the query 'data/postgresql/create_sbaas.sql'

3.	Login to the newly created database and run the query 'data/posgresql/initialize_sbaas.sql'

4.	Load initial data required for analyses by running the query data/posgresql/initialize_data_stage00_sbaas.sql'

5.	Define local user settings in the file data/sbaas_settings for use by the ORM

6.	Run one or multiple of the desired tests

Dependencies:
------------
Python 2.7+

R 2.12+

Postgresql 9.0+

Python-dependencies:
-------------------
cobrapy

escher

numpy

scipy

matplotlib

r2py

sqlalchemy

...