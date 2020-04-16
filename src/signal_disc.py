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
        plt.figure()
        plt.plot(self.x_cont, self.y_cont)
        plt.plot(self.x_values, self.y_values, 'ro')
        plt.title("Rekonstrukcja z sygnału dyskretnego metoda " + methodStr)
        plt.xlabel("x axis caption")
        plt.ylabel("y axis caption")
        plt.grid(True)
        plt.show()

    def zoh(self):
        duration = self.impuls_ops_object.obj.d
        distance_between_samples = duration / int(len(self.x_values))
        for i in range(len(self.y_values)-1):
            xTmp = self.x_values[i]
            yVal = self.y_values[i]
            j = xTmp
            while j < self.x_values[i+1]:
                self.x_samples.append(xTmp)
                self.y_samples.append(yVal)
                j += 0.05

            self.x_samples.append(xTmp+distance_between_samples)
            self.y_samples.append(yVal)

        print("============ WARTOSCI MIAR DLA ZOH ===========")
        self.showMeasures(self.y_values, self.y_samples)

    def foh_interpolate_value(self, x):
        if x <= self.x_values[0]:
            return self.y_values[0]
        vlen = len(self.x_values)
        if x >= self.x_values[vlen-1]:
            return self.y_values[vlen-1]

        i = 0
        while x > self.x_values[i+1]:
            i = i + 1

        x1 = self.x_values[i]
        x2 = self.x_values[i+1]
        y1 = self.y_values[i]
        y2 = self.y_values[i+1]

        xRange = x2-x1
        yRange = y2-y1

        t = (x - x1) / xRange

        y = y1 + (yRange * t)
        return y

    def foh(self):
        distance_between_samples = abs(self.x_values[0]-self.x_values[1])
        samplesBetween = 3
        t = distance_between_samples/samplesBetween

        for i in range(len(self.x_values)-1):
            for j in range(samplesBetween):
                tmpX = self.x_values[i] + (j*t)
                tmpY = self.foh_interpolate_value(tmpX)
                self.x_samples.append(tmpX)
                self.y_samples.append(tmpY)

        print("============ WARTOSCI MIAR DLA FOH ===========")
        self.showMeasures(self.y_values, self.y_samples)

    def sine(self, N, ts, t):
        i = 0
        sumSine = 0.0
        while i < N:
            sumSine += self.y_values[i] * np.sinc((t - self.x_values[i]) / ts)
            i += 1
        return sumSine

    def sineMethod(self):
        N = int(len(self.x_values))
        ts = abs(self.x_values[0]-self.x_values[1])

        for i in range(len(self.y_cont)):
            valY = self.sine(N, ts, self.x_cont[i])
            self.y_samples.append(valY)
            self.x_samples.append(self.x_cont[i])

        print("============ WARTOSCI MIAR DLA SINE ===========")
        self.showMeasures(self.y_values, self.y_samples)

    def showMeasures(self, x, x_dash):
        print("Mean Square Error MSE:" + str(MSE(x, x_dash)))
        snr = SNR(x, x_dash)
        if (snr[0]) == True:
            print("Signal to Noise Ratio SNR:" + str(snr[1]))
        else:
            print("Signal to Noise Ratio SNR2: ---")
        snr2 = SNR2(x, x_dash)
        if (snr2[0]) == True:
            print("Signal to Noise Ratio SNR2:" + str(snr2[1]))
        else:
            print("Signal to Noise Ratio SNR2: ---")
        # print("Signal to Noise Ratio SNR:" + str(SNR(x, x_dash)))
        print("Maximum Difference:" + str(MD(x, x_dash)))
