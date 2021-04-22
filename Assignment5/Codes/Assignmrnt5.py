import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson,norm
from scipy.integrate import quad
from IPython.display import display, Math, Latex

simulen = int(1e4)
n=int(1e6)
X_n=list(poisson.rvs(mu=n**2,size=simulen))
count=[0,0,0,0]

for j in range(0,simulen):
   if(X_n[j]>(n+1)**2):
     count[0]+=1
   if(X_n[j]<=(n+1)**2):
     count[1]+=1
   if(X_n[j]<(n-1)**2):
     count[2]+=1
   if(X_n[j]<(n-2)**2):
     count[3]+=1


display(Math(r"\text{A)}\lim \limits_{n \to \infty} \text{Pr}(X_n>(n+1)^2) = "+str(round(count[0]/simulen,4))))
display(Math(r"\text{B)}\lim \limits_{n \to \infty} \text{Pr}(X_n \leqslant(n+1)^2) = "+str(round(count[1]/simulen,4))))
display(Math(r"\text{C)}\lim \limits_{n \to \infty} \text{Pr}(X_n<(n-1)^2) = "+str(round(count[2]/simulen,4))))
display(Math(r"\text{D)}\lim \limits_{n \to \infty} \text{Pr}(X_n<(n-2)^2) = "+str(round(count[3]/simulen,8))))

def integrand(x):
  return ((np.e)**(-x*x/2))/((2*np.pi)**(0.5))
ans,err=quad(integrand,2,np.infty)

display(Math(r"\frac{1}{\sqrt{2 \pi}} \int \limits_{2}^{\infty} e^{-x^2/2} = "+str(round(ans,4))))

print("Therefore Option (A) and (C) is correct")