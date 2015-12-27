#!/usr/bin/env python

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
    f = open(abspath, 'rb') #open file for reading
    header = csv.Sniffer().has_header(f.read(1024)) #check for headers
    f.seek(0) #return to start of file
    reader = csv.reader(f, delimiter=delim)
    
    if header:
        #get header text
        header_text = reader.next()

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
    if header:
        ax.set_xlabel(header_text[0])
        ax.set_ylabel(header_text[1], color='blue')
        ax2.set_ylabel(header_text[2], color='red')

    return fig 

if __name__ == "__main__":
    plot = plot_file(sys.argv[1])
    plt.show(plot)

