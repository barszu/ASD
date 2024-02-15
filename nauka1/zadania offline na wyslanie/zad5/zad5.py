from zad5testy import runtests

#Bartłomiej Szubiak

# Algorytm tworzy calkowicie nowy graf bazujac na liscie krawedzi starego grafu
# - nowy graf zapisywany jest jako lista sasiedztwa
# - wszystkie czarne dziury bedziemy traktowac jako jeden (nowy) wierzcholek (x), wiec odpowiednio merge'ujemy te wierzcholki
#   (dlatego ze koszt transferu miedzy nimi to 0 czyli defakto na nic nie wplywaja i mozna je pominac)
#   (to znaczaco zmniejsza nam rozmiary grafu plus nie musimy tworzyc kliki dla czarnych dziur)
#   (kliki dlatego ze mozemy teleportowac sie z dowolnej czarnej dziury do kazdej innej)
#   polaczenia planet z dowolna czarna dziura sa zapisane jako polaczenie tej planety z wierzcholkiem x
# -+ dla szybkiego dostepu i sprawdzenia czy wierzcholek jest czarna dziura tj czy jest w S uzywam "hash table"
#   (pod idx k w tablicy bh znajduje sie informacja czy el k jest w S)
# Dla odpowiednio spreparowanego grafu uruchamiam algorytm dikstry ktory znajdzie mi najtansza sciezce z a do b
# (nie uzywam wewnetrznej funkcji relax jest ona dokladnie zawarta pod for'em)
# (koncze prace dikstry kiedy przetworze wierzcholek docelowy)

# zlozonosc: O( E+S+ElogV ) = O(ElogV)

def create_bh_table(S,n):
    tab=[False]*n
    for el in S:
        tab[el]=True
    return tab

def create_graph(E,bh,n): #-> G as ls -> [(dist , wierzcholek )]
    G=[ [] for _ in range(n+1) ]
    # n+1 wierzcholek to jest merge wszystkich dziur
    # dalej go nazywam x
    # miejsca dziur w ls sa puste
    x=n #len=n+1
    for (u,v,d) in E:
        if bh[u] and bh[v] : continue #oba sa dziurami
        elif bh[u]: #u jest x
            #tworze krawedz x,v & v,x
            (G[x]).append((d,v))
            (G[v]).append((d,x))
        elif bh[v]: #v jest x
            #tworze krawedz x,u & u,x
            (G[x]).append((d,u))
            (G[u]).append((d,x))
        else: #u,v v,u
            (G[u]).append((d,v))
            (G[v]).append((d,u))
    return G

from queue import PriorityQueue

def dikstra(G, n , a, b):
    inf = float('infinity')
    dist = [inf]*n
    dist[a] = 0
    visited= [False]*n
    q = PriorityQueue()
    q.put((0, a)) #(d,u)

    while not q.empty():
        d_u, u = q.get()  # dla u szukamy v
        if visited[u]: continue
        
        for d_v,v in G[u]:
            # relax
            temp_dist = d_u + d_v
            if temp_dist < dist[v]:
                dist[v] = temp_dist
                q.put((temp_dist, v))
        
        visited[u]=True #po przetworzeniu wierzcholka u
        if u == b and dist[b] != inf: 
            return dist[b]
    return None
        

def spacetravel( n, E, S, a, b ):
    bh = create_bh_table(S,n) #szybki dostep czy u jest w S #black holes
    
    if bh[a] and bh[b]: #oba sa dziurami
        return 0 # mozna sie tepnac z jednej w druga
    
    G=create_graph(E,bh,n)
    x = n
    
    if bh[a]: a=x #a jest dziura
    elif bh[b]: b=x #b jest dziura
    
    wynik=dikstra(G,n+1,a,b) #n+1 bo ten x jest jeszcze
    return wynik

runtests( spacetravel, all_tests = True )
