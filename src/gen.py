import random
import numpy as np

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
        ''' returns a list in shape (n,) '''
        random.setstate(self.state)
        x=[ random.randint(1,self.k-1) if random.random()<self.P else 0
                     for i in range(self.n)]
        self.state=random.getstate()
        return x
    
    def rand(self):
        mean = random.random()
        sig = random.randint(1,10)
        x = np.random.normal(mean,sig,size=(1,))
        if x[0] > 1:
            x[0] = 1.0
        elif x[0] < -1:
            x[0] = -1.0
        return x[0]
