import random

simulen=int(1e6)
X=[[] for j in range(0,4)]

for j in range(0,4):
  X[j] = random.sample([-1,1], 1)
  for i in range(0,simulen):
    X[j].append(random.sample([-1,1], 1)[0])

Y=[(X[0][i]+X[1][i]+X[2][i]+X[3][i])**(4) for i in range(0,simulen)]

sum=0
for i in range(0,simulen):
  sum+=Y[i]

print("expectation value of E(X1+x2+X3+X4)^4 is :",sum/simulen)