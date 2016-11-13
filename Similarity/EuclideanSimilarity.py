import math as m
import numpy as np

class EuclideanSimilarity:

    def sim(self, d, q):
        a = np.array(d)
        b = np.array(q)
        c = np.subtract(a,b)
        print(a,b,c**2)
        return 1 - m.sqrt(np.sum(c**2))
