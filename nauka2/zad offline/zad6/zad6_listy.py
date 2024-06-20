from zad6testy import runtests

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
            # normal jump, always resets from_ to 0
            temp_dist = d_u + d_v
            if temp_dist < distance[v][0]:
                distance[v][0] = temp_dist
                Q.put((temp_dist, v, 0)) #normal jump
                # print(f"dodano krawedz {u}_{from_} -> {v}_{0} z dystansem {temp_dist}")

            # fast jump
            if from_ == 0: #tylko dla normal jump
                for (b, d_b) in G[v]: #b sasiad v 
                    if b == u: continue #bo taki skok nie ma sensu (u ->(v)-> u)
                    temp_dist = d_u + max(d_v , d_b)
                    if temp_dist < distance[b][1]:
                        distance[b][1] = temp_dist
                        Q.put((temp_dist, b, 1)) #fast jump
                        # print(f"dodano krawedz {u}_{from_} -> {b}_{1} z dystansem {temp_dist}")

        visited[u][from_]=True #po przetworzeniu wierzcholka u

    return min(distance[w][0], distance[w][1])


from queue import PriorityQueue #jakis bug jest w kodzie
def dikstra2(G, s, w):
    # 0 - wszedlem normalnie
    # 1 - chce go przeskoczyc (jestem w trakcie skoku)
    # 2 - wszedlem skokiem
    n = len(G)
    INF = float('inf')
    distance = [[INF for __ in range(len([0,1,2]))] for _ in range(n)]
    visited = [[False for __ in range(len([0,1,2]))] for _ in range(n)]
    # visited[u][from_]
    # distance[u][from_]
    distance[s][0] = 0

    Q = PriorityQueue()
    Q.put((0, s, 0)) # distance_to_u, u, from normal jump | fast jump => 0 | 1

    while not Q.empty():
        u_dist, u, from_ = Q.get()
        if visited[u][from_]: continue

        for (v, d_v) in G[u]: # v sasiad u
            if from_ == 0: #wchodze normalnie, moge znowu normalnie kolejny przejsc albo nad nim
                temp_dist = u_dist + d_v
                if temp_dist < distance[v][0]: #normalnie
                    distance[v][0] = temp_dist
                    Q.put((temp_dist, v, 0))
                    print(f"dodano krawedz {u}_{from_} -> {v}_{0} z dystansem {temp_dist}")
                if temp_dist < distance[v][1]: #nad nim #HAZARD
                    distance[v][1] = d_v #tylko jako bufor zeby zapamietac ze bylismy nad nim
                    Q.put((u_dist, v, 1)) #zeby pamietac wartosc starej trasy
                    print(f"dodano krawedz {u}_{from_} -> {v}_{1} z dystansem {temp_dist}")

            elif from_ == 1: #jestem nad nim to do sasiada skokiem wchodze
                temp_dist = u_dist + max(distance[u][1], d_v)
                if temp_dist < distance[v][2]: #skokiem
                    distance[v][2] = temp_dist
                    Q.put((temp_dist, v, 2))
                    print(f"dodano krawedz {u}_{from_} -> {v}_{2} z dystansem {temp_dist}")

            elif from_ == 2: #weszlem skokiem, moge tylko normalnie
                temp_dist = u_dist + d_v
                if temp_dist < distance[v][0]: #normalnie
                    distance[v][0] = temp_dist
                    Q.put((temp_dist, v, 0))
                    print(f"dodano krawedz {u}_{from_} -> {v}_{0} z dystansem {temp_dist}")

        visited[u][from_]=True #po przetworzeniu wierzcholka u
    
    

    res = min(distance[w][0], distance[w][2])
    print(distance[w][0], distance[w][2])
    return res


