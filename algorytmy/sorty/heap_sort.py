"dzialajace rzeczy kopcowe na dole"

# w tablicy jest kopiec
def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-2)//2

def buildheap(A): #maxcheap sorting male->duze
    n=len(A)
    for i in range(parent(n-1),-1,-1): #sprytnie zeby lisci nie miec tylko pelne trojkaty z tego node'a
        heapify(A,i,n)

def heapify(A,i,n):
    # patrzymy jako parent = i
    l=left(i)
    r=right(i)
    max_ind=i 
    # decydowanie czy parenta swapowac z left czy right
    if ( (l<n) and (A[l]>A[max_ind]) ): max_ind=l
    if ( (r<n) and (A[r]>A[max_ind]) ): max_ind=r
    
    if max_ind != i : #bedzie zamiana
        # swap( A[i] , A[max_ind])
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,max_ind,n) #trojkata z parentem co swapniety zostal

def heapsort(A):
    n=len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        # swap(A[0],A[i])
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i)

"dzialajace kopce lol?"

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

T=[8,50,10,10,12,1,55,1000,2020,30,100,50,-100]
heapsort(T)
print(T)