import numpy as np
from CosineSimilarity import CosineSimilarity
from JaccardSimilarity import JaccardSimilarity
from EuclideanSimilarity import EuclideanSimilarity
from ManhattanSimilarity import ManhattanSimilarity


class Similarity:
    def __init__(self, method):
        self.method = method


    def sim(self,d,q,method):
        if method == "Cosine":
            print("\n\nCosine\n==============\n")
            technique = CosineSimilarity()
            return technique.sim(d,q)
        elif method == "Jaccard":
            print("\n\nJaccard\n==============\n")
            technique = JaccardSimilarity()
            return technique.sim(d,q)
        elif method == "Euclidean":
            print("\n\nEuclidean\n==============\n")
            technique = EuclideanSimilarity()
            return technique.sim(d,q)
        elif method == "Manhattan":
            print("\n\nManhattan\n==============\n")
            technique = ManhattanSimilarity()
            return technique.sim(d,q)
        else:
            print("Default")
