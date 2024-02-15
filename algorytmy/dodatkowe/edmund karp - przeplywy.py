# dziala na matrixie
# waga 0 -> brak krawedzi
import collections

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    q = collections.deque()
    q.append(s)
    visited[s] = True
    while q:
        u = q.popleft()
        for idx, waga in enumerate(graph[u]):
            if (visited[idx] == False) and (waga > 0):
                q.append(idx)
                visited[idx] = True
                parent[idx] = u
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow