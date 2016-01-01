#!/usr/bin/env python

#Mission 006 | The Next Dimension
#Autor | Robert Treharne
#Date | 30 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.mlab import griddata
import os
import sys
import csv
import getopt

mpl.rcParams['axes.labelsize'] = 'x-large'

def contour_plot(d, type = 'bw'):
    x, y, z = format_data(d)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    L = ax.contour(x, y, z, 10, colors = 'k')
    ax.clabel(L, fontsize=10, fmt='%1.0f')

    if type=='col':
        S = ax.contourf(x, y, z, 20, cmap = plt.cm.rainbow)
        CB = plt.colorbar(S)
        if d.get('headers'):
            CB.set_label(d.get('headers')[2])
      

    if d.get('headers'):
        ax.set_xlabel(d.get('headers')[0])
        ax.set_ylabel(d.get('headers')[1])

    return fig

def format_data(d):
    x = d.get('data')[0]
    y = d.get('data')[1]
    z = d.get('data')[2]

    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)

    zi = griddata(x, y, z, xi, yi, interp='linear')

    return xi, yi, zi

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

    abspath = os.path.abspath(path) #get absolute path
    f = open(abspath, 'rb') #open file for reading
    header = csv.Sniffer().has_header(f.read(1024)) #check for headers
    f.seek(0) #return to start of file
    reader = csv.reader(f, delimiter=delim)
    
    if header:
        #get header text
        header_text = reader.next()
    else:
        header_text = None
        
    data = get_data(reader)

    #return as dictionary
    return {'headers': header_text, 'data': data}

if __name__ == "__main__":
    d = data_dict(sys.argv[1])
    options, remainder = getopt.getopt(sys.argv[2:], 'o:', ['option='])
    print 'OPTIONS  :', options
    contour_type = 'bw'
    for opt, arg in options:
        if opt in ('-o', '--option'):
            contour_type = arg
       
    plot = contour_plot(d, type=contour_type)
    plt.show(plot)
