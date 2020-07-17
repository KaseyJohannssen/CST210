# -*- coding: utf-8 -*-
"""
Spyder Editor
this code shows the spread of the covid-19 through a population
This is a temporary script file.
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#population of united states 
TP = 328239523

#people infected in the united states
PI = 2679230

#Total people recovered from covid at the estimated 
# 78% recovery rate (from CDC) time the number infected
PR = 2089799.4

# at first everyone,EO, is suspectable to Covid-19 
EO = TP - PI - PR

#infection rate,beta,
beta = .4

#Recovery rate,gamma,(1/14days)
gamma = 1.0/14

#create grid spacing
t = np.linspace(0,100,100)

#set up our def to solve SIR differiential equations
def disease(p,t,TP,beta,gamma):
    S, I, R = p
    dSdt = -beta * S * I / TP
    dIdt = beta * S * I / TP - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

#Intial conditions
d0 = EO,PR,PI

#integrate using odient function over t
ret = odeint(disease, d0, t, args=(TP, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
plt.plot(t, S/100000000, 'b', lw=2, label='Susceptible')
plt.plot(t, I/100000000, 'r', lw=2, label='Infected')
plt.plot(t, R/100000000, 'g', linestyle='--', lw=2, label='Recovered with immunity')
plt.xlabel('Days')
plt.ylabel('Numbers in the tens of millions')
plt.legend()
plt.grid()
plt.savefig('Covid19.png')
plt.show()


