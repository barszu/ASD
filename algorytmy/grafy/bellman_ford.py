"""
DIKSTRA WAGI UJEMNE !!!
BELLMAN-FORD - dikstra ale wagi moga byc ujemne (brut)

GRAF SKIEROWANY
- kiedy jest ujemna waga to tak jakby byla krawedz w druga strone z ta waga
- musimy wykrywac ujemne cykle zeby sie nie zapetlac
- mozna sie wrocic do odwiedzonego wierzcholka i go poprawic! <- w przeciwienstwie do dikstry

1. inicjalizacja
    for v e V:
        v.d = inf
        v.parent = None
    s.d = 0

2. relax'je
    for i in range( V - 1 ):
        for (u,v) e E:  #dla kazdej krawedzi
            relax(u,v)
            
3. weryfikacja - czy kazdego (u,v) e E:

    v.d <= u.d + distance(u,v) ?
    - jezeli to nie zachodzi dla kazdego oznacza to ze jest jakis cykl o ujemnej wartosci

kroki 1,2 daja dobry wynik jesli nie ma cykli o ujemnej wadze
kazda iteracja relaksuje co najmniej jedna dalej krawedz najkrotszej sciezki

zlozonosc O(VE)
        
"""

def bellman_ford_ls(G, s):
    n = len(G)
    inf = float('inf')
    distances = [inf] * n
    parent = [None] * n
    distances[s] = 0

    # Relaksacja krawędzi V-1 razy
    for k in range(n-1): #cheapest flight withing n-1 stops (all posible) -> stops bfs layers from starting node
        for u in range(n): #dla kazdej krawedzi u,v
            for (weight,v)  in G[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parent[v] = u

    # Sprawdzenie na obecność cykli o ujemnej wadze
    for u in range(n):
        for (weight,v) in G[u]:
            if distances[u] + weight < distances[v]:
                return None  # Wykryto cykl o ujemnej wadze

    return distances,parent

# bellman ford ale najtanszy koszt dotarcia w k zatrzymaniach (przez k wierzcholkow) do zrodla
# k - zatrzymania pomiedzy src , dst + 1 (na mete)
def bellman_ford(n: int, edges: list[list[int]], src: int, dst: int, k_max: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for k in range(1 , k_max+1): #wysokosc fali BFS -> stops
            tmp_dist = dist.copy()

            for u , v , p in edges: #u->v , weight
                if dist[u] == INF : continue
                if dist[u] + p < tmp_dist[v]:
                    tmp_dist[v] = dist[u] + p
            dist = tmp_dist
        return dist[dst] if dist[dst] != INF else -1

g = [[(-1, 1), (3, 2)], [(4, 0), (1, 2)], [(2, 0), (5, 1)]]

print(bellman_ford_ls(g,0))
