import numpy as np
data_train = np.random.randn(2000,2,3)
print(data_train.shape)
np.random.shuffle(data_train)
batch_size = 100
for i in range(0,len(data_train),batch_size):
    x_batch_sum = np.sum(data_train[i:i+batch_size])
    print("第{}批次，该批次的数据之和，{}".format(i,x_batch_sum))