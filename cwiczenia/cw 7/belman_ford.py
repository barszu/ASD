from math import inf

def relax(dist,parent,u,v,w):
    pass

def verify(dist,u,v,w):
    pass

def make_edges(G):
    n=len(G)
    E=[]
    for u in range(n):
        for v,w in G[u]:
            E.append((u,v,w))
    return E

def belmondo(G,s):
    n=len(G)
    E=make_edges(G)
    parent = [None]*n
    dist = [inf]*n
    dist[s]=0
    for i in range(n-1):
        for j in range(len(E)):
            (u,v,w)=E[j]
            relax(dist,parent,u,v,w)
    
    for i in range(len(E)):
        u,v,w = E[i]
        if not verify(dist,u,v,w):
            return False
    return True