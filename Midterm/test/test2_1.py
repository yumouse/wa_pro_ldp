# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from generate import *

# c = 10 fixed
# test u and k for RE and log(MSE)

REList = []
MSEList = []
userList = []
color = ['green','blue','skyblue','hotpink','red','olive','yellow',]
colorPos = 0

for e in [0.1,0.2,0.4,0.8]:
	REList = []
	userList = []
	for userNumber in range(10,1010,50):
		temp1 = []
		for i in range(3):
			command = 'python ../code/PrivKVM.py ' + str(userNumber) + ' 3 ' + str(e) +' 10'
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
			temp1.append(float(result[0].split('\n')[-4]))
		print(str(userNumber))
		REList.append(sum(temp1)/3)
		userList.append(userNumber)
	x = np.array(userList)
	yRE = np.array(REList)
	parameterRE = np.polyfit(x, yRE, 4)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos],label='e='+str(e))	
	colorPos += 1

plt.title('Graph of RE and the number of users in LDP [c=10/k=3]')
plt.xlabel('the number of users')
plt.ylabel('RE')
plt.legend()
plt.show()