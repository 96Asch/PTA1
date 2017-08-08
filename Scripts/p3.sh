#!/bin/bash

#######################
#Andrew Huang S1913999#
#######################

src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
num_of_days="$(ls -1 /vol/share/groups/liacs/scratch/pt2017/opdracht1/*.bz2 | wc -l)"
python="python"
temp="temp"
files="wc_day*.out.bz2"

# From the files, we filter the 4, 5 and last element from the line and then for each 4th element we add the bytes at
# the end of the line together for each day.
for i in $src/$files; do
	bzcat $files | awk '{print $4 $5 $NF}'| tr  []/:+ " " | awk '{h[$4] += $NF} END{for (i in h) print i, h[i]}' >> $temp/byte_data.txt;
done


# From the accumulated data we first calculate the number of days which is the number of files in the folder.
# We then do the same as first by adding up the bytes for each day and then outputting it per day divided by the number of days
# in total, then feeding the data to the plot which then draws the plot and outputs it to a PDF file.
cat $temp/byte_data.txt | awk -v c="$num_of_days" '{h[$1] += $NF} END{for (i in h) print i, h[i]/c}'| sort | python $python/plot.py

# Remove the temporary file.
rm $temp/byte_data.txt
