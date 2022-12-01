from Models.Graph import Graph
from utils.graphFile import readGraphFile
from algoritmos.DepthFirstSearch import DFS
from algoritmos.BreadthFirstSearch import BFS
from time import time, sleep

import sys

import networkx as nx 
import matplotlib.pyplot as plt

BREAK = False

def graphTraverse(G, type):
    for node in G.nodes:
        G.setVisitedNode(node['value'])
    
    visited = []
    start = time()
    for node in G.nodes:
        if node['visited'] != True:
            if type == 'DFS':
                DFS(G, node['value'], visited)
            elif type == 'BFS':
                BFS(G, node['value'], visited)
                
    end = time()
    
    return [visited, format(end - start)]


if __name__ == '__main__':

    sys.setrecursionlimit(1500)

    graph = readGraphFile(10)

    G = Graph()
    G.generated(nodes=graph[0], edges=graph[1])

    output = graphTraverse(G, type='BFS')

    print('\033[91m------------------- Saida -------------------\033[0m')
    print(f'Resultado em vertices: {output[0]}')

    




