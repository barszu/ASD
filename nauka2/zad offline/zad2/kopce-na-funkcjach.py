from zad2testy import runtests

def left(i):return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

#jako kopiec min
def heapify(A, i, n):
    # patrzymy jako parent = i
    l = left(i)
    r = right(i)
    max_ind = i
    # decydowanie czy parenta swapowac z left czy right
    if l < n and A[l] < A[max_ind]:
        max_ind = l
    if r < n and A[r] < A[max_ind]:
        max_ind = r

    if max_ind != i:  # bedzie zamiana
        # swap( A[i] , A[max_ind])
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)  # trojkata z parentem co swapniety zostal


def insert(A, item):
    A.append(item)
    i = len(A) - 1
    # i nie jest korzeniem , wartosc i jest mniejsza (lepsza) od rodzica -> swap
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i) #naprawiam w gore


def pop(A):
    if len(A) == 0:
        raise IndexError("Heap is empty")
    if len(A) == 1:
        return A.pop()
    root = A[0]
    A[0] = A.pop() #za korzen wchodzi ostatni element
    heapify(A, 0, len(A)) #naprawiam kopiec
    return root

def buildheap(A): #maxcheap sorting male->duze
    n=len(A)
    for i in range(parent(n-1),-1,-1): #sprytnie zeby lisci nie miec tylko pelne trojkaty z tego node'a
        heapify(A,i,n)






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
    


    buildheap(min_heap)
    while not len(min_heap) <= k: #kopiec jest za duzy
        (el,index) = pop(min_heap)
        max_heap.append((-el , index))
        position_cashe[index] = "max_heap"

    buildheap(max_heap)
    suma += min_heap[0][0]
    i += 1

    while i+p < len(T): #od tad dzialam na pierwszym dobrze zbudowanym kopcu, i przesuwam to nieszczesne okno

        was_in_min_heap = position_cashe[i-1] == "min_heap" #ten wyrzucany i-1
        
        if was_in_min_heap:
            (el1,index1) = T[i+p]

            #czyszczenie kopcow
            while max_heap and max_heap[0][1] <= i-1:
                (el,index) = pop(max_heap)
                position_cashe[index] = None

            max_popped = pop(max_heap)
            (el2,index2) = -max_popped[0] , max_popped[1]
            position_cashe[index2] = None

            greater = (el2 , index2)
            less = (el1 , index1)

            if not greater > less :
                #swap
                less = (el2 , index2)
                greater = (el1 , index1)

            insert(max_heap, (-less[0], less[1]))
            insert(min_heap, greater)

            position_cashe[less[1]] = "max_heap"
            position_cashe[greater[1]] = "min_heap"
        else:
            (el1,index1) = T[i+p]

            #czysc kopce tutaj
            while min_heap and min_heap[0][1] <= i-1:
                (el,index) = pop(min_heap)
                position_cashe[index] = None

            (el2,index2) = pop(min_heap)
            position_cashe[index2] = None

            greater = (el2 , index2)
            less = (el1 , index1)
            if not greater > less :
                #swap
                less = (el2 , index2)
                greater = (el1 , index1)

            insert(min_heap, greater)
            insert(max_heap, (-less[0], less[1]))

            position_cashe[greater[1]] = "min_heap"
            position_cashe[less[1]] = "max_heap"
            

        #czysc kopce tutaj
        while min_heap and min_heap[0][1] <= i-1:
            (el,index) = pop(min_heap)
            position_cashe[index] = None

        suma += min_heap[0][0]
        i += 1
    return suma

runtests( ksum, all_tests=True )