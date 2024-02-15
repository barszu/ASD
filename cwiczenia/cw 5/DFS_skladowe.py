"""
ile skladowych ma graf , graf nie jest spojny ma skladowe nie spojne
uzyj DFS
graf jest jako tablica sasiedztwa

"""

    


def DFS_skladowe(G):
    
    def deep_explore(j):
        nonlocal G, visited
        visited[j]=True
        for v in G[j] : #v - sasiad
            if visited[v]==False :
                deep_explore(v)
        
    
    
    n = len(G)
    visited=[False]*n
    counter=0 #licznik tych skladowych
    for j in range(n):
        if ( not visited[j]):
            
            counter += 1
            
    