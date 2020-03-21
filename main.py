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
    
    #while string != 'q':
    if signal == "S1":
        print()
    elif signal == "S2":
        print()
    elif signal == "S3":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        sinus = Sin_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(sinus, int(array[5]), int(array[6]))
        ops.prezentuj()
    elif signal == "S4":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        sinus = Sin_sygnal_wyp_jedno(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(sinus, int(array[5]), int(array[6]))
        ops.prezentuj()
    elif signal == "S5":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        sinus = Sin_sygnal_wyp_dwu(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(sinus, int(array[5]), int(array[6]))
        ops.prezentuj()
    elif signal == "S6":
        if len(array) < 8 or array[7] == "": 
            array.append('1')
        prosto = Prost_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
        ops = Signal_operations(prosto, int(array[6]), int(array[7]))
        ops.prezentuj()
    elif signal == "S7":
        if len(array) < 8 or array[7] == "": 
            array.append('1')
        prosto = Prost_sygnal_sym(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))  
        ops = Signal_operations(prosto, int(array[6]), int(array[7]))
        ops.prezentuj()
    elif signal == "S8":
        if len(array) < 8 or array[7] == "": 
            array.append('1')
        troj = Troj_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
        ops = Signal_operations(troj, int(array[6]), int(array[7]))
        ops.prezentuj()
    elif signal == "S9":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        skok = Skok_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(skok, int(array[5]), int(array[6]))
        ops.prezentuj()
    elif signal == "S10":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        impuls = Impuls_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[6]))
        imp_ops = Impuls_operations(impuls, int(array[5]))
        imp_ops.prezentuj()
    else: 
        print("Błędne argumenty funkcji")
    string = ''
    string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")

signal_init()

impuls = Impuls_jedno(2, -3, 0, 10, 2)
imp_ops = Impuls_operations(impuls, 10)
#imp_ops.wykres()
print(imp_ops.srednia())
print(imp_ops.srednia_bezwgl())
print(imp_ops.moc_srednia())
print(imp_ops.wariancja())
print(imp_ops.wart_skut())



