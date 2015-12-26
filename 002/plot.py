#!/usr/bin/env python

#Mission 002 | Lock and Load
#Autor | Robert Treharne
#Date | 25 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import sys
import csv

def plot_file(filename):
    f = open(filename, 'rb')
    reader = csv.reader(f)
    headers = reader.next()
    data = []
    for line in reader:
        data.append(line)
    data = [[float(y) for y in x] for x in np.transpose(data)]
    plt.plot(data[0], data[1], '-o')
    plt.xlabel(headers[0])
    plt.ylabel(headers[1])

if __name__ == "__main__":
    plot_file(sys.argv[1])
    plt.show()

