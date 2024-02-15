from zad8testy import runtests
# Bartlomiej Szubiak
# Dzialanie algorytmu:
# - na poczatku laczymy osiagalne plamy ze soba i traktujemy jako jedno cialo
# - otrzymujemy tablice 1D mowiaca ze zatrzymujac sie w komorce i mozna zatankowac gas_tab[i] paliwa
# - plamy sa scalane z uzyciem bfs plansze tarktuje jako graf i bfs przejdzie tylko po czesciach ktore sa spojne i stad wiemy co jest plama
# - sprawdzam czy poczatkowe tankowanie juz nie wystarcza
# - jesli nie wystarcza na bierzaco bedzie generowane male drzewo z uzyciem klasy Graph_Node

# - glowa jest najwieksza (chwilowo) ilosc paliwa brana pod uwage (wzieta)
# - dziecmi sa ilosci paliwa ktore sa osiagalne na ten moment (te jeszcze nie wziete)
# - sortuje zawsze dzieci tak aby jako nowa glowe (tankowac) najwieksza ilosc paliwa
# - na bierzaca dopisuje kolejne osiagalne wartosci paliwa do dzieci

# zlozonosc: O( m*V + k*(p log p)) <=> O(mn) 
# m - szerkosc planszy
# V - wielkosc plamy (ile pol zajmuje)
# k - ilosc plam do ktorych jest realny dostep (wszystkich)
# p - ilosc plam do ktorych jest dostep (dzieci root'a)

from collections import deque 


def fits(i,n):
    return (-1<i<n)

def BFS(T,visited,s):
    # wierzcholek jako (i,j) {wiersz,kolumna} krawedz istnieje jesli na okolo != 0
    collected_gas = T[0] [s]
    q=deque()
    m = len(T[0]) #szerokosc
    n = len(T) #wysokosc
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    if ( (visited[0] [s]) or (T[0] [s] == 0) ):
        return 0 #pomin to, pole bylo juz wziete lub to nie plama
    q.append((0,s))
    visited[0] [s] = True
    
    while q :
        (i,j)=q.popleft()
        for (di,dj) in moves : #sasiedzi u
            new_i = i+di
            new_j = j+dj
            if not fits(new_i,n) or not fits(new_j,m): continue #poza zakresem tablicy
            if T[new_i] [new_j] == 0 : continue #nie nalezy do plamy
            if not visited[new_i] [new_j]: #not v.visited
                visited[new_i] [new_j] = True
                collected_gas += T[new_i] [new_j]
                q.append((new_i,new_j))
    return collected_gas 

def merge_plamy(T):
    m = len(T[0]) #szerokosc
    n = len(T) #wysokosc
    merged_gas = [0 for i in range(m)]
    visited_bfs = [[False for i in range(m)] for j in range(n)]
    for i in range(m):
        merged_gas[i] = BFS(T,visited_bfs,i)
    return merged_gas
    
class Graph_Node:
    def __init__(self,v,old_access,max_access,):
        self.childs_tab = [] #int tab
        self.val = v
        self.max_access = max_access
        self.old_access = old_access
    
    def add_child(self,v):
        #TODO dodawanie do posortowanej listy
        self.childs_tab.append(v)
    
    def sort_child(self):
        self.childs_tab.sort()

def spisz_z_tab(Gas,Node):
    n = len(Gas)
    s = Node.old_access
    k = Node.max_access
    for i in range(s,k+1):
        if i> n-1: break
        if Gas[i] > 0 :
            Node.add_child(Gas[i])
    if len(Node.childs_tab) > 1:
        Node.sort_child()


def tree(Gas_tab,Node): #-> new = Node
    #dostaje posortowane dzieci
    new_value = Node.childs_tab.pop(-1)
    old_access = Node.max_access
    new_Node = Graph_Node(new_value , old_access+1 , old_access + new_value )
    new_Node.childs_tab = Node.childs_tab
    spisz_z_tab(Gas_tab , new_Node)
    return new_Node

def plan(T):
    # tu prosze wpisac wlasna implementacje
    gas_tab = merge_plamy(T)
    n = len(gas_tab)
    stops_cnt = 1
    accesable_idx = gas_tab[0]
    if accesable_idx >= n-1 :
        return 1 #tankowanie na poczatku wystarcza
    
    root = Graph_Node(gas_tab[0] , 1 , gas_tab[0])
    spisz_z_tab(gas_tab,root)
    
    while not root.max_access >= n-1 :#juz da sie dojsc 
        root = tree(gas_tab,root)
        stops_cnt += 1

    return stops_cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

