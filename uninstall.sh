#!/bin/bash

#removing link and chrome drivers
sudo rm -rf /usr/local/bin/mu
sudo rm -rf /usr/local/bin/chromedriver
sudo rm -rf /usr/local/bin/chromedriver_linux64.zip

#removing conda env and dependencies. Also clone folder
#NOTE: removes clone folder also.
eval "$(conda shell.bash hook)"
conda deactivate
conda remove --name test --all
rm -rf ../muCLIar
