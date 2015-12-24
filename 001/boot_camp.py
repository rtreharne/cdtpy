#Mission 001 | Boot Camp
#Autor | Robert Treharne
#Date | 24 Dec 2015

#pylab combines pyplot with numpy into a single namespace. This is convenient for interactive work, but for programming it is recommended that the namespaces be kept separate

import numpy as np
import matplotlib.pyplot as plt

#Objective 1
print  "{0:.2f}".format(np.pi)

#Objective 2

x = np.arange(0, 5*np.pi, 0.1)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.title('My first plot using a python script!')

plt.show() #You need to include this to show the plot
