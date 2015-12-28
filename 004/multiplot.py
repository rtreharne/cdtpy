#!/usr/bin/env python

#Mission 004 | Splitsville | Objective 2: Multiplot
#Autor | Robert Treharne
#Date | 28 Dec 2015

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
import csv
import os
import glob

mpl.rcParams['axes.labelsize'] = 'x-large'

def get_filenames(dir):
    files = glob.glob('{0}/*.csv'.format(dir))
    files.sort()
    return files

def get_data(fname):
    
    data = []

    with open(fname, 'r') as f:
        try:
            reader = csv.reader(f)
            header = next(reader)
            for line in reader:
                data.append(line)
        except StopIteration:
            pass 

    return np.transpose(data)

def multiplot(files, param='::'):

    p = param.split(':')

    for i in range(len(p)):
        if p[i] == '':
            p[i] = None
        else:
            p[i] = int(p[i])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for fname in files[p[0]:p[1]:p[2]]:
        data = get_data(fname)
        if len(data) == 2:
            l, = ax.plot(data[0], data[1], label = fname)
            ax.legend(loc=4)

    return fig


if __name__ == "__main__":
    files = get_filenames(sys.argv[1])
    try:
        multiplot(files, sys.argv[2])
    except IndexError:
        multiplot(files)
    plt.show()

    

