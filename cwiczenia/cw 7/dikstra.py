"""

"""
from math import inf
from queue import PriorityQueue


def djikstra(G,a,b):
    n=len(G)
    distance=[inf]*n
    visited= [False]*n
    parent = [None]*n
    q = PriorityQueue()
    
    def relax(v,u,cost):
        nonlocal q , distance , parent , visited
        if distance[u] > distance[v] + cost:
            distance[u] = distance[v] + cost
            q.put((u,distance[u]))
            parent[u] = v
    
    q.put((a,0))
    distance[a] = 0
    while q:
        v,dv = q.get()
        if visited[v]: continue
        for el in G[v]:
            u , cost = el
            relax(v,u,cost)
    
    return distance,parent,visited

        