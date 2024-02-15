#zakladamy ze ma ten cykl trzeba go wypisac

def fun(G):
    path=[]
    n=len(G)
    
    def DFS_visit(i):
        nonlocal G , path , n
        for j in range(n):
            if G[i][j]==1:
                G[i] [j] , G[j] [i] = 0 , 0 #format tej krawedzi , graf jest NIE skierowany
                DFS_visit(j)
        path.append(i)
        
    DFS_visit(0)
    return path