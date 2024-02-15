from egzP3btesty import runtests 
from queue import PriorityQueue

class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0 #ilosc el w tym zbiorze w ktorym jest node -> 
        # wyplynie i zawsze prawdziwe bedzie dla roota zbioru
        # -> tutaj (w tej impelemtavji) mowi to tyle ze ile ma dzieci #gdyby startowo = 1 to dzieci + 1 = size_of_tree
        self.value = value

def find_set(x: Node): #find oryginal parent
    #znajduje reprezentacja zbioru do ktorego nalezy x
    if x.parent != x:
        x.parent = find_set(x.parent)  # kompresja ścieżki
    return x.parent

def union(x: Node, y: Node):
    # polaczenie dwoch zbiorow A B do ktorych nalezy x , y
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(edges_tab, v_no): #edges=[(u,v,waga)]
    # Inicjalizacja zbiorów rozłącznych
    nodes = [Node(i) for i in range(v_no)] #nodes dla wierzcholkow

    max_sum = 0
    added_extra = False
    
    for e in reversed(edges_tab):
        u, v, weight = e
        if find_set(nodes[u]) != find_set(nodes[v]): #nodes[u] - obiekt_u (parent,rank,value)
            #u,v naleza do innych zbiorow
            max_sum += weight
            union(nodes[u], nodes[v])
        elif not added_extra: #krawedz nie pasuje do MST, ale jest 1 gruba rybą
            added_extra = True
            max_sum += weight
    
    return max_sum

def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację 
    # max spanning tree + 1 krawedz kolidujaca
    n = len(G)
    used_edges = [ [False for i in range(n)] for j in range(n)]
    E = [] #(u,v,weight)
    #conwert graph
    all_weight = 0
    for u in range(n):
        for ( v , weight ) in G[u]:
            if used_edges[u][v]: continue
            E.append((u,v,weight))
            all_weight += weight
            used_edges[u][v] = True
            used_edges[v][u] = True
    E.sort(key = lambda x: x[2])
    #uruchom kruskala i dodaj najciezsza niepasujaca
    max_taken_sum = kruskal(E,n)
    
    return all_weight-max_taken_sum

runtests ( lufthansa, all_tests=True )