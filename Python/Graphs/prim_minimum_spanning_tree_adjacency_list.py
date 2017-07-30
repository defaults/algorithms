"""
Prim's alrogithm for Minimum Spanning Tree of a Graph - Adjacency List representation

Algorithm Category: Greedy Algoithm
Complexity = O(VLogE)
"""


from collections import defaultdict
import sys

class Heap:
    def __init__(self):
        self.array = []
        self.pos = []
        self.size = 0

    def min_heapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = left + 1

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            self.swap_min_heap_nodes(smallest, idx)
            self.min_heapify(smallest)

    def extract_min(self):

        root = self.array[0]

        last_node = self.array[self.size - 1]
        self.array[0] = last_node

        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.min_heapify(0)

        return root

    def swap_min_heap_nodes(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def is_empty(self):
        return True if self.size == 0 else False

    def decrease_key(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]:
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[(i - 1) / 2][0]] = i
            self.swap_min_heap_nodes(i, (i - 1)/2)

            i = (i - 1) / 2

    def is_in_min_heap(self, vertex):
        print self.pos
        print self.array
        print self.size
        return True if (self.pos[vertex] < self.size) else False


class Graph:

    DEFAULT_WEIGHT = 1

    def __init__(self, vertices):
        self.V = vertices
        self._graph = defaultdict(list)

    def add_edge(self, edge, weight=DEFAULT_WEIGHT):
        src, dest = set(edge)

        new_node =  [src, weight]
        self._graph[src].insert(0, new_node)

        new_node = [dest, weight]
        self._graph[dest].insert(0, new_node)


    def print_mst(self, parent):
        print 'Edge \tWeight'
        for i in xrange(1, self.V):
            print parent[i], '-', i
        print self._graph


    def prims_mst_adjecency_list(self):
        key = [sys.maxint] * self.V
        parent = [None] * self.V
        min_heap = Heap()

        for i in xrange(self.V):
            min_heap.array.append([i, key[i]])
            min_heap.pos.append(i)

        min_heap.pos[0] = 0
        key[0] = 0
        min_heap.decrease_key(0, key[0])

        min_heap.size = self.V

        while min_heap.is_empty() is False:

            new_heap_node = min_heap.extract_min()
            u = new_heap_node[0]

            for p_crawl in self._graph[u]:
                v = p_crawl[0]

                if min_heap.is_in_min_heap(v) and p_crawl[1] < key[v]:
                    print 'here '
                    key[v] = p_crawl[1]
                    parent[v] = u

                    min_heap.decrease_key(v, key[v])


        self.print_mst(parent)

"""Test for Prism's Algorithm for adjacency list"""


graph = Graph(9)
graph.add_edge((0, 1), 4)
graph.add_edge((0, 7), 8)
graph.add_edge((1, 2), 8)
graph.add_edge((1, 7), 11)
graph.add_edge((2, 3), 7)
graph.add_edge((2, 8), 2)
graph.add_edge((2, 5), 4)
graph.add_edge((3, 4), 9)
graph.add_edge((3, 5), 14)
graph.add_edge((4, 5), 10)
graph.add_edge((5, 6), 2)
graph.add_edge((6, 7), 1)
graph.add_edge((6, 8), 6)
graph.add_edge((7, 8), 7)
graph.prims_mst_adjecency_list()

