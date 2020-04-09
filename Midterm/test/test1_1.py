# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from generate import *

# c = [5,40] for every 5 distance
# test e for RE

REList = []
MSEList = []
eList = []
color = ['green','olive','yellow','hotpink','red','blue','skyblue',]
colorPos = 0

for c in range(5,40,5):
	REList = []
	eList = []
	for e in range(5,40,3):
		temp1 = []
		for i in range(3):
			command = 'python ../code/PrivKVM.py 100 100 ' + str(float(e)/100) + ' ' + str(c)
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
			temp1.append(float(result[0].split('\n')[-4]))
		print(float(e)/100)
		REList.append(sum(temp1)/3)
		eList.append(float(e)/100)
	x = np.array(eList)
	yRE = np.array(REList)
	parameterRE = np.polyfit(x, yRE, 4)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos],label='c='+str(c))	
	colorPos += 1
	
plt.title('Graph of RE and e in LDP [user=100/k=100]')
plt.xlabel('e')
plt.ylabel('RE')
plt.legend()
plt.show()