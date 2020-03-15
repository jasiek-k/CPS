import numpy as np


class Skok_jedno:

    def __init__(self, A, t1, d, ts):
        self.A = A
        self.t1 = t1
        self.d = d
        self.ts = ts

    def signal(self, t):
        if float(t) > float(self.ts):
            return self.A
        elif float(t) == float(self.ts):
            return (0.5 * self.A)
        else: 
            return 0