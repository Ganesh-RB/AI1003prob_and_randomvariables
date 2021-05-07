import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
k=range(0,20)

Xn=[poisson.pmf(k,mu=i) for i in range(1,4)]

plt.plot(k,Xn[0],'o',mec='black')
plt.plot(k,Xn[0],'-')
plt.plot(k,Xn[1],'o',mec='black')
plt.plot(k,Xn[1],'-')
plt.plot(k,Xn[2],'o',mec='black')
plt.plot(k,Xn[2],'-')

plt.show()