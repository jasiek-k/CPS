import numpy as np
import random

# impuls jednostkowy
class Impuls_jedno:

    def __init__(self, A, n1, ns, l, f):
        self.A = A
        self.n1 = n1
        self.ns = ns
        self.l = l
        self.f = f

    def x(self, n):
        if int(n) == 0:
            return 1
        else:
            return 0
    
    def signal(self, n):
        return self.A * self.x(n - self.ns)

    def getFields(self):
        return f'{self.A} {self.n1} {self.ns} {self.l} {self.f}'


# szum impulsowy
class Szum_impuls:

    def __init__(self, A, t1, d, f, p):
        self.A = A
        self.t1 = t1
        self.d = d
        self.f = f
        self.p = p

    def getFields(self):
        return f'{self.A} {self.t1} {self.d} {self.f} {self.p}'


# szum o rozkładzie jednostajnym
class Szum_jedno:

    def __init__(self, A, t1, d):
        self.A = A
        self.t1 = t1
        self.d = d

    def getFields(self):
        return f'{self.A} {self.t1} {self.d}'
    
    def signal(self, t):
        t = random.randint((-1) * self.A, self.A-1)
        return t 

    
# szum gaussowski
class Szum_gauss:

    def __init__(self, A, t1, d):
        self.A = A
        self.t1 = t1
        self.d = d

    def getFields(self):
        return f'{self.A} {self.t1} {self.d}'

    def signal(self, t):
        t = self.A * random.gauss(0, 1)
        #t = random.gauss(0, 1)
        return t