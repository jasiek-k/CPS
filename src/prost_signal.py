import numpy as np


class Prost_sygnal:

    def __init__(self, A, T, t1, d, kw):
        self.A = A
        self.T = T
        self.t1 = t1
        self.d = d
        self.kw = kw

    def signal(self, t):
        k: int = 0
        check: bool = False
        while check == False:
            x0 = self.kw * self.T + k * self.T + self.t1
            x1 = k * self.T + self.t1
            #print(f"{t} {x0} {x1}")
            if x1 <= t < x0: 
                check = True
                return self.A
            elif x0 <= t < x1 + self.T:
                check = True
                return 0
            else:
                k = k + 1
           

class Prost_sygnal_sym(Prost_sygnal):

    def signal(self, t):
        k: int = 0
        check: bool = False
        while check == False:
            x0 = self.kw * self.T + k * self.T + self.t1
            x1 = k * self.T + self.t1
            #print(f"{t} {x0} {x1}")
            if x1 <= t < x0: 
                check = True
                return self.A
            elif x0 <= t < x1 + self.T:
                check = True
                return (-1) * self.A
            else:
                k = k + 1
