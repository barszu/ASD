from kol1btesty import runtests

def compare(A:list,B:list):
    # len A == len B == 26
    for i in range(len(A)):
        if A[i] == B[i]: continue
        if A[i] > B[i]: return 1
        else:
            return -1
    return 0

def QS(A):
    if len(A) == 0 : return []
    piv = A[0]
    less = QS([i for i in A[1:] if compare(i,piv) == -1])
    eq = [i for i in A[1:] if compare(i,piv) == 0]
    grt = QS([i for i in A[1:] if compare(i,piv) == 1])
    return [*less , piv , *eq , *grt]
    

def f(T):
    # tu prosze wpisac wlasna implementacje
    A = [None]*(len(T))
    for i in range(len(T)):
        cnt_tab = [0]*(ord('z')-ord('a')+1)
        for l in T[i]:
            cnt_tab[ord(l)-ord('a')] += 1
        A[i] = cnt_tab
    
    # QS(A)
    used = [False]*len(T)
    max_get = [1]*len(T)
    for i in range(len(T)):
        if used[i]: continue
        used[i] = True
        
        for j in range(i+1,len(T)):
            if used[j]: continue #uzyty byl i napewno cmp != 0
            if compare(A[i],A[j])==0:
                max_get[i] += 1
                used[j] = True
  
    return max(max_get)


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
