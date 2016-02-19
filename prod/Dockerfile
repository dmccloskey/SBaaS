# Dockerfile to build SBaaS container images
# Based on Ubuntu

# Set the base image
FROM dmccloskey/python3cobrapy:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com

# Switch to root for installation
USER root

# Set several environmental variables that will be later removed
ENV GIT_USERNAME dmccloskey
ENV GIT_PASSWORD 18dglass
ENV GIT_ACCOUNT dmccloskey
ENV GIT_BRANCH master
ENV GIT_REPOS component-contribution ddt_python genomeScale_MFA genomeScale_MFA_INCA genomeScale_MFA_model io_utilities listDict matplotlib_utilities MDV_utilities molmass MS_utilities physiology_analysis python_statistics quantification_analysis r_statistics SBaaS_ale SBaaS_base SBaaS_COBRA SBaaS_database SBaaS_dataPreProcessing SBaaS_isotopomer SBaaS_LIMS SBaaS_MFA SBaaS_models SBaaS_physiology SBaaS_quantification SBaaS_resequencing SBaaS_rnasequencing SBaaS_statistics SBaaS_thermodynamics SBaaS_visualization SBaaS_webServer sequencing_analysis sequencing_utilities thermodynamics

#curl -sL --user "${GIT_USERNAME}:${GIT_PASSWORD}" https://github.com/$account/$repo/tarball/$tag_name > tarball.tar

# Install SBaaS modules from github
USER root
WORKDIR /usr/local
RUN mkdir SBaaS
WORKDIR /usr/local/SBaaS

COPY scripts/git_download.sh scripts/git_download.sh
RUN /bin/bash -c 'source scripts/git_download.sh ${GIT_USERNAME} ${GIT_PASSWORD} ${GIT_BRANCH} ${GIT_ACCOUNT} ${GIT_REPOS};'
RUN rm -rf scripts

# remove the environmental variables
RUN env --unset=GIT_USERNAME \
	&& env --unset=GIT_PASSWORD \
	&& env --unset=GIT_ACCOUNT \
	&& env --unset=GIT_BRANCH \
	&& env --unset=GIT_REPOS
	
EXPOSE 8080

# Create workspace directories
RUN mkdir /home/user/workspace_notebooks \
	&& mkdir /home/user/workspace_data \
	&& mkdir /home/user/workspace_data/_input \
	&& mkdir /home/user/workspace_data/_output \
	&& mkdir /home/user/workspace_data/models \
	&& mkdir /home/user/visualization_data \
	&& mkdir /home/user/visualization_resources \
	&& mkdir /home/user/postgresql \
	&& mkdir /home/user/settings
	
WORKDIR $HOME
USER user