from matplotlib import pyplot as plt 
import numpy as np 
import math
from src.prost_signal import *
from src.skok_signal import *
from src.troj_signal import *
from src.sin_signal import * 
from src.signal_ops import *
from src.impuls_ops import *


def signal_init():
    string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")
    array = string.split(" ")
    signal = array[0] 

    if signal == "S3":
        sinus = Sin_sygnal(int(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[5]))
        ops = Signal_operations(sinus)
        ops.wykres()
        ops.histogram(int(array[6]))
    elif signal == "S4":
        sinus = Sin_sygnal_wyp_jedno(int(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[5]))
        ops = Signal_operations(sinus)
        ops.wykres()
        ops.histogram(int(array[6]))
    elif signal == "S5":
        sinus = Sin_sygnal_wyp_dwu(int(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[5]))
        ops = Signal_operations(sinus)
        ops.wykres()
        ops.histogram(int(array[6]))
    elif signal == "S6":
        print("chuj3")
    elif signal == "S7":
        print("chuj4")
    elif signal == "S8":
        print("chuj5")
    elif signal == "S9":
        print("chuj6")
    elif signal == "S10":
        print("chuj7")
    else: 
        print("Błędne argumenty funkcji")
        string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")


#sinus_wyp = Sin_sygnal_wyp_dwu(3, 4, 0, 10, 1)

#prost = Prost_sygnal(3, 4, 0, 10, 0.5)
#sin = Signal_operations(sinus_wyp)
#sin.wykres()

#signal_init()

#print(ops.srednia())
#print(ops.srednia_bezwgl())
#imp_ops.wykres()
#imp_ops.histogram(5)
#ops.wykres()
#ops.histogram(5)

