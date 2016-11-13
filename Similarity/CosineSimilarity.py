import math as m
import numpy as np

class CosineSimilarity:

    def computeVectNorm(self, vector):
        return m.sqrt(sum([m.pow(i, 2) for i in vector]))
        
    def sim(self, d, q):
        dot = np.dot(d,q)
        norm = self.computeVectNorm(d) * self.computeVectNorm(q)
        print(dot, norm)
        return dot/norm

