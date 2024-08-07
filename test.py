import unittest
from scripts.dijkstra import Dijkstra
from scripts.bellmanFord import Bellman_Ford
from scripts.floydWarshall import Floyd_Warshall
from scripts.fcts import csv_to_mtx
import numpy as np
from os import system

def run_test():
    system('python3 test.py')

TEST_PATHS = np.array(["data/test1.csv", "data/test2.csv"])
SOLUTION_PATHS = np.array(["data/soluce1.csv", "data/soluce2.csv"])

class TestAlgorithms(unittest.TestCase):
    solutions = [csv_to_mtx(elem) for elem in SOLUTION_PATHS]
    tests = [csv_to_mtx(elem) for elem in TEST_PATHS]

    def test_dijkstra(self):
        for i in range(len(self.tests)):
            self.assertTrue(np.allclose(Dijkstra(self.tests[i]), self.solutions[i]),
                            f"Dijkstra failed for test case {i}")

    def test_bellman_ford(self):
        for i in range(len(self.tests)):
            self.assertTrue(np.allclose(Bellman_Ford(self.tests[i]), self.solutions[i]),
                            f"Bellman-Ford failed for test case {i}")

    def test_floyd_warshall(self):
        for i in range(len(self.tests)):
            self.assertTrue(np.allclose(Floyd_Warshall(self.tests[i]), self.solutions[i]),
                            f"Floyd-Warshall failed for test case {i}")

if __name__ == "__main__":
    unittest.main()
