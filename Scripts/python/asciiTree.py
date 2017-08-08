#!/usr/bin/env python

import sys

# Function to calculate the correction for proper alignment.
def calcAlignment (hits):
	numberOfSpaces = 15
	spacing = numberOfSpaces - len(hits)
	return spacing

# Function to add nodes to the tree list.
def appendTreeList(treeArray, hits, folderCount, dirList, correction, deletion):
	if folderCount == 1: # first directory in the tree
		treeArray.append(hits + ' '*correction + ' ' + dirList[-deletion] + "/")		
	else:
		treeArray.append(hits + ' '*correction + " | "*(folderCount - deletion) + " x---- " + dirList[-deletion] + "/")
	return

# Main function to split the data from the output and
# insert them to the array in the correct order which will then
# be printed to the console.

def main():
	treeArray = []
	prevLine = ""
	for line in sys.stdin:
		temp = line.split()
		hits = temp[0]
		dirString = temp[1]
		folderCount = dirString.count('/')
		prevfolderCount = prevLine.count('/')
		correction = calcAlignment(hits)
		dirList = dirString.split('/')
		if (folderCount-prevfolderCount) > 1: #if directory has never been visited
			appendTreeList(treeArray, hits, folderCount, dirList, correction, 3)		
		appendTreeList(treeArray, hits, folderCount, dirList, correction, 2)
		prevLine = line

	spacing = calcAlignment("Hits:")
	print("Hits:" + " "*spacing + "Directory:\n")	
	for node in treeArray:
		print(node)
	return

main()
