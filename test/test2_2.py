# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# c = 10 fixed
# test u and k for RE and log(MSE)

REList = []
MSEList = []
kList = []
color = ['green','blue','skyblue','hotpink','red','olive','yellow',]
colorPos = 0

for e in [0.1,0.2,0.4,0.8]:
	REList = []
	kList = []
	for k in range(10,200,10):
		temp1 = []
		temp2 = []
		for i in range(3):
			command = 'python ../code/PrivKVM.py 1000 ' + str(k) + ' ' + str(e) +' 10'
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
			temp1.append(float(result[0].split('\n')[-4]))
		print(k)
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
		kList.append(k)
	print(REList)
	x = np.array(kList)
	yRE = np.array(REList)
	parameterRE = np.polyfit(x, yRE, 4)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos],label='e='+str(e))	
	colorPos += 1

plt.title('Graph of RE and k in LDP [c=10/user=1000]')
plt.xlabel('k')
plt.ylabel('RE')
plt.legend()
plt.show()