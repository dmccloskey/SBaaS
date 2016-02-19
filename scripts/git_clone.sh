#!/bin/bash
#DESCRIPTION: Clone git repositories using OAuth
#INPUT:
#GIT_BRANCH=branch name
#GIT_OAuth=OAuthentication key
#GIT_ACCOUNT=name of the git account
#GIT_REPOS=list of repository names
#EXAMPLE: git_clone.sh master 0de99441df6e8603623ed8c32b7583c435416c2e dmccloskey python3scientific python3cobrapy listDict

#parse the input
args=( "$@" )
GIT_BRANCH=${args[0]}
GIT_OAuth=${args[1]}
GIT_ACCOUNT=${args[2]}
GIT_REPOS=("${args[@]:3}")

#clone each repository
for GIT_REPO in ${GIT_REPOS[@]}
do
	echo GIT_REPO=$GIT_REPO, GIT_BRANCH=$GIT_BRANCH, GIT_OAuth=$GIT_OAuth, GIT_ACCOUNT=$GIT_ACCOUNT
	git clone -b $GIT_BRANCH https://$GIT_OAuth:x-oauth-basic@github.com/$GIT_ACCOUNT/$GIT_REPO.git
done