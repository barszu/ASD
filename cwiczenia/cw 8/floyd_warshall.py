def floyd_warshall(G): #G as a matrix
    inf = float('infinity')
    n = len(G)
    distance = [[inf for i in range(n)] for k in range(n)]
    parent = [[None for i in range(n)] for k in range(n)]
    # ustawienie tablicy distance (generalnie kopja G)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                distance[i][j]=inf
            else:
                distance[i][j]=G[i][j]
        distance[i][i]=0
    
    for z in range(n):
        for k in range(n):
            for y in range(n):
                # tutaj cos inaczej
                distance[k][y] = min( distance[k][y] , distance[z][y] + distance[z][k])
                parent[k][y] = parent[z][y]
        
        for i in range(n):
            if distance[i][i]<0 : return False #ujemny cykl
    
    return distance , parent
                
                
    
    