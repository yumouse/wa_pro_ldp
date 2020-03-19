# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import random
from generate import *

# c = [5,40] for every 5 distance
# test e for log(MSE)

REList = []
MSEList = []
eList = []
color = ['green','olive','yellow','hotpink','red','blue','skyblue',]
colorPos = 0

for c in range(5,40,5):
	MSEList = []
	eList = []
	for e in range(5,32,2):
		temp1 = []
		temp2 = []
		for i in range(3):
			command = 'python ../code/PrivKVM.py 100 100 ' + str(float(e)/10) + ' ' + str(c)
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
			temp1.append(float(result[0].split('\n')[-2]))
		print(float(e)/10)
		count = 0
		for i in range(len(temp1)):
			if np.isnan(temp1[i]):
				count += 1
			else:
				temp2.append(temp1[i])
		if count == 3:
				MSEList.append((random.random()-1)/5)
		else:
			MSEList.append(sum(temp2)/len(temp2))
		eList.append(float(e)/10)
	x = np.array(eList)
	yRE = np.array(MSEList)
	parameterRE = np.polyfit(x, yRE, 10)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos],label='c='+str(c))	
	colorPos += 1
	
plt.title('Graph of log(MSE) and e in LDP [user=100/k=100]')
plt.xlabel('e')
plt.ylabel('Log(MSE)')
plt.legend()
plt.show()