from queue import PriorityQueue #jakis bug jest w kodzie
def dikstra3(G, s, w):
    # 0 - wszedlem normalnie
    # 1 - chce go przeskoczyc (jestem w trakcie skoku)
    # 2 - wszedlem skokiem
    n = len(G)
    INF = float('inf')
    distance = [[INF for __ in range(len([0,1,2]))] for _ in range(n)]
    visited = [[False for __ in range(len([0,1,2]))] for _ in range(n)]
    # visited[u][from_]
    # distance[u][from_]
    distance[s][0] = 0

    Q = PriorityQueue()
    Q.put((0, s, 0, None)) # distance_to_u, u, from normal jump | fast jump => 0 | 1

    while not Q.empty():
        u_dist, u, from_, last_edge = Q.get()
        if visited[u][from_]: continue
        if u_dist > distance[u][from_]: 
            continue
        distance[u][from_] = u_dist if u_dist < distance[u][from_] else distance[u][from_]

        if u == 5 and from_ == 2:
            print('tu')

        for (v, d_v) in G[u]: # v sasiad u
            if u == 3 and from_ == 0 and v == 4:
                print('tu')
            if u == 4 and from_ == 1 and v == 5:
                print('tu')
            if from_ == 0: #wchodze normalnie, moge znowu normalnie kolejny przejsc albo nad nim
                temp_dist = u_dist + d_v
                Q.put((temp_dist, v, 0, None)) #normalnie
                print(f"dodano krawedz {u}_{from_} -> {v}_{0} z dystansem {temp_dist}")
                Q.put((u_dist, v, 1, d_v)) #zeby pamietac wartosc starej trasy
                print(f"dodano krawedz {u}_{from_} -> {v}_{1} z zapamietanym dystansem {u_dist} | {d_v}")

            elif from_ == 1: #jestem nad nim to do sasiada skokiem wchodze
                temp_dist = u_dist + max(last_edge, d_v)
                Q.put((temp_dist, v, 2, None)) #skokiem
                print(f"dodano krawedz {u}_{from_} -> {v}_{2} z dystansem {temp_dist}")

            elif from_ == 2: #weszlem skokiem, moge tylko normalnie
                temp_dist = u_dist + d_v
                Q.put((temp_dist, v, 0, None)) #normalnie
                print(f"dodano krawedz {u}_{from_} -> {v}_{0} z dystansem {temp_dist}")

        visited[u][from_]=True #po przetworzeniu wierzcholka u

    return min(distance[w][0], distance[w][2])

from queue import PriorityQueue

def dikstra3(G, s, w):
    n = len(G)
    INF = float('inf')
    distance = [[INF for _ in range(3)] for _ in range(n)]
    visited = [[False for _ in range(3)] for _ in range(n)]
    distance[s][0] = 0

    Q = PriorityQueue()
    Q.put((0, s, 0, None))

    while not Q.empty():
        u_dist, u, from_, last_edge = Q.get()
        if visited[u][from_]:
            continue
        visited[u][from_] = True

        for v, d_v in G[u]:
            if from_ == 0:  # Normal entry, can transition to normal or jump state
                new_dist_normal = u_dist + d_v
                if new_dist_normal < distance[v][0]:
                    distance[v][0] = new_dist_normal
                    Q.put((new_dist_normal, v, 0, None))
                # Begin a jump
                Q.put((u_dist, v, 1, d_v))

            elif from_ == 1:  # Mid-jump, must complete jump
                new_dist_jump = u_dist + max(last_edge, d_v)
                if new_dist_jump < distance[v][2]:
                    distance[v][2] = new_dist_jump
                    Q.put((new_dist_jump, v, 2, None))

            elif from_ == 2:  # Jump completed, can only move to normal
                new_dist_normal = u_dist + d_v
                if new_dist_normal < distance[v][0]:
                    distance[v][0] = new_dist_normal
                    Q.put((new_dist_normal, v, 0, None))

    return min(distance[w][0], distance[w][2]) if distance[w][0] != INF or distance[w][2] != INF else -1

# Sample adjacency list graph
G = [
    [(1, 5), (2, 2)],
    [(2, 1), (3, 2)],
    [(3, 3)],
    []
]
print(dikstra3(G, 0, 3))



def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje
    # print(G)

    # G = rebuild_graph( G ) #na macierzy jeszcze

    G = cretate_adjacency_list( G )

    # G = rebuild_graph( G )

    return dikstra1( G, s, w )

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )

G = [[(1, 1), (2, 200), (3, 200), (4, 200), (5, 200)],
    [(0, 1), (2, 2), (3, 200), (4, 200), (5, 200)],
    [(0, 200), (1, 2), (3, 40), (4, 200), (5, 200)],
    [(0, 200), (1, 200), (2, 40), (4, 40), (5, 200)],
    [(0, 200), (1, 200), (2, 200), (3, 40), (5, 117)],
    [(0, 200), (1, 200), (2, 200), (3, 200), (4, 117)]
    ]

# Use a list comprehension to filter out elements with a second value of 200
# G = [[(v, d) for (v, d) in row if d != 200] for row in G]

print(dikstra3( G, 0, 5 )) # 0 1 2 41 43 159

#mozna ten skok potraktowac jako skok o 3 wierzcholki, 2 szybko i 1 normalnie
# struktura grafu nie naruszona