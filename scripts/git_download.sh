#!/bin/bash
#DESCRIPTION: Download git repositories using curl
#INPUT:
#GIT_USERNAME=username
#GIT_PASSWORD=password
#GIT_BRANCH=branch name
#GIT_ACCOUNT=name of the git account
#GIT_REPOS=list of repository names
#EXAMPLE:bash git_download.sh dmccloskey 18dglass master dmccloskey python3scientific python3cobrapy listDict

#parse the input
args=( "$@" )
GIT_USERNAME=${args[0]}
GIT_PASSWORD=${args[1]}
GIT_BRANCH=${args[2]}
GIT_ACCOUNT=${args[3]}
GIT_REPOS=("${args[@]:4}")

#download each repository
for GIT_REPO in ${GIT_REPOS[@]}
do
	echo GIT_REPO=$GIT_REPO, GIT_USERNAME=$GIT_USERNAME, GIT_PASSWORD=$GIT_PASSWORD, GIT_BRANCH=$GIT_BRANCH, GIT_ACCOUNT=$GIT_ACCOUNT
	curl -sL --user "${GIT_USERNAME}:${GIT_PASSWORD}" https://github.com/$GIT_ACCOUNT/$GIT_REPO/archive/$GIT_BRANCH.zip > $GIT_BRANCH.zip
	unzip $GIT_BRANCH.zip
	mv $GIT_REPO-$GIT_BRANCH $GIT_REPO
	rm $GIT_BRANCH.zip