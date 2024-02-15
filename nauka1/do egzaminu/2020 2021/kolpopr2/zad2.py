from zad2testy import runtests

def order(L,K):
    # modulo_map = [[] for i in range(10**K)] # modulo_map[i] idx wystapien el gdzie ich %10^K = i
    division_map = [[] for i in range(10**K)] # division_map[i] idx wystapien el gdzie ich //10^k = i
    min_val = float('inf') 
    min_idx = None
    for i in range(len(L)):
        # modulo_map[L[i]%(10**K)].append(i)
        division_map[L[i]//(10**K)].append(i)
        if L[i] < min_val:
            min_val = L[i]
            min_idx = i
    
    #TOP SORT
    n = len(L)
    visited = [False] * n
    result = [] #topsort

    def dfs(v):
        visited[v] = True
        for neighbor in division_map[L[v]%(10**K)]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(v)

    dfs(min_idx)
    if len(result) != n:
        return None
    return [L[i] for i in reversed(result)]


    
runtests( order )


