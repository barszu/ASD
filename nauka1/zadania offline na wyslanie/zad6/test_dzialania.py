from zad6testy import runtests

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

def decreace_cap(G,start,end,parent_tab,curr_flow): #TODO
    v = end
    while v != start :
        (idx_wzgl_u,u) = parent_tab[v]
        # mamy krawedz (u,v)
        # G[u][v] -= curr_flow
        cap , vk = G[u] [idx_wzgl_u] #wartosc krawedzi (u,v)?
        G[u] [idx_wzgl_u] = (cap-curr_flow , vk)
        
        # nie istnieja krawedzie (v,u)(wsteczne) wiec nie robie G[v][u] + path_flow
        
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


T = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
# G = binworker(T)
H = [ [(1, 5), (1, 6), (1, 8)] , [(1, 7), (1, 9)] , [(1, 5), (1, 7)] , [(1, 8)] ,[(1, 8), (1, 7)] ,[(1, 11)] , [(1, 11)] , [(1, 11)] , [(1, 11)] , [(1, 11)] , [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)] ,[] ]


a = ford_fulkerson(H,len(H),len(H)-2,len(H)-1)+1
E = 0
for taby in H[0:5]:
    E += len(taby)

for taby in H:
    print(taby)
print("wlasciwy: "+str(E))