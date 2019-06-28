import numpy as np


def LCSLength(Q, L):
    n = len(Q)
    m = len(L)
    c = np.zeros((n + 1, m + 1))  # matrice di lunghezza ottima
    raw = np.arange(n) + 1
    column = np.arange(m) + 1
    for i in raw:
        for j in column:
            if Q[i-1] == L[j-1]:  #per Q (e L) il range è tra 0 e n(m)-1, non tra 1 e n(m)
                c[i, j] = c[i-1, j-1] + 1
                #NON mi interessa tenere traccia della sottosequenza, solo la sua lunghezza
            elif c[i-1, j] < c[i, j-1]:
                c[i, j] = c[i, j-1]
            else:
                c[i, j] = c[i-1, j]
    return c[n, m]