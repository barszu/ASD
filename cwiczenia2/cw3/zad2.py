# funkcja wstawiajaca element do kopca

def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-2)//2

def insert(A, item):
    A.append(item)
    i = len(A) - 1
    # i nie jest korzeniem , wartosc i jest mniejsza (lepsza) od rodzica -> swap
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i) #naprawiam w gore