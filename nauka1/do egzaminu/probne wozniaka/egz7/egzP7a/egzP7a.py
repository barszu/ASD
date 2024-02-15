from egzP7atesty import runtests 
"""
SOLUTION: przeplywy -> max skojarzenie w grafie 2 dzielnym
- krawedz -> preferencja 

Sens zadania -> student nie zadowolony kiedy mial jakies preferencje i zadna z nich nie wypalila
-> dostanie on cos randomowego ale NAPEWNO dostanie
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

def akademik( T ): #O(n^4)
    #Tutaj proszę wpisać własną implementację
    n = len(T) #ilos studentow i pokoi
    G = [[] for i in range(2*n+2)] 
    start = 2*n
    end = start+1
    #build graph -> [0,n-1] studenci , [n,2n-1] - pokoje , 2n- start , 2n+1 - end
    NNN_cnt = 0
    for i in range(len(T)): #i-ty student preferencje , zrodlo - student , pokoj - end
        neutral = True
        for p in T[i]:
            if p is None: continue
            G[i].append((1,p+n)) #(cap,vertex)
            neutral = False
        if neutral: NNN_cnt += 1
        
        G[start].append((1,i)) #dla startu student
        G[i+n].append((1,end)) #dla pokoju koniec
    
    max_cap = ford_fulkerson(G,len(G),start,end)

    
    
    # res = studenci_no - max_skojarzenie - (NNN) -> (ludzie co im obojetnie)
    return n-max_cap-NNN_cnt

runtests ( akademik )