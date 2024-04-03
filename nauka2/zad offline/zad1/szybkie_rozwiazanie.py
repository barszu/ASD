from zad1testy import Node, runtests

import heapq

def SortH(p, k):
    lista = []
    while p != None:
        lista.append(p.val)
        p = p.next

    heap = []

    done =[]

    while len(lista) > 0:
        if len(heap) == 2* k + 1:
            popped = heapq.heappop(heap)
            done.append(popped)

        heapq.heappush(heap, lista.pop(0))

    while len(heap) > 0:
        popped = heapq.heappop(heap)
        done.append(popped)

    print(done)
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(SortH, all_tests=False)