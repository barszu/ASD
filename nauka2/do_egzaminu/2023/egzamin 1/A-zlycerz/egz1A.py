from egz1Atesty import runtests
from queue import PriorityQueue

INF = float("inf")
def dikstra(G, start_node, transform_weight=lambda x: x):
    n = len(G)

    distance = [INF for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, start_node))  # (distance, node)
    while not Q.empty():
        dist, node = Q.get()
        if dist >= distance[node]: continue

        distance[node] = dist  # first and last encounter
        for neighbour, weight in G[node]:
            weight = transform_weight(weight)  # transforming
            if distance[neighbour] > dist + weight:
                Q.put((dist + weight, neighbour))

    return distance


def gold(G, V, s, t, r) -> int:  # wzorcowka, (vertex, weight)
    # dikstra s -> ... (koszt dojazdu do zamku z)
    # dikstra t -> ... (koszt wyjazdu ... do t | t do ... )

    to_target = dikstra(G, s)
    from_target = dikstra(G, t, lambda x: 2*x+r)

    max_cost = -INF
    for i in range(len(G)):
        if to_target[i] == INF or from_target[i] == INF: continue
        max_cost = max( (-to_target[i] + V[i] - from_target[i] ) , max_cost)

    max_cost = max((-to_target[t]), max_cost)


    return -max_cost


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
