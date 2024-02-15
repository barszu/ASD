from kol3btesty import runtests
from queue import PriorityQueue

def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    sky = len(G)
    G.append([])
    for u,landing in enumerate(A):
        G[u].append((sky,landing))
        G[sky].append((u,landing))
    
    n = len(G)
    q = PriorityQueue()
    q.put((0,s))
    visit = [False]*n
    dist = [float('inf') for i in range(n)]

    while not q.empty():
        w1 , u = q.get() # w - dystans od zrodla 
        if w1 < dist[u]: dist[u] = w1
        if visit[u]: continue
        visit[u] = True # oznacz jako przetworzony
        for v , w2 in G[u]: #normalni sasiedzi
            q.put((w1+w2,v)) #warunek krotszej drogi nie musi byc spelniony

    return dist[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )