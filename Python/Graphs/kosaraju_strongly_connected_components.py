"""
A directed graph is strongly connected if there is a path between all pairs of vertices. A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph.

Time Complexity: The above algorithm calls DFS, fins reverse of the graph and again calls DFS. DFS takes O(V+E) for a graph represented using adjacency list. Reversing a graph also takes O(V+E) time. For reversing the graph, we simple traverse all adjacency lists.

Time Complexity: O(V + E)
"""


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)

    def fill_order(self, vertex, visited, stack):
        visited[vertex] = True

        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.fill_order(neighbour, visited, stack)

        stack.append(vertex)

    def get_traspose(self):
        g = Graph(self.V)

        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)

        return g

    def dfs_util(self, vertex, visited, curr_res):
        visited[vertex] = True

        curr_res.append(vertex)

        for u in self.graph[vertex]:
            if visited[u] == False:
                self.dfs_util(u, visited, curr_res)

    def get_strongly_connected_component(self):
        stack = []
        result = []

        visited = [False for i in xrange(self.V)]

        for u in xrange(self.V):
            if visited[u] == False:
                self.fill_order(u, visited, stack)

        transposed_graph = self.get_traspose()

        visited = [False for i in xrange(self.V)]

        while stack:
            vertex = stack.pop()

            if visited[vertex] == False:
                curr_res = []
                transposed_graph.dfs_util(vertex, visited, curr_res)
                result.append(curr_res)

        return result


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print g.get_strongly_connected_component()

