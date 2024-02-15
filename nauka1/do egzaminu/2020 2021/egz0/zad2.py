class Node:
    def __init__(self):
        self.left = None # lewe poddrzewo
        self.leftval = 0 # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None # prawe poddrzewo
        self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None # (ch_l,ch_r) #tyle ma na lewo i prawo dzieci
        
    def create_edge(self,left,to,val):
        if left:
            self.left = to
            self.leftval = val
        else:
            self.right = to
            self.rightval = val 

#obserwacja tyle node'ow ma pod soba ile krawedzi
def dfs_find_childs(node:Node,Map):
    Map.append(node)
    ch_l = 1 + dfs_find_childs(node.left,Map) if node.left else -1
    ch_r = 1 + dfs_find_childs(node.right,Map) if node.right else -1
    node.X = (ch_l,ch_r)
    return ch_l+ch_r
    
def valuableTree(root:Node,K):
    Map = [] # 0:a
    dfs_find_childs(root,Map)
    Reversed_Map = {el: i for i,el in enumerate(Map)} #a:0
    
    
    
    INF = float('inf')
    DP = [[None for j in range(K+1)] for i in range(len(Map)) ]
    
    def f(i,k): #max sum o korzeniu i , k krawedziach 
        if DP[i][k]: return DP[i][k]
        v = Map[i]
        
        if k == 0 :
            DP[i][k] = 0
            return 0
        if k > 0 and v.X == (0,0): #jest lisciem i k>0
            DP[i][k] = -INF
            return DP[i][k]
            
        if k == 1 :
            l = v.leftval if v.left else -INF
            r = v.rightval if v.right else -INF
            DP[i][k] = max(l,r)
            return DP[i][k]
        
        take_only_left = v.leftval + f(Reversed_Map[v.left],k-1) if v.left else -INF
        take_only_right = v.rightval  + f(Reversed_Map[v.right], k-1) if v.right else -INF
        take_both = -INF
        if v.left and v.right:
            take_both = v.leftval + v.rightval
            maxy = -INF
            for p in range(0,k-2+1):
                l = f(Reversed_Map[v.left],p)
                r = f(Reversed_Map[v.right],k-2-p)
                if l != -INF and r != -INF: #poprawna sciezka
                    maxy = max(maxy,max(l,r))
                
            take_both += maxy
            
        DP[i][k] = max(take_only_left,take_only_right,take_both)
        return DP[i][k]
    
    res = -INF
    for i in range(len(Map)):
        res = max(res , f(i,K))
    return res

L = True
P = False

a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()

a.create_edge(L,b,1)
a.create_edge(P,c,5)
b.create_edge(L,d,6)
b.create_edge(P,e,2)
e.create_edge(L,f,8)
e.create_edge(P,g,10)

print(valuableTree(a,2))
