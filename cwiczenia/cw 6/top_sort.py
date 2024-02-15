# top sort dla DIAG od czego zaczynamy (co jest glowa grafu) do konca (ogona)
# graf jest skierowany uruchom python -> wlacz program -> daj wynik
#                                   ---------------------->
# top sort : [python -> program -> wynik]
#                   ---------------> 

def top_sort(G):
    # G=(V,E)
    time=0
    n=len(G)
    visited=[False]*n
    parent=[None]*n
    path=[] #sciezka hamiltona
    
    def DFS_visit(G,u):
        nonlocal time, visited , parent, path
        print(u, end = " ")
        time += 1 #czas odwiedzania wierzcholka u
        visited[u]=True
        for v in G[u]: #v sasiad u
            if not visited[v]:
                parent[v]=u
                DFS_visit(G,v)
        path.append(i)
        time += 1 # czas przetworzenia
        
    for u in range(n): #veV
        if not visited[u]:
            DFS_visit(G,u)
    for i in range(n-1, 0 ,-1):
        if path[i-1] not in G[path[i]]:
            return False
    return True
