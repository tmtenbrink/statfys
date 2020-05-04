# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:17:02 2020

@author: TheoJRKoenig
"""
import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt

#---Constants used
pi = np.pi

n = 20          #no. of heads
N_start = 30    #starting number of coints
N_end = 100     #ending number of coins

def exact_multiplicity(N_start,N_end,n):
    n_array = np.ones(N_end-N_start)*n
    N_array = np.linspace(N_start,N_end, N_end-N_start)
    multiplicity = factorial(N_array)/(factorial(n_array)*factorial(N_array-n_array))
    return multiplicity

def stirling_multiplicity(N_start, N_end,n):
    n_array = np.ones(N_end-N_start)*n
    N_array = np.linspace(N_start,N_end, N_end-N_start)
    root = np.sqrt(np.divide(N_array,np.multiply(n_array,(N_array-n_array))))
    float_power = np.divide(np.float_power(N_array,N_array),np.multiply(np.float_power(n_array,n_array),np.float_power(N_array-n_array,N_array-n_array)))
    multiplicity = 1/np.sqrt(2*pi)*np.multiply(root,float_power)
    return multiplicity

exact = exact_multiplicity(N_start, N_end, n)
stirling = stirling_multiplicity(N_start, N_end, n)

error = np.divide(stirling-exact,stirling)*100

answer1_1 = error
answer1_2a = np.where(error<0.5)[0][0]+1
answer1_2b = len(np.where(error<0.5)[0])

index = np.where(error>0)[0]+30
plt.subplot(111)
plt.plot(index, error)
plt.title('Stirling approximation percentage error')
plt.xlabel('number of coints (N)')
plt.ylabel('percentage error (%)')

#print("The percentage errors of the stirling approxiamtion are:", error)
print("From coin number "+str(answer1_2a)+" the error of Stirling's approximation is less than 0.5%.")
print("There are "+str(answer1_2b)+" coins above which the error satisfies the 0.5% criterion.")

def multiplicity_with_probability(n_start,n_end,N):
    N_array = np.ones(N+1)*N
    n_array = np.linspace(n_start,n_end,N+1)
    multiplicity = factorial(N_array)/(factorial(n_array)*factorial(N_array-n_array))
    return multiplicity

def probability(N, n, p):
    bin_coef = factorial(N)/(factorial(n)*factorial(N-n))
    probability = bin_coef*(p**n)*(1-p)**(N-n)
    return probability
    
p_fair = 0.5
p_unfair = 1.3/2.3     # Probability for obtaining heads is 1.3 times the probability for obtaining tails
N = 50
n = np.linspace(0,50,N+1)

fair = probability(N, n, p_fair)
unfair = probability(N, n, p_unfair)
#multiplicity = multiplicity_with_probability(0,50,N)

fig, ax = plt.subplots()
ax.plot(n, fair, label = 'Fair')
ax.plot(n, unfair, label = 'Unfair')
#ax.plot(n, multiplicity/np.max(multiplicity), label = 'Multiplicity')
#plt.axvline(25, 0, 1.2, ls = ':', alpha = 0.9)
plt.xlabel('Number of heads (n)')
plt.ylabel('Probability of heads')
plt.title('Probability of heads for fair and unfair coins')
plt.legend()

















