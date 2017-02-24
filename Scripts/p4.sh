#######################
#Andrew Huang S1913999#
#######################

src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
temp="../temp"
python="../python"
result="../Result"

bzcat $src/wc_day*.out.bz2 | grep -E '200|3??' | awk '{print $7}' | sed 's%/[^/]*$%/%' | egrep -v '\.|\*' | egrep -v '\/\/' | sort | uniq -c | sort -k2 > ../temp/tree_data.txt

chmod +x ./../python/asciiTree.py
echo "Creating ASCII tree..."
./../python/asciiTree.py

cat ../Result/ascii_tree.txt
rm ../temp/tree_data.txt

