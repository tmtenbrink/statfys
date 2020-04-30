# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:17:02 2020

@author: TheoJRKoenig
"""
import numpy as np
from scipy.special import factorial

#---Constants used
pi = np.pi

n = 20          #no. of heads
N_start = 30    #starting number of coints
N_end = 100     #ending number of coins

def exact_multiplicity(N_start,N_end):
    size = N_end-N_start
    multplicity = np.empty(size)
    for i in range(N_start, N_end):
        m = factorial(i)/(factorial(n)*factorial(i-n))
        multplicity[i-N_start] = m 
    return multplicity

def stirling_multiplicity(N_start, N_end):
    size = N_end-N_start
    multplicity = np.empty(size)
    for i in range(N_start, N_end):
        m = 1/np.sqrt(2*pi)*np.sqrt(i/(n*(i-n)))*np.float_power(i,i)/(np.float_power(n,n)*np.float_power(i-n,i-n))
        multplicity[i-N_start] = m 
    return multplicity


exact = exact_multiplicity(N_start, N_end)
stirling = stirling_multiplicity(N_start, N_end)

error = np.divide(stirling-exact,stirling)*100

answer1_1 = error
answer1_2 = np.where(error<0.5)[0][0]+1
answer1_3 = len(np.where(error<0.5)[0])

print("The percentage errors of the stirling approxiamtion are:", error)
print("From coin number "+str(answer1_2)+" the error of Stirling's approximation is less than 0.5%")
print("There are "+str(answer1_3)+" coins above which the error satisfies the 0.5 % criterion")


