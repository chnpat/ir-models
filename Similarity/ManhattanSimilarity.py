import numpy as np

class ManhattanSimilarity:

    def sim(self, d, q):
        a = np.array(d)
        b = np.array(q)
        print(np.subtract(a,b), np.abs(np.subtract(a,b)), np.sum(np.abs(np.subtract(a,b))))
        return 1 - np.sum(np.abs(np.subtract(a,b)))
