src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
temp="../temp"
python="../python"
result="../Result"

bzcat wc_day*.out.bz2 | grep -v '200','3??' | awk '{print $7}' | sed 's%/[^/]*$%/%' | grep -v '\.' | sort | uniq -c

