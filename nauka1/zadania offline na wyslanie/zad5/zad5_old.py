from zad5testy import runtests

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
    
    while q :
        u , d = q.pop(0)
        main_dist += d
        q=reduce_d(q,d)
        if (u==t): return main_dist #,parent
    # print(u, end = " ")
        for v in range(n) : #sasiedzi u -> v
            if G[u] [v] == -1 : continue
            if not visited[v]: #not v.visited
                # distance[v] += 1
                # parent[v] = u
                visited[v] = True
                q=insert_sorted(q,[v , G[u] [v] ])
                
    return None


def make_matrix(n,E,S):
    matrix= [ [ -1 for _ in range(n)] for i in range(n) ]
    for (u,v,d) in E:
        matrix[u] [v] = d
        matrix[v] [u] = d
    m = len(S)
    for i in range(m):
        for j in range(i+1,m):
            u=S[i]
            v=S[j]
            matrix[u] [v] = 0
            matrix[v] [u] = 0
    return matrix
            
# TODO przerob zrob dikstre 
def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    if_a = a in S
    if_b = b in S
    if if_a and if_b:
        return 0
    elif if_a:
        a = n
    elif if_b:
        b = n
    # G = zwiaz(E,S,n)
    G = make_matrix(n,E,S)
    return BFS_dikstra(G,a,b,n)
    # return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )

E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
S=[0, 2, 3]
a=1
b=3
n=4
G=[[-1,5,0,0],[5,-1,21,3],[0,21,-1,-1],[0,3,-1,-1]]

# spacetravel(n,E,S,a,b)
# print(BFS_dikstra(G,a,b,n))