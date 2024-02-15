from egz2btesty import runtests

def magic( C ): #nie dziala problem bo wchodzac do komnaty potrzeba splacic dlug (miec jakies sztabki przy sobie)
  #[G,[K0,W0],[K1,W1],[K2,W2]]
  n = len(C)
  INF = float('inf')
  G = C[n-1][0]
  dp = [None for i in range(n)] #max ilosc sztabek co mozna wyniesc, i dostaje sie na pole n-1
  # have = [False for i in range(n)] #ile trzeba miec sztabek aby wejsc do tego optymalnego rozwiazania
  dp[n-1] = 0
  # have[n-1] = 0

  for i in range(n-2,-1,-1):
    G,[K0,W0],[K1,W1],[K2,W2] = C[i]
    # print(C[i])

    first_door = -INF
    if W0 > i :
      take = G - K0
      if take <= 10:
        first_door = take + dp[W0]

    second_door = -INF
    if W1 > i :
      take = G - K1
      if take <= 10:
        second_door = take + dp[W1]

    third_door = -INF
    if W2 > i :
      take = G - K2
      if take <= 10:
        third_door = take + dp[W2]

    dp[i]  = max(first_door , second_door , third_door)
  return dp[0] if dp[0] >= 0 else -1

# dla kazdego ruchu tablica opisujaca ile mozna zyskac idac w I drzwi ale ile trzeba w tych drzwiach zostawic

def magic2(C):
    INF = float('inf')
    n = len(C)
    B = sum([C[i][0] for i in range(n)]) + 1
    cache = [[None for i in range(B)] for j in range(n)]
    
    def dfs(i,b): #jestem w komnacie i majac b sztabek zlota
        if cache[i][b]: return cache[i][b]
        if i == n-1: 
          cache[i][b] = b
          return b
        G,[K0,W0],[K1,W1],[K2,W2] = C[i]
        # print("przetwarzanie {0} , {1}".format(i,b))
        
        first_door = -INF
        if W0 > i and G+b >= K0:
            take = G - K0
            if take <= 10:#zostanie za duzo to i dzrzwi sie nie otworza
              first_door = dfs(W0 , b + take)

        second_door = -INF
        if W1 > i and G+b >= K1:
            take = G - K1
            if take <= 10: 
              second_door = dfs(W1 , b + take)

        third_door = -INF
        if W2 > i and G+b >= K2:
            take = G - K2
            if take <= 10:
              third_door = dfs(W2 , b + take)
        
        cache[i][b] = max(first_door,second_door,third_door)
        return cache[i][b]
    
    dfs(0,0)
    a = cache[0][0]
    b = [cache[n-1][i]  for i in range(B) if cache[n-1][i]]
    return a

def maxGoldInPath(C): # "Problemem najdłuższej ścieżki w DAG z wagami"
    n = len(C)
    #[G,[K0,W0],[K1,W1],[K2,W2]]
    # Initialize max_gold array
    max_gold = [float('-inf')] * n
    max_gold[0] = 0 #ilosc zlota ktora mozna wyniesc do pozycji i
    
    # Iterate through vertices in topological order
    for i in range(n):
        G = C[i][0]
        for k,v in C[i][1:]:
            if v == -1 or G-k > 10: continue #niepoprawny wierzcholek , w skrzynce zostaje za duzo
            travel = max_gold[i] + G-k #cost to get from start to v
            if travel < 0 : continue #nie ma mowy o tym zeby tam przejsc
            max_gold[v] = max(max_gold[v], travel) #update dist[v]

    
    return max_gold[n-1]  # Max gold at the last vertex

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( magic, all_tests = True )
# runtests( magic2 , all_tests = True)
runtests( maxGoldInPath, all_tests = True )
