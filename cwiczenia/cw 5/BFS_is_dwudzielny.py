"""
jak sprawdzic czy graf jest dwudzielny
BFS macierzowa reprezentacja

graf jest spojny


oprocz wisited wpisywac
do tablicy [1,2,1,1,2,1,2,1,2] - tablica kolorow dla wierzcvholka 0 1 2 3 (idx)
kolor to distance%2

"""
class deque(): #poprostu kolejka
    pass

def BFS_is_dwudzielny(G):
    n=len(G)
    colors=[0]*n
    q=deque()
    q.append(0)
    colors[0]=1
    while (not (q.is_empty())): #cos jest w queue
        w = q.popleft()
        for i in range(n):
            if(G[w][i]==1): #jest ta krawedz miedzy wierzcholkami w , i
                if (colors[i]==0): #nie ma nadanego koloru
                    colors[i]=3-colors[w] #nadaje oposite kolor wzgledem starego(parenta)
                elif(colors[i]==colors[w]):
                    return False
    return True
            
        
