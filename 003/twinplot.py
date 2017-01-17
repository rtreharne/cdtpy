#!/usr/bin/env python3

#Mission 003 | Double Trouble
#Autor | Robert Treharne
#Date | 26 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
import csv
import os

mpl.rcParams['axes.labelsize'] = 'x-large'

def get_data(reader):
    data = []
    for line in reader:
        data.append(line)

    #transpose data into columns
    data = [[float(y) for y in x] for x in np.transpose(data)]

    return data

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
        data = get_data(reader)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([min(data[0]),max(data[0])])
        ln1 = ax.plot(data[0], data[1], color='blue', label=header_text[1])

        ax2 = ax.twinx()
        ax2.set_xlim([min(data[0]),max(data[0])])
        ln2 = ax2.plot(data[0], data[2], color='red', label=header_text[2])
       #create plot

        #if file has headers use these as label axes
        if has_header:
            ax.set_xlabel(header_text[0])
            ax.set_ylabel(header_text[1], color='blue')
            ax2.set_ylabel(header_text[2], color='red')

    return fig 

if __name__ == "__main__":
    plot = plot_file(sys.argv[1])
    plt.show(plot)

