from zad6testy import runtests

INF = float("inf")

def bfs(m, M, pairU, distance, pairV):
    queue = []

    for u in range(1, m+1):
        if pairU[u] == 0:
            distance[u] = 0
            queue.append(u)
        else:
            distance[u] = INF
    distance[0] = INF

    while len(queue) != 0:
        u = queue.pop()

        if distance[u] < distance[0]:
            for v in M[u]:
                if distance[pairV[v]] == INF:
                    distance[pairV[v]] = distance[u] + 1
                    queue.append(pairV[v])

    return distance[0] != INF, pairU, pairV, distance

def dfs(u, M, pairU, pairV, distance):
    if u != 0:
        for v in M[u]:
            if distance[pairV[v]] == distance[u] + 1:
                has_path_for_u, pairU, pairV, distance = dfs(pairV[v], M, pairU, pairV, distance)
                if has_path_for_u:
                    pairV[v] = u
                    pairU[u] = v
                    return True, pairU, pairV, distance

        distance[u] = INF
        return False, pairU, pairV, distance
    
    return True, pairU, pairV, distance

def Hopcroft_Karp( M ):
    m, n = len(M), len(M)+1
    M = [[]]+M

    pair_U = [0]*(m+1)
    pair_V = [0]*(n+1)
    distance = [0]*(m+1)

    result = 0

    hasAugmentedPath, pair_U, pair_V, distance = bfs(m, M, pair_U, distance, pair_V)

    while hasAugmentedPath:
        for u in range(1, m+1):
            if pair_U[u] == 0:
                hasPathFor_u, pair_U, pair_V, distance = dfs(u, M, pair_U, pair_V, distance)
                if hasPathFor_u:
                    result += 1

        hasAugmentedPath, pair_U, pair_V, distance = bfs(m, M, pair_U, distance, pair_V)

    return result

def binworker(M):
    return Hopcroft_Karp( M )

runtests( binworker, all_tests = True )