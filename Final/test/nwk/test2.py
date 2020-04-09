# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np

REList = []
MSEList = []
eList = []
color = ['green','red','yellow','hotpink','olive','blue','skyblue',]
colorPos = 0

e = 0.8
k = 5
colorPos = 0
labels = ['non-normalization','normalization']
for content in labels:
	res = []
	uList = []
	for u in range(10000,400000,10000):
		command = 'python PrivKVD.py ' + str(u) + ' ' + str(k) + ' ' + str(float(e))
		result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		if content == 'non-normalization':
			res.append(float(result[0].split('\n')[5]))
		else:
			res.append(float(result[0].split('\n')[12]))
		uList.append(u)
		print(u)
	x = np.array(uList)
	yRE = np.array(res)
	parameterRE = np.polyfit(x, yRE, 6)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos], label=content)	
	colorPos += 1
	
plt.title('Graph of RE and u in LDP [e=0.8/k=5]')
plt.xlabel('u')
plt.ylabel('RE')
plt.legend()
plt.show()