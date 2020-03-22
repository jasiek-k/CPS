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
from src.dzialania import *



def plik_czytaj(nazwa_pliku):
    init_data = lc.getline(nazwa_pliku, 1)
    y_data = lc.getline(nazwa_pliku, 2)

    y_data = y_data.translate({ord('['): None})
    y_data = y_data.translate({ord(']'): None})
    y_array = y_data.split(", ")

    for i in range(len(y_array)):
        y_array[i] = float(y_array[i])

    return [init_data, y_data]
   
# Attention -> ostry młyn poniżej
def signal_init():
    string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")
    string_copy = string
    save_file = False
    save_op = False
    read_file = False
    dzialania = False
    dzialanie = ""
    op_f = 0

    if string.find("Z") != (-1):
        save_op = True
        string = string.translate({ord('Z'): None})

   
    if string.find("dodaj") != (-1):
        dzialania = True
        dzialanie = "dodaj"
        string = string.split(" ")

        print(string)
        for i in range(len(string)):
            if string[i] == "dodaj":
                index = i
        para1 = string[0:index]
        para2 = string[index + 1:len(string) - 2]
        op_f = int(string[len(string) - 2])
        print(op_f)

    elif string.find("odejmij") != (-1):
        dzialania = True
        dzialanie = "odejmij"
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "odejmij":
                index = i
        para1 = string[0 : index]
        para2 = string[index + 1:len(string) - 2]
        op_f = int(string[len(string) - 2])

    elif string.find("mnoz") != (-1):
        dzialania = True
        dzialanie = "mnoz"
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "mnoz":
                index = i
        para1 = string[0 : index]
        para2 = string[index + 1:len(string) - 2]
        op_f = int(string[len(string) - 2])

    elif string.find("dziel") != (-1):
        dzialania = True
        dzialanie = "dziel"
        string = string.split(" ")
        for i in range(len(string)):
            if string[i] == "dziel":
                index = i
        para1 = string[0 : index]
        para2 = string[index + 1:len(string) - 2]
        op_f = int(string[len(string) - 2])


    if dzialania == True:
        counter = 2
        objs = []
    else: 
        counter = 1

    for i in range(counter):
        if i == 0 and dzialania == True:
            string = " "
            string = string.join(para1)
            print(string)
        if i == 1 and dzialania == True:
            string = " "
            string = string.join(para2)
            print(string)
   
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

            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)

        elif signal == "S2":
            if len(array) < 6 or array[5] == "":
                array.append('1')
            if array[5] == "T":
                array.append("T")
                array[5] = 1

            szum = Szum_gauss(float(array[1]), int(array[2]), int(array[3]))
            ops = Signal_operations(signal, szum, int(array[4]), int(array[5]))

            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)

        elif signal == "S3":
            if len(array) < 7 or array[6] == "":
                array.append('1')
            if array[6] == "T":
                array.append("T")
                array[6] = 1

            sinus = Sin_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
            ops = Signal_operations(signal, sinus, int(array[5]), int(array[6]))

            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)
        
        elif signal == "S4":
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            if array[6] == "T":
                array.append("T")
                array[6] = 1

            sinus = Sin_sygnal_wyp_jedno(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
            ops = Signal_operations(signal, sinus, int(array[5]), int(array[6]))
        
            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)

        elif signal == "S5":
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            if array[6] == "T":
                array.append("T")
                array[6] = 1

            sinus = Sin_sygnal_wyp_dwu(float(array[1]), float(array[2]), int(array[3]), int(array[4]))
            ops = Signal_operations(signal, sinus, int(array[5]), int(array[6]))
            
            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj() 
            else:
                objs.append(ops)

        elif signal == "S6":
            if len(array) < 8 or array[7] == "": 
                array.append('1')
            if array[7] == "T":
                array.append("T")
                array[7] = 1
            prosto = Prost_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
            ops = Signal_operations(signal, prosto, int(array[6]), int(array[7]))
            
            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else: 
                objs.append(ops)
        
        elif signal == "S7":
            if len(array) < 8 or array[7] == "": 
                array.append('1')
            if array[7] == "T":
                array.append("T")
                array[7] = 1
            prosto = Prost_sygnal_sym(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))  
            ops = Signal_operations(signal, prosto, int(array[6]), int(array[7]))
            
            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)

        elif signal == "S8":
            if len(array) < 8 or array[7] == "": 
                array.append('1')
            if array[7] == "T":
                array.append("T")
                array[7] = 1
            troj = Troj_sygnal(float(array[1]), float(array[2]), int(array[3]), int(array[4]), float(array[5]))
            ops = Signal_operations(signal, troj, int(array[6]), int(array[7]))
            
            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)
            
        elif signal == "S9":
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            if array[6] == "T":
                array.append("T")
                array[6] = 1
            skok = Skok_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]))
            ops = Signal_operations(signal, skok, int(array[5]), int(array[6]))
            
            if dzialania == False:
                if read_file == True:
                    ops.setYs(y_array)
                elif read_file == False: 
                    ops.licz()
                    ops.wywolaj()
                if save_file == True:
                    ops.plik_zapisz(file_string)
                ops.prezentuj()
            else:
                objs.append(ops)

        elif signal == "S10":
            if len(array) < 7 or array[6] == "": 
                array.append('1')
            if array[6] == "T":
                array.append("T")
                array[6] = 1
            impuls = Impuls_jedno(float(array[1]), int(array[2]), int(array[3]), int(array[4]), int(array[6]))
            imp_ops = Impuls_operations(signal, impuls, int(array[5]))
            
            if dzialania == False:
                if read_file == True:
                    imp_ops.setYs(y_array)
                elif read_file == False: 
                    imp_ops.licz()
                    imp_ops.wywolaj()
                if save_file == True:
                    imp_ops.plik_zapisz(file_string)
                imp_ops.prezentuj()
            else:
                objs.append(imp_ops)
        else: 
            print("Błędne argumenty funkcji")
    
    if dzialania == True:
        dzialaj = Dzialania(objs[0], objs[1], op_f, string_copy)

        if dzialanie == "dodaj":
            dzialaj.dodaj()
        elif dzialanie == "odejmij":
            dzialaj.odejmij()
        elif dzialanie == "mnoz":
            dzialaj.mnoz()
        else:
            dzialaj.dziel()
        #dzialaj.print()
        if save_op == True:
            dzialaj.plik_zapisz(f"./files/{dzialaj.obj1.signal}_{dzialaj.obj2.signal}_data")
        dzialaj.wykres()
       
    #string = ''
    #string = input("Podaj argumenty funkcji. (Szczegóły znajdziesz w README.md): ")









signal_init()




