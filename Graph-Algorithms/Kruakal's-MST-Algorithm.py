class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i : [] for i in range(self.vertices)}
        self.MST = {}
        
    def addEdge(self, u, v, w):
        self.graph[u].append((w, n))
        self.graph[v].append((w, u))
        
    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            
        
    def kruskalsMST(self):
        