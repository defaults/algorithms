# Pseudo code

# Python Implementation

from directional_graph import Graph

def DFS(Graph, start):
	graph = Graph.graph()
	visited = []

	dfs_util(graph, start, visited)
	return visited


def dfs_util(graph, start, visited):
	if start in visited:
		return False
	visited.append(start)

	for i in graph[start]:
		if i not in visited:
			dfs_util(graph, i, visited)


if __name__ == "__main__":

	g = {
			"a": {"d": 4},
			"b": {"c": 2},
			"c": {"b": 2, "c": 5, "d": 1, "e": 7},
			"d": {"a": 4, "c": 1},
			"e": {"c": 7},
			"f": {"e": 5}
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
	print'\n'
	print (DFS(graph, 'f'))
