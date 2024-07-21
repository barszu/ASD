from egz1btesty import runtests
from collections import deque
from queue import PriorityQueue

INF = float("inf")


def planets(D, C, T, E):
    D = [D[0]] + [D[i] - D[i-1] for i in range(1, len(D))]
    n = len(C)  # ilosc planet

    def dikstra(start, end):
        distance = [[INF for _ in range(E + 1)] for __ in range(n)]  # cost

        Q = PriorityQueue()
        Q.put((0, start, 0))  # (curr_cost, vertex, fuel)
        while not Q.empty():
            curr_cost, vertex, fuel = Q.get()
            if distance[vertex][fuel] != INF:  # already visited and min value set
                continue

            distance[vertex][fuel] = curr_cost
            if vertex == end:
                continue  # nothing to do

            if fuel == 0:  # mozna skorzystac z teleportu
                _from = vertex
                _to, _cost = T[vertex]
                if _to > _from:
                    Q.put((curr_cost + _cost, _to, 0))

            if fuel - D[vertex + 1] >= 0:  # mozna przejechać
                Q.put((curr_cost, vertex + 1, fuel - D[vertex + 1]))

            if fuel < E:  # mozna zatankowac i to jest ta sama sytuacja na tym wierzcholku
                Q.put((curr_cost + C[vertex], vertex, fuel + 1))

        return min(distance[n - 1])

    return dikstra(0, n - 1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
