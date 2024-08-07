import numpy as np
import heapq

def Dijkstra(W):
    """
    Compute the shortest paths between all pairs of vertices using Dijkstra's algorithm.

    :param W: numpy.ndarray, the adjacency matrix with edge costs
    :return: numpy.ndarray, matrix of shortest paths between each node
    """
    if not isinstance(W, (np.ndarray, np.generic)):
        W = np.array(W)

    n = W.shape[0]

    if W.shape[0] != W.shape[1]:
        raise ValueError('Matrix of costs must be a square matrix')

    if not np.allclose(W, W.T):
        raise ValueError('Matrix must be symmetrical')

    L = np.full((n, n), float('inf'))
    np.fill_diagonal(L, 0)

    def dijkstra_single_source(W, start):
        dist = np.full(n, float('inf'))
        dist[start] = 0
        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)
            if u in visited:
                continue
            visited.add(u)

            for v in range(n):
                if W[u, v] > 0 and v not in visited:
                    new_dist = current_dist + W[u, v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(priority_queue, (new_dist, v))

        return dist

    for i in range(n):
        L[i] = dijkstra_single_source(W, i)

    return L

# Example usage with a larger graph
graph = [
    [0, 10, 15, 0, 0, 0],
    [10, 0, 35, 25, 0, 0],
    [15, 35, 0, 30, 20, 0],
    [0, 25, 30, 0, 15, 10],
    [0, 0, 20, 15, 0, 5],
    [0, 0, 0, 10, 5, 0]
]

print(Dijkstra(graph))