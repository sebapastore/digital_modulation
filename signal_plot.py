#https://stackoverflow.com/questions/14058340/adding-noise-to-a-signal-in-python

# Signal Generation
# matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import math

#ejemplo de un vector de 11 elementos que empieza en cero y termina en 100
t = np.linspace(0, 100, 11)
print(t)

def linspace_with_step(start, stop, step):
    elements = math.ceil((stop - start) / step) + 1
    return np.linspace(start, stop, elements)

t = linspace_with_step(0, 10, 2)
print(t)


t = np.linspace(1, 100, 1000)
x_volts = 10*np.sin(t/(2*np.pi))
#Grafico con 3 filas, 1 columna, el primer grafico va a la fila 1
plt.subplot(3,1,1)
plt.plot(t, x_volts)
plt.title('Signal')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')

x_watts = x_volts ** 2
#Grafico con 3 filas, 1 columna, el primer grafico va a la fila 2
plt.subplot(3,1,2)
plt.plot(t, x_watts)
plt.title('Signal Power')
plt.ylabel('Power (W)')
plt.xlabel('Time (s)')

x_db = 10 * np.log10(x_watts)
#Grafico con 3 filas, 1 columna, el primer grafico va a la fila 3
plt.subplot(3,1,3)
plt.plot(t, x_db)
plt.title('Signal Power in dB')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')
plt.show()
