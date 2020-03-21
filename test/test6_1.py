# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("../code")
sys.path.append('../src')
import gen
from PrivKVMplus import PrivKVMplus
from PrivKVM import PrivKVM

MSEList = []
userList = []
cList = []
color = ['green','olive','skyblue','hotpink','red','blue','yellow',]
k = 30
e = 0.4
iter = 5

for user in range(10, 1010, 20):
    S = np.array(gen.generator(user, k).gen())
    K = []
    for index in range(k):
        K.append('tmp')

    result = PrivKVM(S, K, e, 6)
    ori_mean = (np.sum(S[:, :, 1], axis=0)) / (np.sum(S[:, :, 0], axis=0))
    dealt = ori_mean - result[1]
    dealt_clean = dealt[~np.isnan(dealt)]
    mse = np.log(np.sum(np.power(dealt_clean, 2)) * (1.0 / len(dealt_clean)))
    MSEList.append(mse)
    userList.append(user)

x1 = np.array(userList)
y1 = np.array(MSEList)
parameter1 = np.polyfit(x1, y1, 3)
func1 = np.poly1d(parameter1)

plt.plot(x1, func1(x1), color=color[1], label='PrivKVM-6')

userList = []
MSEList = []
for user in range(10, 1010, 20):
    S = np.array(gen.generator(user, k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    print(user)
    result = PrivKVMplus(S, K, e, 0.2)
    ori_mean = (np.sum(S[:, :, 1], axis=0)) / (np.sum(S[:, :, 0], axis=0))
    dealt = ori_mean - result[1]
    dealt_clean = dealt[~np.isnan(dealt)]
    mse = np.log(np.sum(np.power(dealt_clean, 2)) * (1.0 / len(dealt_clean)))
    MSEList.append(mse)
    userList.append(user)

x2 = np.array(userList)
y2 = np.array(MSEList)
parameter2 = np.polyfit(x2, y2, 3)
func2 = np.poly1d(parameter2)
plt.plot(x2, func2(x2), color=color[2], label='PrivKVM+')


userList = []
MSEList = []

for user in range(10, 1010, 20):
    S = np.array(gen.generator(user, k).gen())
    K = []
    for index in range(k):
        K.append('tmp')

    result = PrivKVM(S, K, e, 3)
    ori_mean = (np.sum(S[:, :, 1], axis=0)) / (np.sum(S[:, :, 0], axis=0))
    dealt = ori_mean - result[1]
    dealt_clean = dealt[~np.isnan(dealt)]
    mse = np.log(np.sum(np.power(dealt_clean, 2)) * (1.0 / len(dealt_clean)))
    MSEList.append(mse)
    userList.append(user)

x3 = np.array(userList)
y3 = np.array(MSEList)
parameter3 = np.polyfit(x3, y3, 3)
func3 = np.poly1d(parameter3)

plt.plot(x3, func3(x3), color=color[3], label='PrivKVM-3')

plt.title('Graph of Log(MSE)  and the number of users in PrivKVM+')
plt.xlabel('The number of users')
plt.ylabel('Log(MSE)')
plt.legend()
plt.show()