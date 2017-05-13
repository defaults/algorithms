"""
Pseudo code

Breadth-First-Search(Graph, root):

    create empty set S
    create empty queue Q

    root.parent = NIL
    Q.enqueue(root)

    while Q is not empty:
        current = Q.dequeue()
        if current is the goal:
            return current
        for each node n that is adjacent to current:
            if n is not in S:
                add n to S
                n.parent = current
                Q.enqueue(n)

Implementation
"""
from collections import deque
from directional_graph import Graph


def BFS(Graph, s):
    graph = Graph.graph()
    if s not in graph:
        raise Exception("Edge %s not in graph" % s)
    q = deque([s])
    visited = set([s])
    while len(q) != 0:
        node = q.popleft()
        print graph
        for each in graph[node]:
            print visited
            if each not in visited:
                visited.add(each)
                q.append(each)
    return visited


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
#    print("\nDeleting vertex a:")
#    graph.delete_vertex("a")
    print (graph.list_vertices())
    print(graph.list_edges())
    print(graph.graph())

    print("\nPath between b to e:")
    print(graph.find_path("b", "e"))

    print("\nSetting edge weight for (c, e):")
    graph.set_edge_weight(("c", "e"), 2)
    print(graph.graph())

    print '\n'
    print (BFS(graph, 'e'))
