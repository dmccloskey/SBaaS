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
USER root
RUN mkdir /usr/local/lib/SBaaS
WORKDIR /usr/local/lib/SBaaS

COPY scripts/git_download.sh scripts/git_download.sh
RUN /bin/bash -c 'source scripts/git_download.sh ${GIT_USERNAME} ${GIT_PASSWORD} ${GIT_BRANCH} ${GIT_ACCOUNT} ${GIT_REPOS};'
RUN rm -rf scripts

# remove the environmental variables
RUN env --unset=GIT_REPOS	
	
EXPOSE 8088

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
	
WORKDIR $HOME
USER user

ENTRYPOINT ["python","/usr/local/lib/SBaaS/SBaaS_webServer/template_scripts/run_webServer_docker.py"]

#docker run -p 8088:8088 \
#	-v /Documents/Dockerbuild/settings/settings_metabolomics_docker.ini:/home/user/settings/settings_metabolomics_docker.ini \
#	-v /Documents/Dockerbuild/visualization_resources/:/home/user/visualization_resources/ \
#	--name=sbaas \
#	#--net=sbaas_network \
#	#--ip=172.22.0.3 \
#	-it dmccloskey/sbaas bash
#python /usr/local/lib/SBaaS/SBaaS_webServer/template_scripts/run_webServer_docker.py