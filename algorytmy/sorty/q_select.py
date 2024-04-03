

def median(T):
    n = len(T)
    if n==0 : 
        print("blad w medianie")
    if n<3 : return max(T)
    a = T[0]
    b = T[n//2]
    c = T[n-1]
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

def quick_select(arr, k): #wybor pivota jest dowolny k=[0:n-1]
    if len(arr) == 1: return arr[0]

    # pivot = arr[len(arr) // 2]  # Wybieramy element środkowy jako pivot
    pivot = median(arr)
    less = [x for x in arr if x < pivot]  # Elementy mniejsze od pivota
    greater = [x for x in arr if x > pivot]  # Elementy większe od pivota
    equal = [x for x in arr if x == pivot]  # Elementy równe pivotowi

    if k < len(less):
        return quick_select(less, k)
    elif k < len(less) + len(equal):
        return equal[0] #byle jaki z tych rownych
    else:
        return quick_select(greater, k - len(less) - len(equal))

def qSelect(nums,k): #k th- largest el , k>= 1
    k = len(nums)-k
    
    def qsel_helper(l,r):
        pivot, ptr = nums[r] , l #pivot right most el
        for i in range(l,r): #without pivot
            if nums[i] <= pivot:
                nums[ptr] , nums[i] = nums[i] , nums[ptr] #swap
                ptr += 1
        nums[ptr] , nums[r] = nums[r] , nums[ptr]
        if ptr > k : return qsel_helper(l,ptr-1) #qs on left
        elif ptr < k: return qsel_helper(ptr + 1,r)
        else: return nums[ptr] 
    
    return qsel_helper(0,len(nums)-1)

T=[4,5,3,2,1,1,4,6,10,2,3,1,0,-10,100]
# T=[1,1,1,1,1,1]
T_sorted = [-10, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 10, 100]
# print(sorted(T))
# print(quick_select(T,5))
a = qSelect(T,5)
print(T ,a)

def swap(T,a,b):
    T[a],T[b]=T[b],T[a]

def partition(A,p,r):
    # bierzemy x(pivot) z samego konca
    # analizujemy tablice od lewa do prawa
    # szukamy miejsca medianowego chwilowego
    # x - pivot
    # j - aktualnie przetwarzany el
    # i - el tuz przed el > x (na lewo od niego sa <)
    x=A[r]
    i=p-1 #przed tablica bo nie przetworzylismy el >= x
    for j in range(p,r,1):
        if A[j]<=x:
            i += 1
            # swap(A[i],A[j])
            swap(A,i,j)
    # swap(A[i+1],A[r])
    swap(A,i+1,r)
    return i+1

def qselect(A , l , r , k):
    if l <= r :
        pivot_idx = partition(A,l,r)
        if pivot_idx == k:
            return A[pivot_idx]
        elif pivot_idx < k:
            return qSelect(A, pivot_idx , r , k)
        elif pivot_idx > k:
            return qSelect(A, l , pivot_idx-1 , k)
        
import random
A = [random.randint(0,20) for i in range(20)]
q = qSelect(A,0,len(A)-1,1)