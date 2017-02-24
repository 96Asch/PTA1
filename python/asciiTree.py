#!/usr/bin/python

with open("../temp/directory_list.txt","r") as f:
	for line in f:
		line = line.rstrip("\n");
		rank = line.count("/")	 -1
		print line, rank
f.close()
