# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:42:27 2020

@author: TheoJRKoenig
"""

import numpy as np
from scipy.special import factorial, gamma
import matplotlib.pyplot as plt

n_integer = np.arange(1, 20, 1)
n_halfinteger = np.arange(1, 20, 0.5)

factorial = factorial(n_integer)
gamma = gamma(n_halfinteger+1)

fig, ax = plt.subplots()
ax.semilogy(n_integer, factorial, label = 'factorial(n)')
ax.semilogy(n_halfinteger, gamma, label = 'gamma(n+1)')
plt.xlabel('n')
plt.ylabel('factorial')
plt.legend()

#---Constants used
pi = np.pi
h = 6.62607004e-34
k_B = 1.38064852e-23
T_R = 293
amu = 1.66053904e-27 #kg
m = 4*amu
N = 1


u_R = (3/2)*k_B*T_R                 # U_R delen door N
λ_R = h*np.sqrt((3)/(4*pi*m*u_R))

# $\lambda = h\sqrt{\frac{3N}{4\pi m U_R}}\sqrt{\frac{U_R}{U}} = \lambda_R\sqrt{\frac{U_R}{U}}$ 