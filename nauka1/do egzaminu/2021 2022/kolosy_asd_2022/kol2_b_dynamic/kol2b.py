from kol2btesty import runtests

def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje
    Data = [( O[i] , C[i] )for i in range(len(O))] # (dist from A , cost of staying)
    Data.append((L,0))
    Data.append((0,0))
    # O = None
    # C = None
    Data.sort()
    #zrob aby znac dystanse pomiedzy
    dist = Data[0][0]
    for i in range(1,len(Data)):
        dA , cost = Data[i]
        Data[i] = (dA-dist , cost)
        dist = dA
    
    #Data =  (dist beetween , cost of staying)
    DP = [[[None,None] for j in range(T+1)] for i in range(len(Data))]
    INF = float('inf')
    for j in range(T+1):
        DP[len(Data)-1][j] = [0,0]
    
    def dfs(i,b,sp):
        if DP[i][b][sp] != None: return DP[i][b][sp]
        # print(f"przetwarzam {i}{b}{sp}")
        stay = INF
        drive = INF
        special_used = INF
        
        if b + Data[i+1][0] <= T:
            drive = dfs(i+1,b + Data[i+1][0],sp)
        if b != 0 :
            stay = dfs(i,0,sp) + Data[i][1]
        if not b + Data[i+1][0] <= T and b + Data[i+1][0] - T <= T and sp == 0:
            special_used = dfs(i+1,b + Data[i+1][0] - T,1)
        
        DP[i][b][sp] = min(stay,drive,special_used)
        return DP[i][b][sp]
    
    # a = 5    
    res = dfs(0,0,0)
    
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
