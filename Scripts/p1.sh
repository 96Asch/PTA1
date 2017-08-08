#!/bin/bash

#######################
#Andrew Huang S1913999#
#######################

src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
files="wc_day*.out.bz2"

# Here we get the ninth element from a line which contains the HTTP return code,
# then we filter out all codes containing HTTP code 200 and then sorting them and
# adding the unique ones up, which is then printed to the console.
bzcat $src/$files | awk -F' ' '{print $9}' | grep -v "200" | sort | uniq -c
