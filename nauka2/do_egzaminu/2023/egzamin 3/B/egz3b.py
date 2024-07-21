# Jakub Worek
#
# Opis: tzw bruteforce, sprawdzam wszystkie przedziały
# 
# Złożoność: O(n^2)
import heapq

from egz3btesty import runtests


def areDisjoint(interval1, interval2):
    if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
        return True
    return False


def areContaining(interval1, interval2):
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
        return True
    if interval2[0] <= interval1[0] and interval2[1] >= interval1[1]:
        return True
    return False


def uncool(P):
    # tu prosze wpisac wlasna implementacje
    n = len(P)
    for i in range(n): P[i] = (P[i][0], P[i][1], i)
    P.sort(key=lambda x: x[0])

    for i in range(n - 1):
        for j in range(i + 1, n):
            if areDisjoint(P[i], P[j]): continue
            if areContaining(P[i], P[j]): continue
            return (P[i][2], P[j][2])

    return None


def uncool(P):  # nlogn
    n = len(P)
    P = [(a, b, idx) for idx, (a, b) in enumerate(P)]
    P.sort()  # sortowanie po poczatkach
    heap = []  # (end, start, idx), daje nam przedzial ktory najszybciej sie konczy
    for idx in range(n):
        while heap and heap[0][0] < P[idx][0]:  # heap_end  < P_start
            # nie stykaja sie jak kolwiek wiec usuwaj do skutku
            heapq.heappop(heap)

        c, d, P_idx = P[idx]

        if heap:
            b, a, heap_idx = heap[0]
            if a < c < b < d:  # koliduja ze soba
                return heap_idx, P_idx

        heapq.heappush(heap, (d, c, P_idx))


def uncool(P):  # nlogn
    P = [(P_start, P_end, idx) for idx, (P_start, P_end) in enumerate(P)]
    P.sort()  # sortowanie po poczatkach (startach)
    heap = []  # (end, start, idx), daje nam przedzial ktory najszybciej sie konczy
    for P_start, P_end, P_idx in P:
        #usuwanie smieci z kopca
        while heap and heap[0][0] < P_start:  # heap_end  < P_start
            # nie stykaja sie jak kolwiek wiec usuwaj do skutku
            # ten z kopca przedzial konczy sie zanim ten sie rozpoczyna
            heapq.heappop(heap)

        if heap: #sprawdz kolizje
            heap_end, heap_start, heap_idx = heap[0]
            if heap_start < P_start < heap_end < P_end:  # koliduja ze soba
                return heap_idx, P_idx

        heapq.heappush(heap, (P_end, P_start, P_idx)) # po przetworzeniu dodaj do kopca


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
