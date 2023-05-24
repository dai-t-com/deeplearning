# -*- coding = utf-8 -*-
# @Time:2023/5/24 22:05
# @Author: 蔡祎帆
# @File : download.py
# @Software: PyCharm
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
print(mnist.train.images.shape)
print(mnist.train.labels.shape)