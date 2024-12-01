import heapq
import random

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i : [] for i in range(self.vertices)}
        self.MST = {}
        
    def addEdge(self, u, v, w):
        self.graph[u].append((w, v))
        self.graph[v].append((w, u))
        
    def primsMST(self):
        cost = 0
        visited = set()
        heap = []
        visited.add(0)
        for edge in self.graph[0]:
            heapq.heappush(heap, edge)
        
        while len(visited) < self.vertices:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            cost += weight
            visited.add(node)
            for edge in self.graph[node]:
                if edge[1] not in visited:
                    heapq.heappush(heap, edge)
        return cost
        
        
g = Graph(4)
g.addEdge(0, 1, 2)
g.addEdge(0, 3, 6)
g.addEdge(1, 3, 3)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 4)
cost = g.primsMST()
print(cost)