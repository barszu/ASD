"""
wierzcholek jest poczatkiem kiedy kazdy inny wierzcholek mozna usiagnac sciezka skierowana wychodzaca z tego wierzcholka
"""

def DFS_ls(G):
    # G=(V,E)
    time=0
    n=len(G)
    visited=[False]*n #0 nie bylismy , 1 bylismy , 2 przetwarzamy go
    parent=[None]*n
    czas_przetworzenia=[-1]*n
    
    def DFS_visit(G,u):
        nonlocal time, visited , parent, czas_przetworzenia
        # print(u, end = " ")
        time += 1 #czas odwiedzania wierzcholka u
        visited[u]=True
        for v in G[u]: #v sasiad u
            if not visited[v]:
                parent[v]=u
                DFS_visit(G,v)
        time += 1 # czas przetworzenia
        czas_przetworzenia[u]=time
        
    for u in range(n): #veV
        if not visited[u]:
            DFS_visit(G,u)
    
    for i in range(n):
        if czas_przetworzenia[i]==n:
            index=i
    visited=[False]*n
    time=0
    DFS_visit(G,index)
        
    return time==n #koniec programu return co potrzebne