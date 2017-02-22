#!/usr/bin/python
import pandas
import matplotlib.pyplot as plt
import sys
D = pandas.read_csv(sys.stdin, sep=" ", header=None, index_col=0)
D.plot(kind="bar", rot=30, legend=False)
plt.title("Mijn plot")
plt.show()
exit(0)
