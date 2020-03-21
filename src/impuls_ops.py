from matplotlib import pyplot as plt 
import numpy as np
import math

from src.impuls_signal import * 


class Impuls_operations:

    def __init__(self, signal, obj, bins):
        self.signal = signal
        self.obj = obj
        self.bins = bins
        self.x_values = []
        self.y_values = []
        self.values = []
        self.licz()
        self.wywolaj()

    def setYs(self, y_array):
        self.y_values = y_array
        self.x_values = np.arange(self.t(self.obj.n1), self.t(self.obj.n1 + self.obj.l), (1 / self.obj.f))

         
    def t(self, n):
        return n / self.obj.f

    def x(self, n):
        return self.obj.signal(n)

    def licz(self):
        self.x_values = np.arange(self.t(self.obj.n1), self.t(self.obj.n1 + self.obj.l), (1 / self.obj.f))
        y = []
        for i in np.arange(len(self.x_values)):
            y.append(self.x(self.x_values[i]))
        self.y_values = round(y, 2)
    
    def wywolaj(self):
        values = []
        values.append(self.srednia())
        values.append(self.srednia_bezwgl())
        values.append(self.moc_srednia())
        values.append(self.wariancja())
        values.append(self.wart_skut())
        self.values = values

    def raport(self):
        print(f"Średnia: {self.values[0]}")
        print(f"Średnia bezwzgledna: {self.values[1]}")
        print(f"Moc średnia: {self.values[2]}")
        print(f"Wariancja: {self.values[3]}")
        print(f"Wartość skuteczna: {self.values[4]}")

    def wykres(self):
        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption") 
        plt.scatter(self.x_values, self.y_values, 10) 
        plt.grid(True)
        plt.show() 

    """
    def histogram(self):
        #x = [self.srednia(), self.srednia_bezwgl(), self.moc_srednia(), self.wariancja(), self.wart_skut()]
        plt.hist(self.values, self.bins, facecolor='blue', alpha=0.5)
        plt.grid(True)
        plt.show()
    """

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

    def prezentuj(self):
            self.raport()
            self.wykres()
            #self.histogram()

    