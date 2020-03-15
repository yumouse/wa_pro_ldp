# Algorithm 1 Decomposition of Harmony
# Input: User ui'sset of values V [-1,1]d   -> array(k,)
#        Privacy budget epsilon             -> float
# Output: Perturbed set of values Vstar     -> array(k,)
import sys
sys.path.append('../src')
import gen
import random
import math
import numpy as np

# V-> User Ui's set of values
# e-> epsilon
def dof(V,e):
    # step 1
    Vstar = np.zeros(V.shape)
    # step 2
    j = random.randint(0,len(V)-1)
    v = V[j]
    # step 3 Discretization
    if random.random() < (1+v)/2:
        vstar = 1
    else:
        vstar = -1
    # step 4 Pertubation
    if random.random() < (math.exp(e)/(1+math.exp(e))):
        vstar = vstar
    else:
        vstar = -vstar
    # step 5 Calibration
    vstar = vstar * ((math.exp(e)+1)/(math.exp(e)-1)) * len(V)
    # step 6
    Vstar[j] = vstar
    # step 7
    return Vstar

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    epsilon = float(sys.argv[3])
    tmpdata = gen.generator(u,k).gen()
    ary = np.array(tmpdata)
    # print ary.shape
    index = random.randint(0,9)
    V = ary[index,:,1]
    print V.shape
    Vstar = dof(V,epsilon)
    print Vstar

