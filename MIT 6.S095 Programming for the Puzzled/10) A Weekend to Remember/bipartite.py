#Programming for the Puzzled -- Srini Devadas
#A Weekend to Remember
#This puzzle deals with the problem of inviting friends to dinner over two days
#such that no two of your friends who dislike each other are invited on the same
#day.  This can be done if the graph is a bipartite graph.

#The code determines if a graph is bipartite or not. If the graph can be colored
#using two colors, it is bipartite, else it is not.

graph = {'B': ['C'],
          'C': ['B', 'D'],
          'D': ['C', 'E', 'F'],
          'E': ['D'],
          'F': ['D', 'G', 'H', 'I'],
          'G': ['F'],
          'H': ['F'],
          'I': ['F']}

graph2 = {'F': ['D', 'I', 'G', 'H'],
          'B': ['C'],
          'D': ['C', 'E', 'F'],
          'E': ['D'],
          'H': ['F'],
          'C': ['D', 'B'],
          'G': ['F'],
          'I': ['F']}

gra3 = {'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']}

grap = {'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['D', 'B'],
        'D': ['A', 'C']}

dgraph = { 'B': ['C'],
            'C': ['B', 'D'],
            'D': ['C', 'E', 'F'],
            'E': ['D'],
            'F': ['D', 'G', 'H', 'I'],
            'G': ['F'],
            'H': ['F'],
            'I': ['F'],
          'F1': ['D1', 'I1', 'G1', 'H1'],
          'B1': ['C1'],
          'D1': ['C1', 'E1', 'F1'],
          'E1': ['D1'],
          'H1': ['F1'],
          'C1': ['D1', 'B1'],
          'G1': ['F1'],
          'I1': ['F1']}

dgraph2 = {'F': ['D', 'I', 'G', 'H'],
            'B': ['C'],
            'D': ['C', 'E', 'F'],
            'E': ['D'],
            'H': ['F'],
            'C': ['D', 'B'],
            'G': ['F'],
            'I': ['F'],
            'A1': ['B1', 'C1'],
            'B1': ['A1', 'C1'],
            'C1': ['A1', 'B1']}

dgraph3 = {'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C', 'E', 'F'],
            'E': ['D'],
            'F': ['D', 'G', 'H', 'I'],
            'G': ['F'],
            'H': ['F'],
            'I': ['F']}

graphc = {'A': ['B', 'D', 'C'],
          'B': ['C', 'A', 'B'],
          'C': ['D', 'B', 'A'],
          'D': ['A', 'C', 'B']}

def bipartiteGraphColor(graph, start, coloring, color):
    if start not in graph:
        return False, {}
    
    if start not in coloring:
        coloring[start] = color
    elif coloring[start] != color:
        cycle = list(coloring.keys())
        cycle.append(start)
        print('Here is a cyclic path that cannot be colored ', cycle)
        return False, {}
    else:
        return True, coloring
    
    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'
        
    for vertex in graph[start]:
        val, coloring = bipartiteGraphColor(graph, vertex, coloring, newcolor)
        if val == False:
            return False, {}
        
    return True, coloring


#Colors a disconnected graph and returns if all sub graphs are colorable
def disconnectedBipartite(graph, coloring):
    for vertex in graph:
        if vertex not in coloring:
            val, coloring = bipartiteGraphColor(graph, vertex, coloring, 'Sha')
            if not val:
                return False, {}
           
    return True, coloring
        

#Finds and prints a possible path from start to end in graph
#using a DFS, if none exists return None
def findPath(graph, start, end, path):
    path = path + [start]
        
    if start == end:
        return path
    
    for vertex in graph[start]:
        if vertex not in path:
            newPath = findPath(graph, vertex, end, path)
            
            if newPath != None:
                return newPath
                        
    return

print (bipartiteGraphColor(gra3, 'A', {}, 'Sha'), end = '\n\n')
print (bipartiteGraphColor(graph, 'B', {}, 'Sha'), end = '\n\n')
print (bipartiteGraphColor(graph2, 'B', {}, 'Sha'), end = '\n\n')
print (bipartiteGraphColor(grap, 'A', {}, 'Sha'), end = '\n\n')
    
print(disconnectedBipartite(dgraph, {}), end = '\n\n')
print(disconnectedBipartite(dgraph2, {}), end = '\n\n')
print(disconnectedBipartite(dgraph3, {}), end = '\n\n')
    
print(bipartiteGraphColor(graphc, 'A', {}, 'Sha'), end = '\n\n')
            
print(findPath(graph, 'B', 'I', []), end = '\n\n')