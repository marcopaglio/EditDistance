from EditDistance import *


def nameCalculator(Query, numWords, nearestNames):     #numWorks è il numero massimo di parole vicine che vogliono vedere
    ordWords = {}                   #indica la classifica delle parole rispetto alla distanza
    probableNames = []              #contiene le parole il cui ordine indica l'importanza
    for j in nearestNames:
        thisDistance = editDistance(Query, j)
        yetPut = len(probableNames)
        # se è la prima parola la inserisco
        if yetPut == 0:
            ordWords[1] = thisDistance
            probableNames.append(j)
        #se posso ancora inserire parole o la distanza dell'ultima è maggiore di quella appena calcolata
        elif yetPut < numWords or thisDistance < ordWords[yetPut]:
            if yetPut < numWords:                           #nel caso in cui non avessi raggiunto la massima estensione
                probableNames.insert(yetPut, j)             #inserisco il valore in fondo alla lista
                yetPut += 1                                 #e ne aumento la dimensione
           #devo sostituire il valore con l'ultimo e farlo scalare nella giusta posizione
            count = yetPut - 1
            while count >= 1 and ordWords[count] > thisDistance:
                ordWords[count + 1] = ordWords[count]  # copio il valore nella locazione successiva
                probableNames[count] = probableNames[count - 1]
                count -= 1
            ordWords[count + 1] = thisDistance
            probableNames[count] = j
    return probableNames                                #faccio tornare i nomi probabili

