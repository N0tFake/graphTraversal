class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def generated(self, nodes, edges):
        for node in nodes:
            self.addNodes(node)

        for edge in edges:
            self.addEdges(edge)

    def setVisitedNode(self, value, VISITED=False):
        for node in self.nodes:
            if node['value'] == value:
                if VISITED:
                    node['visited'] = True
                else:
                    node['visited'] = False
                break

    def getVisitedNode(self, value):
        for node in self.nodes:
            if node['value'] == value:
                return node['visited']

    def addNodes(self, value):
        self.nodes.append({'value': value, 'visited': False})
    
    # path = [value da vertice, value da vertice]
    def addEdges(self, path):
        self.edges.append(path)

    def neighbors(self, vertice):
        result = []
        for edge in self.edges:    
            if vertice in edge:
                if vertice != edge[0]:
                    result.append(edge[0])
                else:
                    result.append(edge[1])
        
        return result

