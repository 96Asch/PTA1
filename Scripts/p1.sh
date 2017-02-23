src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
result="../Result"
bzcat $src/wc_day*.out.bz2 | grep -v "200" | awk -F' ' '{print $1}' > $result/p1_result.txt
