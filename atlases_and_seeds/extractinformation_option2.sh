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

# subject list
ls derivatives/halfpipe/ > $1/subject_list.txt

# confound files
mkdir $1/confounds
mkdir $1/seed_tsnr
mkdir $1/dualreg_tsnr
mkdir $1/corrmat_tsnr
for i in `cat $1/subject_list.txt`
do
cp derivatives/fmriprep/${i}/func/*confounds_timeseries.tsv $1/confounds/${i}_confounds.tsv
cp derivatives/halfpipe/${i}/func/*seed*stat-effect_statmap.json $1/seed_tsnr
cp derivatives/halfpipe/${i}/func/*map*stat-effect_statmap.json $1/dualreg_tsnr
cp derivatives/halfpipe/${i}/func/*timeseries.json $1/corrmat_tsnr
done



