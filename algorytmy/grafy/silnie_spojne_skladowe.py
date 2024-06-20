"""
SSS w grafie SKIEROWANYM dla DAG'u

Silnie spójne składowe (SCC - ang. Strongly Connected Components) 
to grupy wierzchołków w skierowanym grafie, gdzie z kazdego u mozna dostac sie do v

def: wierzcholki u,v naleza do (tej samej) silnie spojnej skladowej jesli istnieje
    sciezka skierowana z u->v , v->u -> takie pseudo cykle

gdyby nie byl dagiem mielibysmy dokladnie jedna wspolna skladowa

Algorytm:
- wykonaj DFS na grafie zapisujac czasy przetworzenia, 
  time++ kiedy dfs zostanie zdjety ze stacka, wierzcholek przetworzony (nie ma dokad pojsc)
- odwroc kierunek wszystkich krawedzi
- wykonaj DFS, wybierajac (puszczajac DFS visit) startowe wierzcholki w kolejnosci malejacych czasow przetworzenia (duze->male)
  wierzcholki odwiedzone w danym DFS_visit tworza sinie spojna skladowa (iteracja glownej petli sterujacej)
  x malych dfs zostanie wykonanych

zlozonosc:
V( E+V ) -ls , V(V^2) -matrix
"""
def DFS_time_set(G,done_time):

    # G=(V,E)
    time=0
    n=len(G)
    visited=[False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    
    def DFS_visit(G,u): #odwiedznie danego wierzcholka
        nonlocal time, visited , parent, done_time
        # time += 1 #czas odwiedzenia(dotkniecia) wierzcholka u
        visited[u]=True
        for v in G[u]: #v sasiad u
            if not visited[v]:
                parent[v]=u
                DFS_visit(G,v)
        #wtedy kiedy nie moge juz pojsc z tego wierzcholka gdzies indziej
        time += 1 # czas calkowitego przetworzenia u
        done_time[u] = time
        
    for u in range(n): #veV 
        if not visited[u]:
            DFS_visit(G,u) #rekurencyja sciezka w dol
    
    return

def reroll_edges(G,done_time):
    n = len(G)
    R = [[] for i in range(n)]
    for u in range(n):
        for v in G[u]:
            R[v].append(u)
    #sortuje tak zeby dfs wchodzil zawsze do wierzcholka z najwiekszym czasem odwiedzenia
    for wiersz in R:
        #key zwraca defakto wartosc ktora jest sortowana
        if len(wiersz)<2: continue #1, 0 el
        wiersz.sort(key=lambda u: done_time[u] , reverse=True)
    return R

def DFS_visit_skladowa(R,s,visited,parent,SSS_tab):
    #wybiera juz te co maja najwyzszy czas przetworzenia
    #to co jest w wykonaiu dfs visit to wspolna skladowa
    n = len(R)
    skladowa = []
    stack = []
    stack.append(s) 
    # DFS visit
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u]=True
            skladowa.append(u)
            # reverse iterate through edge list so results match recursive version
            for v in reversed(R[u]):
                if not visited[v]:
                    parent[v]=u
                    stack.append(v)
    SSS_tab.append(skladowa)
    return

# dla ls
def SS_skladowe(G):
    n = len(G)
    done_time = [-1]*n
    DFS_time_set(G,done_time)
    R = reroll_edges(G,done_time)
    
    SSS_tab = []
    visited = [False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    highest_v = [i for i in range(n)]
    highest_v.sort(key=lambda u: done_time[u] , reverse=True)
    for u in highest_v: #veV 
        if visited[u]: continue
        DFS_visit_skladowa(R,u,visited,parent,SSS_tab) #rekurencyja sciezka w dol
        # create_path(parent,u,t,SSS_tab)
    return SSS_tab
    
    

# g = [[1, 4, 5], [0, 4, 2, 3 ], [1, 3], [1, 2], [0, 1], [0]]
# # print(dfs_iter(g))
# SS_skladowe(g)

def create_path(parent,s,t,SSS_tab):
    path = []
    v = t
    while v != s :
        u = parent[v]
        path.append(v)
        v = u
    SSS_tab.append(path)
    return 

# g = [[1, 2], [2], [0,3], [4], [5], [3]]
g = [[1],[2],[0,8,3],[4,6],[5],[3],[5],[8],[9],[5,10],[7,3]]
print(SS_skladowe(g))

