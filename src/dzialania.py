from matplotlib import pyplot as plt 
import numpy as np


class Dzialania:

    def __init__(self, obj1, obj2, f, string_copy):
        self.obj1 = obj1
        self.obj2 = obj2
        self.string_copy = string_copy
        self.f = f
        self.n1 = 0
        self.n2 = 0
        self.przedzial1 = []
        self.przedzial2 = []
        self.x_values = []
        self.y_values = []
        self.ustaw_przedzial()

    def plik_zapisz(self, nazwa_pliku):
        plik = open(f'{nazwa_pliku}', 'w')
        plik.write(f'{self.string_copy} \n') 
        plik.write(f'{self.y_values}')    
        plik.close()

    def print(self):
        print(self.n1)
        print(self.n2)
        print(f'{self.przedzial1[0]} {self.przedzial1[1]}')
        print(f'{self.przedzial2[0]} {self.przedzial2[1]}')

    def ustaw_przedzial(self):
        if self.obj1.obj.signal == "S10":
            start1 = self.obj1.obj.n1
            end1 = self.obj1.obj.n1 + self.obj1.obj.l
            self.przedzial1 = [start1, end1]
        else:
            start1 = self.obj1.obj.t1
            end1 = self.obj1.obj.t1 + self.obj1.obj.d
            self.przedzial1 = [start1, end1]

        if self.obj2.obj.signal == "S10":
            start2 = self.obj2.obj.n1
            end2 = self.obj2.obj.n1 + self.obj2.obj.l
            self.przedzial2 = [start2, end2]

        else:
            start2 = self.obj2.obj.t1
            end2 = self.obj2.obj.t1 + self.obj2.obj.d
            self.przedzial2 = [start2, end2] 

        if start1 < start2:
            self.n1 = start1
        else:
            self.n1 = start2

        if end1 < end2:
            self.n2 = end2
        else:
            self.n2 = end1

    def dodaj(self):
        x_values = np.arange(self.n1, self.n2, (1 / self.f))
        y_values = []

        for i in np.arange(len(x_values)):
            if self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and self.przedzial2[0] <= x_values[i] <= self.przedzial2[1]:
                value = self.obj1.obj.signal(x_values[i]) + self.obj2.obj.signal(x_values[i])
                y_values.append(value)
            elif self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and (self.przedzial2[0] > x_values[i] or x_values[i] > self.przedzial2[1]):
                value = self.obj1.obj.signal(x_values[i]) 
                y_values.append(value)
            else:
                value = self.obj2.obj.signal(x_values[i])
                y_values.append(value)

        self.x_values = x_values
        self.y_values = y_values
        print(x_values)
        print(y_values)


    def odejmij(self):
        x_values = np.arange(self.n1, self.n2, (1 / self.f))
        y_values = []

        for i in np.arange(len(x_values)):
            if self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and self.przedzial2[0] <= x_values[i] <= self.przedzial2[1]:
                value = self.obj1.obj.signal(x_values[i]) - self.obj2.obj.signal(x_values[i])
                y_values.append(value)
            elif self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and (self.przedzial2[0] > x_values[i] or x_values[i] > self.przedzial2[1]):
                value = self.obj1.obj.signal(x_values[i]) 
                y_values.append(value)
            else:
                value = self.obj2.obj.signal(x_values[i])
                y_values.append(value)

        self.x_values = x_values
        self.y_values = y_values

    def mnoz(self):
        x_values = np.arange(self.n1, self.n2, (1 / self.f))
        y_values = []

        for i in np.arange(len(x_values)):
            if self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and self.przedzial2[0] <= x_values[i] <= self.przedzial2[1]:
                value = self.obj1.obj.signal(x_values[i]) * self.obj2.obj.signal(x_values[i])
                y_values.append(value)
            elif self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and (self.przedzial2[0] > x_values[i] or x_values[i] > self.przedzial2[1]):
                value = self.obj1.obj.signal(x_values[i]) 
                y_values.append(value)
            else:
                value = self.obj2.obj.signal(x_values[i])
                y_values.append(value)

        self.x_values = x_values
        self.y_values = y_values

    def dziel(self):
        x_values = np.arange(self.n1, self.n2, (1 / self.f))
        y_values = []

        for i in np.arange(len(x_values)):
            if self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and self.przedzial2[0] <= x_values[i] <= self.przedzial2[1]:
                if self.obj2.obj.signal(x_values[i]) == 0:
                    div = 1
                else: 
                    div = self.obj2.obj.signal(x_values[i])
                value = self.obj1.obj.signal(x_values[i]) / div
                y_values.append(value)
            elif self.przedzial1[0] <= x_values[i] <= self.przedzial1[1] and (self.przedzial2[0] > x_values[i] or x_values[i] > self.przedzial2[1]):
                value = self.obj1.obj.signal(x_values[i]) 
                y_values.append(value)
            else:
                value = self.obj2.obj.signal(x_values[i])
                y_values.append(value)

        self.x_values = x_values
        self.y_values = y_values

    def wykres(self):
        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption")
        plt.plot(self.x_values, self.y_values) 
        plt.grid(True)
        """
        plt.title("Wykres zależności amplitudy od czasu") 
        plt.xlabel("x axis caption") 
        plt.ylabel("y axis caption")
        plt.hist(self.values, self.bins, facecolor='blue', alpha=0.5)
        plt.grid(True)
        """
        plt.show() 