"""
BFS - znajduje najkrotsze sciezki w sensie liczby krawedzi,

dzialanie:
    idziemy fala -> rozchodzimy sie po grafie rownomiernie od pkt startu
    (najpierw zalatwiane sa wierzcholki o dystansie 1,2,3... itd)
    wchodzimy tylko do odwiedzonych

zastosowania:
- spojnosc grafu
- dwudzielnosc, kolorowania(visited->kolory)
- wykrywanie cykli
- promieniowanie od obiektow -> trzymaj w q tylko node z jednej fali ->
    petla wyciagnij tyle ile bylo przed dodawaniem i je przetworz

zlozonosc:
    O(V+E) - ls
    O(V^2) - macierz.

"""

from collections import deque 
# lista sasiedzctwa to tablica 2d (szarpana)
def BFS_ls(G,s): #graf , startowy punkt rozwijania
    #G=(V,E) , s eV
    q=deque()
    n=len(G) #len(v)
    distance=[-1]*n #distance i-tego wierzchokka od tego s
    visited=[False]*n #czy odwiedzono juz ten, zeby sie nie zapetlac
    parent=[None]*n #kto byl rodzicem i-tego wierzcholka -> jak dotarlismy
    
    q.append(s)
    visited[s] = True
    distance[s]=0
    parent[s]=None
    
    while q :
        u=q.popleft()
        # print(u, end = " ")
        for v in G[u] : #sasiedzi u
            if not visited[v]: #not v.visited
                distance[v] += 1
                parent[v] = u
                visited[v] = True
                q.append(v)
    return distance,parent,visited # koniec algorytmu zwroc co potrzebne

# macierz i->start j->koniec (u->v)
#  - - - - -
#| 0 1 0 0 0
#| 0 0 1 0 0
#| 0 0 0 1 0
#| 1 0 0 0 1
#| 0 1 1 0 0

def BFS_mat(G,s): #graf , startowy punkt rozwijania
    #G=(V,E) , s eV
    q=deque()
    n=len(G) #len(v)
    distance=[-1]*n #distance i-tego wierzchokka od tego s
    visited=[False]*n #czy odwiedzono juz ten, zeby sie nie zapetlac
    parent=[None]*n #kto byl rodzicem i-tego wierzcholka -> jak dotarlismy
    
    #przediteracja
    q.append(s)
    visited[s] = True
    distance[s]=0
    parent[s]=None
    
    while q :
        u=q.popleft()
        # print(u, end = " ")
        for v in range(n) : #sasiedzi u -> v
            if G[u] [v] == 0 : continue
            if not visited[v]: #not v.visited
                distance[v] += 1
                parent[v] = u
                visited[v] = True
                q.append(v)
    return (distance,parent,visited) # koniec algorytmu zwroc co potrzebne

graph = [ [0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[1,0,0,0,1],[0,1,1,0,0] ]
a=BFS_mat(graph,3)

g=[[1], [2], [3], [0, 4], [1, 2] ]
print("\n")
BFS_ls(g,3)
