#!/bin/bash

#env ops
conda env create -f arch_install.yaml
eval "$(conda shell.bash hook)"
conda activate test
pip install -r requirements.txt
sudo wget -P /usr/local/bin https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_linux64.zip
sudo unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin

#move into local/bin
SHELL_TARGDIR="/usr/local/bin"
REPO_TARGDIR="/usr/local"
CURRDIR=$(readlink -f "$0")
CURRDIR=$(dirname "$CURRDIR")

sudo ln -s $CURRDIR/mu /usr/local/bin
chmod 777 /usr/local/bin/mu
chmod +x ./uninstall.sh
