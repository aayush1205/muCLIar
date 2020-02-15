#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate test
CURRDIR=$(readlink -f "$0")
CURRDIR=$(dirname "$CURRDIR")
python $CURRDIR/src/App.py "$@"