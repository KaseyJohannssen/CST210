#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Title: Module 4 Program Modification Problem 3
Author: Jenna Rogge
Version: 7-19-2020.1
Summary: This program reads in covid data from the new york times and plots it on a graph.
It also finds a best fit equasion for the first 80 days and finds the beta and gamma values 
for our SIR model. 
"""
import numpy as np
import matplotlib.pylab as plt
#import scipy.integrate as si
import scipy.optimize as so
# Create a function that defines the rhs of the differential equation system

def calc_RHS(y,t,p):
#   y = a list that contains the system state
#   t = the time for which the right-hand-side of the system equations
#       is to be calculated.
#   p = a tuple that contains any parameters needed for the model

#   Unpack the state of the system
    s = y[0]  # susceptible fraction
    i = y[1]  # 

#   Unpack the parameter list
    b, g = p

#   Calculate the rates of change (the derivatives)
    dsdt = -b*s*i
    didt = b*s*i - g*i
    drdt = g*i

    return [dsdt,didt,drdt]

def i_f(t,b,g):
    import numpy as np
    import scipy.integrate as si
    p = b,g
    yv = []
    for tt in t:
        if np.abs(tt)<1.e-5:
            yvt = y_0[1]
        else:
            ta = np.linspace(0,tt,10)
            # Solve the DE
            sol = si.odeint(calc_RHS,y_0,ta,args=(p,))
            yvt = sol[-1,1]
        yv.append(yvt)
    return yv
    import numpy as np
    import scipy.integrate as si
    p = b,g
    yv = []
    for tt in t:
        if np.abs(tt)<1.e-5:
            yvt = y_0[1]
        else:
            ta = np.linspace(0,tt,10)
            # Solve the DE
            sol = si.odeint(calc_RHS,y_0,ta,args=(p,))
            yvt = sol[-1,1]
        yv.append(yvt)
    return yv

# Main Program
N = 329201263.00 # US population January 2020

# Read in data
data = np.genfromtxt('NYTimes_COVID-19_US_revised.txt', dtype='unicode', 
                     delimiter='\t', skip_header=1)
tData = data[:,1]
tData = tData.astype(np.float)
tDataSub = tData[0:80]
IData = data[:,2]
IData = IData.astype(np.float)
IData = IData/N
IDataSub = IData[0:80]
# Define the initial conditions
y_0 = [1.0,1.0/N,0.]

# Define the initial condition
b = 2.0
g = 1.9
p = b, g


popt,pcov = so.curve_fit(i_f,tDataSub,IDataSub,p)
p_stderr = np.sqrt(np.diag(pcov))

# Calculate theoretical values
b,g = popt

# Define the time grid
ta = np.linspace(0,80,200)


Ntheory = i_f(ta,b,g)
   
# Plot the solution
plt.semilogy(tDataSub,IDataSub,linestyle='',marker='o',
         markersize=2.0, label='Data')
plt.semilogy(ta,Ntheory,color='g',label='best fit line')
plt.legend()
plt.grid()

# print the stats
print('b = ', b)
print('g = ',g)
db,dg = p_stderr
print( "db = ", db)
print( "dg = ", dg)

#showing graph
plt.grid(linestyle='-')
plt.title('beta and gamma fitting graph')
plt.xlabel('days')
plt.ylabel('number infected')
plt.legend()

plt.savefig('final.png')
plt.show()



