def BFS(G, value, visited):
    queue = []
    visited.append(value)
    queue.append(value)
    while queue:
        v = queue.pop(0)
        for neighbor in G.neighbors(v):
            if G.getVisitedNode(neighbor) != True:
                G.setVisitedNode(neighbor, VISITED=True)
                visited.append(neighbor)
                queue.append(neighbor)
