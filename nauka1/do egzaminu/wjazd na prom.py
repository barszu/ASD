"""
Auta sa w kolejce , 2 pasy na promie o  dlugosci L , ile max mozna zaladowac na prom
"""
def prom(Cars,L):
    n = len(Cars)
    pre_sum = [0]*n #ile wynosi suma liczb przed i-ta bez niej
    pre_sum[1] = Cars[0]
    for i in range(2,n): pre_sum[i] = pre_sum[i-1] + Cars[i-1]
    INF = float('inf')
    DP = [[None for j in range(L+1)] for i in range(n)]
    
    def f(i,s): #wpychajac auta od [0:i] gdzie na lewym pasie jest zapchanego s [metrow]
        if DP[i][s]: return DP[i][s]
        
        left = 0 #ile samochodow mozna wepchac wpychajac to i-te na lewy pas
        right = 0
        if s+Cars[i] <= L: # da sie wepchac na lewy pas
            left = 1 + f(i+1,s+Cars[i])
        if (pre_sum[i]-s)+Cars[i] <= L: #da sie wepchac na prawy pas
            right = 1 + f(i+1,s)
        
        DP[i][s] = max(left,right)
        return DP[i][s]
    res = f(0,0)
    return res

Cars = [1,2,10,1,1,4,5,6,7,8]
print(prom(Cars,10))
        
        
            
        