from kolutesty import runtests

def build_graph(disk,depends):
    n = len(depends)
    G = [[] for _ in range(n)]

    for i in range(n): 
        for j in range(len(depends[i])): 
            if disk[i] != disk[depends[i][j]]: 
                G[depends[i][j]].append((i, 1))
            else: 
                G[depends[i][j]].append((i, 0))
    return G

def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    result = []

    def dfs(v):
        visited[v] = True
        for neighbor , d in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(v)

    for vertex in range(n):
        if not visited[vertex]:
            dfs(vertex)

    result.reverse()
    return result
        

def swaps( disk, depends ):
    # tu prosze wpisac wlasna implementacje
    INF = float('inf')
    n = len(depends) #ilosc node'ow
    cache = [[None for j in range(n)] for i in range(n)]
    G = build_graph(disk,depends) #(node,waga)
    print("top sort ->" + str(topological_sort(G)))
    
    def dfs(u,sustained):
        if sustained == n: 
            return 0
        if cache[u][sustained]: return cache[u][sustained]
        
        d = INF
        for v , dist in G[u]:
            d = min(d , dist + dfs(v,sustained+1))
        cache[u][sustained] = d
        return d
    
    min_to_get = INF
    for i in range(n):
        if len(depends[i]) == 0:
            min_to_get = min( min_to_get , dfs(i,1))
    
    
    return min_to_get

def swaps2( disk, depends ):
    # sorted_order = topological_sort(build_graph(disk,depends))
    swaps_cnt = 0
    for u in range(0,len(disk)): #(v->u)
        if len(depends[u])==0: continue
        
        for v in depends[u]:
            if disk[u] == disk[v]:
                min_cost = 0
                break
            else:
                min_cost = 1
        swaps_cnt += min_cost
    return swaps_cnt

def swaps_dfs(color,depends):
    n = len(color)
    cache = [None for i in range(n)]
    
    def dfs(u): #-> ile swapow aby to zainsatlowac
        if cache[u]: return cache[u]
        
        rek_path = 0 #ile trzeba swapow aby zainstalowac programy 
        # ktore musza byc juz zainsatlowane przed tym
        for v in depends[u]:
            if color[u] == color[v]:
                rek_path = max( rek_path , dfs(v) ) #nie zmieniam plyty
            else:
                rek_path = max( rek_path , 1 + dfs(v) ) #zmieniam plyte aby zainstalowac potrzebny
        
        cache[u] = rek_path
        return rek_path
    
    for i in range(n): #uzupelnij cache
        if not cache[i]:
            dfs(i) 
    
    return max(cache)
        
        

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps_dfs , all_tests = True )
color = ['A','B','A','A','B','A','B']
depends = [
    [],
    [0,4],
    [1,4],
    [],
    [3],
    [4],
    [2,5,4],
]
# print(swaps_dfs(color,depends))

