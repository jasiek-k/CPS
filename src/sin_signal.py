import numpy as np


#sygnał sinusoidalny
class Sin_sygnal:

    def __init__(self, A, T, t1, d):
        self.A = A
        self.T = T
        self.t1 = t1
        self.d = d

    def signal(self, t):
        return self.A * np.sin((2 * np.pi) / self.T * (t - self.t1))

    def getFields(self):
        return f'{self.A} {self.T} {self.t1} {self.d}'

#sygnał sinusoidalny wyprostowany jednopołówkowo
class Sin_sygnal_wyp_jedno(Sin_sygnal):

    def signal(self, t):
        return 0.5 * self.A * (np.sin(((2 * np.pi) / self.T) * (t - self.t1)) + np.fabs(np.sin(((2 * np.pi) / self.T) * (t - self.t1))))


#sygnał sinusoidalny wyprostowany dwupołówkowo
class Sin_sygnal_wyp_dwu(Sin_sygnal):

    def signal(self, t):
        return self.A * np.fabs(np.sin(((2 * np.pi) / self.T) * (t - self.t1)))







