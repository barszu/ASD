"""
bfs ma znalezc najkrotsza sciezke w grafie
i podaj ta trase

Graf w postaci listy sasiedztwa
"""
from queue import deque

def BFS_find_shortest_path(G,x,y): #find shortest path from x to y
    n=len(G) 
    visited=[False]*n
    parent=[-1]*n
    q=deque()
    q.append(x)
    visited[x]=True
    while len(q)>0:
        v=q.popleft()
        if v==y: #TODO
            i=y
            pass
            
            
            
        for adj in G[v]:
            if (not visited[adj]):
                visited[adj]=True
                parent[adj]=v
                q.append(adj) 
    