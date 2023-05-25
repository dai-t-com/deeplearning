import time
import math
import numpy as np

x = [1*0.001 for i in np.arange(1000000)]
tic = time.time()
for i,t in enumerate(x):
    x[i] = math.sin(t)
toc = time.time()
print("math.sin:",toc-tic)
x = [1*0.001 for i in np.arange(1000000)]
x = np.array(x)
tic = time.time()
np.sin(x)
toc = time.time()
print("numpy.sin:",toc-tic)