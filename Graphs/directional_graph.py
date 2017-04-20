#!/usr/bin/python


class Graph:
    """
    Directed Graph class - containing vertices and edges
    """

    DEFAULT_WEIGHT = 1
    DIRECTED = True

    def __init__(self, graph_dict=None):
        """initializes a graph object"""
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dist = graph_dict

    def __str__(self):
        return "Directed Graph \nNodes: %s \nEdges: %s" % (
            self.list_vertices(), self.list_edges())

    def graph(self):
        return self.__graph_dist

    def list_vertices(self):
        return list(self.__graph_dist.keys())

    def list_edges(self):
        return self.__generate_edges()

    def __generate_edges(self):
        graph_edges = []
        for vertex in self.__graph_dist:
            for neighbour in self.__graph_dist[vertex]:
                if {vertex, neighbour} not in graph_edges:
                    graph_edges.append({vertex, neighbour})

        return graph_edges

    def add_edge(self, edge, weight=DEFAULT_WEIGHT):
        u, v = set(edge)
        if u not in self.__graph_dist[v] and v not in self.__graph_dist[u]:
            self.__graph_dist[v][u] = weight

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dist:
            self.__graph_dist[vertex] = {}

    def has_edge(self, edge):
        u, v = set(edge)
        return (v in self.__graph_dist.get(u, []))

    def delete_edge(self, edge):
        u, v = set(edge)
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        del self.__graph_dist[v][u]

    def delete_vertex(self, vertex):
        if vertex in self.__graph_dist:
            for edge in list(self.__graph_dist[vertex]):
                self.delete_edge((vertex, edge))
            del(self.__graph_dist[vertex])

    def set_edge_weight(self, edge, weight):
        u, v = set(edge)
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        self.__graph_dist[u][v] = weight

    def get_edge_weight(self, edge):
        u, v = set(edge)
        if not self.has_edge(edge):
            raise Exception("%s not an existing edge" % edge)
        return self.__graph_dist[u].get(v, self.DEFAULT_WEIGHT)

    def find_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path
        if start_vertex not in self.__graph_dist:
            return None
        for vertex in self.__graph_dist[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path

        return None


if __name__ == "__main__":

    g = {
            "a": {"d": 4},
            "b": {"c": 2},
            "c": {"b": 2, "c": 5, "d": 1, "e": 7},
            "d": {"a": 4, "c": 1},
            "e": {"c": 7}
    }

    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.list_vertices())
    print("\nEdges of graph:")
    print(graph.list_edges())

    print("\nAdding a vertice")
    graph.add_vertex("g")
    print (graph.list_vertices())

    graph.add_edge(("g", "a"))
    graph.add_edge(("a", "c"))
    graph.add_edge(("g", "c"))
    print("\nEdges of graph:")
    print(graph.list_edges())
    print (graph.list_vertices())
    print(graph.graph())

    print(graph.has_edge(("a", "c")))
    print(graph.graph())

    print("\nDeleting edge (a, d):")
    graph.delete_edge(("a", "d"))
    print(graph.list_edges())
    print (graph.list_vertices())
    print(graph.graph())
    print("\nDeleting vertex a:")
    graph.delete_vertex("a")
    print (graph.list_vertices())
    print(graph.list_edges())
    print(graph.graph())

    print("\nPath between b to e:")
    print(graph.find_path("b", "e"))

    print("\nSetting edge weight for (c, e):")
    graph.set_edge_weight(("c", "e"), 2)
    print(graph.graph())
