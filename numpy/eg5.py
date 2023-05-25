import numpy as np
nd5 = np.zeros([3,3])
nd6 = np.ones([3,3])

nd7 = np.eye(4)

nd8 = np.diag([1,8,3,10])
print("nd5=\n",nd5)
print("nd6=\n",nd6)
print("nd7=\n",nd7)
print("nd8=\n",nd8)

nd9 = np.random.random([3,5])
np.savetxt(X=nd9,fname='./data.txt')
nd10 = np.loadtxt('./data.txt')
print(nd10)

print(np.arange(10))
print(np.arange(0,10))
print(np.arange(1,4,0.5))
print(np.arange(9,-1,-1))

