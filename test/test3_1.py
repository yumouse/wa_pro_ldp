# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# c = 10 fixed
# test u and k for RE and log(MSE)

REList = []
MSEList = []
cList = []
color = ['green','blue','skyblue','hotpink','red','olive','yellow',]
colorPos = 0

for e in [0.1,0.2,0.4,0.8,1.6]:
	REList = []
	cList = []
	for c in range(1,40,2):
		temp1 = []
		temp2 = []
		for i in range(3):
			command = 'python ../code/PrivKVM.py 400 30 ' + str(e) + ' ' + str(c)
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
			temp1.append(float(result[0].split('\n')[-4]))
		print(c)
		count = 0
		for i in range(len(temp1)):
			if np.isnan(temp1[i]):
				count += 1
			else:
				temp2.append(temp1[i])
		if count == 3:
			REList.append(REList[-1])
		else:
			REList.append(sum(temp2)/len(temp2))
		cList.append(c)
	x = np.array(cList)
	yRE = np.array(REList)
	parameterRE = np.polyfit(x, yRE, 4)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos],label='e='+str(e))	
	colorPos += 1

plt.title('Graph of RE and iterations in LDP [user=400/k=30]')
plt.xlabel('# of iterations')
plt.ylabel('RE')
plt.legend()
plt.show()