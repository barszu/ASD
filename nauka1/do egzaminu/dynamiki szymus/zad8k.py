from zad8ktesty import runtests 

def minDistance(word1: str, word2: str) -> int:
        dp = [ [None for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        dp[len(word1)][len(word2)] = 0
        for i in range(len(word1)): dp[i][len(word2)] = len(word1)-i
        for j in range(len(word2)): dp[len(word1)][j] = len(word2)-j

        for i in range(len(word1)-1 , -1 ,-1):
            for j in range(len(word2)-1 , -1 , -1):
                if word1[i] == word2[j]: 
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]

                    dp[i][j] = min(insert,delete,replace)
        
        return dp[0][0]

runtests ( minDistance )