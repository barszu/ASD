from zad6testy import runtests

"""
Bartlomiej Szubiak 415810

Na samym poczatku przechodze po macierzy grafu i tworze z niego reprezentacje listowa (liste sasiedztwa)
Nastepnie uruchomie zmodyfikowany algorytm dikstry, kazdemu wierzcholkowi dam etykiete 0 | 1 
-> czy przyszlem do niego z normalnego skoku czy z podwojnego
Rozmnazając wierzcholki, czyli od teraz wierzcholek u -> (u,from_)

jesli przyszlem z normalnego skoku to moge znowu isc normalnie lub zrobic podwojny skok
jesli przyszlem z podwojnego skoku to moge tylko isc normalnie

zlozonosc czasowa: O(EVlogV) -> E - liczba krawedzi, V - liczba wierzcholkow
dlatego ze dla kazdego mozliwego wierzcholka iterujemy po jego sasiadach i sasiaadach sasiadow


"""

def cretate_adjacency_list( G ): # (u,dist)
    n = len( G )
    adj_list = [ [] for _ in range( n ) ]
    for i in range( n ):
        for j in range( n ):
            d = G[ i ][ j ]
            if d != 0:
                adj_list[ i ].append( (j,d) )
                # adj_list[ j ].append( (i,d) )
    return adj_list


from queue import PriorityQueue

def dikstra1(G, s, w): #dziala
    n = len(G)
    INF = float('inf')
    distance = [[INF for __ in range(len(['from_normal', 'from_jumper']))] for _ in range(n)]
    visited = [[False for __ in range(len(['from_normal', 'from_jumper']))] for _ in range(n)]
    # visited[u][from_]
    # distance[u][from_]
    distance[s][0] = 0
    distance[s][1] = 0

    Q = PriorityQueue()
    Q.put((0, s, 0)) # distance_to_u, u, from normal jump | fast jump => 0 | 1

    while not Q.empty():
        d_u, u, from_ = Q.get()
        if visited[u][from_]:
            continue

        for (v, d_v) in G[u]: # v sasiad u
            # normalny skok -> 0 (wchodze normalnie)
            temp_dist = d_u + d_v
            if temp_dist < distance[v][0]:
                distance[v][0] = temp_dist
                Q.put((temp_dist, v, 0)) #normal jump

            # podwojny skok -> 1 (wchodze z podwojnego)
            if from_ == 0: #tylko dla normal jump
                for (b, d_b) in G[v]: #b sasiad v 
                    if b == u: continue #bo taki skok nie ma sensu (u ->(v)-> u)
                    temp_dist = d_u + max(d_v , d_b)
                    if temp_dist < distance[b][1]:
                        distance[b][1] = temp_dist
                        Q.put((temp_dist, b, 1)) #fast jump

        visited[u][from_]=True #po przetworzeniu wierzcholka u

    return min(distance[w][0], distance[w][1])


def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje

    G = cretate_adjacency_list( G )
    res = dikstra1( G, s, w )

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )

