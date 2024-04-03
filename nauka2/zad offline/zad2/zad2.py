from zad2testy import runtests

'''
Bartlomiej Szubiak 415810

skrocowe nazewnictwo, uwagi:
    p zmniejszylem o jeden zeby byly przedzialy [i , i+p], domkniete obustronnnie  !
    chunk - kawalek tablicy T , przedzial [i , i+p] ,
    ghost node - el ktory nie powinien znajdowac sie w tablicy bo aktualny chunk go nie zawiera, 
                niestety nie mozemy za kazdym raczem czyscic dokladnie kopcow bo wtedy cierpi zlozonosc,
                tak wiec zostawimy takie ghost_node'y w kopcu i bedziemy je ignorowac, jesli wyplyna na szczyt to wtedy je usuniemy
                (bedziemy przez cale zadanie traktowac ze ich nie ma tak jakby w kopcu)
    czyszczenie kopcow - usuwanie tylko ghost node'ow ktore wyplynely na szczyt

Algorytm korzysta z kopcow,
aby znalezc k-ty najwiekszy el w tablicy (abstrachujac od zadania) potrzebujemy kopca min (minheap) o wielkosci k,
    wtedy na szczycie mamy najgorszy el (pod wzgledem max wielkosci) , a w srodku mamy k-1 el mniejszych od niego
    wiec ten element na szczycie takiego kopca jest k-tym najwiekszym el w tablicy (w tym zadaniu chunku)

W zdaniu, musimy utrzymac strukture z ktorej zawsze jest latwo wydobyc k-ty najwiekszy el, 
    tak wiec potrzebujemy kopca min o wielkosci k , oraz kopca max na "odpadki" o wielkosci p-k

Przesuwajac chunk bedziemy "usuwac" i-1  el z kopca , i dokladac i+p el do kopca
-> jesli i-1 znajdowal sie w min kopcu to wezmiemy pod uwage el z max kopca (wypelniajacy dziure w min kopcu (odrazu)) oraz dochodzacy el i+p
     (robimy tak aby ograniczyc operacje na kopcach do minimum)
     wiekszy z nich trafi do min kopca (aby byc tam najgorszym) , a mniejszy do max kopca (aby byc tam najgorszym)

-> jesli i-1 znajdowal sie w max kopcu to wezmiemy pod uwage el z min kopca oraz dochodzacy el i+p (decyzja gdzie dochodacy powinien trafic)
    -//-

-> kopce sie ustabilizuja, a struktura sie zachowa (wielkosc kopcow zostanie ta sama, a na szczycie bedzie k-ty el) , 
    w kopcu min beda elementy > od k-tego , a w kopcu max el < od k-tego

(przy kazdej operacji gdzie potrzebujemy czystego szczytu czyscimy kopce , przy insercie nie potrzeba)

chunkow mamy n-p , w najlepszym wypadku operacje kopcowe maja po log(k) zlozonosci, lecz w najgorszym przypadku maja log(n)
tak wiec zlonosc algorytmu to O((n-p)log(n)) = O(nlog(n))

Dodatkowo uzywam swojej implememntacji kopcow zamknietej w klasie dla wygody, kopiec max to tak naprawde kopiec min tylko ze wartosci sa *-1 
(dla odwrocenia kierunku porzadkowania ku min)
'''

class MinHeap:
    def __init__(self , l=[]) -> None:
        self.heap = l
        self.buildheap()

    def __len__(self) -> int:
        return len(self.heap)
    
    def left(self,i):return 2 * i + 1
    def right(self,i): return 2 * i + 2
    def parent(self,i): return (i - 1) // 2

    def heapify(self, i, n):
        A=self.heap
        # patrzymy jako parent = i
        l = self.left(i)
        r = self.right(i)
        max_ind = i
        # decydowanie czy parenta swapowac z left czy right
        if l < n and A[l] < A[max_ind]:
            max_ind = l
        if r < n and A[r] < A[max_ind]:
            max_ind = r

        if max_ind != i:  # bedzie zamiana
            # swap( A[i] , A[max_ind])
            A[i], A[max_ind] = A[max_ind], A[i]
            self.heapify(max_ind, n)  # trojkata z parentem co swapniety zostal
    
    def buildheap(self): #maxcheap sorting male->duze
        n=len(self.heap)
        for i in range(self.parent(n-1),-1,-1): #sprytnie zeby lisci nie miec tylko pelne trojkaty z tego node'a
            self.heapify(i,n)

    def repair_bottom_up(self , i=None):
        A = self.heap
        if i is None:
            i = len(A) - 1
        # i nie jest korzeniem , wartosc i jest mniejsza (lepsza) od rodzica -> swap
        while i > 0 and A[self.parent(i)] > A[i]:
            A[i], A[self.parent(i)] = A[self.parent(i)], A[i]
            i = self.parent(i) #naprawiam w gore

    def insert(self, item):
        self.heap.append(item)
        self.repair_bottom_up()

    def pop(self):
        A = self.heap
        if len(A) == 0:
            raise IndexError("Heap is empty")
        if len(A) == 1:
            return A.pop()
        root = A[0]
        A[0] = A.pop() #za korzen wchodzi ostatni element
        self.heapify(0, len(A)) #naprawiam kopiec
        return root
    
    def get_top(self):
        return self.heap[0]
    
    # def __str__(self) -> str:
    #     return "H:" + str(self.heap)
    

class MaxHeap(MinHeap): #tylko dla tego zadania i krotek (val,idx)
    def __init__(self, l=[]) -> None:
        l = [(-el , idx) for (el,idx) in l]
        super().__init__(l)

    def insert(self, item):
        super().insert((-item[0], item[1]))

    def pop(self):
        (a,b) = super().pop()
        return (-a,b)
    
    def get_top(self):
        (a,b) = super().get_top()
        return (-a,b)
    
    # def __str__(self) -> str:
    #     l = [(-el , idx) for (el,idx) in self.heap]
    #     return "H:" + str(l)
    
#Wlasciwe zadanie

def ksum(T, k, p):
    T = [(T[i], i) for i in range(len(T))]
    position_cashe = [None for _ in range(len(T))] #w ktorym kopcu i-ty el sie znajduje
    p = p - 1 #po to zeby byly przedzialy [i , i+p]
    suma = 0
    
    i = 0
    #pseudo 0 iteracja
    min_heap = MinHeap(T[i:i+p+1]) #len=k , na topie ma najlepszy element (ten k-ty)
    for j in range(i, i+p+1): position_cashe[j] = "min_heap"
    max_heap = [] #len=p-k
    
    while not len(min_heap) <= k: #kopiec jest za duzy
        (el,index) = min_heap.pop()
        max_heap.append((el , index))
        position_cashe[index] = "max_heap"

    max_heap = MaxHeap(max_heap)
    suma += min_heap.get_top()[0]
    i += 1

    def clean_ghosts_nodes(h):
        while len(h)>0 and h.get_top()[1] <= i-1:
            (el,index) = h.pop()
            position_cashe[index] = None

    while i+p < len(T): #od tad dzialam na pierwszym dobrze zbudowanym kopcu, i przesuwam to nieszczesne okno

        was_in_min_heap = position_cashe[i-1] == "min_heap" #ten wyrzucany i-1

        if was_in_min_heap:
            (el1,index1) = T[i+p]

            clean_ghosts_nodes(max_heap)

            (el2,index2) = max_heap.pop()
            position_cashe[index2] = None

            greater = (el2 , index2)
            less = (el1 , index1)

            if not greater > less :
                #swap
                less , greater = greater , less

            # clean_ghosts_nodes(max_heap)
            # clean_ghosts_nodes(min_heap)

            min_heap.insert(greater)
            max_heap.insert(less)

            position_cashe[less[1]] = "max_heap"
            position_cashe[greater[1]] = "min_heap"
        else:
            (el1,index1) = T[i+p]

            clean_ghosts_nodes(min_heap)

            (el2,index2) = min_heap.pop()
            position_cashe[index2] = None

            greater = (el2 , index2)
            less = (el1 , index1)
            if not greater > less :
                #swap
                less , greater = greater , less

            # clean_ghosts_nodes(max_heap)
            # clean_ghosts_nodes(min_heap)

            min_heap.insert(greater)
            max_heap.insert(less)

            position_cashe[greater[1]] = "min_heap"
            position_cashe[less[1]] = "max_heap"
            

        clean_ghosts_nodes(min_heap)
        suma += min_heap.get_top()[0]
        i += 1
    return suma


runtests( ksum, all_tests=True )