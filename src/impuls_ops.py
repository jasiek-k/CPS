from matplotlib import pyplot as plt 
import numpy as np

from src.impuls_signal import * 


class Impuls_operations:

    def __init__(self, obj, bins):
        self.obj = obj
        self.bins = bins
         
    def t(self, n):
        return n / self.obj.f

    def x(self, n):
        return self.obj.signal(n)

    def wykres(self):
        x = np.arange(self.t(self.obj.n1), self.t(self.obj.n1 + self.obj.l), (1 / self.obj.f))
        y = []
    
        for i in np.arange(len(x)):
            y.append(self.x(x[i]))

        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption") 
        plt.scatter(x, y, 10) 
        plt.grid(True)
        plt.show() 

    def histogram(self):
        x = [self.srednia(), self.srednia_bezwgl(), self.moc_srednia(), self.wariancja(), self.wart_skut()]
        plt.hist(x, self.bins, facecolor='blue', alpha=0.5)
        plt.grid(True)
        plt.show()
    
    def srednia(self):
        sum = 0 
        for i in range(self.obj.n1, self.obj.n1 + self.obj.l):
            sum += self.x(i)
        return (1/(self.obj.l + 1)) * sum 

    def srednia_bezwgl(self):
        sum = 0 
        for i in range(self.obj.n1, self.obj.n1 + self.obj.l):
            sum += np.fabs(self.x(i))
        return (1/(self.obj.l + 1)) * sum 

    def moc_srednia(self):
        sum = 0 
        for i in range(self.obj.n1, self.obj.n1 + self.obj.l):
            sum += self.x(i) * self.x(i)
        return (1/(self.obj.l + 1)) * sum 

    def wariancja(self):
        sum = 0 
        for i in range(self.obj.n1, self.obj.n1 + self.obj.l):
            sum += np.power((self.x(i) - self.srednia()), 2)
            #print(f"{sum} {i}")
        return (1/(self.obj.l + 1)) * sum 
    
    def wart_skut(self):
        return np.sqrt(self.moc_srednia())
