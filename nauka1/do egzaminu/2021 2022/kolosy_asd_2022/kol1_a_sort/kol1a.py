from kol1atesty import runtests

def g(T):
    # tu prosze wpisac wlasna implementacje
    for i in range(len(T)):
        rvr = (T[i])[::-1]
        if rvr < T[i]: #cba -> abc
            T[i] = rvr

    T.sort()
    l = 0
    r = 0
    max_cnt = 0
    while r < len(T):
        if T[l] == T[r]: #rozrzerz okno
            r += 1
        else: #okno juz jest zepsute
            max_cnt = max(max_cnt , r-l)
            l = r
    max_cnt = max(max_cnt , r-l)
    return max_cnt


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
