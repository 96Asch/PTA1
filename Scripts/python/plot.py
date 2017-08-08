#!/usr/bin/env python

import pandas
import sys
import os
import matplotlib as mpl

if os.environ.get('DISPLAY','') == '':
    mpl.use('Agg')

import matplotlib.pyplot as plt

#Read the output of the bash script
D = pandas.read_csv(sys.stdin, sep=" ", header=None, index_col=0)

#Plot the graph with the right labels and title
D.plot(kind="bar", rot=30, legend=False)
plt.xlabel('Hours per day')
plt.ylabel('Bytes sent')
plt.title("Average byte per hour")

#Save the graph to a pdf file
plt.savefig("../Result/avg_byte_per_hour.pdf")

