import math
from LCS import *
#A partire da una parola X e un indice di Ngram numGram,
#Ngram calcola tutti gli numGram-gram di X e li restituisce
#tramite una lista. Se numGram >= len(X) restituisce la parola stessa

limit = 0.6

def nGram(X, numGram):
    n = len(X)
    if numGram >= n:
        return X
    listGram = []
    count = numGram
    while count <= n:
        gram = X[count - numGram : count]
        listGram.append(gram)
        count += 1
    return listGram

def chooseGram(Query):
    #la scelta di quale indice di ngram utilizzare si può effettuare sulla base della lunghezza di Query
    n = len(Query)
    #una buona scelta può essere il logaritmo in base 2 di n
    numGram = int(math.log(n, 2))
    #tuttavia si pone un limite inferiore dell'indice
    if numGram < 2:
        numGram = 2
    gramQ = nGram(Query, numGram)                                   #gramQ = list di ngram di Query
    return numGram, gramQ

def jaccardGram(vocabulary, numGram, gramQ):
    # leggo una parola alla volta, ne calcolo gli ngram e li confronto con gramQ
    nearestNames = []
    for i in vocabulary:
        gramL = nGram(i, numGram)
        nPositive = LCSLength(gramQ, gramL)
        # per decidere se inserire o meno la parola nella lista uso il coefficente di Jaccard
        union = set().union(gramQ, gramL)
        jaccard = nPositive / len(union)
        ###Il coefficiente assume un valore > 1 se alcuni ngram sono uguali, a causa dell'unione###
        if jaccard >= limit:
            nearestNames.append(i)
    return nearestNames