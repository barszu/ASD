from zad2testy import runtests
import heapq

def ksum(T, k, p):
    T = [(T[i], i) for i in range(len(T))]
    p = p - 1 #po to zeby byly przedzialy [i , i+p]
    suma = 0
    
    i = 0
    #pseudo 0 iteracja
    min_heap = T[i:i+p+1] #len=k , na topie ma najlepszy element
    max_heap = [] #len=p-k


    heapq.heapify(min_heap)
    while not len(min_heap) <= k: #kopiec jest za duzy
        (el,index) = heapq.heappop(min_heap)
        max_heap.append((-el , index))

    heapq.heapify(max_heap)
    suma += min_heap[0][0]
    i += 1

    while i+p < len(T): #od tad dzialam na pierwszym dobrze zbudowanym kopcu, i przesuwam to nieszczesne okno

        (el,index) = T[i+p]
        heapq.heappush(max_heap, (-el, index))

        while min_heap[0][1] <= i-1: #ten edge case ze u gory kopca min jest ghost block
            heapq.heappop(min_heap) #usuwam ghost block z kopca min

            (m_el,index) = heapq.heappop(max_heap) #przerzucam el z kopca max do min
            heapq.heappush(min_heap, (-m_el, index)) 

        if min_heap[0] < (-max_heap[0][0], max_heap[0][1]): #jesli na szczycie min kopca jest el mniejszy niz ten na szczycie max kopca
            (m_el,index) = heapq.heappop(max_heap) #przerzucam el z kopca max do min
            heapq.heappush(min_heap, (-m_el, index))

        suma += min_heap[0][0]
        i += 1
    return suma

#TODO trzeba bylo by zmapowac ze element o idx i jest w kopcu lewym/prawym

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )