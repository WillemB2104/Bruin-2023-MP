#!/bin/bash

# create folder with site name that is going to be shared
mkdir $1

#copy spec.json
cp spec.json $1

#copy list of files in halfpipe folder
ls $(ls -d derivatives/halfpipe/*/|head -n 1)/func > $1/list_output.txt

#copy report files
cp reports/reportpreproc.txt $1
cp reports/reportvals.txt $1
cp reports/exclude.json $1
