"""
mosty w grafach NIEskierowanych

def: most -> taka krawedz ze jak sie ja wywali to jest niespojny (a wczesniej byl spojny)

tw: krawedz e jest mostem <=> nie lezy na zadnym cyklu prostym (nie powtarzaja sie wierzcholki)
    e = {u,v} to jej usuniecie powoduje brak jakiekolwiek sciezki z u do v 

t(v) - czas odwiedzenia wierzcholka v (wyklad d(v))
low(v) = min( t(v) , #t(u) , #low(w) )
    u - wierzcholek taki ze z v jest krawedz wsteczna do u (krawedz siegajaca do wierzcholka w ktorym juz bylismy)(ostatnie odwiedzone)
    w - dziecko w drzewie DFS
    # - dla kazdego dostepnego

Algo:
1. DFS dla #v zapisujac visit_time -> t(v)
2. dla #v oblicz low(v) 
3. mosty to krawedzie {v,p(v)} (p(v) - rodzic v w drzewie DFS)
    gdzie t(v) = low(v)

IDEA:
low(v) - identyfikator cyklu w grafie 
(ten sam numer low maja te co naleza do tego samego cyklu) <- szuka najwikeszych mozliwych cykli i je grupuje

dzialanie:
- zapisuj w tablicy visit_time wedrujac w dfs
* low odpalany kiedy wracamy rekurencyjnie
- (taki sam czas wpisuj do tablicy zawierajacej wartosci low dla kazdego wierzcholka (pozniej naprawimy ten low))
    + kiedy trafie na wierzcholek taki ze nastepny juz zostal odwiedzony uruchamiam prawowite low

"""
"""
jesli t(v) = low(v) to krawedz {p(v),v} jest mostem dlatego ze jakby byl ten cykl to naprawimy low() tego parenta 
i by sie wszystko unormowalo
"""
#GPT
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

    bridges.pop() #(0,-1) wywal
    return bridges,lowest_time

graph = [ [1, 2], [0, 2], [0,1, 3], [2, 4,5], [3,5,6],[3,4],[4]]
# graph = [ [1, 2], [0, 2], [0,1, 3], [2, 4,5], [3,5],[3,4],]
# graph = [[1],[0,2],[1,3],[2]]
# graph = [[1,3],[2],[3],[]]
print(find_bridges(graph))



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
    
    
    
     