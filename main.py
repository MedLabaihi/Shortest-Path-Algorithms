"""
This script runs the main program for evaluating shortest path algorithms on a graph.
It supports the following command-line arguments:

- -f or --file: Specify the path to a CSV file containing the graph data. Defaults to 'data/graph.csv' if not provided.
- -v or --verbose: Enable verbose output to display detailed execution time for each algorithm.
- -t or --tests: Execute unit tests defined in 'test.py' before running the main program.
- -to or --testOnly: Run unit tests only and skip the execution of the main program.

You can specify the CSV file containing the graph data via the command line.

You can use:
- `graph.csv` for default testing
- `graph2.csv` as an alternative or additional graph data file

Don't forget to ensure the correct path to the CSV file and provide the appropriate verbosity option for detailed output.
"""

from scripts.fcts import csv_to_mtx
from scripts.bellmanFord import Bellman_Ford
from scripts.dijkstra import Dijkstra
from scripts.floydWarshall import Floyd_Warshall
from test import run_test
from datetime import datetime
import argparse

def main(path: str = "data/graph.csv", verbosity: bool = False):
    if verbosity:
        print("\nFile to use: ", path, "\n")  # print the used file if verbosity is active in option
    else:
        print()  # add a blank line at the top of the file

    C = csv_to_mtx(path)
    print('Costs matrix:\n', C, '\n')  # print the result of the transformation of the file .csv to matrix

    start = datetime.now()  # get time of the algorithm running
    bellman_ford = Bellman_Ford(C)   # run the Bellman-Ford algorithm and store the result
    stop = datetime.now()  # get the stop time of the algorithm
    print("Bellman-Ford:\n", bellman_ford)  # print the matrix returned by Bellman-Ford algorithm
    if verbosity:
        print("Running time: ", stop - start)  # print the running time if verbosity is active
    print()

    start = datetime.now()  # get the start time of the algorithm
    dijkstra = Dijkstra(C)  # run the Dijkstra algorithm and store the result
    stop = datetime.now()  # get the stop time of the algorithm
    print("Dijkstra:\n", dijkstra)  # print the matrix returned by Dijkstra algorithm
    if verbosity:
        print("Running time: ", stop - start)  # print the running time if verbosity is active
    print()

    start = datetime.now()  # get the start time of the algorithm
    floyd_warshall = Floyd_Warshall(C)  # run the Floyd-Warshall algorithm and store the result
    stop = datetime.now()  # get the stop time of the algorithm
    print("Floyd-Warshall:\n", floyd_warshall)  # print the matrix returned by Floyd-Warshall algorithm
    if verbosity:
        print("Running time: ", stop - start)  # print the running time if verbosity is active

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="File .csv you want to use as costs graph", type=str)
    parser.add_argument('-v', '--verbose', help="Verbosity", action="store_true")
    parser.add_argument('-t', '--tests', help="Run tests before the main program", action="store_true")
    parser.add_argument('-to', '--testOnly', help="Run tests only and don't run the main program", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print('\t**********************\t')
        print('\t\tRunning')
        print('\t**********************\t\n')

    if args.tests or args.testOnly:
        run_test()

    if not args.testOnly:
        if not args.file:
            main(verbosity=args.verbose)
        else:
            main(path=args.file, verbosity=args.verbose)
