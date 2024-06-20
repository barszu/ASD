from zad4testy import runtests
# Bartlomiej Szubiak 415810

#Zlozonosc czasowa: O(V+E)
#Zlozonosc pamieciowa: O(V+E)

#Tworzymy graf z listy krawedzi
#Robimy przediteracje BFS dla czytelnosci, przekazujemy do kolejki wierzcholek startowy i etykiete (min_p, max_p) gdzie min_p = max_p = p
# etykieta oznacza ze wszystkie obecnie napotkane pulapy sa w przedziale [min_p, max_p]

# w trakcie algorytmu BFS przechodzimy do sasiada v wtedy i tylko wtedy gdy nowe okno [min_p, max_p] jest poprawne tz. max_p - min_p <= 2t
# napotykajac wierzcholek y zwracamy True konczac dzialanie wiemy ze okno dla nieg jest poprawne z zalozenia ze staramy sie go nie psuc

# Dowod poprawnosci:
# 1. W grafie acyklicznym wystarczy ze bedziemy brneli do przodu az do napotkania wierzcholka y skaczac tylko tak aby nie psuc okna
# 2. W grafie cyklicznym jesli wpadniemy w cykl to nie bedzie mialo to nigdy benefitu, jesli wszystkie krawedzie w cyklu nie rujnowaly 
#    okna to powrot spowrotem do startu cyklu (dolozenie poraz kolejny tej samej krawedzi) kompletnie nic nie zmieni
#    sytuacja ta wydłuzy jedynie trase przybycia do wierzcholka y (zakladajac ze nie nalezal do cyklu), wiec spokojnie mozna ignorowac cykle
#    przez to wystarczy odwiedzac 1 raz wierzcholek, a nie odswiezac go wielokrotnie


def create_graph(L): #O(E)
  vertex_no = max([v for u,v,p in L]) + 1 # zawsze v > u
  G = [ [] for _ in range(vertex_no) ]
  for u,v,p in L:
    G[u].append((v,p))
    G[v].append((u,p))
  return G


from collections import deque
def Flight(L,x,y,t): #O(V+E)
  G = create_graph(L)
  n = len(G)

  visited = [False] * n
  Q = deque()
  #przed iteracja
  for v,p in G[x]:
    Q.append((v,(p,p)))
  visited[x] = True

  while Q:
    u , (min_p , max_p) = Q.popleft() #zawsze poprawne tz. diff(min_p,max_p) <= 2t
    if visited[u]:
      continue

    if u == y: #okno poprawne bo wczesniej to bylo sprawdzane
        return True

    for v,p in G[u]: #sasiad u , pulap pomiedzy u a v
      visited[u] = True

      new_min_p = min(min_p,p)
      new_max_p = max(max_p,p)
      if new_max_p - new_min_p > 2*t:
        continue #psuje okno

      Q.append((v,(new_min_p,new_max_p)))

  return False



  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )


# my test
L = [(0,1,50),(1,2,50),(0,3,20),(3,4,10),(4,2,20),(2,5,10)]
t = 5
x = 0
y = 5
print(Flight(L,x,y,t)) #true