"""
MST (minimal spanning trees) - MINIMALNE DRZEWA ROZPINAJACE
- graf NIEskierowany
- krawedzie maja wagi (ujemne tez moga byc)

-> graf dalej jest spojny ale sa tylko krawedzie min , nie ma cyklow

cel:
znalezc podzbior krawedzi tworzacy spojny podgraf 
(obejmujacy wszytskie wierzcholki)
o minimalnej sumie wag

ujemne wagi zamienic na dodatnie dodajac stala

tworzymy algorytm zachlanny ktory podejmuje lokalnie optymalne decyzje
np. dikstra jest zachlannym

KIEDY MOZEMY DOLOZYC KRAWEDZ DO BUDOWANEGO DSC???: (swapnac)

Jesli A jest podzbiorem zbioru krawedzi MST 
    e=(u,v):
-> e nie nalezy do A
-> (A+(e)) nie zawiera cyklu - kiedy wsadzimy cykl to MST przestanie byc drzewem -> nie bedziemy miec minimalnego kosztu
-> e ma min wage : wsrod krawedzi spelniajacych ^ (powyzsze warunki)

to: Au(e) jest podzbiorem krawedzi pewnego MST
"""
"""
KRUSKAL dla MST
-> da nam zbior krawedzi ale nie stworzy struktury drzewa
1. posortuj krawedzie po wagach
2. zacznij z A=() - zbior pusty
3. przegladaj krawedzie w kolejnosci (nierosnacych) \_> wag
    - jesli Au(e) nie zawiera cyklu: A := Au(e)
4. return A

zlonosc: O(E logV ) - zlozonosc czasowa przy szybkim wykrywaniu tych cykli
"""
"""
PRIM dla MST - kopja dikstry
v - wierzcholek startowy
1. wrzuc kazdy wierzcholek do PQ w waga inf (ale tak naprawde to nie) 
    (jakim kosztem mozna rozszerzyc MST o dany wierzcholek)
2. zmien wage v na 0
3. while not PQ.is_empty(): #to samo co w dikstrze ale zmodyfikowany relax
    - wyjmij u o min wadze z PQ
    - dla kazdej krawedzi (u,x) , jesli 
        waga((u,x)) < x.waga w PQ :
        -> x.waga = waga((u,x))
        (dokladamy do drzewa -> uaktualnij parent)

zlonosc: O(E log V)

"""
"""
Mozna sprawdzac ile jest spojnych skladowych (connected compotents) 
-> n - ilosc successful uni (kruskala)
"""
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
    
    # Sortowanie krawędzi według wag
    edges_tab.sort(key=lambda x: x[2]) #def fn(x:el_tab): return x[2]
    
    minimum_spanning_tree = []
    
    for e in edges_tab:
        u, v, weight = e
        if find_set(nodes[u]) != find_set(nodes[v]): #nodes[u] - obiekt_u (parent,rank,value)
            #u,v naleza do innych zbiorow
            minimum_spanning_tree.append(e)
            union(nodes[u], nodes[v])
    
    return minimum_spanning_tree

edg = [(0, 1, 4), (0, 7, 8), (1, 7, 11), (1, 2, 8), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
v_no = 9
print(kruskal(edg,v_no))