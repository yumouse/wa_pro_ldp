# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("../code")
sys.path.append('../src')
import gen
from PrivKVMplus import PrivKVMplus
from PrivKVM import PrivKVM

# test privacy budget for total cost
user = 400
k = 30
iter = 10

eList = np.linspace(0.1,3.3,11)
color = ['green','olive','skyblue','hotpink','red','blue','yellow',]
CostList_6 = []
CostList_3 = []
CostList_plus = []
# prikvm c = 6
for e in eList:

    S = np.array(gen.generator(user, k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    sum = 0
    for i in range(iter):
        result = PrivKVM(S, K, e, 6)
        sum += result[2]
    sum /= iter

    CostList_6.append(sum)

x_p6 = np.array(eList)
y_p6 = np.array(CostList_6)
plt.scatter(x_p6,y_p6)
plt.plot(x_p6, y_p6, color=color[0],label='PriKVM-6')

# prikvm c = 3
for e in eList:

    S = np.array(gen.generator(user, k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    sum = 0
    for i in range(iter):
        result = PrivKVM(S, K, e, 3)
        sum += result[2]
    sum /= iter

    CostList_3.append(sum)

x_p3 = np.array(eList)
y_p3 = np.array(CostList_3)
plt.scatter(x_p3, y_p3)
plt.plot(x_p3, y_p3, color=color[1], label='PrivKVM-3')

# prikvm plus
for e in eList:

    S = np.array(gen.generator(user, k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    sum = 0
    for i in range(iter):
        result = PrivKVMplus(S, K, e, 0.02)
        sum += result[2]
    sum /= iter

    CostList_plus.append(sum)

x_plus = np.array(eList)
y_plus = np.array(CostList_plus)
plt.scatter(x_plus, y_plus)
plt.plot(x_plus, y_plus, color=color[2], label='PrivKVM+')

plt.title('Graph of total cost')
plt.xlabel('e')
plt.ylabel('Total cost')
plt.legend()
plt.show()