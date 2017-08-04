#!/usr/bin/python

"""
Given a graph and a source vertex in  find shortest paths from source to all vertices in the given graph.
Dijkstra algorithm doesnot work for graphs with negative weight edges.

Time Complexity: is O(V^2). If the input graph is represented using adjacency list, it can be reduced to O(E log V) with the help of binary heap.
"""

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self._graph = [[0 for row in xrange(vertices)]
                        for column in xrange(vertices)]

    def print_solution(self, dist):
        print "Vertex distance from source"
        for node in xrange(self.V):
            print node, "\t", dist[node]

    def min_distance(self, dist, spt_set):
        min_val = sys.maxint
        min_vertex = -1

        for v in xrange(self.V):
            if dist[v] < min_val and not spt_set[v]:
                min_val = dist[v]
                min_vertex = v

        return min_vertex

    def dijkstra_adjecency_matrix(self, src):
        dist = [sys.maxint] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for count in xrange(self.V):
            u = self.min_distance(dist, spt_set)

            spt_set[u] = True

            for v in xrange(self.V):
                if self._graph[u][v] and not spt_set[v] and dist[v] > dist[u] + self._graph[u][v]:
                        dist[v] = dist[u] + self._graph[u][v]

        self.print_solution(dist)


g  = Graph(9)
g._graph = [ [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]];

g.dijkstra_adjecency_matrix(0);

