from matplotlib import pyplot as plt 
import linecache as lc
import numpy as np 
import math

from src.impuls_signal import *
from src.prost_signal import *
from src.skok_signal import *
from src.troj_signal import *
from src.sin_signal import * 
from src.signal_ops import *
from src.impuls_ops import *



def plik_czytaj(nazwa_pliku):
    init_data = lc.getline(nazwa_pliku, 1)
    y_data = lc.getline(nazwa_pliku, 2)

    y_data = y_data.translate({ord('['): None})
    y_data = y_data.translate({ord(']'): None})
    y_array = y_data.split(", ")

    for i in range(len(y_array)):
        y_array[i] = float(y_array[i])

    return [init_data, y_data]
   

def signal_init():
    string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")
    save_file = False
    read_file = False
    dzialania = False
   
    if string.find("dodaj") != (-1):
        dzialania = True
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "dodaj":
                index = i
        para1 = string[0:index]
        para2 = string[index + 1:len(string) - 1]
    elif string.find("odejmij") != (-1):
        dzialania = True
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "odejmij":
                index = i
        para1 = string[0 : index]
        para2 = string[index + 1:len(string) - 1]
    elif string.find("mnoz") != (-1):
        dzialania = True
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "mnoz":
                index = i
        para1 = string[0 : index]
        para2 = string[index + 1:len(string) - 1]
    elif string.find("dziel") != (-1):
        dzialania = True
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "dziel":
                index = i
        para1 = string[0 : index]
        para2 = string[index + 1:len(string) - 1]

    if dzialania == True:
        counter = 2
    else: 
        counter = 1

    for i in range(counter):
        if i == 1 and dzialania == True:
            string = " "
            string = string.join(para1)
            print(string)
        if i == 2 and dzialania == True:
            string = " "
            string = string.join(para2)
            print(string)
    """
    if string.find("R") != (-1):
        read_file = True
        read_string = string.translate({ord('R'): None})
        read_string = read_string.translate({ord(' '): None})

        data = plik_czytaj(read_string)
        string = data[0].translate({ord('\n'): None})
        y_array = data[1].split(', ')
        
        for i in range(len(y_array)):
            y_array[i] = float(y_array[i])
    
    array = string.split(" ")
    signal = array[0] 
 
    if string.find("T") != (-1):
        save_file = True
        file_string = f'./files/{signal}_data'
        
    if signal == "S1":
        if len(array) < 6 or array[5] == "":
            array.append('1')
        if array[5] == "T":
            array.append("T")
            array[5] = 1

        szum = Szum_jedno(float(array[1]), int(array[2]), int(array[3]))
        ops = Signal_operations(signal, szum, int(array[4]), int(array[5]))

        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()

    elif signal == "S2":
        if len(array) < 6 or array[5] == "":
            array.append('1')
        if array[5] == "T":
            array.append("T")
            array[5] = 1

        szum = Szum_gauss(float(array[1]), int(array[2]), int(array[3]))
        ops = Signal_operations(signal, szum, int(array[4]), int(array[5]))

        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()

    elif signal == "S3":
        if len(array) < 7 or array[6] == "":
            array.append('1')
        if array[6] == "T":
            array.append("T")
            array[6] = 1

        sinus = Sin_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(signal, sinus, int(array[5]), int(array[6]))

        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()
       
    elif signal == "S4":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        if array[6] == "T":
            array.append("T")
            array[6] = 1

        sinus = Sin_sygnal_wyp_jedno(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(signal, sinus, int(array[5]), int(array[6]))
       
        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()

    elif signal == "S5":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        if array[6] == "T":
            array.append("T")
            array[6] = 1

        sinus = Sin_sygnal_wyp_dwu(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(signal, sinus, int(array[5]), int(array[6]))
        
        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj() 

    elif signal == "S6":
        if len(array) < 8 or array[7] == "": 
            array.append('1')
        if array[7] == "T":
            array.append("T")
            array[7] = 1
        prosto = Prost_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
        ops = Signal_operations(signal, prosto, int(array[6]), int(array[7]))
        
        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()
        
       
    elif signal == "S7":
        if len(array) < 8 or array[7] == "": 
            array.append('1')
        if array[7] == "T":
            array.append("T")
            array[7] = 1
        prosto = Prost_sygnal_sym(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))  
        ops = Signal_operations(signal, prosto, int(array[6]), int(array[7]))
        
        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()

    elif signal == "S8":
        if len(array) < 8 or array[7] == "": 
            array.append('1')
        if array[7] == "T":
            array.append("T")
            array[7] = 1
        troj = Troj_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
        ops = Signal_operations(signal, troj, int(array[6]), int(array[7]))
        
        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()
        
    elif signal == "S9":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        if array[6] == "T":
            array.append("T")
            array[6] = 1
        skok = Skok_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]))
        ops = Signal_operations(signal, skok, int(array[5]), int(array[6]))
        
        if read_file == True:
            ops.setYs(y_array)
        elif read_file == False: 
            ops.licz()
            ops.wywolaj()
        if save_file == True:
            ops.plik_zapisz(file_string)
        ops.prezentuj()

    elif signal == "S10":
        if len(array) < 7 or array[6] == "": 
            array.append('1')
        if array[6] == "T":
            array.append("T")
            array[6] = 1
        impuls = Impuls_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[6]))
        imp_ops = Impuls_operations(signal, impuls, int(array[5]))
        
        if read_file == True:
            imp_ops.setYs(y_array)
        elif read_file == False: 
            imp_ops.licz()
            imp_ops.wywolaj()
        if save_file == True:
            imp_ops.plik_zapisz(file_string)
        imp_ops.prezentuj()
        
    else: 
        print("Błędne argumenty funkcji")
    #string = ''
    #string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")
    """
def main():
    signal_init()



main()
