from zad2testy import runtests
import heapq

# def ksum(T, k, p):
#     T = [(T[i], i) for i in range(len(T))]
#     position_cashe = [None for _ in range(len(T))] #w ktorym kopcu i-ty el sie znajduje
#     p = p - 1 #po to zeby byly przedzialy [i , i+p]
#     suma = 0
    
#     i = 0
#     #pseudo 0 iteracja
#     min_heap = T[i:i+p+1] #len=k , na topie ma najlepszy element
#     for j in range(i, i+p+1): position_cashe[j] = "min_heap"
#     max_heap = [] #len=p-k
    


#     heapq.heapify(min_heap)
#     while not len(min_heap) <= k: #kopiec jest za duzy
#         (el,index) = heapq.heappop(min_heap)
#         max_heap.append((-el , index))
#         position_cashe[index] = "max_heap"

#     heapq.heapify(max_heap)
#     suma += min_heap[0][0]
#     i += 1

#     while i+p < len(T): #od tad dzialam na pierwszym dobrze zbudowanym kopcu, i przesuwam to nieszczesne okno

#         #wrzucam zawsze do min kopca
#         (el,index) = T[i+p]
#         heapq.heappush(min_heap, (el, index))
#         position_cashe[index] = "min_heap"

#         was_in_max_heap = position_cashe[i-1] == "max_heap" #ten wyrzucany i-1

#         #czysc kopce tutaj
#         while min_heap and min_heap[0][1] <= i-1:
#             (el,index) = heapq.heappop(min_heap)
#             position_cashe[index] = None

#         while max_heap and max_heap[0][1] <= i-1:
#             (el,index) = heapq.heappop(max_heap)
#             position_cashe[index] = None

#         if was_in_max_heap: #znika el z max kopca wiec potrzeba jeden dodac
#             (el , index) = heapq.heappop(min_heap)
#             heapq.heappush(max_heap, (-el, index))
#             position_cashe[index] = "max_heap"

#         #else el byl w max kopcu wiec nie trzeba nic robic bo juz dodalismy

#         suma += min_heap[0][0]
#         i += 1
#     return suma



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
            (el1,index1) = T[i+p]

            #czyszczenie kopcow
            while max_heap and max_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(max_heap)
                position_cashe[index] = None

            max_popped = heapq.heappop(max_heap)
            (el2,index2) = -max_popped[0] , max_popped[1]
            position_cashe[index2] = None

            greater = (el2 , index2)
            less = (el1 , index1)

            if not greater > less :
                #swap
                less = (el2 , index2)
                greater = (el1 , index1)

            #czysc kopce tutaj
            while min_heap and min_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(min_heap)
                position_cashe[index] = None

            while max_heap and max_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(max_heap)
                position_cashe[index] = None

            heapq.heappush(max_heap, (-less[0], less[1]))
            heapq.heappush(min_heap, greater)

            position_cashe[less[1]] = "max_heap"
            position_cashe[greater[1]] = "min_heap"
        else:
            (el1,index1) = T[i+p]

            #czysc kopce tutaj
            while min_heap and min_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(min_heap)
                position_cashe[index] = None

            (el2,index2) = heapq.heappop(min_heap)
            position_cashe[index2] = None

            greater = (el2 , index2)
            less = (el1 , index1)
            if not greater > less :
                #swap
                less = (el2 , index2)
                greater = (el1 , index1)


            #czysc kopce tutaj
            while min_heap and min_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(min_heap)
                position_cashe[index] = None

            while max_heap and max_heap[0][1] <= i-1:
                (el,index) = heapq.heappop(max_heap)
                position_cashe[index] = None

            heapq.heappush(min_heap, greater)
            heapq.heappush(max_heap, (-less[0], less[1]))

            position_cashe[greater[1]] = "min_heap"
            position_cashe[less[1]] = "max_heap"
            


        suma += min_heap[0][0]
        i += 1
    return suma


#TODO trzeba bylo by zmapowac ze element o idx i jest w kopcu lewym/prawym

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )