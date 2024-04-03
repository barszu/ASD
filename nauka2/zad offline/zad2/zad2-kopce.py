from zad2testy import runtests


def left(i):return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

def buildheap(A): #maxcheap sorting male->duze
    n=len(A)
    for i in range(parent(n-1),-1,-1): #sprytnie zeby lisci nie miec tylko pelne trojkaty z tego node'a
        heapify(A,i,n)

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

def repair_bottom_up(A, i):
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

# idx of item in A else None
def find(A, item):
    for i in range(len(A)):
        if A[i] == item:
            return i
    return None

# def find(heap, key):
#     index = 0
#     while index < len(heap):
#         current_key = heap[index]
#         if current_key == key: return index #found
#         elif current_key < key: index = left(index) 
#         else: index = right(index)
#     return None

# def ksum(T, k, p):
#     p = p - 1 #po to zeby byly przedzialy [i , i+p]
#     suma = 0
#     heap_odpadku = [] #TODO zmienic na kopiec max obslugujacy pop i insert

#     i = 0
#     #pseudo 0 iteracja
#     heap = T[i:i+p+1]
#     buildheap(heap)
#     while not len(heap) <= k: #kopiec jest za duzy
#         heap_odpadku.append(pop(heap))

#     buildheap(heap_odpadku)
#     suma += heap[0]
#     i += 1

#     while i+p < len(T):
#         #wyjeb i-1 element z kopca badz listy odpadkow
        
#         pop_idx = find(heap_odpadku, T[i-1])
#         if pop_idx is not None:
#             heap_odpadku.pop(pop_idx)
#             repair_bottom_up(heap_odpadku, len(heap_odpadku)-1)
#         else:
#             pop_idx = find(heap, T[i-1])
#             if pop_idx is not None:
#                 heap.pop(pop_idx)
#                 repair_bottom_up(heap, len(heap)-1)
#             else:
#                 raise ValueError("Element not found!!!!")

#         #dodaj i+p element do kopca, wywalajac z niego cos jesli jest za duzy
#         insert(heap, T[i+p])
#         if len(heap) > k:
#             insert(heap_odpadku, pop(heap))
#             # lista_odpadkow.append(pop(heap))
#         if len(heap) != k: #check
#             raise ValueError("Heap is not k size!!!")

#         suma += heap[0]
#         i += 1
    
#     return suma


def ksum(T, k, p):
    p = p - 1 #po to zeby byly przedzialy [i , i+p]
    suma = 0

    i = 0

    while i+p < len(T):
        heap = T[i:i+p+1]
        buildheap(heap)
        while not len(heap) <= k: #kopiec jest za duzy
            pop(heap)

        suma += heap[0]
        i += 1
    
    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )