# Algorithm 6 PrivKVM+: Adaptive PrivKVM
# Input:  All users' sets of KV pairs S = {S1,...,Sn}   -> array(u,k,2)
#         The set of keys K                             -> list(k)
#         Privacy budget epsilon                        -> float
#         Communication cost of one iteration A0
# Output: Frequency vector fstar                        -> list(k)
#         Mean vector mstar                             -> list(k)
#                                                       -> [[],[]]
import numpy as np
import PrivKV
import random
import sys
sys.path.append('../src')
import gen

def PBAt(e):
    scale = 10      # like super parameter
    t = random.randint(3,scale)
    return [1.0/t,1.0/t]

def discretization(Para):
    vstar = []
    for v in Para:
        if random.random() < (1.1+v)/2:
            vstar.append(1.0)
        else:
            vstar.append(-1.0)
    return vstar

def PrivKVMplus(S,K,e,A0):
    # Allocate privacy budget
    [e1,e2] = PBAt(e)
    mb = [ 1 for n in range(len(K))]
    vstar = discretization(mb)
    [fstar,mstar] = PrivKV.PrivKVp_2o(S,K,e1,e2,vstar)
    # Calculate the bias
    Fstar = A0 - 1.0/len(K)*np.sum(np.abs(np.array(mstar)-np.array(mb)))
    while Fstar < 0:
        vstar = discretization(mstar)
        mb = mstar
        [e1,e2] = PBAt(e-e1-e2)
        mstar = PrivKV.PrivKVp(S,K,e1,e2,vstar)
        Fstar = A0 - 1.0/len(K)*np.sum(np.abs(np.array(mstar)-np.array(mb)))
    return [fstar,mstar]

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    e = float( sys.argv[3] )
    A0 = float( sys.argv[4] )
    S = np.array(gen.generator(u,k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    vec = PrivKVMplus(S,K,e,A0)
    # Calcualate the original data
    ori_fre =  (np.sum(S[:,:,0],axis=0))/u
    ori_mean =  (np.sum(S[:,:,1],axis=0))/(np.sum(S[:,:,0],axis=0))
    print 'The frequency vector for original data is:'
    print ori_fre
    print 'The Mean vector for original data is:'
    print ori_mean
    print 'The frequency vector after is:'
    print vec[0]
    print 'The Mean vector after is:'
    print vec[1]
    print 'The error rate is for frequency estimation(RE)'
    print np.median((np.abs(ori_fre-vec[0]))/ori_fre)
    print 'The error rate is for mean estimation(log(MSE))'
    print np.log(np.sum((1.0/len(K))*np.power((ori_mean-vec[1]),2)) )
