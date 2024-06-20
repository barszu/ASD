# Bartlomiej Szubiak 415810

#Zlozonosc czasowa: O(V+E)
#Zlozonosc pamieciowa: O(V+E)

#Tworzymy graf z listy krawedzi, bedziemy naraz szli bfs od przodu i od tylu (od x do y) i (od y do x)
#Robimy przediteracje BFS dla czytelnosci, przekazujemy do kolejki wierzcholek startowy i etykiete (min_p, max_p) gdzie min_p = max_p = p
# oraz kolor czyli informacje z ktorego bfsa on pochodzi, bfs sa od siebie niezalezne, maja swoje pamieci oraz tablice visited
# etykieta oznacza ze wszystkie obecnie napotkane pulapy sa w przedziale [min_p, max_p], etykieta jest zapisywane w pamieci dla wierzcholka

# w trakcie algorytmu BFS przechodzimy do sasiada v wtedy i tylko wtedy gdy nowe okno [min_p, max_p] jest poprawne tz. max_p - min_p <= 2t
# napotykajac wierzcholek y zwracamy True konczac dzialanie wiemy ze okno dla nieg jest poprawne z zalozenia ze staramy sie go nie psuc

# W przypadku gdy odwiedzimy wierzcholek z koloru 1 i z koloru 2 to ewaluujemy okna, jesli sie zlacza to zwracamy True (istaniala by ta sciezka)
# (lub odwrotnie)

# Dowod poprawnosci:
# 1. W grafie acyklicznym wystarczy ze bedziemy brneli do przodu az do napotkania wierzcholka y skaczac tylko tak aby nie psuc okna
# 2. W grafie cyklicznym jesli wpadniemy w cykl to nie bedzie mialo to nigdy benefitu, jesli wszystkie krawedzie w cyklu nie rujnowaly 
#    okna to powrot spowrotem do startu cyklu (dolozenie poraz kolejny tej samej krawedzi) kompletnie nic nie zmieni
#    sytuacja ta wydłuzy jedynie trase przybycia do wierzcholka y (zakladajac ze nie nalezal do cyklu), wiec spokojnie mozna ignorowac cykle
#    przez to wystarczy odwiedzac 1 raz wierzcholek, a nie odswiezac go wielokrotnie
# 3. W grafie z cyklem takim ze zla sciezka jest u góry tz. dochodzimy do wyjscia z cyklu i dalej nie da sie przejsc. A idac od dolu by sie dalo
#    pojedynczy BFS nie wystarczy, ale BFS od dolu i od gory wystarczy, bo zawsze bedziemy mieli informacje o oknie z obu stron (bfs'y sie dotknal)

from zad4testy import runtests
from collections import deque

def create_graph(L): #O(E)
  vertex_no = max([v for u,v,p in L]) + 1 # zawsze v > u
  G = [ [] for _ in range(vertex_no) ]
  for u,v,p in L:
    G[u].append((v,p))
    G[v].append((u,p))
  return G

def isIn(this, other):
  # other szerszy
  a , b = this
  x, y = other
  return x <= a and b <= y

from collections import deque
def Flight(L,x,y,t): #O(V+E)
  G = create_graph(L)
  n = len(G)

  visited_start = [False] * n #kolor 1 -> 1 bfs odwiedzil , 
  visited_end = [False] * n #kolor 2 -> 2 bfs odwiedzil

  memory_bfs_start = [None]*n #zapamietanie okna dla wierzcholka bfs1
  memory_bfs_end = [None]*n #zapamietanie okna dla wierzcholka bfs2

  Q = deque()
  #przed iteracja

  #bfs1
  for v,p in G[x]:
    Q.append((v,(p,p),1)) #wierzcholek, okno, kolor
    memory_bfs_start[v] = (p,p)
  visited_start[x] = True

  #bfs2
  for v,p in G[y]:
    Q.append((v,(p,p),2))
    memory_bfs_end[v] = (p,p)
  visited_end[y] = True

  while Q:
    u , (min_p , max_p), color = Q.popleft() #zawsze poprawne tz. diff(min_p,max_p) <= 2t

    if color == 1: #z bfs1
      if u == y: return True
      if visited_start[u]: continue
      if visited_end[u]: #bylismy juz tu 2 bfs, ewaluacja okien
        old_min_p , old_max_p = memory_bfs_end[u]
        if isIn((old_min_p , old_max_p), (min_p,max_p) ): #przedzialy sie zlaczyly
          return True
        

    elif color == 2: #z bfs2
      if u == x: 
        return True
      if visited_end[u]: continue
      if visited_start[u]: #bylismy juz tu 1 bfs, ewaluacja okien
        old_min_p , old_max_p = memory_bfs_start[u]
        if isIn((min_p,max_p) , (old_min_p , old_max_p)): #przedzialy sie zlaczyly
          return True
        
    for v,p in G[u]: #sasiad u , pulap pomiedzy u a v
      new_min_p = min(min_p,p)
      new_max_p = max(max_p,p)
      if new_max_p - new_min_p > 2*t:
        continue #psuje okno
      Q.append((v,(new_min_p,new_max_p),color))
      if color == 1:
        memory_bfs_start[v] = (new_min_p,new_max_p)
        visited_start[u] = True
      elif color == 2:
        memory_bfs_end[v] = (new_min_p,new_max_p)
        visited_end[u] = True

  return False


runtests( Flight, all_tests = True )
