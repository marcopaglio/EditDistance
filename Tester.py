from NameCalculator import *
from NGram import *
from timeit import default_timer as timer
from decimal import *
import numpy as np
import matplotlib.pyplot as plt

#I test implicano la ricerca di alcune query con o senza l'ausilio degli nGram
#verranno eseguiti più volte per calcolare tempi più attendibili

numWords = 7
getcontext().prec = 4

def openFile(file):                       #fileDict è il dizionario di parole da confrontare, deve avere anche l'estensione
    in_file = open(file, "r")             #apre file in lettura
    text = in_file.read()                                   #legge i dati e li scrive in text (stringa)
    in_file.close()                                         #chiude il file in lettura
    list = text.split("\n")                                 #crea una lista delle parole separate da \n
    return list

def main():
    Query = ['abbondanzio', 'marca', 'luha', 'anna']

    ###apertura e conversione in lista del file.text in input###
    vocabulary = openFile("9000_nomi_propri.txt")

    result = []            #memorizza i nomi simili

    recordName = {}
    for i in Query:
        recordName[i] = 0  # inizializzo tempi a 0

    recordGramName = {}
    for i in Query:
        recordGramName[i] = 0  # inizializzo tempi a 0

    for query in Query:
        print('Cerchiamo le parole vicine a', query)
        (numGram, gramQ) = chooseGram(query)

        ###TEST senza Ngram###
        for i in range(5):
            start = Decimal(timer())
            result = nameCalculator(query, numWords, vocabulary)
            end = Decimal(timer())
            time = end - start
            print('Senza nGram servono ', time, 's. ')
            recordName[query] += time
        recordName[query] = recordName[query] / 5
        print('Le parole trovate sono :>', result)

        ###TEST con Ngram###
        for i in range(5):
            start = Decimal(timer())
            ###Calcolo parole vicine tramite NGram###
            nearestNames = jaccardGram(vocabulary, numGram, gramQ)
            result = nameCalculator(query, numWords, nearestNames)
            end = Decimal(timer())
            time = end - start
            print('Con nGram servono ', time, 's.')
            recordGramName[query] += time
        recordGramName[query] = recordGramName[query] / 5
        print('Le parole trovate sono :>', result)


    ###DISEGNA tabella###
    listName = list(recordName.values())
    listGramName = list(recordGramName.values())
    data = [listName, listGramName]

    columns = ('Abbondanzio', 'Marca', 'Luha', 'Anna')
    rows = ['Senza gram', 'Con gram']

    values = np.arange(5)
    value_increment = 1

    #Definisce i colori del grafico
    colors = plt.cm.autumn(np.linspace(1, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4

    #Disegna la tabella
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=0, color=colors[row])
        cell_text.append([x for x in data[row]])

    #Aggiunge la tabella in fondo al grafico
    the_table = plt.table(cellText=cell_text,
                          rowLabels=rows,
                          rowColours=colors,
                          colLabels=columns,
                          loc='bottom')

    #Aggiusta la posizione
    plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.ylabel("Tempo di esecuzione")
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Differenza di tempo di Edit Distance')

    plt.show()


if __name__ == '__main__':
    main()