from matplotlib import pyplot as plt
import numpy as np
import math
import sys

from src.signal_cont import *
from src.signal_disc import *
from src.signal_init import *

# signal_init()
if len(sys.argv) != 2:
    print("Podaj wszystkie parametry wywolania programu")
    exit(0)

mode = sys.argv[1]

if(mode == "ADC"):
    print("Tryb konwertera analogowo-cyfrowego (Analog to Digital)")
    sampling_frequency = (int)(input("Podaj czestotliwosc probkowania: "))
    quantization_level = (int)(input("Podaj prog kwantyzacji: "))
    ops = signal_init("adc")
    sig = Signal_Cont(ops, sampling_frequency, quantization_level)
    sig.wykres()

if(mode == "DAC"):
    print("Tryb konwertera cyfrowo-analogowego (Digital to Analog)")
    print("Dostepne metody rekonstrukcji sygnalu:")
    print("[r1] zero-order hold")
    print("[r2] first-orded hold")
    print("[r3] rekonstrukcja w oparciu o funkcje sine")
    reconstruction_method = input(
        "Wybierz metode rekonsturkcji podajac oznaczenie z kwadratowych nawiasow: ")
    # samples_amount = int(input("Podaj ilosc probek generowanego sygnalu: "))
    ops = signal_init("dac")
    sig = Signal_Disc(ops, reconstruction_method)
    sig.wykres()

if mode != "DAC" and mode != "ADC":
    print("Niepoprawny parametr wywolania. Dostepne opcje: DAC, ADC")
    exit(0)
