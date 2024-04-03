class MinHeap: #dzialajacy dla krotek jak i pojedynczych obiektow (genrealnie dl aczego kolwiek co obsluguje > <)
    def __init__(self , l=[]) -> None:
        self.heap = l
        self.buildheap()

    def __len__(self) -> int:
        return len(self.heap)
    
    def left(self,i):return 2 * i + 1
    def right(self,i): return 2 * i + 2
    def parent(self,i): return (i - 1) // 2

    def heapify(self, i, n): #repair top-down from 0 to n
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
    
    def __str__(self) -> str:
        return "H:" + str(self.heap)
    

class MaxHeap(MinHeap): #tylko dla tego zadania i krotek (val,idx)
    def __init__(self, l=[]) -> None:
        l = [(-el , idx) for (el,*idx) in l]
        super().__init__(l)

    def insert(self, item):
        super().insert((-item[0], item[1]))

    def pop(self):
        (a,b) = super().pop()
        return (-a,b)
    
    def get_top(self):
        (a,b) = super().get_top()
        return (-a,b)
    
    def __str__(self) -> str:
        l = [(-el , idx) for (el,idx) in self.heap]
        return "H:" + str(l)
    
#uzycie 
h = MinHeap([1,2,3,4,5,6,7,8,9])
print(h)
h.insert(0)
print(h)
