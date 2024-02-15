"""
GRAFY WAZONE

Reprezentacja:
matrix - G[i][j] - czy krawedz {i,j} jest i ile ona wynosi (inf to np nie ma krawedzi)
ls - G[i][j] = (waga , wierzcholek) {i,v}

BFS udajacy dikstre - wrzucic ten sam wierzcholek do kolejki(zwyklej) ale z waga o 1 mniejsza
"""
# -------------------------------------------------------------------------------------------
"""
DJIKSTRA
- w kazdym kroku skacze do najblizszego prawdziwego wierzcholka
- wagi > 0

u.distance - oszacowanie odleglosci z root'a do u
u.parent - rodzic u - mozna odtworzyc drzewo i droge

Algo:
1. (nie robi sie tego generalnie) (PQ typu min)
    wrzuc wszytskie wierzcholki do PQ z distance = inf  
    - kazdy wierzcholek w kolejce to nie jest przetworzony
    - kazdy POZA kolejka juz jest przetworzony
2. s.dist = 0
3. while (wierzcholki sa w kolejce)
    - (get) u o minimalnej wadze
    - iteruje po sasiadach
    - dla #{u,v} relax
    * jezeli zmieniamy wartosc v.d to wrzucamy go do kolejki (kolejka ma najblizszych nie przetworzonych)
        relax - upewniam sie ze najkrotsze sciezki spelniaja nierownosc trojkata

    def relax(u,v):
        if v.dist > u.dist + odleglosc(u,v):    #najoptymalniejsza trasa zostaje zapisana( v.dist bylo za duze)
            v.dist = u.dist + odleglosc(u,v)
            v.parent = u                        #najlepsza sciezka prowadzi przez u

zlonosc(ElogV) - zalezy od G i PQ (ls , kopiec binarny)
(V^2) (matrix , kopiec zbedny mozna samemu kombinowac)

"""
"""
Mozna na bierzaco modyfikowac wagi w grafie - kontrolowac dikstre wkladajac inne wagi do kolejki
-> zdefinuj co to dystans miedzy u->v
"""

from queue import PriorityQueue

def dikstra(G, n , a, b):
    inf = float('inf')
    dist = [inf]*n
    visited= [False]*n
    q = PriorityQueue()
    
    dist[a] = 0
    q.put((0, a)) #(d,u)

    while not q.empty():
        d_u, u = q.get()  # dla u szukamy v
        if visited[u]: continue
        
        for d_v,v in G[u]:
            # relax
            temp_dist = d_u + d_v #przez u->v mozna szybciej niz jakos ()->v
            if temp_dist < dist[v]:
                dist[v] = temp_dist
                q.put((temp_dist, v)) #dodaje do przetwarzania kiedy warunek drogi jest speniony
        
        visited[u]=True #po przetworzeniu wierzcholka u
        if u == b and dist[b] != inf: 
            return dist[b]
    return None

def networkDelayTime2(times: list[list[int]], n: int, k: int) -> int:# times = edges
    G = [[] for i in range(n+1)] # (waga , v)
    for u , v , w in times:
        G[u].append((w,v))
    
    #dikstra
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put((0,k))
    visit = set()
    dist = [float('inf') for i in range(n+1)]
    while not q.empty():
        w1 , u = q.get() # w - dystans od zrodla 
        if w1 < dist[u]: dist[u] = w1
        if u in visit: continue

        visit.add(u) # oznacz jako przetworzony
        for w2 , v in G[u]:
            "ten if jest obcjonalny"
            # if v not in visit: #dodaje zawsze wszystko ale nigdy przetworzonego
            q.put((w1+w2,v)) #warunek krotszej drogi nie musi byc spelniony
    
    t = max(dist[1:])
    return t if t != float('inf') else -1

import heapq

def dikstra_heap(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]  # Kolejka priorytetowa (minimalna)

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue

        if node == end:
            return distances[end]

        for weight, neighbor in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return float('inf')

g = [[(2, 1), (3, 2)], [(4, 0), (1, 2)], [(2, 0), (5, 1)]]
print(dikstra(g,len(g),0,2))
print(dikstra_heap(g,0,2))

