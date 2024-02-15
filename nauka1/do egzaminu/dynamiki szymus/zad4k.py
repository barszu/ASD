from zad4ktesty import runtests
# f(i,j) = T[i][j] + min(f(i+1),f(i,j+1)) if in bound else INF
def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    dp = [[None for j in range(n)] for i in range(n)]
    dp[n-1][n-1] = T[n-1][n-1]
    INF = float('inf')
    
    def dfs(i,j):
        if i>=n or j>=n: return INF
        if dp[i][j] is not None: return dp[i][j]
        
        dp[i][j] = T[i][j] + min(dfs(i+1,j) , dfs(i,j+1))
        return dp[i][j]
    
    res = dfs(0,0)
    return res

runtests ( falisz )
