"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph. The graph may contain negative weight edges.


Time Complexity: O(VE)
"""

#!/usr/bin/python

import sys


# Bellmon ford for adjecency matric representation of graph

class MatrixGraph:
	def __init__(self, vertices):
		self.V = vertices
		self._graph = [[0 for row in xrange(vertices)]
						for column in xrange(vertices)]

	def print_distance(self, dist):
		print "Vertex  Distance From Source"
		for v in xrange(self.V):
			print v, "\t\t", dist[v]

	def bellmon_ford(self, src):
		dist = [float("INF")] * self.V
		dist[src] = 0

                for i in xrange(self.V - 1):
                    for u in xrange(self.V):
                        for v in xrange(self.V):
                                if dist[u] != float("INF") and dist[v] > dist[u]  + self._graph[u][v]:
                                        dist[v] = self._graph[u][v] + dist[u]

                for u in xrange(self.V):
                    for v in xrange(self.V):
                        if dist[u] != float("INF") and dist[v] > dist[u] + self._graph[u][v]:
                                print "Graph contains negative weight cycle"

                                return

		self.print_distance(dist)



g  = MatrixGraph(9)
g._graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.bellmon_ford(0)

print '\n\n'
# Bellmon ford for adjecency list representation
from collections import defaultdict


class ListGraph:
    def __init__(self, vertices):
        self.V = vertices
        self._graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self._graph[u][v] = w

    def bellmon_ford(self, src):
        dist = [float('INF') for _ in xrange(self.V)]
        dist[src] = 0

        for i in xrange(self.V - 1):
            for u in self._graph:
                for v in self._graph[u]:
                    if dist[u] != float('INF') and dist[v] > dist[u] + self._graph[u][v]:
                        dist[v] = dist[u] + self._graph[u][v]

        for u in self._graph:
            for v in self._graph[u]:
                if dist[u] != float('INF') and dist[v] > dist[u] + self._graph[u][v]:
                    print 'graph contains negative weight cycle'

        print('Distance form src to each vertex')
        print('Index \t distance')
        for i in xrange(self.V):
            print i, '\t\t', dist[i]



g = ListGraph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellmon_ford(0)

