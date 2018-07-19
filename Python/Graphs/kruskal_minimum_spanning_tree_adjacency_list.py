#!/usr/bin/python

class Subset:
    parent = None
    rank = 0


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self._graph = []
        self.subsets = [None for i in xrange(vertices)]

    def add_edge(self , u, v, weight):
        self._graph.append([u, v, weight])

    def find(self, index):
        if self.subsets[index].parent != index:
            self.subsets[index].parent = self.find(self.subsets[index].parent)

        return self.subsets[index].parent

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.subsets[x_root].rank < self.subsets[y_root].rank:
            self.subsets[x_root].parent = y_root
        elif self.subsets[x_root].rank > self.subsets[y_root].rank:
            self.subsets[y_root].parent = x_root

        else:
            self.subsets[x_root].parent = y_root
            self.subsets[y_root].rank += 1

    def kruskal_mst(self):
        result = []

        self._graph = sorted(self._graph, key=lambda item: item[2])

        for i in xrange(self.V):
            subset = Subset()
            subset.parent = i
            subset.rank = 0

            self.subsets[i] = subset

        i  = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self._graph[i]
            i += 1
            u_parent = self.find(u)
            v_parent = self.find(v)

            if u_parent != v_parent:
                e = e + 1
                self.union(u_parent, v_parent)
                result.append([u, v, w])

        print('Printing Minimum spanning tree:')
        for u, v, w in result:
            print('%d -- %d == %d' % (u, v, w))

# Driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()

