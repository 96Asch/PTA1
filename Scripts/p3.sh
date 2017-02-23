src="/vol/share/groups/liacs/scratch/pt2017/opdracht1"
num="$(ls -1 /vol/share/groups/liacs/scratch/pt2017/opdracht1/*.bz2 | wc -l)"
python="../python"
temp="../temp"

echo "Beginning to process large batch..."
for i in $src/*.bz2; do
	echo "Processing: " $i;
	bzcat $i | awk '{print $4 $5 " " $10}'| tr  []/:+ " " | awk '{h[$4] += $NF} END{for (i in h) print i, h[i]}' >> $temp/byte_data.txt;
done

echo "Done processing files..."

echo "Now calculating averages..."
cat $temp/byte_data.txt | awk -v c="$num" '{h[$1] += $NF} END{for (i in h) print i, h[i]/c}'| sort > $temp/plot_byte.txt

echo "Now plotting..."
chmod +x ./$python/plot.py
./$python/plot.py

echo "Success!!! Saved in ../Result/avg_byte_per_hour.pdf"

echo "Removing temp files..."
rm $temp/plot_byte.txt $temp/byte_data.txt
