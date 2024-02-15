rank = [0 for i in range(n)]
parr = [i for i in range(n)]

def find_set(x):
    nonlocal parr
    if parr[x] != x:
        parr[x]=find_set(parr[x])

def find_union(x,y):
    repr_x = find_set(x)
    repr_y = find_set(y)
    if x != y:
        if rank[x] > rank [y]:
            parr[y]=x
        else:
            parr[x]=y
        if rank[x]==rank[y]:
            
        