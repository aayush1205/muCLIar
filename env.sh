#!/bin/bash
conda env create -f env.yaml
eval "$(conda shell.bash hook)"
conda activate test
pip install PyVirtualDisplay==0.2.5
#move into local/bin

SHELL_TARGDIR="/usr/local/bin"
REPO_TARGDIR="/usr/local"
CURRDIR=$(readlink -f "$0")
CURRDIR=$(dirname "$CURRDIR")

sudo ln -s $CURRDIR/mu /usr/local/bin
chmod 777 /usr/local/bin/mu