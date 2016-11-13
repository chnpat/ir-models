import numpy as np
import math as m

'''
Term-Document Matrix

    d1   d2   d3   ...
k1   x   x   x
k2   x   x   x
k3   x   x   x
.
.

'''


class Weighting_Scheme:


    def CalculateTermFreq(self, term_doc_matrix):
        for i in range(len(term_doc_matrix)):
            for j in range(len(term_doc_matrix[i,:])):
                if term_doc_matrix[i,j] != 0:
                    term_doc_matrix[i,j] = 1 + m.log(term_doc_matrix[i,j],2)
        print(term_doc_matrix)
        return term_doc_matrix

    def CalculateInvDocFreq(self, i, term_doc_matrix):
        N = len(term_doc_matrix)
        ni = 0
        for i in term_doc_matrix[i, :]:
            if i != 0:
                ni += 1
        if ni != 0:
            return m.log(float(N)/ni, 2)
        else:
            return 0

    def TF_IDF(self, term_doc_matrix):
        term_doc_matrix = self.CalculateTermFreq(term_doc_matrix)
        for i in range(len(term_doc_matrix)):
            for j in range(len(term_doc_matrix[i,:])):
                term_doc_matrix[i,j] = term_doc_matrix[i,j] * self.CalculateInvDocFreq(j, term_doc_matrix)
        print(term_doc_matrix)
        return term_doc_matrix

