"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Time Complexity: The algorithm is simply DFS with an extra stack. So time complexity is same as DFS which is O(V+E).
"""

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(set)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].add(v)

    def _topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True
        print vertex
        print '\n'
        for i in self.graph[vertex]:
            if visited[i] is False:
                self._topological_sort_util(i, visited, stack)

        print 'here' + str(vertex)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        print self.graph.items(), self.V
        for each in self.graph.keys():
            if visited[each] is False:
                self._topological_sort_util(each, visited, stack)

        return stack


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print g.topological_sort()
