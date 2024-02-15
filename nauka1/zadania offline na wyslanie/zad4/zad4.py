from zad4testy import runtests

# Bartlomiej Szubiak
# algorytm dziala na zasadzie znalezienia BFS'em najkrotszej sciezki/drogi (BFS_find_path)
# (bfs przeszukuje wierzcholki radialnie wiec jesli dotkniemy wierzcholek t to znalezlismy ta droge)
# droga jest dystkretnie zapisana w tablicy parent wiec uzywam funkcji create path aby wyluskac ta sciezke/droge
# funkcja (BFS_find_path) zwraca ta najkrotsza droge i jej dlugosc
# gdyby okazalo sie ze ten BFS nie dotarl do t oznacza to ze graf na wejsciu jest niespojny wiec koncze program bo zadanie wtedy nie ma sensu
# teraz pokolei usuwam krawedzie z tej najkrotszej sciezki szukajac czy nie istnieje druga najkrotsza tj. o tej samej dlugosci (BFS_distance_exclude_edges)
# gdyby sie okazalo ze takowej nie ma a nie musimy sprawdzac czy graf jest nadal spojny po usunieciu tej krawedzi funkcja BFS_distance_exclude_edges
# konczy dziala zwracajac inf (aby przyspieszyc dzialanie) w naszym domniemaniu inf oznacza tutaj ze moze istniec jakas ale jest ona napewno dluzsza od najkrotszej
# zwracamy ta krawedz pod warunkiem kiedy nowy dystans jest napewno wiekszy od (starego) najmniejszego

# uzywam lekko zmodyfikowanego BFS'a podanego na wykladzie przepisanego z pseudo kodu do python

# zlozonosc O(2V+E+V(V+E))


from collections import deque

def create_path(G,path,s,t,parent):
    # odtwarzaj od t do s i zapisuj
    old = t
    path.append(t)
    while old!=s :
        path.append(parent[old])
        old=parent[old]  
    return path
    

def BFS_find_path(G,s,t): #graf , startowy punkt rozwijania , koniec
    #G=(V,E) , s eV
    q=deque()
    n=len(G) #len(v)
    distance=[-1]*n #distance i-tego wierzchokka od tego s
    visited=[False]*n #czy odwiedzono juz ten, zeby sie nie zapetlac
    parent=[None]*n #kto byl rodzicem i-tego wierzcholka -> jak dotarlismy
    path=[] #sciezka jak dotarlismy z s do t
    
    q.append(s)
    visited[s] = True
    distance[s]=0
    parent[s]=None
    
    while q :
        u=q.popleft()
        for v in G[u] : #sasiedzi u
            if not visited[v]: #not v.visited
                distance[v] = distance[u] + 1
                parent[v] = u
                visited[v] = True
                q.append(v)
                if (v == t): #znaleziono ta najkrotsza sciezke -> dotknieto t
                    return distance[t] , create_path(G,path,s,t,parent)
    return -1 , path 

from math import inf

def BFS_distance_exclude_edges(G,s,t,excluded,min_dist): #graf , startowy punkt rozwijania
    #G=(V,E) , s eV
    q=deque()
    n=len(G) #len(v)
    distance=[-1]*n #distance i-tego wierzchokka od tego s
    visited=[False]*n #czy odwiedzono juz ten, zeby sie nie zapetlac
    
    q.append(s)
    visited[s] = True
    distance[s]=0
    
    while q :
        u=q.popleft()
        for v in G[u] : #sasiedzi u
            #po "sztucznie usuwam ta krawedz z grafu"
            if (u==excluded[0] and v==excluded[1])or(u==excluded[1] and v==excluded[0]): continue
            if not visited[v]: #not v.visited
                distance[v] = distance[u] + 1
                visited[v] = True
                q.append(v)
                
                #przy zalozeniu ze nie trzeba sprawdzac czy sie rozspojnia po usunieciu danej krawedzi
                # i nie znalezlismy innej drogi do t ktora ma ten sam dystans spelnione sa warunki zadania
                if distance[v] > min_dist: 
                    return inf 
                if (v == t): #znaleziono ta najkrotsza sciezke -> dotknieto t
                    return distance[v] 
    return inf 

def longer( G, s, t ):
    shortest_distance , path = BFS_find_path(G,s,t)
    if shortest_distance==-1: return None #graf niespojny nie da sie dojsc wogole z s do t
    for i in range(shortest_distance): 
        excluded_edges = [path[i],path[i+1]] #(10,9)
        new_dist = BFS_distance_exclude_edges(G,s,t,excluded_edges,shortest_distance)
        if new_dist>shortest_distance: return excluded_edges
    return None 
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )