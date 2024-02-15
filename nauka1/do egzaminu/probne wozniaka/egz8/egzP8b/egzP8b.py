from egzP8btesty import runtests

def floyd_warshall(G,n):
    INF = float('inf')
    
    D = G.copy()
    for i in range(n): D[i][i] = 0 #0 na przekatnej      
    
    for t in range(n):
        for x in range(n):
            for y in range(n):
                if D[x][y] > D[x][t] + D[t][y] :
                #przez t mozna dostac sie szybciej wierzcholkiem posrednim
                    D[x][y] = D[x][t] + D[t][y] #przypisz ten szybszy dystans
                    # parent[x][y] = parent[t][y]
    return D

def robot( G, P ):
    n = len(G) #G -> (v,x)
    INF = float('inf')
    matrix = [[INF for _ in range(n)] for i in range(n)]
    
    #rewrite graph
    for u in range(len(G)):
        for v,x in G[u]:
            matrix[u][v] = x
    
    Dist = floyd_warshall(matrix,n)
    
    res = 0
    for i in range(0,len(P)-1):
        a = P[i]
        b = P[i+1]
        res += Dist[a][b]

    return res
    
runtests(robot, all_tests = True)
