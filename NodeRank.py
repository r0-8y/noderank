from sys import stdout
from time import time


# noinspection PyShadowingNames
def read_input():
    n, beta = [float(x) for x in input().strip().split(' ')]
    n = int(n)

    adjacency_list = [[0, []]] * n
    for source in range(n):
        nodes = [int(x) for x in input().strip().split(' ')]
        adjacency_list[source] = [len(nodes), nodes]

    q = int(input().strip())

    queries = []
    for _ in range(q):
        query = input().strip().split(' ')
        queries.append((int(query[0]), int(query[1])))

    return n, beta, adjacency_list, q, queries


# noinspection PyShadowingNames
def node_rank(n, beta, adjacency_list):
    r = [[0 for k in range(n)] for j in range(101)]
    r[0] = [(1.0 / n) for i in range(n)]

    for t in range(100):
        r[t + 1] = [((1.0 - beta) / n) for i in range(n)]
        for i in range(n):
            if adjacency_list[i][0]:
                for j in adjacency_list[i][1]:
                    r[t + 1][j] += ((beta * r[t][i]) / adjacency_list[i][0])

    return r


if __name__ == '__main__':
    start = time()
    n, beta, adjacency_list, q, queries = read_input()
    r = node_rank(n, beta, adjacency_list)

    for node, iteration in queries:
        stdout.write("{:.10f}\n".format(r[iteration][node]))
    print(time() - start)
