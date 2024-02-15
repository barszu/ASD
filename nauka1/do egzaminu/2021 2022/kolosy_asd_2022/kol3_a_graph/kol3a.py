from kol3atesty import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    G = [[] for i in range(n)]
    for u , v , waga in E:
        G[u].append((v,waga))
        G[v].append((u,waga))
    
    #DIKSTRA
    
    q = PriorityQueue()
    q.put((0,a))
    visit = [False]*n
    dist = [float('inf') for i in range(n)]
    
    is_dziura = [False]*n
    for j in S: is_dziura[j] = True #hashmap
    uzyto_dziury = False
    
    while not q.empty():
        w1 , u = q.get() # w - dystans od zrodla 
        if w1 < dist[u]: dist[u] = w1
        if visit[u]: continue
        visit[u] = True # oznacz jako przetworzony
        
        #dodaj wszystkie co sa sasiadami po drugiej stronie czarnej dziury
        if not uzyto_dziury and is_dziura[u]:
            uzyto_dziury = True
            # (u -> s) ->v
            for s in S: # u-> u tez sie zalicza
                # przetworzenie tych dziur
                visit[s] = True
                dist[s] = w1
                for v,w2 in G[s]:
                    if not is_dziura[v]:
                        q.put((w1+w2,v))
                    
        else:
            for v , w2 in G[u]: #normalni sasiedzi
                q.put((w1+w2,v)) #warunek krotszej drogi nie musi byc spelniony

    return dist[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )