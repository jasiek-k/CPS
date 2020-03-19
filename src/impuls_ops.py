from matplotlib import pyplot as plt 
import numpy as np

from src.impuls import * 


class Impuls_operations:

    def __init__(self, A, n1, ns, l, f):
        self.A = A
        self.n1 = n1
        self.ns = ns
        self.l = l
        self.f = f

    def t(self, n):
        return n / self.f

    def x(self, n):
        imp = Impuls_jedno(self.A, self.n1, self.ns, self.l, self.f)
        return imp.signal(self.t(n))

    def wykres(self):
        x = np.arange(self.t(self.n1), self.t(self.n1 + self.l), 0.5)
        y = []

        for i in np.arange(len(x)):
            y.append(self.x(x[i]))

        #plt.title("Matplotlib demo") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption") 
        plt.scatter(x, y, 0.5) 
        plt.show() 
    """
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
    """
    