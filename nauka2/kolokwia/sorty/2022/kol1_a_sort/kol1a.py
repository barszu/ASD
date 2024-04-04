from kol1atesty import runtests

def bin_search(A,target,l=0,h=None):
    if h is None: h = len(A)
    while l <= h:
        mid = (l+h)//2
        if A[mid] == target: return mid
        elif A[mid] < target:
            l = mid
        elif target < A[mid]:
            h = mid
        if mid == l : break
    return l

def qsort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    less = [A[i] for i in range(1,len(A)) if A[i]<=pivot]
    greater = [A[i] for i in range(1,len(A)) if A[i]>pivot]
    
    less = qsort(less)
    greater = qsort(greater)
    return less + [pivot] + greater

def g(T):
    for i,word in enumerate(T):
        if word[0] > word[-1]: #swap
            T[i] = word[::-1]
    #teraz wszystkie rownowazne sa takimi samymi
    # T.sort()
    T = qsort(T)
    l = 0
    r = 0
    best_seq_len = 1
    for i,_ in enumerate(T):
        if not (r <= len(T)-1):
            best_seq_len = max(best_seq_len , r-l)
            break
        if T[i] == T[l]:
            r += 1
        else:
            best_seq_len = max(best_seq_len , r-l)
            l = r
            r += 1
    return best_seq_len


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )


# arr = [1,2,5,1000,5000,2000,3567,3567,5000,5000,]
# arr = qsort(arr)
# print(arr)
# i = bin_search(arr,target=3569)
# print(i,'val:',arr[i])