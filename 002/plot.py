#!/usr/bin/env python3

#Mission 002 | Lock and Load
#Autor | Robert Treharne
#Date | 25 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import os
import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 'x-large'

def plot_file(path, delim=','):

    abspath = os.path.abspath(path) #get absolute path

    sniffer = csv.Sniffer()

    with open(abspath, 'r') as f:
        has_header = sniffer.has_header(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, delimiter=delim)
    
        if has_header:
            #get header text
            header_text = next(reader)

        #read data to list
        data = []
        for line in reader:
            data.append(line)

        #transpose data into columns
        data = [[float(y) for y in x] for x in np.transpose(data)]

       #create plot
        plot = plt.plot(data[0], data[1], '-o')

        #if file has headers use these as label axes
        if has_header:
            plt.xlabel(header_text[0])
            plt.ylabel(header_text[1])
        return plot

if __name__ == "__main__":
    plot = plot_file(sys.argv[1])
    plt.show(plot)

