# tablica n liczb naturalnych , parametr t,
# znajdz podciag podciag z a ktory sumuje sie do t, (nie spojny)

def findSubsequence(A, t): #(n*t)
    #  f(i,sum) - czy mozna uzyskac sume t z podciagu z wartosi A[0:i]
    # f(i,sum) = f(i+1,sum) or f(i+1,sum+A[i]) #top down
    #             biore         nie biore

    # f(i,sum) = f(i-1,sum) or f(i-1,sum-A[i]) #bottom up
    
    #to down
    n = len(A)
    dp = [[False for i in range(t+1)] for j in range(n+1)]
    for i in range(n+1): dp[i][0] = True
    for i in range(n-1,-1,-1):
        for j in range(t+1):
            if j - A[i] >= 0:
                dp[i][j] = dp[i+1][j] or dp[i+1][j - A[i]]
            else:
                dp[i][j] = dp[i+1][j]

# dane 2 tablice o dlugosci n znalezc najdluzszy podciag



def longestCommonSubsequence(text1: str, text2: str) -> int:
        # f(i,j) = LCS beetwen s[i] and t[i]
        # f(i,j) = f(i+1,j+1) + 1 if s[i] == t[j] (te same znaki)
        # f(i,j) = max( f(i+1,j) , f(i,j+1) ) if s[i] != t[j] (rozne znaki)

        A , B = text1 , text2
        a , b = len(A) , len(B)
        # b - wiersze , a- kolumny
        dp = [[None for i in range(a+1)] for j in range(b+1) ]
        for i in range(a+1):
            dp[b][i] = 0
        for i in range(b+1):
            dp[i][a] = 0


        for i in range(b-1,-1,-1):
            for j in range(a-1,-1,-1):
                if A[j] == B[i]: #ten sam znak
                    dp[i][j] = 1 + dp[i+1][j+1] #if in bound
                else: #rozne znaki
                    dp[i][j] = max( dp[i+1][j] , dp[i][j+1] )
        
        return dp[0][0]


# jak wykorzystac z zad 2 zeby najdluzyszy rosnacy podciag

def longestIncreasingSubsequence(A):
    # f(i) = dlugosc najdluzszego podciagu konczacego sie na A[i]
    # f(0) = 1 - defultowa wartosc
    # f(i) = max( f(t) + 1 ) : t<i , A[t]<A[i]

    n = len(A)
    F = [-1]*n #tablica wartosci funkcji dlugosc najdluzszego podciagu konczacego sie na A[i]
    P = [-1]*n #parent - P[i] - z jakiego idx pochodzi A[i]
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    return max(F), P

