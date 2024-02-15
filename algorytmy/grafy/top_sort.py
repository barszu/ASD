"""
musi byc dag - directed Acyclic graph (skierowany graf Acykliczny)
top_sort - ulozenie wierzcholkow w takiej kolejnosci ze krawedzie
           wskazuja wylacznie z lewej do prawej

--------->
1 -> 3 -> 7 -> 8
      -------->
-------------->

zastosowanie: wyznaczenie kolejnosci realizacji zadan 
ktore musza byc wykonane przed innymi

Algo:
-uruchom DFS na losowym wierzcholku
-po przetworzeniu wierzcholka dopisz go na poczatek listy
 (albo na koniec i obroc liste)(zrob dla kazdego wierzcholka tak)

"""

def DFS_tp_ls(G, s_array):
    n = len(G)
    visited = [False] * n
    parent = [None] * n #drzewo przegladania wierzcholkow
    idx = 0

    def DFS_visit(u): #odwiedznie danego wierzcholka
        nonlocal visited, parent, s_array, idx
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(v) #rekurencyja sciezka w dol
        s_array[idx] = u
        idx += 1

    for u in range(n):
        if not visited[u]:
            DFS_visit(u)

    return parent

def top_sort(G):
    n = len(G)
    strt = [None] * n
    parent = DFS_tp_ls(G, strt)
    return strt[::-1]

def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    result = []

    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(v)

    for vertex in range(n):
        if not visited[vertex]:
            dfs(vertex)

    result.reverse()
    return result
  
# g = [[1, 2], [3], [4], [2, 4], []]
# g = [[1,2], [3,4], [5,6], [7,10], [8,9], [11,12], [14,13],[],[],[],[],[],[],[],[]]
# g = [[],[2], [3], [4], [5],[]]
g = [[],[2,3,4],[5],[5],[5],[]]
print(top_sort(g))
print(topological_sort(g))