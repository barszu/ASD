from zad4testy import runtests

def select_buildings(T,max_price):
    T = [(a,b,cost,h*(b-a),idx) for idx,(h,a,b,cost) in enumerate(T)]
    T.sort(key = lambda x: x[1]) #sort by endings
    n = len(T)
    dp = [[None for _ in range(max_price+1)] for _ in range(n)] #cache
    INF = float('inf')
    SubCache = [[[] for _ in range(max_price+1)] for _ in range(n)]
  
    def nonoverlap(i,j):
        if T[i][0]>T[j][0]: i,j = j,i
        return not T[j][0]<=T[i][1]  # a<y colision
  
    def dfs(i,cap):
        if dp[i][cap]: return dp[i][cap] #already cashed
        # f(i,cap) = max( f(j,cap-i.cost) + i.val )
        maxy = -INF
        if cap-T[i][2] >= 0: #can take i
            maxy = T[i][3] 
            SubCache[i][cap] = [T[i][4]]
            for j in range(i-1,-1,-1):
                if nonoverlap(i,j): 
                    if dfs(j,cap-T[i][2]) + T[i][3] > maxy:
                        maxy = dfs(j,cap-T[i][2]) + T[i][3]
                        SubCache[i][cap] = SubCache[j][cap-T[i][2]] + [T[i][4]]
            
        dp[i][cap] = maxy
        return dp[i][cap]
    
    res_help = -INF
    res = []
    for i in range(n):
        if dfs(i,max_price) > res_help:
            res_help = dfs(i,max_price)
            res = SubCache[i][max_price]

    return res

# tab = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)] 
# p=5 #14

# tab = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# p = 40 #27

#test 3 !

runtests( select_buildings )
# print(select_buildings(tab,p))