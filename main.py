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
    
    while string != 'q':
        if signal == "S1":
            print()
        elif signal == "S2":
            print()
        elif signal == "S3":
            sinus = Sin_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
            if len(array) < 7 or array[6] == '': 
                array.append('1') 
            ops = Signal_operations(sinus, int(array[6]))
            ops.wykres()
            ops.histogram(int(array[5]))
        elif signal == "S4":
            sinus = Sin_sygnal_wyp_jedno(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            ops = Signal_operations(sinus, int(array[6]))
            ops.wykres()
            ops.histogram(int(array[5]))
        elif signal == "S5":
            sinus = Sin_sygnal_wyp_dwu(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            ops = Signal_operations(sinus, int(array[6]))
            ops.wykres()
            ops.histogram(int(array[5]))
        elif signal == "S6":
            prosto = Prost_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
            if len(array) < 8 or array[7] == "": 
                array.append('1')
            ops = Signal_operations(prosto, int(array[7]))
            ops.wykres()
            ops.histogram(int(array[6]))
        elif signal == "S7":
            prosto = Prost_sygnal_sym(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
            if len(array) < 8 or array[7] == "": 
                array.append('1')
            ops = Signal_operations(prosto, int(array[7]))
            ops.wykres()
            ops.histogram(int(array[6]))
        elif signal == "S8":
            troj = Troj_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
            if len(array) < 8 or array[7] == "": 
                array.append('1')
            ops = Signal_operations(troj, int(array[7]))
            ops.wykres()
            ops.histogram(int(array[6]))
        elif signal == "S9":
            skok = Skok_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]))
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            ops = Signal_operations(skok, int(array[6]))
            ops.wykres()
            ops.histogram(int(array[5]))
        elif signal == "S10":
            impuls = Impuls_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[5]))
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            ops = Signal_operations(impuls, int(array[6]))
            ops.wykres()
            ops.histogram(int(array[5]))
        else: 
            print("Błędne argumenty funkcji")
        string = ''
        string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")

signal_init()

#print(ops.srednia())
#print(ops.srednia_bezwgl())
#imp_ops.wykres()
#imp_ops.histogram(5)
#ops.wykres()
#ops.histogram(5)

