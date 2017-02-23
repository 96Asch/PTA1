#!/usr/bin/env python
import pandas
import matplotlib.pyplot as plt
import sys
D = pandas.read_csv("../temp/plot_byte.txt", sep=" ", header=None, index_col=0)
D.plot(kind="bar", rot=30, legend=False)
plt.title("Average byte per hour")
plt.savefig("../Result/avg_byte_per_hour.pdf")
exit(0)
