# from collections import deque

def insert_sorted(lst, item):
    i = 0
    while i < len(lst) and lst[i] [1] < item[1]:
        i += 1
    lst.insert(i, item)
    return lst

def reduce_d(queue,d):
    for i in range(len(queue)):
        queue[i][1] -= d
    return queue
        

def BFS_dikstra(G,s,t,n): #graf , startowy punkt rozwijania
    #G=(V,E) , s eV
    q=[]
    # n=len(G) #len(v)
    # distance=[-1]*n #distance i-tego wierzchokka od tego s
    visited=[False]*n #czy odwiedzono juz ten, zeby sie nie zapetlac
    # parent=[None]*n #kto byl rodzicem i-tego wierzcholka -> jak dotarlismy
    main_dist=0
    
    #przediteracja
    # q.add(s)
    q=insert_sorted(q,[s,0])
    visited[s] = True
    # distance[s]=0
    # parent[s]=None
    
    while not q.is_empty() :
        u , d = q.pop(0)
        main_dist += d
        q=reduce_d(q,d)
        
    # print(u, end = " ")
        for v in range(n) : #sasiedzi u -> v
            if G[u] [v] == -1 : continue
            if not visited[v]: #not v.visited
                # distance[v] += 1
                # parent[v] = u
                visited[v] = True
                q=insert_sorted(q,[v , G[u] [v] ])
    return main_dist 