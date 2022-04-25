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


#Vector de bits (0, 1) de longitud 10
#limite superior es el 2 (sin incluir al 2)
#el limite ingerior es cero por defecto y le incluye al cero
bits0 = np.random.randint(2, size=10)
print(bits0)

#Vector de simnolos (0, 1, 2, 3) de longitud 20
#limite superior es el 4 (sin incluir al 4)
#el limite ingerior es cero por defecto y le incluye al cero
bits1 = np.random.randint(4, size=20)
print(bits1)


#Vector de simnolos (-2, -1, 0, 1, 2) de longitud 10
#limite superior es el 3 (sin incluir al 3)
#limite inferior es el-2 (incluye al -2)
bits2 = np.random.randint(-2, 3, size=10)
print(bits2)


#longitud del vector de ruido
noise_length = 10000

#Distribucion normal con media 0 y desviacion 2
#con noise_length cantidad de elementos
noise = np.random.normal(0,2,noise_length)

"""
test = [1, 2, 5]

test_squared = np.sum(np.square(test))

print(test_squared)

"""
#suma de los cuadrados del vector de ruido
noise_squared_sum = np.sum(np.square(noise))

print(noise_squared_sum)

#densidad de potencia de ruido
noise_power = noise_squared_sum / noise_length

print(noise_power)
