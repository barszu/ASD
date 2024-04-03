from zad2testy import runtests
import heapq

def ksum(T, k, p):
    T = [(T[i], i) for i in range(len(T))]
    position_cashe = [None for _ in range(len(T))] #w ktorym kopcu i-ty el sie znajduje
    p = p - 1 #po to zeby byly przedzialy [i , i+p]
    suma = 0
    
    i = 0
    #pseudo 0 iteracja
    min_heap = T[i:i+p+1] #len=k , na topie ma najlepszy element
    for j in range(i, i+p+1): position_cashe[j] = "min_heap"
    max_heap = [] #len=p-k
    


    heapq.heapify(min_heap)
    while not len(min_heap) <= k: #kopiec jest za duzy
        (el,index) = heapq.heappop(min_heap)
        max_heap.append((-el , index))
        position_cashe[index] = "max_heap"

    heapq.heapify(max_heap)
    suma += min_heap[0][0]
    i += 1

    while i+p < len(T): #od tad dzialam na pierwszym dobrze zbudowanym kopcu, i przesuwam to nieszczesne okno

        was_in_min_heap = position_cashe[i-1] == "min_heap" #ten wyrzucany i-1

        #czysc kopce tutaj
        while min_heap and min_heap[0][1] <= i-1:
            (el,index) = heapq.heappop(min_heap)
            position_cashe[index] = None

        while max_heap and max_heap[0][1] <= i-1:
            (el,index) = heapq.heappop(max_heap)
            position_cashe[index] = None
        

        if was_in_min_heap:
            #to zabierz sobie z max kopca
            (m_el , index) = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-m_el, index))
            position_cashe[index] = "min_heap"

            #jest teraz dziura w kopcu max i brakuje jednego el

            #wrzucam zawsze do min kopca
            (el,index) = T[i+p]
            heapq.heappush(min_heap, (el, index))
            position_cashe[index] = "min_heap"

            #w kopcu min jest o jeden za duzo el

            #czyszce prewentycje szczyt
            while min_heap and min_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(min_heap)
                position_cashe[index] = None

            #przerzucam ten o 1 za duzy el z min kopca do max kopca
            (el , index) = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-el, index))
            position_cashe[index] = "max_heap"

        else:
            #w kopcu min jest odpowiednia ilosc elementow w kopcu max jest dziura
            #wrzucam zawsze do min kopca
            (el,index) = T[i+p]
            heapq.heappush(min_heap, (el, index))
            position_cashe[index] = "min_heap"

            #w kopcu min jest o jeden za duzo el

            #czyszce prewentycje szczyt
            while min_heap and min_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(min_heap)
                position_cashe[index] = None

            #przerzucam ten o 1 za duzy el z min kopca do max kopca
            (el , index) = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-el, index))
            position_cashe[index] = "max_heap"

        suma += min_heap[0][0]
        i += 1
    return suma

runtests( ksum, all_tests=True )