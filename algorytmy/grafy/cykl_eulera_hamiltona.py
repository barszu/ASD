"""
cykl Eulera - cykl po wszytskich krawedziach kazda odwiedzajac dokladnie 1 raz

warunek konieczny : graf NIEskierowany i SPOJNY ma cykl Eulera wtw:
                -> kazdy wierzcholek ma PARZYSTY stopien    

warunek wystarczajacy: (algo):
-+ wybieramy dowolny wierzcholek v (normal DFS)
-+ startujac z v wedrujemy, za kazdym razem wybierajac dowolna jeszcze nie uzyta krawedz (normal DFS)

  (zuzylismy w wierzcholku v jedna krawedz wiec jego stopien jest nieparzysty to samo dla wierzcholka u1 do ktorego przeszlismy)
  (jezeli z u1 pojdziemy do u2 to w u1 jest parzysty stopien nieuzytych krawedzi a w u2 nieparzysty)
- tworzac ta sciezke mamy zawsze sytuacje ze wierzcholek poczatkowy v i koncowy un maja nieparzysty stopien

-+ (wkoncu z powrotem dotrzemy do v) aby byl ten cykl musi byc krawedz miedzy v a un (wtedy beda miec parzysty stopien)

-+ mamy juz cykl eulera (zobacz czy zostaly krawedzie) 
   /lub dokleic kolejny cykl ktory zawiera jakis wierzcholek uk
   
Algo (DFS):
    - visited krawedzie - usuwamy krawedzie po ktorych przeszlismy
    - do danego wierzcholka mozna wejsc dowolna liczbe razy

- po przetworzeniu danego wierzcholka dopisujemy go na poczatek tworzonego cyklu (tablicy)

zlozonosc: (taka sama jak DFS)
- ls O(V+E)
- matrix O(V^2)

uwaga mozna czasem zle zrobic i miec:
O( V^2 + VE ) , O(V^3)
-> uniknij -> hash table dla ls albo macierzy zeby caly czas po sasiadach nie fruwac albo pointer jakis co ostatnio bylo uzyte


"""

"""
cykl hamiltona - cykl prosty (NIE powtarzajacy wierzcholkow) ktory odwiedza kazdy wierzcholek dokladnie raz

Algorytm: Brute-force - sprawdza O(V!) mozliwosci

Nie da sie lepiej bo rozpoznawanie czy graf ma cykl Hamiltona jest problemem np-zupelnym
 
"""    

def find_euler_cycle_ls(G):
    n = len(G)
    cycle = [-1]*(n**2)  # lista przechowująca cykl Eulera
    c_idx = 0

    def pop_on_other_side(G,u,v):
        for idx in range(len(G[u])):
            if G[u][idx]==v:
                G[u].pop(idx)
                return idx
        return None

    def dfs_visit(u):
        nonlocal c_idx , G , cycle
        while G[u]:
            # wywal G[u][v] , G[v][u] 
            v = G[u].pop()  # usuń pierwszą krawędź z listy sąsiadów v
            pop_on_other_side(G,v,u)
            
            dfs_visit(v)
            
        cycle[c_idx]=u
        c_idx += 1
        
    dfs_visit(0)
    return cycle[:c_idx] #jest on od tylu podany

def find_euler_cycle_non_rek(G):
    cycle = []
    stack = [0]
    
    while stack:
        u = stack[-1]
        if len(G[u]) > 0: #if has childs go to them
            v = G[u].pop()
            stack.append(v)
        else: #now useless
            cycle.append(u)
            stack.pop()
            
    return cycle[::-1]


g = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
# g = [[1,4],[0,4],[4,3],[4,2],[0,1,2,3]]
print(find_euler_cycle_ls(g))