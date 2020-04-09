# Map
# Input:    User ui's level Si
#           Number of discretized levels k
# Output:   KV pairs Si'

import sys
sys.path.append('../src')
import gen

def map(si,k):
    index = si
    sip = [ [0,0] if i != index else [1,1] for i in range(k) ]
    return sip

if __name__ == '__main__':
    u = int( sys.argv[1] )
    k = int( sys.argv[2] )
    tmpdata = gen.generator(u,k).gen_new()
    print tmpdata
    S = [ map(si,k) for si in tmpdata ]
    print S
