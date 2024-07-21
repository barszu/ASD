from egz1atesty import runtests
"""
Bartłomiej Szubiak 415810

Generalnie idea opiera sie na znalezieniu najkrotszej sciezki (s -> b -> t ) albo bezposredniej (s -> t)
Jesli bedziemy znali najkrotszy dystans od 's' do kazdego wierzcholka (to mozemy to potraktowac jako dobiegniecie do niego)
a nastepnie wezmiemy rower na tym wierzchoklku 'b' i interesuje nas najkrotsza sciezka z b do t (ktora jest tym samym co z t->b podzgledem dystansu)
wartosc dist(b,t) zostanie pomnozona przez najlepszy czynnik_roweru i zmniejszona (w gorszym przypadku zwiekszona) nim , 
i dalej pozostanie najkrotsza z b d t (przy wzieciu rowera) bo tylko skalujemy wartosci (mnozymy przez jakas stala)

takze znajac najkrotszy dystans z 's' do kazdego wierzcholka i najkrotszy z kazdego wierzcholka do t (tak naprawde z t do kazdego) mozemy policzyc 
najktortszy calosciowy dystans

czyli obliczamy dlugosc trasy zakladajac ze przejezdamy przez wierzcholek 'b' (kazdy w grafie) :
dist(s,b) + czynnik_roweru * dist(b,t),    gdzie dist(b,t) == dist(t,b)
^                          ^
dobiega do b      bierze najlepszy rower i pokonuje nim najkrotsza trase z b do t

aby znalezc (najlepszy | najmniejszy) czynnik roweru tworze slownik (a tak naprawde tablice) 
gdzie kazdemu wierzcholkowi przypisuje najmniejszy czynnik_roweru = p/q, defaultowo zakladam inf (gdyby nie bylo roweru)

Aby znalezc wynik szykamy min tego wyrazenia: dist(s,b) + czynnik_roweru * dist(b,t) | b e V

funkcja build_graph tworzy graf w postaci listy sasiedztwa z listy krawedzi (zakladam ze nie wystepuje w liscie zduplikowana krawedz)

aby znalezc dystansy z s do kazdego uruchamiam algorytm dikstry, podobnie ze znalezniem wszytskich dystansow z t do kazdego innego 

zakladam ze wszystkie rowery moga byc gorsze (badz trasy trasy z nimi) wiec jako poczatkowa najlepsza wartosc trasy przyjmuje normlany dystans miedzy s, t
(tak jakby ta osoba sie poprostu przebiegla z s do t nie biorac roweru)

Generalnie mozna to rozwiazac z uzyciem 2 diksr poniewaz uczestnik nie moze zmienic roweru!


zlozonosc: O( E + 2*ElogV + len(B) ), dlatego ze budujemy graf (E) , 2* algorytm dikstry (ElogV) , i zmapowanie najlepszych rowerow (len(B))
 = O(ElogV + len(B))
"""


def build_graph(E): #  E = [(u,v,weigt)]
  max_idx = max([max(u,v) for u,v,w in E])
  G = [[] for _ in range(max_idx+1)] #(v,weight)
  for u,v,w in E: #moga sie dublowac ??
    G[u].append((v,w))
    G[v].append((u,w))
  return G


from queue import PriorityQueue
def dikstra(G,s):
  n = len(G)
  D = [float("inf")]*n #robi za visited odrazu, (kiedy D[u] == inf to visited[u] = False )
  D[s] = 0
  Q = PriorityQueue()
  Q.put((0,s)) #dist, vertex
  while not Q.empty():
    dist , u = Q.get()
    for v,w in G[u]:
      if D[v] > dist + w: #szybciej przez u do v
        D[v] = D[u] + w
        Q.put((D[v],v))
  return D


def map_bikes(B, G):
  n = len(G)
  bikes = [float('inf')]*n
  for (vertex, p,q) in B:
    bikes[vertex] = min(p/q , bikes[vertex])
  return bikes


def armstrong( B, G, s, t):
  # tu prosze wpisac wlasna implementacje
  G = build_graph(G)
  from_start = dikstra(G,s)
  from_end = dikstra(G,t) #albo od kazdego do t
  global_min_dist = from_start[t]

  bikes = map_bikes(B,G)

  for u in range(len(G)): #po wszystkich wierzcholkach
    global_min_dist = min(global_min_dist, from_start[u] + from_end[u] * bikes[u])

  return int(global_min_dist) #wziecie podlogi z liczby

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
