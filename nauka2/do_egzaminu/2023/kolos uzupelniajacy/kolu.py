import random

from kolutesty import runtests


def ice_cream(T):  # O(nlogn)
    # tu prosze wpisac wlasna implementacje
    T.sort(reverse=True)
    n = len(T)
    sol = 0
    mins = 0

    for i in range(n):
        if T[i] - mins > 0:
            sol += T[i] - mins
            mins += 1
        else:
            break
    return sol


# def ice_cream(T):
#     n = len(T)
#     max_melt = 0
#     for i in range(n):
#         max_melt += i
#
#     # filtered = [num for num in T if num - max_melt > 0]
#     return sum(T) - n -1


import heapq


def ice_cream(T):  # O(nlogn)
    T = [-x for x in T]
    heapq.heapify(T)
    day = 0
    sum = 0
    while T:
        x = -heapq.heappop(T)
        if x - day > 0:
            sum += x - day
        else:  # nie ma sensu dalej sprawdzac
            break
        day += 1
    return sum


# k-ty najwiekszy element w nieposortowanej liście
def quickselect(A, l, p, k):  # O(n)
    def partition(A, l, p):
        x = A[p]
        i = l - 1
        for j in range(l, p):
            if A[j] > x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[p] = A[p], A[i + 1]
        return i + 1

    if l == p: return A[l]
    q = partition(A, l, p)
    if q == k: return A[q]
    if q < k: return quickselect(A, q + 1, p, k)
    else: return quickselect(A, l, q - 1, k)


def ice_cream(T):  # O(nlogn) ? XD
    # potrzeba nam znalezc k-ty najwiekszy element taki ze T[k] - k <= 0
    # i od tego momentu reszte odrzucamy

    # k element znajdujemy wstrzeliwujac sie binsearchem
    n = len(T)
    l = 0
    r = n
    while l < r:
        k = (l + r) // 2
        # znajdz m-ty najwiekszy element
        x = quickselect(T, 0, n-1, k)

        if x - k <= 0:
            r = k
        else:
            l = k + 1
    return sum(T[:l]) - sum([i for i in range(l)])





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ice_cream, all_tests=True)
