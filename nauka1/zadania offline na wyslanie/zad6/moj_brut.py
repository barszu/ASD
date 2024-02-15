from zad6testy import runtests

def find_machines_no(M):
    global_max=0
    for taby in M:
        if (taby==[]): continue
        curr_max = max(taby)
        if curr_max>global_max : global_max = curr_max
    return global_max+1
 
def make_graph(M,m,k,G): 
    #oznaczenia: [0,m-1] - ludzie , [m,m+k-1] - maszyny
    for i in range(m):
        machines_list = M[i]
        for p in machines_list:
            no = p+m
            (G[i]).append(no)
            (G[no]).append(i)
            
    return

def create_colors(G,m,k,colors_tab):
    n = m+k
    for i in range(n):
        taby = G[i]
        for j in taby:
            colors_tab[j] [i] = 1
            colors_tab[i] [j] = 1
    return

def DFS_color(G,colors_tab,s,t,m):
    # G=(V,E)
    n=len(G)
    visited=[False]*n
    parent=[None]*n #drzewo przegladania wierzcholkow
    is_path_found = False
    # new_colors_tab = colors_tab.copy()
    new_colors_tab = [row.copy() for row in colors_tab]
    
    def DFS_visit(G,u,colors_tab,t,last_color): #odwiedznie danego wierzcholka
        nonlocal visited , parent , is_path_found
        visited[u]=True
        for v in G[u]: #v sasiad u
            if visited[v] : continue 
                     
            curr_color = colors_tab[u][v]
            if last_color!=2137: #kolor poczatkowy
                if last_color*curr_color != -1: #nie sa roznych kolorow
                    return # koncze sciezke
            
            parent[v]=u
            #zmien curr_kolor
            colors_tab[v] [u] *= -1
            colors_tab[u] [v] *= -1
            if v==t : #doszlem
                is_path_found = True
                return # koncze sciezke
            
            DFS_visit(G,v,colors_tab,t, curr_color )

    DFS_visit(G,s,new_colors_tab,t,2137) #rekurencyja sciezka w dol
    if is_path_found: #wpisz naprzemiennie wartosci z tej sciezki
        a = t
        while a != None:
            prev = parent[a]
            if prev == None : break
            if prev < m : #ma byc czlowiekiem, skojarzenia wychodza od ludzi
                colors_tab[prev] [a] *= -1
                colors_tab[a] [prev] *= -1
            a = prev
            
        
    
    return parent , is_path_found

def bruty_brut(G,m,k):
    n = m+k
    # 0 - brak krawedzi , 1- jest krawedz , -1 - krawedz zabrana (w skojarzeniu)
    colors_tab = [[ 0 for i in range(n)] for j in range(n)]
    create_colors(G,m,k,colors_tab)
    
    p_CZ_komp_tab = [None]*m #i-ty czlowiek do tab[i] kompa
    p_KOMP_czl_tab = [None]*n #i-ty komp do tab[i] czlowieka
    
    for human in range(m):
        for machine in G[human]:
            if p_KOMP_czl_tab[machine] != None : #komputer jest zajety
                continue
            #szukamy sciezki z human do machine
            parent_dfs , is_path_found = DFS_color(G,colors_tab,human,machine,m)
            if is_path_found: 
                old_master = p_KOMP_czl_tab[machine]
                if old_master==None: #nie ma go
                    p_CZ_komp_tab[human] = machine
                    p_KOMP_czl_tab[machine] = human
                    break
                else:
                    temp_machine = machine
                    p_CZ_komp_tab[old_master]=None
                    p_CZ_komp_tab[human] = temp_machine
                    p_KOMP_czl_tab[temp_machine] = human
                    break #czlowiek zaspokojony
    return p_CZ_komp_tab

def binworker(M):
    m = len(M)
    k = find_machines_no(M)
    G = [[] for i in range(m+k)]
    make_graph(M,m,k,G)
    h_tab = bruty_brut(G,m,k)
    cnt = 0
    for i in h_tab:
        if i != None : cnt += 1
    return cnt
    
                


# def dfs_brute(u, M, pair_V, pair_U, visited):
#     visited[u] = True

#     for v in M[u]: 
# #nie przypisano czlowiekowi v maszyny, komputer v jest zajety i czlowiek do ktorego on nalezy nie zostal przez nas odwiedzony 
#         if pair_V[v] is None or (not visited[pair_V[v]] and dfs_brute(pair_V[v], M, pair_V, pair_U, visited)):
#             pair_V[v] = u
#             pair_U[u] = v
#             return True

#     return False


# def binworker(M):
#     # M.sort(key=len)

#     result = 0

#     n = len(M)
#     pair_U = [None] * n
#     pair_V = [None] * (n + 1)

#     for u in range(n):
#         if pair_U[u] is None: #nie przypisano komputera
#             visited = [False] * n
#             if dfs_brute(u, M, pair_V, pair_U, visited):
#                 result += 1

#     return result

runtests( binworker, all_tests = True )
# M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
# a = binworker(M)
# print(a)