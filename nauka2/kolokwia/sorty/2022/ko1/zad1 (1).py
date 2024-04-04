from zad1testy import runtests

def partition(A,l,r):
    x=A[r]
    i=l #przed tablica bo nie przetworzylismy el >= x
    for j in range(l,r): #porownywalny el
        if A[j]<=x:
            A[i] , A[j] = A[j] , A[i]
            i += 1
            
    A[i] , A[r] = A[r] , A[i]
    return i

def q_select(A,k):
    l , r = (0,len(A)-1)
    while l <= r:
        pivot_idx = partition(A,l,r)

        if pivot_idx == k: return A[pivot_idx]
        elif pivot_idx < k: 
            l = pivot_idx
            # r = r
        elif pivot_idx > k: 
            # l = l
            r = pivot_idx-1


def Median(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    A = []
    for row in T:
        A.extend(row)
    k = (n*n - n) //2
    q_select(A,k-1)
    q_select(A,k-1+n)

    L = A[:k]
    M = A[k:k+n]
    R = A[k+n:]

    l , m ,r = 0 , 0 ,0
    

    for row in range(n):
        for col in range(n):
            if col < row: T[row][col] = L[l]
            elif col > row: T[row][col] = R[r]
            else: T[row][col] = M[m]

    return T

runtests( Median ) 

# a = [10,2,7,100,-1,30,31,32,56,1,10]
# print(sorted(a))
# print(q_select(a,5))
# print(a)
