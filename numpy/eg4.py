import numpy as np
list = [1,2,3,4,5]
np.random.shuffle(list)
print(list)

arr = np.arange(12).reshape(3,4)
print(arr)
np.random.shuffle(arr)
print(arr)
np.random.permutation(list)
print(list)
arr2 = np.arange(9).reshape(3,3)
print(arr2)

print(np.random.permutation(arr2))