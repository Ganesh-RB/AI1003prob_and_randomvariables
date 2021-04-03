import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,bernoulli,uniform
from operator import add

#function to assign +1 and -1 to variables for given probability of success
def fun_bern(p_success,size_list):
  X=bernoulli.rvs(p=p_success,size=simulen)
  for i in range(0,simulen):
    if (X[i]==0):
      X[i]=-1
  return X

#size
simulen=int(1e6)

#X
X=fun_bern(0.75,simulen)

#Z
Z1=list(norm.rvs(loc=0,scale=1,size=simulen))
Z2=list(norm.rvs(loc=0,scale=2,size=simulen))
Z3=list(norm.rvs(loc=0,scale=3,size=simulen))
Z=[Z1,Z2,Z3]
#print(Z)

#y
Y=[list(map(add,X,Z[0])),list(map(add,X,Z[1])),list(map(add,X,Z[2]))]

tau=np.arange(-5,5,0.1)

#data simulation
pr_X_hat=[[0 for j in range(0,100)] for k in range(0,3)]
for k in range(0,3):
  for j in range(0,100):
    count=0
    for i in range(0,simulen):
      if Y[k][i]>tau[j]:
        count+=1
    X_hat=fun_bern(count/simulen,simulen)
    for l in range(0,simulen):
      if(X[l]!=X_hat[l]):
        pr_X_hat[k][j]+=1
    pr_X_hat[k][j]/=simulen



plt.plot([0,0],[0.2,0.8])
plt.plot(tau,pr_X_hat[0],label="$\sigma^2=1$")
plt.plot(tau,pr_X_hat[1],label="$\sigma^2=4$")
plt.plot(tau,pr_X_hat[2],label="$\sigma^2=9$")
plt.xlabel(r'$\tau$')
plt.ylabel(r"Pr$(\hat{X} \neq X)$")
plt.legend()
plt.title(r"Plot to show Pr$(\hat X \neq X)$ is minimum at negative value of $\tau $ "+'\n'+" for all nonzero values of $\sigma^2$ " )
plt.show()