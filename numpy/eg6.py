import numpy as np
np.random.seed(2019)
nd1 = np.random.random([10])
print(nd1[3])
print(nd1[3:6])
print(nd1[1:6:2])

from numpy import random as nr
a = np.arange(1,25,dtype=float)
c1 = nr.choice(a,size=(3,4))
c2 = nr.choice(a,size=(3,4),replace=False)
c3 = nr.choice(a,size=(3,4),p=a/np.sum(a))
print("随机可重复抽取")
print(c1)
print("随机但不重复抽取")
print(c2)
print(c3)

X =np.random.rand(2,3)
def softmod(x):
    return 1/(1+np.exp(-x))
