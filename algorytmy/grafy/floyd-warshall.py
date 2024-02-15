"""
FLOYD-WARSHALL - Najkrotsze sciezki miedzy kazda para wierzcholkow

konwencja:
- uzywamy matrixa - w specjalizowanych algo uzywa sie matrixa
!!!D[u][v] - dl najkrotszej sciezki z u do v
P[u][v] - parent - wierzcholek tuż przed v na najkrotszej sciezce z u do v

szukanie najkrotszej sciezki calej po wiezrcholkach
P[u][ P[u][v] ]

Idea:
jesli znamy najkrotsze sciezki miedzy kazda para wierzcholkow
ktore jako wewnetrzne wierzcholki uzywaja (v1, ... , v k-1)
<=> mozna zrobic to samo dla extended zbioru wierzcholkow (v1, ... , v k)

w seri n krokow rozszerza sciezki

Argument:
- albo sciezka do vk jest taka sama jak do k-1 
albo ten vk wystepuje gdzies po drodze
i musimy przejechac z x do vk a potem z vk do y
(wybieramy lepsza z 2 obcji (warunek trojkata))

zlozonosc: O(n^3)

konwencja:
V=(v1,...,vn)
St - macierz dlugosci najkrotszych sciezek
    opartych wewnetrzne wierzcholki ze zbioru (v1,...,vt)
S0 - macierz wag krawedzi miedzy wierzcholkami
    (inf - brak krawedzi)(gola nie przerabiana)

"""
# def floyd_warshall(S,n):
#     for t in range(1,n+1): #przez konwencje zapisu #range(n)
#         #dla danego t obliczamy macierz St z S t-1
#         for x e V:
#             for y e V:
#                 St[x][y]=min( S t-1[x][y],| S t-1 [x][vt] + S t-1 [vt][y] )
#                                             ^(trzeba uzyc wierzcholka posredniego)
#     D = Sn - macierz najkrotszych odleglosci to Sn

#te indeksy w macierzy mozna pominac - uzywa sie jednej macierzy
# uzupelnienie macierzy P
#   Pt[x][y] = P(t-1)[x][y]
#   Pt[x][y] = P(t-1)[vt][y]

def floyd_warshall(G,n):
    INF = float('inf')
    # zakladam ze kiedy nie ma krawedzi to w G[x][y] <- inf
    # D = G.copy() #robie backup i bedzie to tablica dystansow
    D = [[INF for _ in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i==j): #przekatna
                D[i][j] = 0
            if G[i][j] != 0: #wartosc co oznacza brak krawedzi
                D[i][j] = G[i][j]
    
    # inicjalizacja parent
    parent = [[None for _ in range(n)] for i in range(n)]
    for x in range(n):
        for y in range(n):
            if G[x][y] != INF : # istnieje krawedz (x,y)
                parent[x][y] = x #parent krawedzi x,y
            
    
    for t in range(n):
        for x in range(n):
            for y in range(n):
                if D[x][y] > D[x][t] + D[t][y] :
                #przez t mozna dostac sie szybciej wierzcholkiem posrednim
                    D[x][y] = D[x][t] + D[t][y] #przypisz ten szybszy dystans
                    parent[x][y] = parent[t][y]
    return D

g = [[0, 2, 0, 4], [2, 0, 1, 0], [0, 1, 0, 3], [4, 0, 3, 0]]
# g = [[0, 5, 0, 10], [0, 0, 3, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
print(floyd_warshall(g,len(g)))