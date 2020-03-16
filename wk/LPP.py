# Algorithm 3 Local Perturbation Protocol
# Input: User ui's set of KV pairs Si   -> array(k,2)
#        The set of keys K              -> list(k)
#        Privacy budgets e1 and e2      -> float
# Output:LPP(Si,K,e1,e2) is the perturbed KV pair 
#        <Kj,vstar> of the j-th key     -> [j,Kj,vstar]
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
    return [j,kj,vstar]

def LPPp(Si,K,e1,e2,vstar_list):
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
        # m_ = random.random()*2-1
        # vstar = VPP.VPP(m_,e2)
        # this random discretization is replaced
        vstar = vstar_list[j]
        if random.random() < (math.exp(e1)/(1+math.exp(e1))):
            kj = 0
            vstar = 0
        else:
            kj = 1
    return [j,kj,vstar]

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    e1 = float( sys.argv[3] )
    e2 = float( sys.argv[4] )
    gene = gen.generator(u,k)
    data = np.array(gene.gen())
    i = random.randint(0,u-1)
    Si = data[i,:,:]
    K = []
    for index in range(k):
        K.append('tmp')
    tmp = LPP(Si,K,e1,e2)
    print 'The original data for user %d is :' % i
    print Si
    print 'The perturbed data is:'
    Si[tmp[0],:] = tmp[1:]
    print Si
