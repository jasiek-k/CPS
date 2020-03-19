from matplotlib import pyplot as plt 
import numpy as np

from src.sin_signal import * 
from src.impuls_ops import * 

class Signal_operations:

    def __init__(self, f, A, T, t1, d):
        self.f = f
        self.A = A
        self.T = T
        self.t1 = t1
        self.d = d

    def n(self, t):
        return t * self.f

    def x(self, n):
        sin = Sin_sygnal(self.A, self.T, self.t1, self.d)
        return sin.signal(n)

    def x_left(self, n):
        sin = Sin_sygnal(self.A, self.T, self.t1, self.d)
        return sin.signal(n)

    def x_right(self, n):
        imp = Impuls_jedno(self.A, self.n(self.t1), 0, self.d, self.f)
        return imp.signal(n)
    
    def mnozenie(self, n):
        return self.x_left(n) * self.x_right(n)

    def wykres(self):
        x = np.arange(self.t1, self.t1 + self.d, 0.05)
        y = []

        for i in np.arange(len(x)):
            y.append(self.mnozenie(x[i]))

        #plt.title("Matplotlib demo") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption") 
        plt.plot(x, y) 
        plt.show() 

    def srednia(self):
        sum = 0 
        for i in range(self.n(self.t1), self.n(self.t1 + self.d)):
            sum += self.x(i)
            #print(f"{sum} {i}")
        return (1/(self.n(self.t1 + self.d) - self.n(self.t1) + 1)) * sum 

    def srednia_bezwgl(self):
        sum = 0 
        for i in range(self.n(self.t1), self.n(self.t1 + self.d)):
            sum += np.fabs(self.x(i))
            #print(f"{sum} {i}")
        return (1/(self.n(self.t1 + self.d) - self.n(self.t1) + 1)) * sum

    def moc_srednia(self):
        sum = 0 
        for i in range(self.n(self.t1), self.n(self.t1 + self.d)):
            sum += self.x(i) * self.x(i)
            #print(f"{sum} {i}")
        return (1/(self.n(self.t1 + self.d) - self.n(self.t1) + 1)) * sum

    def wariancja(self):
        sum = 0 
        for i in range(self.n(self.t1), self.n(self.t1 + self.d)):
            sum += np.power(self.x(i) - self.srednia(), 2)
            #print(f"{sum} {i}")
        return (1/(self.n(self.t1 + self.d) - self.n(self.t1) + 1)) * sum

    def wart_skut(self):
        return np.sqrt(self.moc_srednia())

    