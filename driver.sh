#! /usr/bin/bash
eval "$(conda shell.bash hook)"
conda activate mutest
EXEC_FILE="/usr/local/Musify/driver.py"
python $EXEC_FILE "$@"