from matplotlib import pyplot as plt
import numpy as np
import math

from src.conversion_measures import *


class Signal_Disc:
    def __init__(self, ioo, method, samplesForSine):
        self.impuls_ops_object = ioo
        self.x_cont = ioo.x_values.tolist()
        self.y_cont = ioo.y_values
        self.method = method
        self.x_samples = []
        self.y_samples = []
        self.x_values = ioo.x_disc.tolist()
        self.y_values = ioo.y_disc

        self.samplesForSine = samplesForSine

    def wykres(self):
        methodStr = ""
        if self.method == "r1":
            self.zoh()
            methodStr = "ZOH"
        if self.method == "r2":
            self.foh()
            methodStr = "FOH"
        if self.method == "r3":
            self.sineMethod()
            methodStr = "wykorzystujaca sinc"

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

    def sine(self, N, ts, t):
        i = 0
        sumSine = 0.0
        while i < N:
            sumSine += self.y_values[i] * np.sinc((t - N)/ts)
            i += 1
        return sumSine

    def sineMethod(self):
        N = int(len(self.x_values))
        ts = self.impuls_ops_object.step

        step = abs(self.x_cont[1] - self.x_cont[0])
        for _ in range(len(self.y_cont)):
            valY = self.sine(N, ts, step)
            self.y_samples.append(valY)
            self.x_samples.append(step)
            step += 0.05

    def showMeasures(self, x, x_dash):
        print("Mean Square Error MSE:" + str(MSE(x, x_dash)))
        snr = SNR(x, x_dash)
        if (snr[0]) == True:
            print("Signal to Noise Ratio SNR:" + str(snr[1]))
        else:
            print("Signal to Noise Ratio SNR: ---")
        # print("Signal to Noise Ratio SNR:" + str(SNR(x, x_dash)))
        print("Maximum Difference:" + str(MD(x, x_dash)))
