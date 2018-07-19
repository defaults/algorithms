#!/usr/bin/python

"""
Given a graph and a source vertex in  find shortest paths from source to all vertices in the given graph.
Dijkstra algorithm doesnot work for graphs with negative weight edges.

Time Complexity: is O(V^2). If the input graph is represented using adjacency list,
it can be reduced to O(E log V) with the help of binary heap.
"""
from collections import defaultdict
import heapq


class Graph(object):
    """
    Graph class
    """

    def __init__(self, vertices):
        self._graph = defaultdict(dict)
        self.V = vertices

    def add_edge(self, edge, weight):
        """
        Add ege to graph

        :param edge: Set of two vertices
        :param weight: weight between two vertices
        :return:
        """
        u, v = edge

        self._graph[u][v] = weight
        self._graph[v][u] = weight

    def dijkstra(self, src):
        dist = [float('inf') for _ in xrange(self.V)]
        min_heap_ele = []

        seen = set()
        dist[src] = 0
        min_heap_ele.append((0, src))

        heapq.heapify(min_heap_ele)

        while min_heap_ele:
            ele = heapq.heappop(min_heap_ele)

            vertex = ele[1]
            d = ele[0]
            seen.add(vertex)

            for key in self._graph[vertex]:
                if key not in seen:
                    if dist[key] > d + self._graph[vertex][key]:
                        dist[key] = d + self._graph[vertex][key]
                        heapq.heappush(min_heap_ele, (dist[key], key))

        for i in xrange(self.V):
            print(i, dist[i])


g = Graph(4)
g.add_edge([0, 1], 1)
g.add_edge([0, 2], 4)
g.add_edge([2, 3], 2)
g.add_edge([1, 3], 1)
g.add_edge([1, 2], 1)

g.dijkstra(0)

