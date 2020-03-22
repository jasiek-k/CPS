from matplotlib import pyplot as plt 
import numpy as np
import math


class Impuls_operations:

    def __init__(self, signal, obj, bins):
        self.signal = signal
        self.obj = obj
        self.bins = bins
        self.x_values = []
        self.y_values = []
        self.values = []

    def plik_zapisz(self, nazwa_pliku):
        plik = open(f'{nazwa_pliku}', 'w')
        plik.write(f'{self.signal} {self.obj.getFields()} {self.bins}\n')
        plik.write(f'{self.y_values} \n')     
        plik.close()

    def setYs(self, y_array):
        self.y_values = y_array
        self.x_values = np.arange(self.t(self.obj.n1), self.t(self.obj.n1 + self.obj.l), (1 / self.obj.f))
        self.wywolaj()

    def t(self, n):
        return n / self.obj.f

    def x(self, n):
        return self.obj.signal(n)

    def licz(self):
        self.x_values = np.arange(self.t(self.obj.n1), self.t(self.obj.n1 + self.obj.l), (1 / self.obj.f))
        y = []
        for i in np.arange(len(self.x_values)):
            y.append(self.x(self.x_values[i]))
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
        plt.subplot(1, 2, 1)
        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("t[s]") 
        plt.ylabel("A")
        plt.scatter(self.x_values, self.y_values, 10) 
        plt.grid(True)
        plt.subplot(1, 2, 2)
        plt.title("Histogram") 
        plt.xlabel("A") 
        plt.ylabel("Liczba wystąpień")
        plt.hist(self.y_values, self.bins, range = (math.floor(min(self.y_values)), math.ceil(max(self.y_values))), facecolor = 'blue', alpha = 0.5)
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

    def prezentuj(self):
            self.raport()
            self.wykres()
            #self.histogram()

    