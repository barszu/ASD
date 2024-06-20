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

def rebuild_graph( G ): # G- macierz sasiedztwa
    # prubuje dodawac mergowane krawedzie
    n = len( G )
    is_edge_modified = [[False for _ in range(n)] for _ in range(n)] 
    contains_merged_edge = [[None for _ in range(n)] for _ in range(n)]
    #nie mozna dodac krawedzi mergowanej wczesniej do mergowania
    for u in range( n ): #prubuj mergowac
        for v in range( n ):
            if G[ u ][ v ] == 0 or is_edge_modified[ u ][ v ]: continue
            for b in range( n ):
                if G[ v ][ b ] == 0 or is_edge_modified[ v ][ b ] or b in [u,v]: continue
                for c in range( n ):
                    if G[ b ][ c ] == 0 or is_edge_modified[ b ][ c ] or c in [u,v,b]: continue
                    first_edge = G[ u ][ v ]
                    second_edge = G[ v ][ b ]
                    third_edge = G[ b ][ c ]

                    old_edge = G[ u ][ c ]
                    new_edge = max( first_edge, second_edge ) + third_edge
                    # nie bylo wczesniej tej krawedzi | jest lepsza niz poprzednia
                    if old_edge == 0 or new_edge < old_edge:
                        G[ u ][ c ] = new_edge
                        is_edge_modified[ u ][ c ] = True
                        contains_merged_edge[ u ][ c ] = (u,v,b,c)
    return G, is_edge_modified, contains_merged_edge


from queue import PriorityQueue

def dikstra(G_adj, a, b, G_matrix, is_edge_modified, contains_merged_edge):
    result = []
    inf = float('inf')
    n = len(G_adj)
    dist = [inf]*n
    visited= [False]*n
    q = PriorityQueue()
    
    dist[a] = 0
    q.put((0, a)) #(d,u)

    while not q.empty():
        d_u, u = q.get()  # dla u szukamy v
        if visited[u]: continue
        
        for v, d_v in G_adj[u]:
            # relax
            temp_dist = d_u + d_v #przez u->v mozna szybciej niz jakos ()->v
            if temp_dist < dist[v]:
                dist[v] = temp_dist
                q.put((temp_dist, v)) #dodaje do przetwarzania kiedy warunek drogi jest speniony

            #dodatkowe sprawdzenie czy to krawedz mergowana, i czy w srodku jej nie jest ukryty docelowy wierzcholek
            if is_edge_modified[u][v]:
                _u,_v,_b,_c = contains_merged_edge[u][v]
                if _b == b:
                    first_edge = G_matrix[_u][_v]
                    second_edge = G_matrix[_v][_b]
                    result.append( max(first_edge, second_edge) )

        
        visited[u]=True #po przetworzeniu wierzcholka u
        if u == b and dist[b] != inf: 
            result.append(dist[b])
            return min(result)
    return None


def jumper( G, s, w ): #dalej to samo lol 160 nie 159
    G_matrix, is_edge_modified, contains_merged_edge = rebuild_graph( G ) #na macierzy jeszcze
    G_adj = cretate_adjacency_list( G )

    res = dikstra( G_adj, s, w, G_matrix, is_edge_modified, contains_merged_edge )

    return res

# runtests( jumper, all_tests = True )

#trzeba w tym rozwiazaniu sztuczny wierzcholek dodac zeby wszystkie krawedzie byly te dlugie -> debilizm?


def transform_and_find_shortest_path(matrix, source, target):
    V = len(matrix)  # Number of vertices in the graph
    inf = float('inf')
    
    # Initialize distances
    distances = [inf] * (2 * V)
    distances[source * 2] = 0  # Start from source in normal mode

    # Construct the extended graph edges list
    extended_graph = []
    for u in range(V):
        for v in range(V):
            if matrix[u][v] != 0:  # There is a direct edge
                weight = matrix[u][v]
                # Normal move u -> v
                extended_graph.append((u * 2, v * 2, weight))
                # Jump move u -> v (second part)
                extended_graph.append((u * 2 + 1, v * 2, weight))
                # Add double jumps
                for x in range(V):
                    if matrix[v][x] != 0:
                        weight2 = matrix[v][x]
                        extended_graph.append((u * 2 + 1, x * 2 + 1, max(weight, weight2)))

    # Bellman-Ford algorithm
    for _ in range(2 * V - 1):
        any_update = False
        for u, v, weight in extended_graph:
            if distances[u] != inf and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                any_update = True
        if not any_update:
            break  # No update in this iteration, so exit

    # Get the minimum distance to the target
    return min(distances[target * 2], distances[target * 2 + 1])


runtests( transform_and_find_shortest_path, all_tests = True )