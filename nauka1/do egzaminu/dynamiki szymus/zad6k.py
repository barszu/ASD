from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S)
    dp = [None]*(n+1)
    dp[n] = 1 #S[n] = ""
    
    def dfs(i):
        if dp[i] is not None: return dp[i]
        if S[i] == '0': #zly prefix
            dp[i] = 0
            return 0
        #biore jednocyfrowa - zawsze moge jak 0 nie jest
        take_one = dfs(i+1)
        #biore 2 cyfrowa
        take_two = 0
        if i+1 < n and int(S[i]+S[i+1]) <= 26:
            take_two = dfs(i+2)
            
        dp[i] = take_one + take_two #sum of posibilities
        return dp[i]
    
    return dfs(0)

runtests ( haslo )