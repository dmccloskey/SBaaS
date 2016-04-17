# Dockerfile to build SBaaS container images
# Based on Ubuntu

# Set the base image
FROM dmccloskey/python3cobrapy:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com

# Switch to root for installation
USER root

# Set several environmental variables that will be later removed
ENV GIT_BRANCH master
ENV GIT_OAuth
ENV GIT_ACCOUNT dmccloskey
ENV GIT_REPOS component-contribution ddt_python genomeScale_MFA genomeScale_MFA_INCA genomeScale_MFA_model io_utilities listDict matplotlib_utilities MDV_utilities molmass MS_utilities physiology_analysis python_statistics quantification_analysis r_statistics SBaaS_ale SBaaS_base SBaaS_COBRA SBaaS_database SBaaS_isotopomer SBaaS_LIMS SBaaS_MFA SBaaS_models SBaaS_physiology SBaaS_quantification SBaaS_resequencing SBaaS_rnasequencing SBaaS_statistics SBaaS_thermodynamics SBaaS_visualization SBaaS_webServer sequencing_analysis sequencing_utilities thermodynamics

# Install GitHub
RUN apt-get update && apt-get upgrade -y \
	&& apt-get install -y \
	git \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*
	
# Create a GitHub folder in the home directory
ENV HOME /home/user
RUN mkdir /home/user/GitHub
WORKDIR /home/user/GitHub

# Clone GitHub repos
COPY scripts/git_clone.sh scripts/git_clone.sh
RUN /bin/bash -c 'source scripts/git_clone.sh ${GIT_BRANCH} ${GIT_OAuth} ${GIT_ACCOUNT} ${GIT_REPOS};'
RUN rm -rf scripts

# remove the environmental variables
RUN env --unset=GIT_BRANCH \
	&& env --unset=GIT_OAuth \
	&& env --unset=GIT_ACCOUNT \
	&& env --unset=GIT_REPOS
	
EXPOSE 8080
WORKDIR $HOME
USER user