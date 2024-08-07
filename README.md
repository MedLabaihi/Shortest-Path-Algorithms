# Shortest Path Algorithms
## Overview

This project provides implementations of three classic shortest path algorithms, which are fundamental in graph theory and network analysis. The algorithms are designed to compute shortest paths in weighted graphs and are applied to graph data read from CSV files. The project includes unit tests to verify the correctness of these implementations.
This project implements and compares three classic shortest path algorithms:

1. **Bellman-Ford Algorithm**
2. **Dijkstra's Algorithm**
3. **Floyd-Warshall Algorithm**

## Table of Contents

1. [Overview](#overview)
2. [Algorithms](#algorithms)
3. [Complexity Analysis](#complexity-analysis)
4. [File Structure](#file-structure)
   - [Data Files](#data-files)
   - [Script Files](#script-files)
   - [Test File](#test-file)
   - [Main File](#main-file)
5. [Usage](#usage)
   - [Running the Main Script](#running-the-main-script)
   - [Running Tests](#running-tests)
6. [Contact](#contact)


### Algorithms

1. **Bellman-Ford Algorithm**:
   - Suitable for graphs with negative edge weights and detects negative weight cycles.

2. **Dijkstra's Algorithm**:
   - Efficient for graphs with non-negative edge weights and finds the shortest path from a single source vertex to all other vertices.

3. **Floyd-Warshall Algorithm**:
   - Computes shortest paths between all pairs of vertices in a graph, handling graphs with any edge weights.

## Complexity Analysis

- **Bellman-Ford Algorithm**:
  - **Time Complexity**: \( O(V \cdot E) \)
    - \( V \): Number of vertices
    - \( E \): Number of edges
  - **Space Complexity**: \( O(V) \)

- **Dijkstra's Algorithm**:
  - **Time Complexity**:
    - Using a Binary Heap: \( O((V + E) \log V) \)
    - Using a Fibonacci Heap: \( O(E + V \log V) \)
  - **Space Complexity**: \( O(V + E) \)

- **Floyd-Warshall Algorithm**:
  - **Time Complexity**: \( O(V^3) \)
  - **Space Complexity**: \( O(V^2) \)

## File Structure

### Data Files

- [data/graph.csv](data/graph.csv): Default graph data file.
- [data/graph2.csv](data/graph2.csv): Additional graph data file (can be used similarly to `graph.csv`).
- [data/test1.csv](data/test1.csv), [data/test2.csv](data/test2.csv): Test graph data files.
- [data/soluce1.csv](data/soluce1.csv), [data/soluce2.csv](data/soluce2.csv): Expected solution files for tests.

### Script Files

- [scripts/fcts.py](scripts/fcts.py): Contains utility functions like `csv_to_mtx`.
- [scripts/bellmanFord.py](scripts/bellmanFord.py): Implementation of the Bellman-Ford algorithm.
- [scripts/dijkstra.py](scripts/dijkstra.py): Implementation of Dijkstra's algorithm.
- [scripts/floydWarshall.py](scripts/floydWarshall.py): Implementation of the Floyd-Warshall algorithm.

### Test File

- [test.py](test.py): Unit tests for the algorithms.

### Main File

- [main.py](main.py): Main script to run the algorithms and compare their outputs.

## Usage

### Running the Main Script

To run the main script and compute shortest paths using default graph data (`graph.csv`):

```bash
python main.py
```
To specify a different CSV file for graph data and enable verbosity:

```bash
python main.py -f data/graph2.csv -v
```
### Running Tests

To run all unit tests:

```bash
python test.py
```

To run tests before executing the main program:

```bash
python main.py -t
```

To run tests only:

```bash
python main.py -to
```

## Contact

For any questions or feedback, please contact:

**Labaihi Mohammed**  
Email: [m.labaihi01@gmail.com](mailto:m.labaihi01@gmail.com)
