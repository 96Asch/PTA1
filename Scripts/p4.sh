#!/bin/bash

#######################
#Andrew Huang S1913999#
#######################

src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
temp="temp"
python="python"
result="../Result"
files="wc_day*.out.bz2"


# We first filter the logs for successful connections or redirections, those that contain the 200 or 3xx codes.
# We then isolate the directory paths and cut off the filenames.
# Then we sort and add the unique ones together and then sort again by the second element which is then fed to the python script
# to produce an ascii tree.
bzcat $src/$files | grep -P '(200|3\d\d (\d+|-)$)' | awk '{print $7}' | sed 's%/[^/]*$%/%' | sort | uniq -c | sort -k2  | python $python/asciiTree.py



