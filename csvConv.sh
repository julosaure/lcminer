#!/bin/bash


OPTIONS=" -B 1000 -format yyyy-MM-dd -D 6,7,8,27 " #  5,6,7,24 "
OPTIONS=$OPTIONS" -S 4,10,12,16,21,22,30,38,40 " #  3,9,11,15,20,21,29,37,39 "
OPTIONS=$OPTIONS" -N 5,9,11,14,23,24,26,39,41 " #   4,8,10,13,22,23,24,38,40 "

#OPTIONS=$OPTIONS" -L 5:36 months,60 months  "
CMD="java -cp /Users/julien/workspaces/weka/weka-3-7-9/weka.jar weka.core.converters.CSVLoader $OPTIONS data/LoanStats10k_.csv > data/LoanStats10k_.arff"

echo $CMD

$CMD
