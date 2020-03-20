from matplotlib import pyplot as plt 
from abc import ABC, abstractmethod
import numpy as np

from src.sin_signal import * 
#from src.impuls_ops import * 

class Signal_operations:

    def __init__(self, obj, bins, f=1):
        self.obj = obj
        self.f = f
        self.bins = bins

    def n(self, t):
        return t * self.f
    
    def x(self, n):
        #sin = Sin_sygnal_wyp_jedno(self.A, self.T, self.t1, self.d)
        #return sin.signal(n)
        return self.obj.signal(n)
        
    def wykres(self):
        x = np.arange(self.n(self.obj.t1), self.n(self.obj.t1 + self.obj.d), 0.05)
        #x = np.arange(self.t1, self.t1 + self.d, 0.05)
        print(f'{self.n(self.obj.t1)} {self.n(self.obj.t1 + self.obj.d)}')
        y = []

        for i in np.arange(len(x)):
            y.append(self.x(x[i]))

        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption") 
        plt.plot(x, y) 
        plt.grid(True)
        plt.show() 

    def histogram(self):
        x = [self.srednia(), self.srednia_bezwgl(), self.moc_srednia(), self.wariancja(), self.wart_skut()]
        plt.hist(x, self.bins, facecolor='blue', alpha=0.5)
        plt.grid(True)
        plt.show()

    def srednia(self):
        sum = 0 
        for i in range(self.n(self.obj.t1), self.n(self.obj.t1 + self.obj.d)):
            sum += self.x(i)
            #print(f"{sum} {i}")
        return (1/(self.n(self.obj.t1 + self.obj.d) - self.n(self.obj.t1) + 1)) * sum 

    def srednia_bezwgl(self):
        sum = 0 
        for i in range(self.n(self.obj.t1), self.n(self.obj.t1 + self.obj.d)):
            sum += np.fabs(self.x(i))
            #print(f"{sum} {i}")
        return (1/(self.n(self.obj.t1 + self.obj.d) - self.n(self.obj.t1) + 1)) * sum

    def moc_srednia(self):
        sum = 0 
        for i in range(self.n(self.obj.t1), self.n(self.obj.t1 + self.obj.d)):
            sum += self.x(i) * self.x(i)
            #print(f"{sum} {i}")
        return (1/(self.n(self.obj.t1 + self.obj.d) - self.n(self.obj.t1) + 1)) * sum

    def wariancja(self):
        sum = 0 
        for i in range(self.n(self.obj.t1), self.n(self.obj.t1 + self.obj.d)):
            sum += np.power(self.x(i) - self.srednia(), 2)
            #print(f"{sum} {i}")
        return (1/(self.n(self.obj.t1 + self.obj.d) - self.n(self.obj.t1) + 1)) * sum

    def wart_skut(self):
        return np.sqrt(self.moc_srednia())

    