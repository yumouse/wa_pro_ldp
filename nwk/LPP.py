# LPP
# Input: User ui's set of KV pairs Si   -> array(k,2)
#        Number of discretized levels k -> int
#        Privacy budgets e              -> float
# Output:LPP(Si,K,e) is the perturbed KV pair 
#        <Kj,vstar> of the j-th key     -> [j,Kj,vstar]
import random
import math
import numpy as np
import sys
sys.path.append('../src')
import gen
import Map

def LPP(Si,k,e):
    j = random.randint(0,k-1)
    if Si[j,0] != 0:
        if random.random() < (math.exp(e)/(1+math.exp(e))):
            [kj,vstar]  = [1,1]
        else:
            [kj,vstar]  = [0,0]
    else:
        if random.random() < (math.exp(e)/(1+math.exp(e))):
            [kj,vstar]  = [0,0]
        else:
            [kj,vstar]  = [1,1]
    return [j,kj,vstar]

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    e = float( sys.argv[3] )
    gene = gen.generator(u,k)
    data = gene.gen_new()
    S = [ Map.map(si,k) for si in data ]
    S = np.array(S)
    i = random.randint(0,u-1)
    Si = S[i,:,:]
    tmp = LPP(Si,k,e)
    print 'The original data for user %d is :' % i
    print Si
    print 'The perturbed data is:'
    Si[tmp[0]] = tmp[1:]
    print Si
