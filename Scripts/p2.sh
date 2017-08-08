#!/bin/bash

#######################
#Andrew Huang S1913999#
#######################



src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
temp="temp"
python="python"
result="../Result"
files="wc_day*.out.bz2"

# We isolate the IP addresses by delimiting using the empty space and retrieving the first element,
# then we sort and count the unique occurrences and sort again by number and reversing the outcome so that
# the outcome will list the countries in descending order, then we only have to get the first 10 countries
# of the list and output it to the console.
bzcat $files | cut -d ' ' -f 1| python $python/geo.py | sort | uniq -c | sort -rn | head -n 10


