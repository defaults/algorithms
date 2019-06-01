class Graph:
    def __init__(self, graph_dict=None):
        """initializes a graph object"""
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dist = graph_dict

    def __str__(self):
        return "Undirected Graph \nNodes: %s \nEdges: %s" % (
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

    def add_edge(self, edge):
        u, v = set(edge)
        if u not in self.__graph_dist:
            self.__graph_dist[u] = v
        else:
            self.__graph_dist[u].append(v)

        if v not in self.__graph_dist:
            self.__graph_dist[v] = u
        else:
            self.__graph_dist[v].append(u)

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dist:
            self.__graph_dist[vertex] = []

    def has_edge(self, edge):
        u, v = set(edge)
        return (v in self.__graph_dist.get(u, []))

    def delete_edge(self, edge):
        u, v = set(edge)
        if self.has_edge(edge):
            self.__graph_dist[v].remove(u)
            self.__graph_dist[u].remove(v)

    def delete_vertex(self, vertex):
        if vertex in self.__graph_dist:
            for edge in self.__graph_dist[vertex]:
                self.delete_edge((vertex, edge))
            del self.__graph_dist[vertex]

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
            "a": ["d"],
            "b": ["c"],
            "c": ["b", "c", "d", "e"],
            "d": ["a", "c"],
            "e": ["c"]
    }

    graph = Graph(g)
    print graph
    print("Vertices of graph:")
    print(graph.list_vertices())
    print("\nEdges of graph:")
    print(graph.list_edges())

    print("\nAdding a vertice")
    graph.add_vertex("g")
    print (graph.list_vertices())

    graph.add_edge(("g", "a"))
    graph.add_edge(("a", "c"))
    graph.add_edge(("f", "c"))
    print("\nEdges of graph:")
    print(graph.list_edges())
    print (graph.list_vertices())
    print(graph.graph())

    print(graph.has_edge(("a", "c")))
    print(graph.graph())

    print("\nDeleting edge (a, c):")
    graph.delete_edge(("a", "c"))
    print(graph.list_edges())
    print (graph.list_vertices())
    print(graph.graph())
    print("\nDeleting vertex a:")
    graph.delete_vertex("a")
    print (graph.list_vertices())
    print(graph.list_edges())
    print(graph.graph())

    print("\nPath between b - e")
    print(graph.find_path("b", "e"))
