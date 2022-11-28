def readGraphFile(tamanho):
    result = {}
    with open(f'./GraphFiles/graph-{tamanho}.txt', 'r') as file:
        lines = file.readlines()
        nodes = [int(x) for x in lines[0].replace('\n', '').split(',')]
        edges = []
        for i in range(len(lines)):
            if i != 0:
                line = [int(x) for x in lines[i].replace('\n', '').split(',')]
                edges.append(line)
        
    return [nodes, edges]
