# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

bits = np.random.randint(2, size=10)

print(bits)

bits2 = np.random.randint(-2, 3, size=10)

print(bits2)

noise_length = 10000

#el 2 es la varianza
noise = np.random.normal(0,2,noise_length)

#print(noise)

test = [1, 2, 5]

print(test)

test_squared = np.sum(np.square(test))

print(test_squared)

noise_squared_sum = np.sum(np.square(noise))

print(noise_squared_sum)

noise_power = noise_squared_sum / noise_length

#la potencia es la varianza al cuadrado
print(noise_power)