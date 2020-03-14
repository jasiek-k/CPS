import numpy as np 
import math
from src.sin_signal import * 
from matplotlib import pyplot as plt 

#def y(x):
#    return np.float(math.sin(((math.pi * 2.0) / 5.0) * (x)))

def y(t, A, T, t1):
    return A * np.sin(((2 * np.pi) / T) * (t - t1))

def y3(t, A, T, t1):    
    return 0.5 * A * (np.sin(((2 * np.pi) / T) * (t - t1)) + np.fabs(np.sin(((2 * np.pi) / T) * (t - t1))))

x = np.arange(0,10, 0.1) 
#y2 = y3(x, 2, 5, 0)
#y2 = np.sin(x)

sinus = Sin_sygnal(2, 5, 0, 10)
sinus2 = Sin_sygnal_wyp_dwu(2, 5, 0, 10)
y2 = sinus.signal(x)
y4 = sinus2.signal(x)

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x, y4) 
plt.show()