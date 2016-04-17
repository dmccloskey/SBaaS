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
	
# Add the script for running ipython notebooks
WORKDIR /home/user/workspace/workspace_notebooks
EXPOSE 8888
ADD scripts/run_ipython.sh /home/user/workspace/workspace_notebooks/run_ipython.sh
#CMD ["/home/user/workspace/workspace_notebooks/run_ipython.sh"]

# Install visual studios code dependencies
RUN apt-get update -y && apt-get install -y \
	libasound2 \
	libatk1.0-0 \
	libcairo2 \
	libcups2 \
	libdatrie1 \
	libdbus-1-3 \
	libfontconfig1 \
	libfreetype6 \
	libgconf-2-4 \
	libgcrypt20 \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libgdk-pixbuf2.0-0 \
	libglib2.0-0 \
	libgtk2.0-0 \
	libgpg-error0 \
	libgraphite2-3 \
	libnss3 \
	libnspr4 \
	libpango-1.0-0 \
	libpangocairo-1.0-0 \
	libxcomposite1 \
	libxcursor1 \
	libxdmcp6 \
	libxi6 \
	libxrandr2 \
	libxrender1 \
	libxtst6 \
	liblzma5 \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

# Download the source for visual studios code
RUN buildDeps=' \
		ca-certificates \
		curl \
		unzip \
	' \
	&& set -x \
	&& apt-get update -y && apt-get install -y $buildDeps --no-install-recommends \
	&& curl -sL https://deb.nodesource.com/setup | bash - \
	&& apt-get update && apt-get install -y nodejs --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -sSL https://az764295.vo.msecnd.net/public/0.10.6-release/VSCode-linux64.zip -o /user/local/vs.zip \
	&& unzip /user/local/vs.zip -d /usr/src/ \
	&& rm -rf /user/local/vs.zip \
	&& apt-get purge -y --auto-remove $buildDeps

# Copy the script for running visual studios code
COPY scripts/run_vs.sh /usr/local/bin/run_vs.sh

# Switch back to user
WORKDIR $HOME
USER user
#ENTRYPOINT [ "/usr/local/bin/start.sh" ]
CMD ["/bin/bash"]

# docker run -d \
# 	-v /tmp/.X11-unix:/tmp/.X11-unix \
# 	-e DISPLAY=unix$DISPLAY \
#	--device /dev/dri \
# 	--name visualstudio \
# 	jess/visualstudio