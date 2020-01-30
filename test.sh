#!/bin/bash

#just a test script to check chrome driver installation
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
    sudo wget -p /usr/local/bin https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip
    sudo unzip /usr/local/bin/chromedriver_linux64.zip -d /usr/local/bin
fi    