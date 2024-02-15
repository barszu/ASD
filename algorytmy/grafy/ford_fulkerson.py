"""
PROBLEM MAKSYMALNEGO PRZEPLYWU
- krawedzie <-> pojemnosci maksymalne
- krawedzie sa TYLKO w jedna strone
- PKT SPECJALNE s - źrodlo pkt startowy , t -ujscie (pkt koncowy)
- pojemnosc = 0 - nie ma krawedzi
- w grafie nie ma petli -> wierzcholki NIE zwrotne

zlozonosc: O( (V+E)*(f) ) = O( E*f ) f-ilosc jednostek maksymanego przeplywu
-> to jest duzo kiedy (f) jest duze

Dzialanie:
UWAGA! s,t musi byc "sztucznym" wierzcholkiem tz nic nie wplywa do s (zrodla) i nic nie wyplywa z t (ujscia) 
szukamy BFS/DFS sciezki z s->t , bierzemy min( wartosci na krawedziach ) i odejmujemy tyle jednostek z kazdej krawedzi tej sciezki
zapisujac ile odejmujemy w sumie
robimy to dopoki wszystkie sciezki sie nie skoncza
zwroc wartosc tej sumy

"""

"""
(MAX) SKOJARZENIA W GRAFACH DWUDZIELNYCH (2 kolorowych)
-> zbior krawedzi niezaleznych (takich ze nie maja one wspolnego wierzcholka)

Dzialanie:
1. Zbuduj graf ze starego dodajac wierzcholek S i laczac go (skierowanie ->) z lewa strona grafu , polacz prawa strone z T (dodaj go) (skierowanie ->)
2. Daj wszytskim krawedziom wage(przeplyw) 1
3. uruchom Forda-Fulkersona
4. krawedzie co nalezaly do oryginalnego grafu i maja wartosc 0 naleza do tego max skojarzenia

zlozonosc: O( ~V^3 )

"""
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