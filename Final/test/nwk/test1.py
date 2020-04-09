# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
import numpy as np

REList = []
MSEList = []
eList = []
color = ['green','red','yellow','hotpink','olive','blue','skyblue',]
colorPos = 0

u = 800000
k = 5
colorPos = 0
labels = ['non-normalization','normalization']
for content in labels:
	res = []
	eList = []
	for e in range(1,20):
		command = 'python PrivKVD.py ' + str(u) + ' ' + str(k) + ' ' + str(float(e)/100)
		result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		if content == 'non-normalization':
			res.append(float(result[0].split('\n')[5]))
		else:
			res.append(float(result[0].split('\n')[12]))
		eList.append(float(e)/100)
		print(float(e)/100)
	x = np.array(eList)
	yRE = np.array(res)
	parameterRE = np.polyfit(x, yRE, 8)
	pRE = np.poly1d(parameterRE)
	plt.scatter(x,yRE)
	plt.plot(x, pRE(x), color=color[colorPos], label=content)	
	colorPos += 1
	
plt.title('Graph of RE and e in LDP [u=8x10^6/k=5]')
plt.xlabel('e')
plt.ylabel('RE')
plt.legend()
plt.show()