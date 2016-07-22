#!/usr/bin/env python

#Mission 006 | The Next Dimension
#Autor | Robert Treharne
#Date | 30 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import sys
import csv

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

