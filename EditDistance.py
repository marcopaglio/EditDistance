import numpy as np

def editDistance(X, Y):                #X e Y stringhe da confrontare
    n = len(X)                         #X è sulla ordinata
    m = len(Y)                         #Y è sull'ascissa
    c = np.zeros((n+1, m+1))           #matrice di costi di edit distance
    #op = np.empty_like(c, dtype=np.string_)              #matrice di operazioni di edit distance
    raw = np.arange(n) + 1
    column = np.arange(m) + 1
    c[0, 0] = 0
    #op[0, 0] = None
    for i in raw:
        c[i, 0] = i * cost('delete')
        #op[i, 0] = 'delete'
    for j in column:
        c[0, j] = j * cost('insert')
        #op[0, j] = 'insert'
    for i in raw:
        for j in column:
            if X[i-1] == Y[j-1]:                                        #per X (e Y) il range è tra 0 e n(m)-1, non tra 1 e n(m)
                c[i, j] = c[i-1, j-1] + cost('copy')
                #op[i, j] = 'copy'
            else:
                c[i, j] = c[i - 1, j - 1] + cost('replace')
                #op[i, j] = 'replace'
            if i > 1 and j > 1 and X[i-2] == Y[j-1] and X[i-1] == Y[j-2] and c[i-2, j-2] + cost('swap') < c[i, j]:
                c[i, j] = c[i-2, j-2] + cost('swap')
                #op[i, j] = 'swap'
            if c[i, j] > c[i-1, j] + cost('delete'):
                c[i, j] = c[i-1, j] + cost('delete')
                #op[i, j] = 'delete'
            if c[i, j] > c[i, j-1] + cost('insert'):
                c[i, j] = c[i, j-1] + cost('insert')
                #op[i, j] = 'insert'
    return c[n, m]    ###mi interessa sapere solo quanto è distante, non quali operazioni sono state eseguite###

def cost(op):
    if op == 'copy':
        return 0
    if op == 'replace':
        return 1
    if op == 'swap':
        return 3
    if op == 'insert':
        return 1
    if op == 'delete':
        return 1

