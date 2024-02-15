
from zad6testy import runtests

from collections import deque

def binworker(M):
    n = len(M)  # Liczba pracowników
    num_vertices = n + n + 2  # Liczba wierzchołków w grafie
    source = 0  # Wierzchołek źródłowy
    sink = num_vertices - 1  # Wierzchołek ujście

    # Tworzenie grafu jako macierzy sąsiedztwa
    graph = [0] * (num_vertices * num_vertices)

    # Dodawanie krawędzi od źródła do pracowników
    for i in range(1, n + 1):
        graph[source * num_vertices + i] = 1

    # Dodawanie krawędzi od maszyn do ujścia
    for j in range(n + 1, num_vertices - 1):
        graph[j * num_vertices + sink] = 1

    # Dodawanie krawędzi między pracownikami a maszynami
    for i in range(n):
        for j in M[i]:
            graph[(i + 1) * num_vertices + (j + n + 1)] = 1

    def bfs():
        visited = [False] * num_vertices
        parent = [-1] * num_vertices
        visited[source] = True
        queue = deque()
        queue.append(source)

        while queue:
            u = queue.popleft()
            for v in range(num_vertices):
                if not visited[v] and graph[u * num_vertices + v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True, parent

        return False, parent

    def find_max_flow():
        max_flow = 0
        while True:
            found_path, parent = bfs()
            if not found_path:
                break
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, graph[u * num_vertices + v])
                v = u
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                graph[u * num_vertices + v] -= path_flow
                graph[v * num_vertices + u] += path_flow
                v = u
        return max_flow

    return find_max_flow()

runtests( binworker, all_tests = True )