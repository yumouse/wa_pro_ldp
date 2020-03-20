# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# c = 10 fixed
# test u and k for RE and log(MSE)

REList = []
MSEList = []
cList = []
color = ['green','olive','skyblue','hotpink','red','blue','yellow',]
colorPos = 0

for e in [0.1,0.2,0.4,0.8,1.6]:
	MSEList = []
	cList = []
	for c in range(1,16):
		temp1 = []
		temp2 = []
		for i in range(10):
			command = 'python ../code/PrivKVM.py 400 30 ' + str(e) + ' ' + str(c)
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
			temp1.append(float(result[0].split('\n')[-2]))
		print(c)
		count = 0
		for i in range(len(temp1)):
			if np.isnan(temp1[i]):
				count += 1
			else:
				temp2.append(temp1[i])
		if count == 10:
			MSEList.append(MSEList[-1])
		else:
			MSEList.append(sum(temp2)/len(temp2))
		cList.append(c)
	x = np.array(cList)
	yRE = np.array(MSEList)
	parameterRE = np.polyfit(x, yRE, 5)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos],label='e='+str(e))	
	colorPos += 1

plt.title('Graph of log(MSE) and iterations in LDP [user=100/k=100]')
plt.xlabel('# of iterations')
plt.ylabel('Log(MSE)')
plt.legend()
plt.show()