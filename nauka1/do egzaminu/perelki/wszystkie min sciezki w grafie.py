"""
Dikstra 
dist_src[i] -> min dist (s,i)
dist_end[i] -> min dist (t,i)

dist_src[i] + w(i,j) + dist_end[j] == dist_src[t]
dist_src[j] - w(i,j) + dist_end[i] == dist_src[t]

"""
from queue import PriorityQueue
def dikstra(G, n , a):
    inf = float('inf')
    dist = [inf]*n
    visited= [False]*n
    q = PriorityQueue()
    
    dist[a] = 0
    q.put((0, a)) #(d,u)

    while not q.empty():
        d_u, u = q.get()  # dla u szukamy v
        if visited[u]: continue
        
        for v,d_v in G[u]:
            # relax
            temp_dist = d_u + d_v #przez u->v mozna szybciej niz jakos ()->v
            if temp_dist < dist[v]:
                dist[v] = temp_dist
                q.put((temp_dist, v)) #dodaje do przetwarzania kiedy warunek drogi jest speniony
        
        visited[u]=True #po przetworzeniu wierzcholka u

    return dist

def paths(G,s,t): #G;(wierzcholek,waga)
    d_src = dikstra(G,len(G),s) #dst mierzony od zrodla
    d_end = dikstra(G,len(G),t) #dst mierzony od konca
    
    res = 0 #ilosc tych krawedzi
    if d_src[t] == float('inf'): #wgl nie mozna sie dostac
        return res
    for u in range(len(G)):
        for v,waga in G[u]:
            if d_src[u] + waga + d_end[v] == d_src[t] and d_src[v] - waga + d_end[u] == d_src[t]:
                #ta krawedz zalicza sie
                res += 1
    return res