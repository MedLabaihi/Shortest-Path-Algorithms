import numpy as np

def Bellman_Ford(mtx):
	"""
    Computes shortest paths from each node to every other node in a weighted graph using the Bellman-Ford algorithm.

    Parameters:
    mtx (list of list of int): Adjacency matrix representing the graph.

    Returns:
    np.ndarray: Matrix where entry (i, j) represents the shortest distance from node i to node j.
    """
	n = len(mtx)
	sol = []

	for start in range(n):
		dist = [float('inf')] * n
		dist[start] = 0

		# Relax edges up to n-1 times
		for _ in range(n - 1):
			for u in range(n):
				for v in range(n):
					if mtx[u][v] != 0 and dist[u] != float('inf') and dist[u] + mtx[u][v] < dist[v]:
						dist[v] = dist[u] + mtx[u][v]

		# Check for negative-weight cycles
		for u in range(n):
			for v in range(n):
				if mtx[u][v] != 0 and dist[u] != float('inf') and dist[u] + mtx[u][v] < dist[v]:
					raise ValueError("Graph contains a negative-weight cycle")

		sol.append(dist)

	return np.array(sol)

# Example usage
graph = [
	[0, 6, 7, 0, 0, 0, 0, 0, 0, 0],  # A
	[0, 0, 8, 5, 3, 0, 0, 0, 0, 0],  # B
	[0, 0, 0, 0, 9, 2, 0, 0, 0, 0],  # C
	[0, 0, 0, 0, 4, 0, 6, 0, 0, 0],  # D
	[0, 0, 0, 0, 0, 4, 2, 0, 0, 0],  # E
	[0, 0, 0, 0, 0, 0, 3, 1, 0, 0],  # F
	[0, 0, 0, 0, 0, 0, 0, 5, 0, 0],  # G
	[0, 0, 0, 0, 0, 0, 0, 0, 2, 7],  # H
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # I
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # J
]

print(Bellman_Ford(graph))
