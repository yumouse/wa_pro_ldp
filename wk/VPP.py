# Algorithm 2 Value Perturbation Primitive
# Input:    Value v of a KV pair        -> float
#           Privacy budget epsilon      -> float
# Output:   VPP(v,e) is the perturbed value vstar   -> float
import random
import math
def VPP(v,e):
    # step 1 Discretization
    if random.random() < (1+v)/2:
        vstar = 1
    else:
        vstar = -1
    # step 1 Perturbation
    if random.random() < (math.exp(e)/(1+math.exp(e))):
        vstar = vstar
    else:
        vstar = -vstar
    # Return
    return vstar

if __name__ == '__main__':
    v = random.random()*2-1
    e = random.random()
    print "v is %f and epsilon is %f" %  (v,e)
    vstar = VPP(v,e)
    print "vstar is %f" % vstar
