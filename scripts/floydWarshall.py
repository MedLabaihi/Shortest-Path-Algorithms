import numpy as np

def Floyd_Warshall(m):
    # Convert to numpy array if not already
    mtx = np.array(m, dtype=float)

    n = len(mtx)

    # Ensure the matrix is square
    if mtx.shape[0] != mtx.shape[1]:
        raise ValueError("The adjacency matrix must be square.")

    # Initialize distance matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                mtx[i][j] = 0
            elif mtx[i][j] == 0:
                mtx[i][j] = float('inf')

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mtx[i][k] < float('inf') and mtx[k][j] < float('inf'):
                    mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j])

    return mtx