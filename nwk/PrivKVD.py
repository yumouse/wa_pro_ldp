# PrivKVD
# Input:      All users' levels S = {S1,S2,...,Sn}
#             Number of discretized levels k
#             privacy budget epsilon
# Output:     Frequency vector fstar
 
import math
import sys
sys.path.append('../src')
import gen
import Map
import LPP
import numpy as np

def PrivKVD(S,k,e):
    # User-side map
    nS = np.array([ Map.map(si,k) for si in S])
    clt_S = np.zeros(nS.shape)
    # User-side perturbation
    num = np.zeros(k)
    for i in range(nS.shape[0]):
        tmp = LPP.LPP(nS[i,:,:],k,e)
        j = tmp[0]
        num[j] = num[j]+1
        pair = tmp[1:]
        clt_S[i,j,:] = pair

    fstar = []
    for i in range(k):
        # calculates frequency fkstar
        fkstar = np.sum(clt_S[:,i,0],axis=0)/num[i]
        # Calibrates the frequency
        p = 1.0*math.exp(e)/(math.exp(e)+1)
        fkstar = (p - 1 + fkstar)/(2*p-1)
        fstar.append(fkstar)

    return fstar

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    e = float( sys.argv[3] )
    S = gen.generator(u,k).gen_new()
    fstar = PrivKVD(S,k,e)
    ori_fre = []
    for i in range(k):
        num = len([x for x in S if x== i ])
        fre = num*1.0/u
        ori_fre.append(fre)
    # ori_fre = [ len([x for x in S if x==i])*1.0/u for i in range(k) ]
    ori_fre = np.array(ori_fre)
    fstar = np.array(fstar)

    # If we dont calibrates again
    print 'The frequency vector for original data is:'
    print ori_fre
    print 'The frequency vector after is:'
    print fstar
    print 'The error rate is for frequency estimation(RE)'
    print np.median((np.abs(ori_fre-fstar))/ori_fre)

    # If we add calibrates once again
    print '----Add normalization-----'
    tmp = np.sum(fstar)
    fstar = fstar/tmp
    print 'The frequency vector for original data is:'
    print ori_fre
    print 'The frequency vector after is:'
    print fstar
    print 'The error rate is for frequency estimation(RE)'
    print np.median((np.abs(ori_fre-fstar))/ori_fre)

