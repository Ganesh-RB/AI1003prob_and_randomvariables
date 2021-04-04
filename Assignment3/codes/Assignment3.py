import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,bernoulli,uniform
from operator import add
 
#function to assign +1 and -1 to variables for given probability of success
def fun_bern_new(p_success,size_list):
  X=bernoulli.rvs(p=p_success,size=simulen)
  for i in range(0,simulen):
    if (X[i]==0):
      X[i]=-1
  return X
 
#size
simulen=int(1e5)
var=7

#X
X=fun_bern_new(0.75,simulen)
 
#Z
Z=[[] for i in range(0,var)]
for i in range(0,var):
  Z[i]=list(norm.rvs(loc=0,scale=np.sqrt((i-3)**2),size=simulen))

#y
Y=[list(map(add,X,Z[i])) for i in range(0,var)]

#tau
tau=np.arange(-5,5,0.1)
 
#
X_hat=[0 for i in range(0,simulen)]
pr_error=[[0 for j in range(0,100)] for k in range(0,var)]

for k in range(0,var):
  for j in range(0,100): 
    count=0
    for i in range(0,simulen):    #assigning values to X_hat
      if Y[k][i]>tau[j]:
        X_hat[i]=1
      else:
        X_hat[i]=-1

    for l in range(0,simulen):    #finding pr_error
      if(X[l]!=X_hat[l]):
        pr_error[k][j]+=1
    pr_error[k][j]/=simulen


#for plot of sigma**2 vs tau_min  

pr_min_error = [np.min(pr_error[k]) for k in range(0,var)]  #minimum error from all values of tau for given sigma
tau_csp=[0 for k in range(0,var)]
sigma=[(k-3) for k in range(0,var)]
sigma_cont=np.arange(-3,3,0.05)
tau_csp_th=[-(sigma_cont[k]**2)*np.log(3)/2 for k in range(0,120)]

for k in range(0,var):
  for j in range(0,100) :
    if(pr_min_error[k]==pr_error[k][j]):
      tau_csp[k]=tau[j]


#plot
plt.plot(tau,pr_error[4],label="$\sigma^2=1$")
plt.plot(tau_csp[4],pr_min_error[4],'k.')
plt.text(tau_csp[4],pr_min_error[4],' ('+str(round(tau_csp[4],1))+" , "+str(round(pr_min_error[4],2))+' )')

plt.plot(tau,pr_error[5],label="$\sigma^2=4$")
plt.plot(tau_csp[5],pr_min_error[5],'k.')
plt.text(tau_csp[5],pr_min_error[5],' ('+str(round(tau_csp[5],1))+" , "+str(round(pr_min_error[5],2))+' )')

plt.plot(tau,pr_error[6],'C4-',label="$\sigma^2=9$")
plt.plot(tau_csp[6],pr_min_error[6],'k.')
plt.text(tau_csp[6],pr_min_error[6],' ('+str(round(tau_csp[6],1))+" , "+str(round(pr_min_error[6],2))+' )')

plt.xlabel(r'$\tau$')
plt.ylabel(r"Pr$(\hat{X} \neq X)$")
plt.legend()
plt.show()


sigma.pop(3)
tau_csp.pop(3)
plt.plot(sigma,tau_csp,'D',label=r"simulation")
plt.plot(sigma_cont,tau_csp_th,':',label="Theoritical")
plt.xlabel(r"$\sigma$")
plt.ylabel(r"$\mathbf{\tau}$" + "\n corrosponding to minimum probability of error")
plt.legend()
plt.show()