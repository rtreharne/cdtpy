#!/usr/bin/env python

#Mission 007 | The Next Dimension
#Autor | Robert Treharne
#Date | 31 Dec 2015
import numpy as np
import os
import sys
import csv

def jvrip(fname):
    '''Extract cell parameters from .csv/.txt. file'''
    try:
        d = data_dict(fname)
    except ValueError:
        d = data_dict(fname, delim=' ')
    p = params(d)
    return p

def params(d, area=0.25):
    '''Get cell parameters from data dictionary'''
    data = d.get('data')
    
    #assigning data lists
    y = np.array(data[1])*1000/area
    y = y*-1
    x = np.array(data[0])
    
    #interpolation
    xi = np.linspace(-1, 1, 1e4)
    yi = np.interp(xi, x, y)
    
    #jsc
    idx = abs(xi-0).argmin()
    jsc = yi[idx]
    
    #voc    
    idy = abs(yi-0).argmin()
    voc = xi[idy]
    
    #FF
    P = xi*yi
    idp = list(P).index(P.max())
    FF = P[idp]/(jsc*voc)
    
    #Eff
    Eff = jsc*voc*FF
    
    return {'jsc': jsc,
            'voc': voc,
            'FF': FF,
            'Eff': Eff} 

def get_data(reader):
    data = []
    for line in reader:
        data.append(line)

    #transpose data into columns
    data = [[float(y) for y in x] for x in np.transpose(data)]

    return data 

def data_dict(path, delim=','):
    '''This method creates a dictionary of data
       from a .csv or .txt file'''

    abspath = os.path.abspath(path) #get absolute path
    f = open(abspath, 'r') #open file for reading
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
    
    print(jvrip(sys.argv[1]))

