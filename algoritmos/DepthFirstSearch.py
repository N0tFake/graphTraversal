import sys

def DFS(G, value, visited):
    sys.setrecursionlimit(5000)
    visited.append(value)
    G.setVisitedNode(value, VISITED=True)    
    for neighbor in G.neighbors(value):
        if G.getVisitedNode(neighbor) != True:
            DFS(G, neighbor, visited)
