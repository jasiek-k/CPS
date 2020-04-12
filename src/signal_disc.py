from matplotlib import pyplot as plt
import numpy as np
import math


class Signal_Disc:
    def __init__(self, ioo, method):
        self.impuls_ops_object = ioo
        self.x_cont = ioo.x_values.tolist()
        self.y_cont = ioo.y_values
        self.method = method
        self.x_samples = []
        self.y_samples = []
        self.x_values = ioo.x_disc.tolist()
        self.y_values = ioo.y_disc

    def wykres(self):
        methodStr = ""
        if self.method == "r1":
            self.zoh()
            methodStr = "ZOH"
        if self.method == "r2":
            self.foh()
            methodStr = "FOH"

        plt.figure()
        plt.plot(self.x_samples, self.y_samples)
        plt.plot(self.x_cont, self.y_cont)
        plt.title("Rekonstrukcja z sygnału dyskretnego metoda " + methodStr)
        plt.xlabel("x axis caption")
        plt.ylabel("y axis caption")
        plt.grid(True)
        plt.show()

    def zoh(self):
        duration = self.impuls_ops_object.obj.d
        distance_between_samples = duration / int(len(self.x_values))
        for i in range(len(self.y_values)):
            xTmp = self.x_values[i]
            yVal = self.y_values[i]

            self.x_samples.append(xTmp)
            self.x_samples.append(xTmp+distance_between_samples)
            self.y_samples.append(yVal)
            self.y_samples.append(yVal)

    def foh(self):
        for i in range(len(self.y_values)):
            xTmp = self.x_values[i]
            yVal = self.y_values[i]
            self.x_samples.append(xTmp)
            self.y_samples.append(yVal)
