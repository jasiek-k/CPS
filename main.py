import numpy as np 
import math
from src.sin_signal import * 
from src.prost_signal import *
from src.skok import *
from matplotlib import pyplot as plt 

"""
x = np.arange(0, 10, 0.1) 
sinus = Sin_sygnal(2, 5, 0, 10)
sinus2 = Sin_sygnal_wyp_dwu(2, 5, 0, 10)
skok = Skok_jedno(5, 0, 10, 0)

y2 = sinus.signal(x)
y4 = sinus2.signal(x)
#y5 = prost.signal(x)
y6 = skok.signal(x)

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x, y6) 
plt.show()
"""
prost = Prost_sygnal_sym(10, 2, 0, 10, 0.5)
skok = Skok_jedno(5, 0, 10, 0)
x = np.arange(0, 10, 0.1)
y = []

i = 0
while i < len(x):
    #y.append(skok.signal(x[i]))
    y.append(prost.signal(x[i]))
    i = i + 1

    

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x, y) 
plt.show() 

