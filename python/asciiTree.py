#!/usr/bin/env python
treeArray = []
value = 10
prevLine = ""

# Function to calculate the correction for proper alignment.
def calcAlignment (value, hits):
	correction = value - len(hits)
	return correction

# Function to add nodes to the tree list.
def appendTreeList(treeArray, hits, rank, dirList, correction, deletion):
	if deletion < 0:
		deletion = deletion*-1
	treeArray.append(hits + ' '*correction + "|   "*(rank - deletion) + "x----"*n + dirList[-deletion] + "/")
	return

# Main function to split the data from a txt file and properly
# insert them into an ascii tree.
outFile = open("../Result/ascii_tree.txt", "w")
with open("../temp/tree_data.txt","r") as f:
	for line in f:
		temp = line.split()
		hits = temp[0]
		dirString = temp[1].rstrip()
		rank = dirString.count('/')
		prevRank = prevLine.count('/')
		correct = calcAlignment(value, hits)
		dirList = dirString.split('/')

		if rank > 1:
			n = 1
		else:
			n = 0
		if (rank-prevRank) > 1: #if directory has never been visited
			appendTreeList(treeArray, "0", rank, dirList, correct, 3)		
		appendTreeList(treeArray, hits, rank, dirList, correct, 2)
		prevLine = line

	correct = calcAlignment(value, "Hits:")
	outFile.write("Hits:" + " "*correct + "Directory:\n")
	for node in treeArray:
		outFile.write(node)
f.close()
			
