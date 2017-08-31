#!/usr/bin/python

import sys

class Graph:
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

		for u in xrange(self.V - 1):
			for v in xrange(self.V - 1):
				if dist[u] != float("INF") and dist[v] > dist[u]  + self._graph[u][v]:
					dist[v] = self._graph[u][v] + dist[u]

		for u, v in self._graph:
			if dist[u] != float("INF") and dist[v] > dist[u] + w:
				print "Graph contains negative weight cycle"

				return

		self.print_distance(dist)			

g  = Graph(9)
g._graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		   [4, 0, 8, 0, 0, 0, 0, 11, 0],
		   [0, 8, 0, 7, 0, 4, 0, 0, 2],
		   [0, 0, 7, 0, 9, 14, 0, 0, 0],
		   [0, 0, 0, 9, 0, 10, 0, 0, 0],
		   [0, 0, 4, 14, 10, 0, 2, 0, 0],
		   [0, 0, 0, 0, 0, 2, 0, 1, 6],
		   [8, 11, 0, 0, 0, 0, 1, 0, 7],
		   [0, 0, 2, 0, 0, 0, 6, 7, 0]
		  ];
 
g.bellmon_ford(0);