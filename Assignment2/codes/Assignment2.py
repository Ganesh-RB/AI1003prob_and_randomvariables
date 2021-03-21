import matplotlib.pyplot as plt
from operator import add
from random import randint
import numpy as np

#simulen no of times event occuring
simulen=int(1e7)

#x1 and X2 outcomes of two dices 
z=0
X1=[]
X2=[]
while(z<simulen):
  X1.append(randint(1,6))
  X2.append(randint(1,6))
  z=z+1

#X is random variable representing sum of outcomes of two dices
X=list(map(add,X1,X2))

#Theorotical mean calculation
x_n=[2,3,4,5,6,7,8,9,10,11,12]
pr_x_thr=[1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36]
mean_thr=0

for i in range(0,11):
  mean_thr += x_n[i]*pr_x_thr[i]


#simulation 
pr_x_sim=[0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,simulen):
  pr_x_sim[X[i]-2] += 1

for i in x_n:
  pr_x_sim[i-2] /=simulen

mean_sim=np.mean(X)

#graph
plt.plot(x_n,pr_x_thr,'g:',label='Theorotical')
plt.stem(x_n,pr_x_sim,linefmt='C4-',markerfmt='C0o',use_line_collection=True,label='Simulation')
plt.xlabel("$X$")
plt.ylabel("Pr($X=n$)")
plt.legend()
plt.title("Comparision between theorotical vs simulation values")
plt.show()

#theorotical vs simulation
print("Theorotical expectation value is : ",mean_thr)
print("through simulation expectation value is : ",mean_sim)