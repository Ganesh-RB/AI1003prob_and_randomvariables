import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

simulen = int(1e6)
points=100

mean=[0,0,0,-2]
var=[0.2,1,5.0,0.5]

n=np.arange(-5,5,10/points)
Xn=[[(norm.pdf(n[i],loc=mean[j],scale=var[j]**(0.5))) for i in range(0,points)] for j in range(0,4)]

plt.plot(n,Xn[0],'C0-',label=r"$\mu=$"+str(mean[0])+r"$,\sigma^2=$"+str(var[0]))
plt.plot(n,Xn[1],'C3-',label=r"$\mu=$"+str(mean[1])+r"$,\sigma^2=$"+str(var[1]),lw=2.5)
plt.plot(n,Xn[2],'C6-',label=r"$\mu=$"+str(mean[2])+r"$,\sigma^2=$"+str(var[2]))
plt.plot(n,Xn[3],'C2-',label=r"$\mu=$"+str(mean[3])+r"$,\sigma^2=$"+str(var[3]))

plt.legend()
plt.grid()
plt.ylabel(r"${\varphi_{\mu,\sigma^2}(x)}$")
plt.xlabel(r"$X$")
plt.show()
