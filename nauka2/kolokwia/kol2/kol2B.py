from kol2testy import runtests
def nodify(E):
    n = max(max(u, v) for u, v, _ in E) + 1
    nodes = [[] for _ in range(n)]
    for edge in E:
        nodes[edge[0]].append((edge[1], edge[2]))
        nodes[edge[1]].append((edge[0], edge[2]))
    return nodes

from queue import PriorityQueue
inf = float('inf')

def Dijkstra(N, s, t):
    n = len(N)
    visited = [[inf] * 17 for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, 16))  # (current time, node, remaining travel time without rest)
    
    while not pq.empty():
        current_time, node, time_left = pq.get()
        
        if visited[node][time_left] <= current_time:
            continue
        
        visited[node][time_left] = current_time
        
        if node == t:
            return current_time
        
        for neighbor, weight in N[node]:
            if weight <= time_left:
                new_time = current_time + weight
                new_time_left = time_left - weight
                if visited[neighbor][new_time_left] > new_time:
                    pq.put((new_time, neighbor, new_time_left))
            else:
                new_time = current_time + weight + 8  # 8 hours rest before traveling
                new_time_left = 16 - weight
                if visited[neighbor][new_time_left] > new_time:
                    pq.put((new_time, neighbor, new_time_left))
    
    return -1  # If there's no path

def warrior(G, s, t):
    graph = nodify(G)
    return Dijkstra(graph, s, t)
runtests( warrior, all_tests = True )
