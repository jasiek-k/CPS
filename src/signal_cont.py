from matplotlib import pyplot as plt
import numpy as np
import math

from src.conversion_measures import *


class Signal_Cont:
    def __init__(self, ioo, sampling_frequency, quantization_level):
        self.impuls_ops_object = ioo
        self.x_values = ioo.x_values.tolist()
        self.y_values = ioo.y_values
        self.sampling_frequency = sampling_frequency
        self.quantization_level = quantization_level

        self.y_measure_sampling = []

    def wykres(self):
        self.sampling()
        self.quantization()

        plt.figure()
        plt.plot(self.x_values, self.y_values)
        plt.plot(self.x_samples, self.y_samples, 'ro')
        plt.title("Sygnał wejściowy + próbki")
        plt.xlabel("x axis caption")
        plt.ylabel("y axis caption")
        plt.grid(True)

        plt.figure()
        plt.plot(self.x_values, self.y_values)
        plt.plot(self.x_values, self.quant_y)
        plt.title("Sygnał wejściowy + kwantyzacja")
        plt.xlabel("x axis caption")
        plt.ylabel("y axis caption")
        plt.yticks(np.arange(self.minAmp+self.step,
                             self.maxAmp+self.step, self.step))
        plt.grid(True)

        plt.show()

    def sampling(self):
        samplesAmound = self.impuls_ops_object.obj.d * \
            (self.sampling_frequency)
        samples_floor = math.floor(samplesAmound)
        distanceBetweenSamples = len(self.x_values)/(samples_floor)
        distance_floor = math.floor(distanceBetweenSamples)

        self.x_samples = []
        self.y_samples = []

        i = 0
        while i < len(self.x_values):
            self.x_samples.append(self.x_values[i])
            self.y_samples.append(self.y_values[i])
            self.y_measure_sampling.append(self.y_values[i])
            i += distance_floor

        print("============ WARTOSCI MIAR DLA PROBKOWANIA ===========")
        self.showMeasures(self.y_samples, self.y_measure_sampling)

    def quantization(self):
        maxAmplitude = self.y_samples[0]
        minAmplitude = self.y_samples[0]

        for value in self.y_values:
            if(value > maxAmplitude):
                maxAmplitude = value
            if(value < minAmplitude):
                minAmplitude = value

        difference = maxAmplitude - minAmplitude

        quant_interval = difference/(float)(self.quantization_level-1)

        self.minAmp = minAmplitude
        self.maxAmp = maxAmplitude
        self.step = quant_interval
        intervals_values = []

        tmpVal = minAmplitude
        for x in range(self.quantization_level):
            intervals_values.append(tmpVal)
            tmpVal += quant_interval
        intervals_values.append(tmpVal)
        self.quant_y = []

        for v in self.y_values:
            q = min(intervals_values, key=lambda x: abs(x-v))
            self.quant_y.append(q)

        print("============ WARTOSCI MIAR DLA KWANTOWANIA ===========")
        self.showMeasures(self.y_samples, self.quant_y)

    def showMeasures(self, x, x_dash):
        print("Mean Square Error MSE:" + str(MSE(x, x_dash)))
        snr = SNR(x, x_dash)
        if (snr[0]) == True:
            print("Signal to Noise Ratio SNR:" + str(snr[1]))
        else:
            print("Signal to Noise Ratio SNR: ---")
        # print("Signal to Noise Ratio SNR:" + str(SNR(x, x_dash)))
        # snr2 = SNR2(x, x_dash)
        # if (snr2[0]) == True:
        #     print("Signal to Noise Ratio SNR2:" + str(snr2[1]))
        # else:
        #     print("Signal to Noise Ratio SNR2: ---")
        # print("Signal to Noise Ratio SNR:" + str(SNR(x, x_dash)))
        print("Maximum Difference:" + str(MD(x, x_dash)))
