src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
temp="../temp"
python="../python"
result="../Result"

echo "Processing data...(1/2)"
bzcat $src/wc_day*.out.bz2 | awk -F' ' '{print $1}' > $temp/ipaddress.txt
chmod +x $python/geo.py

echo "Running python script..."
./$python/geo.py

echo "Processing data...(2/2)"
cat $temp/landcodes.txt | sort | uniq -c | head > $result/p2_result.txt

echo "Removing temp files..."
rm $temp/ipaddress.txt $temp/landcodes.txt

