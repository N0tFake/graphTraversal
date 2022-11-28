from Models.Graph import Graph
from utils.graphFile import readGraphFile
from algoritmos.DepthFirstSearch import DFS
from algoritmos.BreadthFirstSearch import BFS
from time import time

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

    output = readGraphFile(10)

    G = Graph()
    G.generated(nodes=output[0], edges=output[1])

    print('grafo criado: \n', G.nodes, '\n')
    print(G.edges, '\n\n')

    output = graphTraverse(G, type='BFS')

    print('DFS rodado: \n', G.nodes)
    print(output)




