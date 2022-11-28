def DFS(G, value, visited):
    visited.append(value)
    G.setVisitedNode(value, VISITED=True)    
    for neighbor in G.neighbors(value):
        if G.getVisitedNode(neighbor) != True:
            DFS(G, neighbor, visited)
