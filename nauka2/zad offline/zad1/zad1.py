# Bartłomiej Szubiak 415810

# Zadanie offline 1
# Do posortowania listy używam kopca min , zauważam że przez k-haotycznosc listy
# element o indeksie 'i' moze znajdowac sie po posortowaniu na pozycjach [i-k, i+k] dalej zwanym "oknem"
# okno to ma szerokosc 2k+1 wiec wielkosc kopca mozemy zredukowac z n do 2k+1
# co nam zredukuje zlozonosc z O(nlogn) do O(nlog(2k+1)) -> O(nlogk)
# zlozonosc taka poniewaz 2*n razy wykonujemy operacje kopcowe na kazdym elemencie (insert,pop)
# ktore kosztuja log(wielkosc kopca)

# W mojej implementacji zamiast uzywac gotowego modulu heapq uzywam wlasnej implementacji kopca min
# do przechowywania kopca wykorzystuje zwykla liste

# funkcje left , right , parent sluza do wyznaczania indeksow lewych/prawych dzieci i rodzica w kopcu
# funkcja heapify sluzy do naprawiania kopca , jesli kopiec jest zle ustawiony to funkcja naprawia go
# funkcja insert sluzy do dodawania elementu do kopca oraz go naprawia
# funkcja pop sluzy do usuwania elementu z kopca oraz go naprawia

# funkcja SortH dziala w taki sposob ze:
# - tworze guardiana ktory bedzie wskazywal na poczatek nowej listy odsyłaczowej
# - tworze kopiec , zapasowe pointery
# - przechodze po liscie odsyłaczowej
# - jesli kopiec jest pelny to wyciagam z niego element i dodaje do listy wynikowej
# - dodaje element do kopca
# - jesli lista sie juz skonczyla to wyciagam z kopca elementy i dodaje do listy wynikowej

# skrocone zlozonosci:
# zlozonosc czasowa to O(nlogk) , zlozonosc pamieciowa to O(k) (rozmiar kopca)
# przy:
# k = O(1) -> zlozonosc czasowa to O(n) , zlozonosc pamieciowa to O(1)
# k = O(n) -> zlozonosc czasowa to O(nlogn) , zlozonosc pamieciowa to O(n)
# k = O(logn) -> zlozonosc czasowa to O(nlog(log n)) , zlozonosc pamieciowa to O(nlogn)




from zad1testy import Node, runtests

class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(A, i, n):
    # patrzymy jako parent = i
    l = left(i)
    r = right(i)
    max_ind = i
    # decydowanie czy parenta swapowac z left czy right
    if l < n and A[l].val < A[max_ind].val:
        max_ind = l
    if r < n and A[r].val < A[max_ind].val:
        max_ind = r

    if max_ind != i:  # bedzie zamiana
        # swap( A[i] , A[max_ind])
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)  # trojkata z parentem co swapniety zostal

def insert(A, item):
    A.append(item)
    i = len(A) - 1
    #i nie jest korzeniem , wartosc i jest mniejsza (lepsza) od rodzica -> swap
    while i > 0 and A[parent(i)].val > A[i].val:
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


def SortH(p,k):
    new_list_g = Node()
    new_ptr = new_list_g

    heap = []
    
    #przeiterowanie po liscie
    ptr = p
    while ptr != None:
        nexty = ptr.next
        if len(heap) == 2*k+1: #kopiec pelny
            #wyciagniecie z kopca i dodanie do nowej listy
            new_ptr.next = pop(heap)
            new_ptr = new_ptr.next

        #dodanie do kopca , ustawienie next na None dla bezpieczenstwa
        ptr.next = None
        insert(heap,ptr)

        ptr = nexty
    
    #oproznianie pozostalosci kopca
    while len(heap) > 0:
        new_ptr.next = pop(heap)
        new_ptr = new_ptr.next
    
    return new_list_g.next

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )