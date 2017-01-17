#!/usr/bin/env python3

#Mission 005 | Scatterbrain
#Autor | Robert Treharne
#Date | 30 Dec 2015

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

def data_dict(path, delim=','):
    '''This method creates a dictionary of data
       from a .csv file'''

    sniffer = csv.Sniffer()

    abspath = os.path.abspath(path)

    with open(abspath, 'r') as f:
        has_header = sniffer.has_header(f.read(1024))
        f.seek(0) #return to start of file
        reader = csv.reader(f, delimiter=delim)
        
        if has_header:
            #get header text
            header_text = next(reader)
            
        data = get_data(reader)

    #return as dictionary
    return {'headers': header_text, 'data': data}

def scatterplot(d):
    
    #set headers and data lists
    headers = d.get('headers', None)
    data = d.get('data', None)
    
    fig = plt.figure() #create figure object
    ax = fig.add_subplot(111)

    #create scatterplot 
    plot = ax.scatter(data[0], data[1], c=data[2])

    #add colorbar to plot
    cb = plt.colorbar(plot)

    if headers:
        #if headers are set then add labels
        ax.set_xlabel(headers[0])
        ax.set_ylabel(headers[1])
        cb.set_label(headers[2]) #colorbar label

    return fig, ax

if __name__ == "__main__":
    d = data_dict(sys.argv[1])
    fig, ax = scatterplot(d)
    plt.show()


