from matplotlib import pyplot as plt 
from abc import ABC, abstractmethod
import numpy as np
import math

from src.sin_signal import * 
#from src.impuls_ops import * 

class Signal_operations:

    def __init__(self, signal, obj, bins, f=1):
        self.signal = signal
        self.obj = obj
        self.f = f
        self.bins = bins
        self.x_values = []
        self.y_values = []
        self.values = []
        self.licz()
        self.wywolaj()

    def plik_zapisz(self, nazwa_pliku):
        plik = open(f'{nazwa_pliku}', 'w')
        plik.write(f'{self.signal} {self.obj.getFields()} {self.f}\n')
        #plik.write(f'{self.x_values} \n')
        plik.write(f'{self.y_values} \n')     

        #plik.write(f'{self.signal} {self.obj.getFields()}')
        plik.close()

    def n(self, t):
        return t * self.f
    
    def x(self, n):
        #sin = Sin_sygnal_wyp_jedno(self.A, self.T, self.t1, self.d)
        #return sin.signal(n)
        return self.obj.signal(n)

    def licz(self):
        self.x_values = np.arange(self.n(self.obj.t1), self.n(self.obj.t1 + self.obj.d), 0.05)
        y = []
        for i in np.arange(len(self.x_values)):
            y.append(round(self.x(self.x_values[i]), 2))
        self.y_values = y

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
        #x = np.arange(self.t1, self.t1 + self.d, 0.05)
        #print(f'{self.n(self.obj.t1)} {self.n(self.obj.t1 + self.obj.d)}')
        plt.subplot(1, 2, 1)
        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption")
        plt.plot(self.x_values, self.y_values) 
        plt.grid(True)
        plt.subplot(1, 2, 2)
        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption")
        plt.hist(self.values, self.bins, facecolor='blue', alpha=0.5)
        plt.grid(True)
        plt.show() 

    """
    def histogram(self):
        plt.hist(self.values, self.bins, facecolor='blue', alpha=0.5)
        plt.grid(True)
        plt.show()
    """

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

    def prezentuj(self):
        self.raport()
        self.wykres()
        #self.histogram()
    