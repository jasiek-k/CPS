import numpy as np


# sygnał trójkątny
class Troj_sygnal:

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

            if x1 <= t < x0: 
                check = True
                return (self.A / (self.kw * self.T)) * (t - k * self.T - self.t1) 
            elif x0 <= t < x1 + self.T:
                check = True
                return (((-1) * self.A / (self.T * (1 - self.kw))) * (t - k * self.T - self.t1)) + (self.A / (1 - self.kw))
            else:
                k = k + 1