from egz2atesty import runtests

def coal( A, T ):
    n = len( A )
    sklady = [T for _ in range(n)]
    ktory = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sklady[j] >= A[i]:
                sklady[j] -= A[i]
                ktory[i] = j
                break

    return ktory[-1]

import heapq
def coal(A,max_capacity): #albo to jest O(nlogn) albo O(n * nlogn)
    last_storage = 0
    heap = [(0,max_capacity)] # (index, capacity)
    thrown_away = [] #aka stack
    for c in A:
        while heap: #wyrzucaj z heapa wszystkie do poki nie natrafisz na odpowiedni sklad
            index, capacity = heap[0] #podejrzyj
            if capacity >= c: break
            else: thrown_away.append(heapq.heappop(heap)) #wyrzuc z heapa

        #heap mogl byc pusty, zaden magazyn sie nie nadaje potrzeba nowego
        if not heap:
            last_storage += 1
            heap.append((last_storage,max_capacity))

        index, capacity = heapq.heappop(heap) #wez magazyn

        if capacity-c > 0: #zaktualizuj magazyn, nie bierz pod uwage pustych
            heapq.heappush(heap,(index,capacity-c))

        while thrown_away: #wrzuc reszte smieci z powrotem do heapa
            heapq.heappush(heap,thrown_away.pop())

    return index #ostatni magazyn na ktorym byla operacja








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
