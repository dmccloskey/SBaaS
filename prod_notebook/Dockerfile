# Dockerfile to build SBaaS container images
# Based on Ubuntu

# Set the base image
FROM dmccloskey/python3cobrapy:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com

# Switch to root for installation
USER root

# Set several environmental variables that will be later removed
ARG GIT_USERNAME
ARG GIT_PASSWORD
ARG GIT_ACCOUNT
ARG GIT_BRANCH
ENV GIT_REPOS component-contribution ddt_python genomeScale_MFA genomeScale_MFA_INCA genomeScale_MFA_model io_utilities listDict matplotlib_utilities MDV_utilities molmass MS_utilities physiology_analysis python_statistics quantification_analysis r_statistics SBaaS_ale SBaaS_base SBaaS_COBRA SBaaS_database SBaaS_isotopomer SBaaS_LIMS SBaaS_MFA SBaaS_models SBaaS_physiology SBaaS_quantification SBaaS_resequencing SBaaS_rnasequencing SBaaS_statistics SBaaS_thermodynamics SBaaS_visualization SBaaS_webServer sequencing_analysis sequencing_utilities thermodynamics

#curl -sL --user "${GIT_USERNAME}:${GIT_PASSWORD}" https://github.com/$account/$repo/tarball/$tag_name > tarball.tar

# Install SBaaS modules from github
RUN mkdir /usr/local/lib/SBaaS
WORKDIR /usr/local/lib/SBaaS

COPY scripts/git_download.sh scripts/git_download.sh
RUN /bin/bash -c 'source scripts/git_download.sh ${GIT_USERNAME} ${GIT_PASSWORD} ${GIT_BRANCH} ${GIT_ACCOUNT} ${GIT_REPOS};'
RUN rm -rf scripts

# remove the environmental variables
RUN env --unset=GIT_REPOS	

# Create visualization directories and volumes
RUN mkdir /home/user/workspace_notebooks \
	&& mkdir /home/user/workspace_data \
	&& mkdir /home/user/visualization_data \
	&& mkdir /home/user/visualization_resources \
	&& mkdir /home/user/settings
VOLUME /home/user/workspace_notebooks \
	/home/user/workspace_data \
	/home/user/visualization_data \
	/home/user/visualization_resources \
	/home/user/settings
	
# Add the script for running ipython notebooks
WORKDIR /home/user/workspace/workspace_notebooks
ADD scripts/run_ipython.sh /home/user/workspace/workspace_notebooks/run_ipython.sh

EXPOSE 8888

WORKDIR $HOME/workspace/workspace_notebooks
USER user

ENTRYPOINT ["bash","/home/user/workspace/workspace_notebooks/run_ipython.sh"]
#docker run -p 8888:8888 -v /home/douglas/Documents/Dockerbuild_sbaas/settings/settings_metabolomics_docker.ini:/home/user/settings/settings_metabolomics_docker.ini -v /home/douglas/Documents/Dockerbuild_sbaas/visualization_resources/:/home/user/visualization_resources/ --name=sbaas --user=root -it -e "PASSWORD=metabolomics" dmccloskey/sbaas
#	#--net=sbaas_network \
#	#--ip=172.22.0.3 \