from kol2testy import runtests
"""
Bartlomiej Szubiak 415810

Uzyje algorytmu dikstry ale rozmnoze wierzcholki w grafie 16 razy bo tyle maksymalnie trwa podroz (w godzinach)
Rozmnazajac wierzcholki kiedy dostane sie lepsza droga do wierzcholka 'u' zostanie to uwzglednione przy calej sciezke

Glowna funkcja rozwiazujaca zadanie to 'dikstra' ktora przyjmuje zparametryzowane czas postoju jak i maksymalny czas podrozy
Kiedy docieram do wierzcholka 'u' z czasem podrozy 't' i z dystansem 'curr_dist' rozchodze sie dalej po sasiadach jak w algorytmie dikstry
Ale uwzgledniam fakt postoju, resetu czasu podrozy

Algorytm dikstry dziala tak ze jesli dojdziemy po raz 1 do wierzcholka to bylo to najszybsze dojscie, rozmnazajac wierzcholki uwzgledniam 
czas podrozy (od 0 do 16)

zwracam najmniejsza wartosc dotarcia do wierzcholka koncowego jako min ze wszytskich mozliwych obcji dotarcia z czasem _t

Zlozoność obliczeniowa: O(ElogV) bo travel_time to stala, pamieciowa O(V^2) bo potrzebny byl bufor w funkcji create_graph

Mozliwe ze przez drobny blad w algorytmie nie przechodzi niektorych testow.
"""

#znajduje liczbe n wierzcholkow
def find_vertex_no(E):
  maxy = -1 #najwiekszy numer wierzcholka
  for u, v, weight in E:
    maxy = max(maxy,u,v)
  return maxy + 1 #jako n - liczba wierzcholkow

def create_graph(E):
  n = find_vertex_no(E)
  G = [[] for u in range(n)] # (v, weight)
  used_edges = [[False for _ in range(n)] for __ in range(n)]
  for u,v,weight in E:
    if (not used_edges[u][v]) and (not used_edges[v][u]): #ta krawedz nie byla uzyta
      G[u].append((v,weight))
      G[v].append((u,weight))
      #oznacz jako uzyta
      used_edges[u][v] = True
      used_edges[v][u] = True
  return G

from queue import PriorityQueue

def dikstra(G , start_node , end_node , max_travel_time=16 , rest_time=8 ):
  n = len(G)
  INF = float('inf')
  distance = [[INF for __ in range(max_travel_time+1)] for _ in range(n)] # [u][travel_time]
  visited = [[False for __ in range(max_travel_time+1)] for _ in range(n)] # [u][travel_time]
  Q = PriorityQueue()

  Q.put((0,start_node,0)) # (curr_dist, start_node, travel_time)

  while not Q.empty():
    curr_d , u , t = Q.get()

    if visited[u][t] == True: continue
    #odwiedzany pierwszy raz
    # if visited[u][t]: continue #added
    
    distance[u][t] = curr_d
    # visited[u][t] = True #added


    for (v,weight) in G[u]: #sasiad u
      if weight > max_travel_time: continue #tej krawedzi nie da sie przejsc

      if t + weight > max_travel_time: #bedzie musial odpoczac
        new_d = curr_d + weight + rest_time
        new_t = weight
      
      else: #podruzuje dalej
        new_d = curr_d + weight
        new_t = t + weight

      if new_d < distance[v][new_t]:
        Q.put((new_d,v,new_t))
        distance[v][new_t] = new_d


    visited[u][t] = True
       
  # res = [distance[end_node][_t] for _t in range(max_travel_time)] <- tutaj ma byc max_travel_time+1
  # return min(res)

  res = min(distance[end_node]) #added
  return res if res != INF else -1 #added







def warrior( G, s, t):
  # tu prosze wpisac wlasna implementacje
  G = create_graph(G)
  res = dikstra(G,s,t,max_travel_time=16, rest_time=8)
  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
