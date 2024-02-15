from egzP5btesty import runtests 

"""
Solution: znajdz mosty -> jezeli krawedz jest mostem to te wierzcholki sa pkt artykulacji
"""

def find_bridges(graph): # ~DFS
    n = len(graph)  # Liczba wierzchołków
    visited = [False] * n  # Tablica odwiedzonych wierzchołków
    discovery_time = [-1] * n  # Czas odkrycia wierzchołków
    lowest_time = [-1] * n  # Najniższy czas, jaki można osiągnąć z danego wierzchołka
    parent = [-1] * n  # Tablica przechowująca rodzica wierzchołka
    bridges = []  # Lista przechowująca mosty w grafie

    time = 1  # Aktualny czas
    #-------
    def dfs_visited(u):
        nonlocal time, graph
        visited[u] = True
        discovery_time[u] = time
        lowest_time[u] = time
        time += 1

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visited(v)
                #po powroceniu z dziecka (tam low juz bylo)
                lowest_time[u] = min(lowest_time[u], lowest_time[v])
                #tutaj tez moze byc ten if
                
            elif v != parent[u]: 
                #dfs dotknal cos co juz bylo kiedys wczesniej (nie jest to rodzic)
                lowest_time[u] = min(lowest_time[u], discovery_time[v])
        if lowest_time[u] == discovery_time[u]: # if lowest_time[v] > discovery_time[u]:
            bridges.append((u, parent[u])) #(0,-1) koncowe wywalaj
        return
    #--------

    for i in range(n):
        if not visited[i]:
            dfs_visited(i)

    return bridges,lowest_time

def pkt_artykulacji(G): #wierzcholki ktore naleza do mostow i ich wywalenie rozspojnia graf -> len(neibours) > 1
    time = 0
    n = len(G)
    ART = [False]*n # czy wierzcholek jest pkt artykulacji
    LOW = [None]*n #funkcja low dla wierzcholka
    D = [None]*n #discovery time
    # Parent = [None]*n #tablica rodzicow 
    
    def dfs(v): #->child no 
        nonlocal time
        childs = 0 
        
        time += 1
        LOW[v] = time
        D[v] = time
        
        for s in G[v]:
            if D[s] == None: #nie odwiedzono jeszcze
                childs += 1
                dfs(s) #idz w glab
                if LOW[s] >= D[v]: #warunek na pkt artykualcji
                    ART[v] = True
                LOW[v] = min( LOW[v] , LOW[s] ) #napraw low
            else:
                LOW[v] = min(LOW[v] , D[s])
                
        return childs

    for u in range(n):
        if D[u] == None: #nie odwiedzono jeszcze
            if dfs(u) > 1: #wiecej niz jedno dziecko ma
                ART[u] = True #korzen drzewa jest punktem artykulacji
            else: ART[u] = False
    
    return ART #ART[i] - wierzcholek jest/nie jest pkt artykulacji

def koleje ( B ):
    #tutaj proszę wpisać własną implementację
    n = len(B)
    sett = set()
    track_max = max(B[0])
    for i in range(n):
        a , b = B[i]
        if a>b : a , b = b , a #b always greater
        track_max = max(track_max,b)
        sett.add((a,b))
    #build graph
    n = track_max + 1
    G = [[] for i in range(n)]
    for u,v in sett:
        G[u].append(v)
        G[v].append(u)
    
    # bridges , lowest_time = find_bridges(G)
    # aktykulacje = set()
    # bridges.pop() 
    # for u,v in bridges:
    #     if len(G[u]) != 1: #wyrzucenie tego wierzcholka rozwala graf
    #         aktykulacje.add(u)
    #     if len(G[v]) != 1:
    #         aktykulacje.add(v)
    # return len(aktykulacje)
    ART = pkt_artykulacji(G)
    cnt = 0
    for b in ART:
        if b: cnt +=1
    return cnt
        

runtests ( koleje, all_tests=True )