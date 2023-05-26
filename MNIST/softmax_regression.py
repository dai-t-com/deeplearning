# -*- coding = utf-8 -*-
# @Time:2023/5/26 21:05
# @Author: 蔡祎帆
# @File : softmax_regression.py
# @Software: PyCharm
# 导入TensorFlow
# 这句import tensorflow as tf是导入TensorFlow约定俗称的做法,请大家记住
import tensorflow as tf
# 导入MNIST教学的模块
from tensorflow.examples.tutorials.mnist import input_data
# 与之前一样,读入MNIST数据
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
# 创建x,x是一个占位符(placeholder),代表待识别的图片
x = tf.placeholder(tf.float32, [None, 784])
# W是Softmax模型的参数,将一个784维的输入转换为一个10维的输出
# 在TensorFlow中,模型的参数用tf.Variable表示
W = tf.Variable(tf.zeros([784, 10]))
# b是又一个Softmax模型的参数,一般叫作"偏置项"(bias)
b = tf.Variable(tf.zeros([10]))

# y表示模型的输出
y = tf.nn.softmax(tf.matmul(x,W)+b)
# y_是实际的图像标签,同样以占位符表示
y_ = tf.placeholder(tf.float32,[None,10])

# 至此，得到了两个重要的Tesnor:y和y_
# y是模型的输出,y_实际的图像标签，注意y_是独热表示的
# 下面会根据y和y_构造损失

#根据y和y_构造交叉熵损失
cross_entropy = \
    tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y)))
# 有了损失,就可以用梯度下降法针对模型的参数(W和b)进行优化
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 创建一个Session