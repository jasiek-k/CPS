from matplotlib import pyplot as plt 
import numpy as np 
import math
from src.prost_signal import *
from src.troj_signal import *
from src.sin_signal import * 
from src.signal_ops import *
from src.impuls_ops import *
from src.skok import *
"""
skok = Skok_jedno(5, 0, 10, 0)
prost = Prost_sygnal_sym(10, 2, 0, 10, 0.5)
troj = Troj_sygnal(10, 2, 0, 10, 0.5)
"""

ops = Signal_operations(1, 1, 2, 0, 5)
imp_ops = Impuls_operations(2, -5, 0, 10, 1)

print(ops.srednia())
print(ops.srednia_bezwgl())
ops.wykres()

