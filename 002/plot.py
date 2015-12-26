#!/usr/bin/env python

#Mission 002 | Lock and Load
#Autor | Robert Treharne
#Date | 25 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import os

def plot_file(path, delim=','):
    abspath = os.path.abspath(path) #get absolute path
    f = open(abspath, 'rb') #open file for reading
    header = csv.Sniffer().has_header(f.read(1024)) #check for headers
    f.seek(0) #return to start of file
    reader = csv.reader(f, delimiter=delim)
    
    if header:
        #get header text
        header_text = reader.next()

    #read data to list
    data = []
    for line in reader:
        data.append(line)

    #transpose data into columns
    data = [[float(y) for y in x] for x in np.transpose(data)]

   #create plot
    plot = plt.plot(data[0], data[1], '-o')

    #if file has headers use these as label axes
    if header:
        plt.xlabel(header_text[0])
        plt.ylabel(header_text[1])
    return plot

if __name__ == "__main__":
    plot = plot_file(sys.argv[1])
    plt.show(plot)

