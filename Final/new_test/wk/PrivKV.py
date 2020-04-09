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
    tmp_de = []
    num = np.zeros(len(K))
    for i in range(S.shape[0]):
        tmp = LPP.LPP(S[i,:,:],K,e1,e2)
        j = tmp[0]
        num[j] = num[j]+1
        pair = tmp[1:]
        # give index j and <kj,v*> to data collector
        clt_S[i,j,:] = pair
        tmp_de.append(tmp[2])
    # print 'Debug:'
    # print '1-> %d  -1 -> %d ' % (len([x for x in tmp_de if x == 1]),len([x for x in tmp_de if x==-1]))
    # print clt_S
    # Collector-side calibration
    fstar = []
    mstar = []
    for k in range(len(K)):
        # calculates frequency fkstar
        fkstar = np.sum(clt_S[:,k,0],axis=0)/num[k]
        # print '1->fk*=%f' %fkstar
        # calibrates the frequency
        p = 1.0*math.exp(e1)/(math.exp(e1)+1)
        # print 'p=%f' % p
        fkstar = (p - 1 + fkstar)/(2*p-1)
        # print '2->fk*=%f' % fkstar
        fstar.append(fkstar)
        # Counts 1 and -1 in the set of values
        n1p = np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==1]),axis=0)
        n2p = -np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==-1]),axis=0)
        N = n1p + n2p
        # print '---------------------'
        # print 'n1p = %d n2p = %d N=%d' % (n1p,n2p,N)
        # Calibrates the counts
        p = math.exp(e2)/(math.exp(e2)+1)
        n1star = ((p-1)*N+n1p)/(2*p-1)
        n2star = ((p-1)*N+n2p)/(2*p-1)
        # print 'n1*= %d n2*=%d ' % ( n1star,n2star )
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
        # print 'After: n1*= %d n2*=%d ' % ( n1star,n2star )
        mkstar = (n1star-n2star)/N
        mstar.append(mkstar)
    return  [fstar,mstar]

def PrivKVp(S,K,e1,e2,vstar):
    clt_S = np.zeros(S.shape)
    # print len([x for x in vstar if x != 0]) 
    # print vstar
    # User-side perturbation
    num = np.zeros(len(K))
    for i in range(S.shape[0]):
        tmp = LPP.LPPp(S[i,:,:],K,e1,e2,vstar)
        # print tmp
        j = tmp[0]
        num[j] = num[j]+1
        pair = tmp[1:]
        # give index j and <kj,v*> to data collector
        clt_S[i,j,:] = pair
    # print 'Debug: 1-> %d -1 -> %d' % (len([x for x in vstar if x == 1]),len([x for x in vstar if x == -1]) )
    # print clt_S
    # Collector-side calibration
    mstar = []
    for k in range(len(K)):
        # Counts 1 and -1 in the set of values
        n1p = np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==1]),axis=0)
        n2p = -np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==-1]),axis=0)
        N = n1p + n2p
        # print '---------------------'
        # print '%f   %f ' % (e1,e2)
        # print 'n1p = %d n2p = %d N=%d' % (n1p,n2p,N)
        # Calibrates the counts
        p = math.exp(e2)/(math.exp(e2)+1)
        # print 'p is %f' % p
        n1star = ((p-1)*N+n1p)/(2*p-1)
        n2star = ((p-1)*N+n2p)/(2*p-1)
        # print 'n1*= %d n2*=%d ' % ( n1star,n2star )
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
        # print 'After: n1*= %d n2*=%d ' % ( n1star,n2star )
        mkstar = (n1star-n2star)/N
        mstar.append(mkstar)
    return  mstar

def PrivKVp_2o(S,K,e1,e2,vstar):
    clt_S = np.zeros(S.shape)
    # User-side perturbation
    num = np.zeros(len(K))
    for i in range(S.shape[0]):
        tmp = LPP.LPPp(S[i,:,:],K,e1,e2,vstar)
        # print tmp
        j = tmp[0]
        num[j] = num[j]+1
        pair = tmp[1:]
        # give index j and <kj,v*> to data collector
        clt_S[i,j,:] = pair
    # print clt_S
    # Collector-side calibration
    fstar = []
    mstar = []
    for k in range(len(K)):
        # calculates frequency fkstar
        fkstar = np.sum(clt_S[:,k,0],axis=0)/num[k]
        # print '1->fk*=%f' %fkstar
        # calibrates the frequency
        p = 1.0*math.exp(e1)/(math.exp(e1)+1)
        # print 'p=%f' % p
        fkstar = (p - 1 + fkstar)/(2*p-1)
        # print '2->fk*=%f' % fkstar
        fstar.append(fkstar)
        # Counts 1 and -1 in the set of values
        n1p = np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==1]),axis=0)
        n2p = -np.sum(np.array([x for x in (clt_S[:,k,1].tolist()) if x==-1]),axis=0)
        N = n1p + n2p
        # print '---------------------'
        # print 'n1p = %d n2p = %d N=%d' % (n1p,n2p,N)
        # Calibrates the counts
        p = math.exp(e2)/(math.exp(e2)+1)
        n1star = ((p-1)*N+n1p)/(2*p-1)
        n2star = ((p-1)*N+n2p)/(2*p-1)
        # print 'n1*= %d n2*=%d ' % ( n1star,n2star )
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
        # print 'After: n1*= %d n2*=%d ' % ( n1star,n2star )
        mkstar = (n1star-n2star)/N
        mstar.append(mkstar)
    return  [fstar,mstar]

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    e1 = float( sys.argv[3] )
    e2 = float( sys.argv[4] )
    S = np.array(gen.generator(u,k).gen())
    K = []
    for index in range(k):
        K.append('tmp')
    vec = PrivKV(S,K,e1,e2)
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
