NORMAL = 0 #podwojne jak i pojedyncze
BAN = 1 #tylko pojedyncze

def jumper(G,s,t):
    from queue import PriorityQueue
    q = PriorityQueue()
    INF = float('inf')
    n = len(G)
    # (wiersz,kolumna)
    # G[u][v] => w(u,v) if != 0

    DP = [[INF,INF] for i in range(n)]
    #pseudo dp -> min dystnas przy zalozeniach
    # dist[u][state]
    
    q.put((0,s,NORMAL)) # (dist,u,state)
    
    while not q.empty():
        u_time , u , u_state = q.get() # w - dystans od zrodla 
        if DP[u][u_state] != INF: #marked as visited -> val changed
            continue
        
        #update time
        DP[u][u_state] = u_time #not min because it's first and only meet
        
        if u_state == BAN:
            for v in range(n):
                if G[u][v] == 0: continue #ta krawedz (u->v) NIE istnieje
                q.put((u_time+G[u][v] , v , NORMAL)) #idz pojedynczo 
                
        #u->v->w
        if u_state == NORMAL:
            for v in range(n):
                if G[u][v] == 0: continue #ta krawedz (u->v) NIE istnieje
                q.put((u_time+G[u][v] , v , NORMAL)) #idz pojedynczo 
                for w in range(n):
                    if G[v][w] == 0: continue #ta krawedz (v->w) NIE istnieje
                    q.put((u_time+max(G[u][v] , G[v][w]) , w , BAN)) #idz podwojnie
    
    return min(DP[t])

G = [[0,1,0,0,0],
     [1,0,1,0,0],
     [0,1,0,7,0],
     [0,0,7,0,8],
     [0,0,0,8,0],]

print(jumper(G,0,4))