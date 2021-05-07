import numpy as np
import matplotlib.pyplot as plt
from random import randint
from operator import add


simulen =int(1e5)
N=[2,5,10,20]

X=[[] for i in range(0,20)]

for k in range(0,simulen):
  for i in range(0,20):
    X[i].append(randint(1,6))

for n in N:
  Z=X[0]
  for l in range(1,n):
    Z=list(map(add,Z,X[l]))

  k=range(n,6*n+1)
  count=[0 for j in range(n,6*n+1)]
  for i in range(0,simulen):
    count[Z[i]-n]+=1

  for j in range(n,6*n+1):
    count[j-n]/=simulen

  plt.bar(k,count,color='C6')
  plt.plot(k,count,'C4',lw=3)
  plt.ylabel(r'Pr($X=k$)')
  plt.xlabel(r'k')
  plt.title("n="+str(n))
  plt.show()
