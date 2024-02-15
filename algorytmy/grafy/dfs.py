"""
DFS - (depth-first search) - przeszukiwanie w glab

dzialanie:
- chodzenie po calym grafie w glab zaczynajac od jakiegos wierzcholka,
- chodzenie jest paternem
- rekurencja
    

zastosowania:
- spojnosc grafu - for w mainie sie wykona >1 raz
- dwudzielnosc, - kolory w visited
- wykrywanie cykli - w DFS_visit napotykamy na odwiedzony wierzcholek 
    visited_set ma obejmowac tylko sciezke na ktorej jest dfs -> wejscie znow -> cykl
- sortowanie topologiczne - dodaj wierz do res jak przetworzyles dzieci (i nie ma cyklu)
- silnie spojne skladowe (czy sie sklada z 2 czesci osobnych razem z oznaczeniem do ktorej czesci nalezy wierzcholek)
- cykl Eulera
- mosty/pkt artykulacji
   (usuniecie tego -> graf nie spojny)

drzewo DFS:
- generuje sie przez pojscie w glab grafu
- widoczne nakierowanie co bylo czyim rodzicem (jak szlismy)

zlozonosc:
    O(V+E) - ls
    O(V^2) - macierz.
"""

def DFS_ls(G):
    # G=(V,E)
    time=0
    n=len(G)
    visited=[False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    
    def DFS_visit(G,u): #odwiedznie danego wierzcholka
        nonlocal time, visited , parent
        # print(u, end = " ")
        time += 1 #czas odwiedzenia(dotkniecia) wierzcholka u
        visited[u]=True
        for v in G[u]: #v sasiad u
            if not visited[v]:
                parent[v]=u
                DFS_visit(G,v)
        time += 1 # czas calkowitego przetworzenia u
        
    for u in range(n): #veV 
        # w grafie zwyklym (nieskierowanym)
        #to jest po to kiedy rekurencyjna sciezka sie skonczy 
        # i jakies wierzcholki jeszcze zostaly
        # potrzebne do grafu niespojnego 
        if not visited[u]:
            DFS_visit(G,u) #rekurencyja sciezka w dol
    
    return time,visited,parent #koniec programu return co potrzebne

# g=[[1,6],[2,3,4],[],[],[5],[],[7],[8],[]]
g = [[1, 4, 5], [0, 4, 2, 3 ], [1, 3], [1, 2], [0, 1], [0]]
print(DFS_ls(g))

def DFS_matrix(G):
    # G=(V,E)
    time=0
    n=len(G)
    visited=[False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    
    def DFS_visit(G,u): #odwiedznie danego wierzcholka
        nonlocal time, visited , parent
        # print(u, end = " ")
        time += 1 #czas odwiedzenia(dotkniecia) wierzcholka u
        visited[u]=True
        for v in range(n): #v sasiad u
            if (G[u] [v] == 0): continue
            if not visited[v]:
                parent[v]=u
                DFS_visit(G,v)
        time += 1 # czas calkowitego przetworzenia u
        
    for u in range(n): #veV 
        # w grafie zwyklym (nieskierowanym)
        #to jest po to kiedy rekurencyjna sciezka sie skonczy 
        # i jakies wierzcholki jeszcze zostaly
        # potrzebne do grafu niespojnego 
        if not visited[u]:
            DFS_visit(G,u) #rekurencyja sciezka w dol
    
    return time,visited,parent #koniec programu return co potrzebne

def dfs_iter(G, s):
    n = len(G)
    visited = [False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    stack = []
    stack.append(s) 

    # DFS visit
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u]=True
            # print(u, end = " ")

            # reverse iterate through edge list so results match recursive version
            for v in reversed(G[u]):
                if not visited[v]:
                    parent[v]=u
                    stack.append(v)

def dfs_iter(G): #po calym grafie
    n = len(G)
    visited = [False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    stack = []
     

    for u in range(n): #veV 
        if visited[u]: continue
        stack.append(u)
        # DFS visit
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u]=True
                # print(u, end = " ")

                # reverse iterate through edge list so results match recursive version
                for v in reversed(G[u]):
                    if not visited[v]:
                        parent[v]=u
                        stack.append(v)
    return visited,parent

dfs_iter(g,0)