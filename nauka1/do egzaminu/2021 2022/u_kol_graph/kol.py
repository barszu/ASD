from kolutesty import runtests

from queue import PriorityQueue

def build_graph(disk,depends):
    n = len(depends)
    G = [[] for _ in range(n)]

    for i in range(n): 
        for j in range(len(depends[i])): 
            if disk[i] != disk[depends[i][j]]: 
                G[depends[i][j]].append((2, i))
            else: 
                G[depends[i][j]].append((1,i))
    return G


def swaps( disk, depends ):
    n = len(disk)
    G = depends
    visited = [False for i in range(n)]
    swaps_cnt = 0

    def dfs(u):
        nonlocal swaps_cnt
        if visited[u]: return False #loop detected

        visited[u] = True
        
        for v in G[u]: #firstly go to node's with same color
            if disk[v] != disk[u]: continue
            if not visited[v]:
                dfs(v)
                # swaps_cnt += 1
        
        for v in G[u]: #firstly go to node's with same color
            if disk[v] == disk[u]: continue
            if not visited[v]:
                dfs(v)
                swaps_cnt += 1

        visited[u] = False #end of visiting 
        G[u] = [] #no prerequirmets -> can be done 

        return True
        
    for i in range(n):
        if not visited[i]: dfs(i)
    
    return swaps_cnt
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = False )
