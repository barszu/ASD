from zad3ktesty import runtests

def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    T.append(0) # zeby -1 istnialo i bylo 0
    dp = [None for i in range(n+1)]
    dp[-1] = 0
    for i in range(n-1,-1,-1):
        dp[i] = T[i] + min([dp[j] for j in range(i+1 , min(i+k , n) + 1 )])
    
    # print(T)
    return min([dp[j] for j in range(0 , k)])
    
runtests ( ksuma )

# [1, 2, 3, 4, 6, 15, 8, 7, 0]