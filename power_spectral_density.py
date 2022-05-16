import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

#delta time
delta_time = 1/10000000
final_time = 1/10000
time = np.arange(0, final_time, delta_time)

f1 = 200000
f2 = 400000

signal = 10 * np.sin(2 * np.pi * time * f1) + 100 * np.cos(2 * np.pi * time * f2)

plt.subplot(211)
plt.plot(time, signal)
plt.subplot(212)
plt.psd(signal, 512, 1 / delta_time)

plt.show()