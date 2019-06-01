"""
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.

Time Complexity: O(V^3) - where V is no of vertex
"""

def floyd_warshall(graph):
    V = len(graph)
    dist = map(lambda i : map(lambda j : j , i), graph)

    for k in xrange(V):
        for j in xrange(V):
            for i in  xrange(V):

                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def print_solution(dist):
    V = len(dist)
    for i in xrange(V):
        for j in xrange(V):
            if dist[i][j] == INF:
                print '%7s' %('INF')
            else:
                print '%7d' %(dist[i][j])
            if j == V - 1:
                print ''

    return


# weighted graph
graph = [[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]]


# Print the solution
floyd_warshall(graph)

