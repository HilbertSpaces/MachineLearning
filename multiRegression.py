import numpy as np
inputs1=input().split()
numObs=int(inputs1[0])
population=int(inputs1[1])
X=[]
Y=[]
for i in range(population):
    inputs=input().split()
    X.append([float(m) for m in inputs[:-1]])
    X[i].insert(0,1)
    Y.append([float(inputs[-1])])
X=np.matrix(X)
Y=np.matrix(Y)
Xt=np.transpose(X)
XX=Xt*X
XXinv=np.linalg.inv(XX)
XXt=XXinv*Xt
b=XXt*Y
dataLength=int(input())
data=[]
ones=[]
for j in range(dataLength):
    inputs=input().split()
    data.append([float(m) for m in inputs])
    ones.append([1])
data=np.matrix(data)
ones=np.matrix(ones)
b0=ones*b[0]
Yhat=b0+data*b[1:]
for j in range(dataLength):
    print(Yhat.item(j))
