"""
znajdz domkniecie przechodnie grafu g w postaci macierzowej
"""
# n.podst. FLOYDA WARSHALLA
def domkniecie(G):
    n= len(G)
    M = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (G[i][j] != 0):
                M[i][j] = True
            else:
                M[i][j] = False
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M[i][j] = ( M[i][j] or ( M[i][k] and M[k][i] ) )
    
    