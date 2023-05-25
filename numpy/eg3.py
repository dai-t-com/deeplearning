import numpy as np

nd3 = np.random.random([4,3])
print(nd3)
print("nd3的形状为:",nd3.shape)
np.random.rand(5)
np.random.rand(2,3)
np.random.randn(5)
np.random.randn(2,3)

np.random.standard_normal(2)
np.random.standard_normal((2,3))

np.random.randint(2)
np.random.randint(2,size=5)
np.random.randint(2,6)
np.random.randint(2,6,size=5)

np.random.randint(2,size=(2,3))
np.random.randint(2,6,(2,3))

