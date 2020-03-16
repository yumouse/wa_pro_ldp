# Algorithm 5 PrivKVM: Iterative PrivKV
# Input:      All users' sets of KV pairs S = {S1,...,Sn}   -> array(u,k,2)
#             The set of keys K                             -> list(k)
#             Privacy budget epsilon                        -> float
#             Number of iterations c                        -> int
# Output:     Frequency vector f_1                          -> list(k)
#             Mean vector m_c                               -> list(k)
#                                                           -> [[],[]]
import numpy as np
import PrivKV
import random
import sys
sys.path.append('../src')
import gen


def PBA(e,c):
    e1 = e2 = e/2
    eps = np.random.random((2,c))
    for i in range(c):
        if i == 0:
            eps[:,i] = np.array([e1,e2/c])
        else:
            eps[:,i] = np.array([0,e2/c])
    # return array(2,c)
    return eps

def discretization(Para):
    vstar = []
    for v in Para:
        if random.random() < (1.1+v)/2:
            vstar.append(1.0)
        else:
            vstar.append(-1.0)
    return vstar


def PrivKVM(S,K,e,c):
    # allocate privacy budget:
    eps = PBA(e,c)
    # calculate frequency and mean in the first iteration:
    m_ = []
    # print 'Debug %f %f' % (eps[0,0],eps[1,0])
    [f_1,m_1] = PrivKV.PrivKV(S,K,eps[0,0],eps[1,0])
    m_.append(m_1)
    # collector sends back v* = discretization(m_1) to each user
    vstar = discretization(m_1)
    for r in range(1,c):
        # Calculate mean
        # print 'Debug %d' % len(vstar)
        m_tmp = PrivKV.PrivKVp(S,K,eps[0,r],eps[1,r],vstar)
        m_.append(m_tmp)
        # Collector sends back vstar
        vstar = discretization(m_tmp)
    return [f_1,m_[c-1]]


if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    e = float( sys.argv[3] )
    c = int( sys.argv[4] )
    S = np.array(gen.generator(u,k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    vec = PrivKVM(S,K,e,c)
    print 'The frequency vector is:'
    print vec[0]
    print 'The Mean vector is:'
    print vec[1]
