#!/usr/bin/python

#!/usr/bin/python
import sys


"""
Prim's alrogithm for Minimum Spanning Tree of a Graph - Adjacency Matrix representation

Complexity = O(V^2) 
"""
class Graph:
	def __init__(self, vetices):
		self.V = vetices
		self._graph = [[0 for row in xrange(vetices)]
						for column in xrange(vetices)]

	def min_key(self, key, mset):
		min = sys.maxint
		min_index = -1

		for v in xrange(self.V):
			if key[v] < min and not mset[v]:
				min = key[v]
				min_index = v

		return min_index                

	def print_mst(self, parent):
		print "Edge \tWeight"
		for i in xrange(1, self.V):
			print i
			print parent[i], "-", i, "\t", self._graph[i][ parent[i] ]

	def prims_MST(self):
		key = [sys.maxint] * self.V
		parent = [None] * self.V
		key[0] = 0
		mset = [False] * self.V

		parent[0] = -1

		for cout in xrange(self.V):
			u = self.min_key(key, mset)

			mset[u] = True

			for v in xrange(self.V):
				if self._graph[u][v] and not mset[v] and key[v] > self._graph[u][v]:
						key[v] = self._graph[u][v]
						parent[v] = u

		self.print_mst(parent)
g  = Graph(5)
g._graph = [ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0],
		   ]
 
g.prims_MST();