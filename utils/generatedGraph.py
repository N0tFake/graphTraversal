import networkx as nx 
import os

import matplotlib.pyplot as plt


number = 10

numberNodes = numberEdges = number

G = nx.gnm_random_graph(numberNodes, numberEdges)

Gr = nx.gn_graph(5)

nx.draw(Gr, with_labels=True)
plt.show()

listNodes = list(G.nodes())
listEdges = list(G.edges())

nameFile = 'graph-' + str(numberNodes) + '.txt'

with open(f'../GraphFiles/{nameFile}', 'w') as file:
    aux = ''
    for i in range(len(listNodes)):
        if i != len(listNodes)-1:
            aux += str(listNodes[i]) + ','
        else: 
            aux += str(listNodes[i]) + '\n'

    file.write(aux)

    edges = []
    for edge in listEdges:
        file.write(f"{edge[0]},{edge[1]}\n")
