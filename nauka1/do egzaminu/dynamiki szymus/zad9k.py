from zad9ktesty import runtests
from math import inf

def prom(Cars,g,d):
    n = len(Cars)
    pre_sum = [0]*n #ile wynosi suma liczb przed i-ta bez niej
    pre_sum[1] = Cars[0]
    for i in range(2,n): pre_sum[i] = pre_sum[i-1] + Cars[i-1]
    INF = float('inf')
    DP = [[None for j in range(g+1)] for i in range(n)]
    
    def f(i,s): #wpychajac auta od [0:i] gdzie na lewym pasie jest zapchanego s [metrow]
        if DP[i][s]: return DP[i][s]
        
        left = 0 #ile samochodow mozna wepchac wpychajac to i-te na lewy pas
        right = 0
        if s+Cars[i] <= g: # da sie wepchac na lewy pas
            left = 1 + f(i+1,s+Cars[i])
        if (pre_sum[i]-s)+Cars[i] <= d: #da sie wepchac na prawy pas
            right = 1 + f(i+1,s)
        
        DP[i][s] = max(left,right)
        return DP[i][s]
    res = f(0,0)
    return res

def prom2(P, g, d):
    return []


runtests ( prom )