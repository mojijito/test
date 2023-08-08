import numpy as np
from matplotlib import pyplot as plt

x_c = 10000
lgt = 5
N = 20
rmd = 0.3

x = np.linspace(0,lgt,x_c)
A = 1/np.sqrt(N)
sta = np.arange(0,2*np.pi*(N-1)/N,2*np.pi/N)
phy = 2*np.pi*np.random.rand(N)

wave = np.zeros((x_c),dtype=complex)

for i in range(x_c):
    for k in range(N):
        wave[i] += A*np.exp(1j*((2*np.pi*x[i]*np.cos(sta[k-1])/rmd) + sta[k-1]))

pwr = 20*np.log10(np.abs(wave))

plt.plot(x,pwr)
plt.show()


