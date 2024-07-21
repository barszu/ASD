from kol2testy import runtests

# Funkcja do znajdowania liczby wierzchołków
def find_vertex_no(E):
    maxy = -1 #największy numer wierzchołka
    for u, v, weight in E:
        maxy = max(maxy, u, v)
    return maxy + 1 # jako n - liczba wierzchołków

# Funkcja do tworzenia grafu
def create_graph(E):
    n = find_vertex_no(E)
    G = [[] for u in range(n)] # (v, weight)
    used_edges = [[False for _ in range(n)] for __ in range(n)]
    for u, v, weight in E:
        if not used_edges[u][v] and not used_edges[v][u]: #ta krawędź nie była użyta
            G[u].append((v, weight))
            G[v].append((u, weight))
            # oznacz jako użyta
            used_edges[u][v] = True
            used_edges[v][u] = True
    return G

from queue import PriorityQueue

# Algorytm Dijkstry z obsługą maksymalnego czasu podróży bez odpoczynku
def dikstra(G, start_node, end_node, max_travel_time=16, rest_time=8):
    n = len(G)
    INF = float('inf')
    distance = [[INF for __ in range(max_travel_time + 1)] for _ in range(n)] # [u][travel_time]
    visited = [[False for __ in range(max_travel_time + 1)] for _ in range(n)] # [u][travel_time]
    Q = PriorityQueue()

    Q.put((0, start_node, 0)) # (curr_dist, start_node, travel_time)

    while not Q.empty():
        curr_d, u, t = Q.get()

        if visited[u][t]:
            continue

        visited[u][t] = True
        distance[u][t] = curr_d

        for (v, weight) in G[u]: # sąsiad u
            if weight > max_travel_time:
                continue # tej krawędzi nie da się przejść

            if t + weight > max_travel_time: # będzie musiał odpocząć
                new_d = curr_d + weight + rest_time
                new_t = weight
            else: # podróżuje dalej
                new_d = curr_d + weight
                new_t = t + weight

            if new_d < distance[v][new_t]:
                Q.put((new_d, v, new_t))
                distance[v][new_t] = new_d

    res = min(distance[end_node])
    return res if res != INF else -1

# Funkcja główna
def warrior(G, s, t):
    G = create_graph(G)
    res = dikstra(G, s, t, max_travel_time=16, rest_time=8)
    return res


runtests( warrior, all_tests = True )