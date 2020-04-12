from matplotlib import pyplot as plt
import numpy as np
import math


class Signal_Cont:
    def __init__(self, ioo, sampling_frequency, quantization_level):
        self.impuls_ops_object = ioo
        self.x_values = ioo.x_values.tolist()
        self.y_values = ioo.y_values
        self.sampling_frequency = sampling_frequency
        self.quantization_level = quantization_level

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
            i += distance_floor

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
        print(intervals_values)
        self.quant_y = []

        for v in self.y_values:
            q = min(intervals_values, key=lambda x: abs(x-v))
            self.quant_y.append(q)
            # for i in range(self.quantization_level - 1):
            #     if x >= intervals_values[i] and x <= intervals_values[i+1]:
            #         d1 = abs(x-intervals_values[i])
            #         d2 = abs(x-intervals_values[i+1])
            #         if d1 > d2 or d1 == d2:
            #             self.quant_y.append(intervals_values[i])
            #             break
            #         elif d2 > d1:
            #             self.quant_y.append(intervals_values[i+1])
            #             break
