from zad6testy import runtests

# Bartlomiej Szubiak
# Dzialanie Algorytmu: buduje nowy graf na podanych danych (graf jest grafem 2-dzielnym)(lewa strona - ludzie)(prawa - maszyny)
# krawedz miedzy czlowiekiem a maszyna jest wtedy kiedy czlowiek potrafi ja obslugiwac (moj graf jest zapisany jako lista sasiedztwa)
# Problem defakto sprowadza sie do znalezienia najwiekszego skojarzenia bo wtedy najwiecej ludzi i maszyn jest zatrudnionych (albo i wszytskie)
# wiec tworze sztuczny wierzcholek ktory bedzie zrodlem buduje krawedzie z niego wychodzace do kazdego czlowieka
# dodatkowo tworze wierzcholek sztuczny ujscie do ktorego prowadza krawedzie z kazdej maszyny
# daje wage (capacity) = 1 wszystkim krawędziom i uruchamiam algorytm forda fulkersona
# ilosc skojarzen to 1*max_flow 

# zlozonosc: O( m*k + k + m + (V+E)t  ) = O( (V+E)t ) gdzie t to maksymalny przeplyw < O(V^3)



def find_machines_no(M):
    global_max=0
    for taby in M:
        if (taby==[]): continue
        curr_max = max(taby)
        if curr_max>global_max : global_max = curr_max
    return global_max+1
 
def make_graph(M,m,k,G): 
    #oznaczenia: [0,m-1] - ludzie , [m,m+k-1] - maszyny
    for i in range(m):
        machines_list = M[i]
        for p in machines_list:
            (G[i]).append((1,p+m))
    return

def add_start_end(G,m,k):
    # m+k - start , m+k+1 - koniec(ujscie)
    start = m+k
    end = m+k+1
    G.append([(1,i) for i in range(0,m)]) #lacze start z ludzmi
    G.append([])
    for i in range(m,m+k): #lacze maszyny z koncem
        (G[i]).append((1,end))
        
from collections import deque  
      
def BFS_find_path(G,n,s,t): #graf , startowy punkt rozwijania , koniec
    # n - rozmiar grafu
    # w queue trzymam tylko wierzcholki
    q=deque()
    visited=[False]*n #czy odwiedzono juz ten, zeby sie nie zapetlac
    parent=[(None,None)]*n #kto byl rodzicem i-tego wierzcholka -> jak dotarlismy
    
    q.append(s)
    visited[s] = True
    parent[s]=None
    
    while q :
        u=q.popleft()
        for idx in range(len(G[u])): #sasiedzi u
            cap , v = G[u] [idx]  # v jest pod idx w G[u]
            if (not visited[v] and cap>0) : #not v.visited
                parent[v] = (idx,u)
                visited[v] = True
                q.append(v)
                if (v == t): #znaleziono ta najkrotsza sciezke -> dotknieto t
                    return (True,parent)
    return (False,parent)       

def max_curr_flow_extract(G,start,end,parent_tab):
    allowed_flow = float("inf")
    v = end
    while v != start :
        (idx_wzgl_u,u) = parent_tab[v]
        # mamy krawedz (u,v)
        cap , smiec = G[u] [idx_wzgl_u] #wartosc krawedzi (u,v)?
        allowed_flow = min(allowed_flow,cap)
        v = u 
        if (allowed_flow==0) : return allowed_flow #nie ma sensu dalej tego sprawdzac
    return allowed_flow

def decreace_cap(G,start,end,parent_tab,curr_flow):
    v = end
    while v != start :
        (idx_wzgl_u,u) = parent_tab[v]
        # mamy krawedz (u,v)
        # G[u][v] -= curr_flow
        cap , vk = G[u] [idx_wzgl_u] #wartosc krawedzi (u,v)?
        G[u] [idx_wzgl_u] = (cap-curr_flow , vk)
        
        # (v,u)(wsteczne)  G[v][u] + path_flow
        found_u = False
        nv = len(G[v])
        for i in range(nv):
            cap , uk = G[v] [i]
            if (uk==u): #jest G[v][u]
                G[v] [i] = (cap+curr_flow , uk)
                found_u = True
        if not found_u:
            #dodaj ten wierzcholek G[v][u]
            (G[v]).append((curr_flow,u))
        
        v = u 
    return 

def ford_fulkerson(G,n,start,end):
    # uzywam bfs do sprawdzania czy jeszcze jakas sciezka istnije
    # zwraca on sciezke po ktorej szedl
    max_flow = 0
    while True:
        extra_paths_exist , parent_tab = BFS_find_path(G,n,start,end)
        if not extra_paths_exist: break
        
        #znajdz przeplyw dla tej sciezki
        curr_flow = max_curr_flow_extract(G,start,end,parent_tab)
        if (curr_flow == 0): continue
        max_flow += curr_flow
        
        #odejmij z tej sciezki
        decreace_cap(G,start,end,parent_tab,curr_flow)
    return max_flow
        
        
    

def binworker( M ):
    #oznaczenia: 
    # [0,m-1] - ludzie , [m,m+k-1] - maszyny
    # m+k - start , m+k+1 - koniec(ujscie)
    # (1,u) - krawedzie
    
    m = len(M) #ilosc ludzi
    k = find_machines_no(M)
    G = [[] for i in range(m+k)]
    make_graph(M,m,k,G)
    add_start_end(G,m,k)
    start = m+k
    end = m+k+1
    n = m+k+2
    flow = ford_fulkerson(G,n,start,end)
   
    return flow #maksymalne skojarzenie

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
