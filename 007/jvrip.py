#!/usr/bin/env python

#Mission 007 | The Next Dimension
#Autor | Robert Treharne
#Date | 31 Dec 2015
import numpy as np
import os
import sys
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.labelsize'] = 'x-large'

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

    p = {'jsc': jsc,
         'voc': voc,
         'FF': FF,
         'Eff': Eff} 

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xi, yi, '-', color='red')
    ylim = [0, max(yi)*1.1]
    xlim = [0, p.get('voc')*1.1]
    ax.set_ylim(ylim)
    ax.set_xlim(xlim)
    ax.set_xlabel('$V$, volts')
    ax.set_ylabel('$J$, mA.cm$^2$')
    text = 'Eff: {0:.2f} %\nJsc: {1:.2f} ma/cm^2\nVoc: {2:.2f} V\nFF: {3:.2f} %'.format(p.get('Eff'), p.get('jsc'), p.get('voc'), p.get('FF')*100)
    ax.annotate(text, xy=(0.05, 0.4), xycoords='axes fraction', size=15)

    return p, fig

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

    sniffer = csv.Sniffer()

    with open(abspath, 'r') as f:
        header = sniffer.has_header(f.read(1024)) #check for headers
        f.seek(0) #return to start of file
        reader = csv.reader(f, delimiter=delim)
        
        if header:
            #get header text
            header_text = next(reader)
        else:
            header_text = None
            
        data = get_data(reader)

    #return as dictionary
    return {'headers': header_text, 'data': data}

if __name__ == "__main__":
    p, fig = jvrip(sys.argv[1])
    print(p)
    plt.show(fig)

