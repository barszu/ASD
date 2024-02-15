"""
PODCIAG ROSNACY!!! najdluzszy (nie) spojny

f(i) = dlugosc najdluzszego podciagu konczacego sie na A[i]
f(0) = 1 - defultowa wartosc
f(i) = max( f(t) + 1 ) : t<i , A[t]<A[i]

max f(i) - dlugosc najdluzszego ciagu rosnacego
"""

def lis(A):
    n = len(A)
    F = [-1]*n #tablica wartosci funkcji dlugosc najdluzszego podciagu konczacego sie na A[i]
    P = [-1]*n #parent - P[i] - z jakiego idx pochodzi A[i]
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    return max(F), P