SBaaS
============
Systems Biochemistry as a Service
============
Douglas McCloskey
-----------------

Project modules:
---------------------
SBaaS_ale
SBaaS_base
SBaaS_COBRA (porting from sbaas_v1...)
SBaaS_dataPreProcessing (refactoring missing value and data normalization methods...)
SBaaS_isotopomer
SBaaS_LIMS
SBaaS_MFA
SBaaS_MASS (in development...)
SBaaS_models
SBaaS_physiology
SBaaS_quantification
SBaaS_resequencing
SBaaS_rnasequencing
SBaaS_statistics
SBaaS_thermodynamics
SBaaS_visualization
SBaaS_webServer

Analysis Pipeline software needs:
---------------------------------
1.	Fluxomics package written as a module for cobrapy that includes support for stationary and non-stationary tracer experiments for any element type.  (expansion of data_stage02_isotopomer)

	a.	atom mapping method

	b.	cobra2emu
	
	c.	tracer simulation and identifiability analysis
	
	d.	flux estimate, parameter continuation, and monte-carlo sampling
	
2.	LC-MS raw data processing and integration software 

	a. pre-processing:
	
		i. mass shift correction
		ii. smoothing
		iii. background removal (i.e., baseline reduction)
		iv. de-spiking
		v. mass defect filtering (MDF) to remove non-relevant background ions
		vi. de-isotoping
		
	b. peak integration
	
		i. improved peak alignment and idenfication
		ii. improved peak integration algorithms based on machine learning techniques
		
3.	Expansion of the toolbox of statistical methods and algorithms to more advanced machine learning algorithms including neural networks and simulated annealing.  

4.	Improved user-friendly web-interface for data processing and analysis using [ddt](https://github.com/dmccloskey/ddt.git) (currently in progress...)

5.	Integration with additional open-source sequencing alignment and annotation utilities

6.	Integration with the MASS toolbox and other Kinetic modelling packages

7.	Improved database security and SSH