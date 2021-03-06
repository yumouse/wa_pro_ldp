import random

class generator:
    ''' PrimKV Data generator '''

    def __init__(self, n, k, sd=-1, P=0.7):
        self.n=n
        self.k=k
        self.P=P
        if sd!=-1:
            self.sd=sd
            random.seed(sd)
        self.state=random.getstate()

    def gen(self):
        ''' returns a list in shape (n,k,2) '''
        random.setstate(self.state)
        x=[[([1,random.random()*2-1] if random.random()<self.P else [0,0])
                    for i in range(self.k)] for i in range(self.n)]
        self.state=random.getstate()
        return x
