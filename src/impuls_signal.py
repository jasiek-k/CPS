import numpy as np


# impuls jednostkowy
class Impuls_jedno:

    def __init__(self, A, n1, ns, l, f):
        self.A = A
        self.n1 = n1
        self.ns = ns
        self.l = l
        self.f = f

    def x(self, n):
        if n == 0:
            return 1
        else:
            return 0
    
    def signal(self, n):
        return self.A * self.x(n - self.ns)


# szum impulsowy
class Szum_impuls:

    def __init__(self, A, t1, d, f, p):
        self.A = A
        self.t1 = t1
        self.d = d
        self.f = f
        self.p = p

    