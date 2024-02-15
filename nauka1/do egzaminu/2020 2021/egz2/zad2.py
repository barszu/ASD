from zad2testy import runtests

# class Node:
#     def __init__(self) -> None:
#         self.edges = []
#         self.weights = []
#         self.ids = []
    
#     def addEdge(self,x,w,ids):
#         self.edges.append(x)
#         self.weight.append(w)
#         self.ids.append(ids)

def balance( root ):
    INF = float('inf')
    Edges = [] #(u:Node,v:Node,ids)
    Sumy = {} #Node:int #sumy w dol drzewa razem z tym nodem
    
    def dfs(u):
        #wpisz sumy pod u , i edges
        Sumy[u] = 0
        for i in range(len(u.edges)):
            Edges.append((u,u.edges[i],u.ids[i]))
            Sumy[u] += u.weights[i] + dfs(u.edges[i])
        return Sumy[u]
    
    dfs(root)
    min_diff = float('inf')
    best_ids = None
    for u,v,ids in Edges:
        divorced = Sumy[v] #suma odzielonego drzewa
        rest = Sumy[root] - divorced
        diff = abs(rest-divorced)
        if diff < min_diff:
            min_diff = diff
            best_ids = ids
    
    return best_ids

#test 1 nie dziala
# [[0,0,[]],[1,1,[]],[2,2,[]],[3,3,[]],[4,4,[]],[5,5,[]],[6,6,[]],[7,7,[]],[8,8,[]],[9,9,[]],]
runtests( balance )


