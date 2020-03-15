# Algorithm 4 PrivKV
# Input: All users' sets of KV pairs S = { S1,...,Sn}   -> array(u,k,2)
#        The set of keys K                              -> list(k)
#        Privacy budgets e1 and e2                      -> float
# Output:Frequency vector fstar                         -> list(k)
#        Mean vector mstar                              -> list(k)
#                                                       -> [[],[]]
import random
import math
import LPP
import numpy as np
import sys
sys.path.append('../src')
import gen


def PrivKV(S,K,e1,e2):
    clt_S = np.zeros(S.shape)
    # User-side perturbation
    for i in range(S.shape[0]):
        tmp = LPP.LPP(S[i,:,:],K,e1,e2)
        j = tmp[0]
        pair = tmp[1:2]
        # give index j and <kj,v*> to data collector
        clt_S[i,j,:] = pair
    # Collector-side calibration
    fstar = []
    mstar = []
    for k in range(len(K)):
        # calculates frequency fkstar
        fkstar = np.sum(clt_S[:,k,0],axis=0)
        # calibrates the frequency
        p = math.exp(e1)/(math.exp(e1)+1)
        fkstar = (p - 1 + fkstar)/(2*p-1)
        fstar.append(fkstar)
        # Counts 1 and -1 in the set of values
        n1p = np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==1]),axis=0)
        n2p = np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==-1]),axis=0)
        N = n1p + n2p
        # Calibrates the counts
        p = math.exp(e2)/(math.exp(e2)+1)
        n1star = ((p-1)*N+n1p)/(2*p-1)
        n2star = ((p-1)*N+n2p)/(2*p-1)
        # Clip n1* to [0,N]
        if n1star >= N:
            n1star = N
        elif n1star <=0:
            n1star = 0
        # Clip n2* to [0,N]
        if n2star >= N:
            n2star = N
        elif n2star <=0:
            n2star = 0
        # Calibrates mean mk*
        mkstar = (n1star-n2star)/N
        mstar.append(mkstar)
    return  [fstar,mstar]

if __name__ == '__main__':
    S = np.array(gen.generator(10,3).gen())
    K = ['qq','vx','tb']
    e1 = random.random()
    e2 = random.random()
    vec = PrivKV(S,K,e1,e2)
    print 'The frequency vector is:'
    print vec[0]
    print 'The Mean vector is:'
    print vec[1]
