import numpy as np 
import math
from src.sin_signal import * 
from src.prost_signal import *
from src.skok import *
from src.troj_signal import *
from matplotlib import pyplot as plt 

skok = Skok_jedno(5, 0, 10, 0)
prost = Prost_sygnal_sym(10, 2, 0, 10, 0.5)
troj = Troj_sygnal(10, 2, 0, 10, 0.5)
x = np.arange(0, 10, 0.1)
y = []

for i in np.arange(len(x)):
    y.append(troj.signal(x[i]))
    

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x, y) 
plt.show() 

