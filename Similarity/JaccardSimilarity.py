import numpy as np

class JaccardSimilarity:

    def sim(self, d, q):
        arr = np.array([d, q])
        part = np.sum(np.min(arr, axis = 0))
        whole = np.sum(np.max(arr, axis = 0))
        print(part, whole)
        return part/whole

