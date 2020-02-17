#!/bin/bash

#env ops
conda env create -f env.yaml
eval "$(conda shell.bash hook)"
conda activate test
pip install -r requirements.txt
sudo apt-get update -y
sudo apt-get install -y xvfb

#get chromedriver
RES="$(google-chrome --version)"
RES="$(echo $RES | cut -d' ' -f3)"
A="$(echo $RES | cut -d'.' -f1)"
if [[ $A == "79" ]];
then
    echo "Getting chrome driver for version 79 ..."
    sudo wget -P /usr/local/bin/ https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
    sudo unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin
fi
if [[ $A == "80" ]]
then 
    echo "Getting chrome driver for version 80 ..."
    sudo wget -P /usr/local/bin https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip
    sudo unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin
fi    

#move into local/bin
SHELL_TARGDIR="/usr/local/bin"
REPO_TARGDIR="/usr/local"
CURRDIR=$(readlink -f "$0")
CURRDIR=$(dirname "$CURRDIR")

sudo ln -s $CURRDIR/mu /usr/local/bin
chmod 777 /usr/local/bin/mu
chmod +x ./uninstall.sh
