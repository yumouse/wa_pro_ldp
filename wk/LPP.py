# Algorithm 3 Local Perturbation Protocol
# Input: User ui's set of KV pairs Si   -> array(k,2)
#        The set of keys K              -> list(k)
#        Privacy budgets e1 and e2      -> float
# Output:LPP(Si,K,e1,e2) is the perturbed KV pair 
#        <Kj,vstar> of the j-th key     -> array(3,) <j,Kj,vstar>
import random
import math
import VPP
import numpy as np
import sys
sys.path.append('../src')
import gen

def LPP(Si,K,e1,e2):
    d = len(K)
    j = random.randint(0,d-1)
    if Si[j,0] != 0:
        vstar = VPP.VPP(Si[j,1],e2)
        if random.random() < (math.exp(e1)/(1+math.exp(e1))):
            kj = 1
        else:
            kj = 0
            vstar = 0
    else:
        m_ = random.random()*2-1
        vstar = VPP.VPP(m_,e2)
        if random.random() < (math.exp(e1)/(1+math.exp(e1))):
            kj = 0
            vstar = 0
        else:
            kj = 1
    return np.array([j,kj,vstar])

if __name__ == '__main__':
    gene = gen.generator(10,3)
    data = np.array(gene.gen())
    i = random.randint(0,9)
    Si = data[i,:,:]
    K = ['qq','vx','tb']
    e1 = random.random()
    e2 = random.random()
    tmp = LPP(Si,K,e1,e2)
    print 'The original data for user %d is :' % i
    print Si
    print 'The perturbed data is:'
    Si[tmp[0],:] = tmp[1:]
    print Si
