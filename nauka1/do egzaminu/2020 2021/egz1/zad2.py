from zad2testy import runtests

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

SLOW = 0 #60s
NORMAL = 1 #40s
FAST = 2 #30s

VELOCITY_COST = [60,40,30]

TURN = 45

def robot( L, A, B ): #rozmnozenie wierzcholkow
    from queue import PriorityQueue
    q = PriorityQueue()
    INF = float('inf')
    ROWS = len(L) 
    COLS = len(L[0])
    # (wiersz,kolumna)
    A = tuple(reversed(A))
    B = tuple(reversed(B))

    # visited = [[False for j in range(COLS)] for i in range(ROWS)]
    DP = [[[[INF] * 3 for _ in range(4)] for j in range(COLS)] for i in range(ROWS)]
    #pseudo dp -> min dystnas przy zalozeniach
    # dist[x][y][direction][speed]
    
    def in_bound(x,y): return 0<=x<ROWS and 0<=y<COLS
    
    q.put((0,A,RIGHT,SLOW)) # (dist,(i,j),direction,run_status)
    # run_status - ile bedzie mnie kosztowac ruch do przodu (60/40/30)
    # direction - facing direction at arrival
    
    while not q.empty():
        u_time , (x,y) , u_direc , u_run = q.get() # w - dystans od zrodla 
        if DP[x][y][u_direc][u_run] != INF: #marked as visited
            continue
        
        #update time
        DP[x][y][u_direc][u_run] = u_time #not min because it's first and only meet
        
        #idz wzdluz u_direc
        dx , dy = DIRECTIONS[u_direc]
        if in_bound(x+dx,y+dy) and L[x+dx][y+dy] != 'X':
            new_run = u_run + 1 if u_run + 1 <= FAST else FAST
            q.put((u_time+VELOCITY_COST[u_run] , (x+dx,y+dy) , u_direc , new_run))
        
        #tylko obroc sie raz (zgodnie ze wskazowkami zegara)
        new_direction = (u_direc + 1)%4 
        q.put((u_time+TURN , (x,y) , new_direction , SLOW))
        
        #tylko obroc sie 1 raz PRZECIWNIE do wskazuwek zegara
        new_direction = (u_direc - 1)%4 
        q.put((u_time+TURN , (x,y) , new_direction , SLOW))
    
    dist = [[None for j in range(len(L[0]))] for i in range(len(L))]
    for i in range(len(L)):
        for j in range(len(L[0])):
            maxy = float('inf')
            for d in range(4):
                for m in range(3):
                    maxy = min(DP[i][j][d][m] , maxy)
            dist[i][j] = maxy
    res = dist[B[0]][B[1]]
    return res if res != INF else None


runtests( robot )
# data = ["XXXXXXXXXX",
#         "X        X",
#         "X  XXXXXXX",
#         "X        X",
#         "X XXXXXX X",
#         "X        X",
#         "XXXXXXXXXX"]

# print(robot2(data,(1,1),(8,4))) #545

def robot_aproxi_not_working( L, A, B ): #nierozmnaza prawidlowo wierzcholkow dziala aproxymacyjnie
    from queue import PriorityQueue
    q = PriorityQueue()
    ROWS = len(L) 
    COLS = len(L[0])
    # (wiersz,kolumna)
    A = tuple(reversed(A))
    B = tuple(reversed(B))

    visited = [[False for j in range(COLS)] for i in range(ROWS)]
    dist = [[float('inf') for j in range(COLS)] for i in range(ROWS)]
    
    def in_bound(x,y): return 0<=x<ROWS and 0<=y<COLS
    
    q.put((0,A,RIGHT,SLOW)) # (dist,(i,j),direction,run_status)
    # run_status - ile bedzie mnie kosztowac ruch do przodu (60/40/30)
    # direction - facing direction at arrival
    
    while not q.empty():
        u_time , (x,y) , u_direc , u_run = q.get() # w - dystans od zrodla 
        if u_time < dist[x][y]: dist[x][y] = u_time
        if visited[x][y]: continue

        visited[x][y] = True
        #idz wzdluz u_direc
        dx , dy = DIRECTIONS[u_direc]
        if in_bound(x+dx,y+dy) and L[x+dx][y+dy] != 'X':
            new_run = u_run + 1 if u_run + 1 <= FAST else FAST
            q.put((u_time+VELOCITY_COST[u_run] , (x+dx,y+dy) , u_direc , new_run))
        
        new_run = SLOW
        
        #obroc sie raz (zgodnie ze wskazowkami zegara)
        new_direction = (u_direc + 1)%4 
        dx , dy = DIRECTIONS[new_direction]
        if in_bound(x+dx,y+dy) and L[x+dx][y+dy] != 'X':
            q.put((u_time+TURN+VELOCITY_COST[SLOW] , (x+dx,y+dy) , new_direction , NORMAL))
        
        #obroc sie 2 razy (zgodnie ze wskazowkami zegara)
        new_direction = (u_direc + 2)%4 
        dx , dy = DIRECTIONS[new_direction]
        if in_bound(x+dx,y+dy) and L[x+dx][y+dy] != 'X':
            q.put((u_time+(2*TURN)+VELOCITY_COST[SLOW] , (x+dx,y+dy) , new_direction , NORMAL))
        
        # obroc sie 1 raz PRZECIWNIE do wskazuwek zegara
        new_direction = (u_direc + 3)%4 
        dx , dy = DIRECTIONS[new_direction]
        if in_bound(x+dx,y+dy) and L[x+dx][y+dy] != 'X':
            q.put((u_time+TURN+VELOCITY_COST[SLOW] , (x+dx,y+dy) , new_direction , NORMAL))
    
    p,q = B
    return dist[p][q] if dist[p][q] != float('inf') else None