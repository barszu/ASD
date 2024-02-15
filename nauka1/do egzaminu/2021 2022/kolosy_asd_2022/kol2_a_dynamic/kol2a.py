from kol2atesty import runtests

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje
    borders = [(0,None)] + [(num,idx) for idx,(num,is_border) in enumerate(P) if is_border] + [(B,None)]
    borders.sort()
    P.sort()
    DIST = [0]*len(borders) #miedzy i a i+1
    left = 0 #idx , startuje w A
    for (v,is_border) in P:
        if is_border: 
            left += 1
            continue
        # if borders[left] < v < borders[left+1]:
        else:
            DIST[left] += 1
    
    # 0 - Marek
    # 1 - ten drugi
    DP = [[ [None,None] for j in range(3+1) ] for i in range(len(borders))]
    SubCache = [[ [[],[]] for j in range(3+1) ] for i in range(len(borders))]
    INF = float('inf')
    
    for i in range(3+1):
        DP[len(borders)-1][i] = [0,0] #na B
    
    def dfs(i,b,driver):
        if DP[i][b][driver] != None : return DP[i][b][driver]
        stay = INF
        change_seats = INF
        if b+1 <= 3 : #mozna jechac jeszcze
            stay = dfs(i+1,b+1,driver)
            if driver == 0: stay += DIST[i]  
                  
        new_driver = (driver + 1) %2
        if b != 0 : #mozna sie zamienic jest tego sens
            change_seats = dfs(i,0,new_driver)
        
        if stay <= change_seats:
            DP[i][b][driver] = stay
            SubCache[i][b][driver] = SubCache[i+1][b+1][driver].copy()
        else:
            DP[i][b][driver] = change_seats
            SubCache[i][b][driver] = SubCache[i][0][new_driver].copy() + [borders[i][1]]
        return DP[i][b][driver]
        
    res = dfs(0,0,1)   
    
    return SubCache[0][0][1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )