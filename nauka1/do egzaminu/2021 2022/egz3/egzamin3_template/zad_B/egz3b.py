from egz3btesty import runtests

"""
Solution rozmnozyc wierzcholki grafu na kierunki przyjscia - uruchomic dfs
dla kazedej kolumny j
scalic DP[x][j][direction] w DP[x][j] biorac max na kazdym polu, i dopiero wtedy pojsc w prawo
"""

def is_room(val): #poprostu aby traktowac '.' jako true
    return val == '.'

def maze(L):
    n = len(L)
    # JAKO KOLUMNY
    col_UP_move = [-1 for i in range(n)] #tablica do chodzenia w GORE i w prawo
    col_DOWN_move = [-1 for i in range(n)] # do chodzenia w DOL i w prawo
    MAX_col = [-1 for i in range(n)] # zbiorcza tablica najdluszych przejsc

    # do pola startowego mozna sie dostac z kosztem 0
    col_UP_move[0] = 0
    col_DOWN_move[0] = 0
    MAX_col[0] = 0

    for x in range(n): #szerokosc 
        # y - wysokosc
        # aktualizowanie w gore (skoku w DOL)
        for y in reversed(range(0,n-2+1)):#-> r[0,n-2] = [n-2,0] 
            # nie jest komnata wogole albo nie da sie pojsc (w dol) 
            if not (is_room(L[y] [x]) and is_room(L[y+1] [x])) : continue #(uzyty de'Morgan)
            if col_DOWN_move[y+1] == -1: continue 
            
            # #bylismy w tym na dole (dziecku) -> update bierzacego (rodzica):
            curr_move = col_DOWN_move[y+1] + 1 #calkowity koszt do tego pola +1 na przejscie
            if curr_move > col_DOWN_move[y]:
                col_DOWN_move[y] = curr_move                   
            
        # aktualizowanie w dol (skoku w GORE)
        for y in range(1, n): 
            if not (is_room(L[y] [x]) and is_room(L[y-1] [x])) : continue
            if col_UP_move[y-1] == -1: continue
            
            # bylismy w tym na gorze (dziecku) -> update bierzacego (rodzica):
            curr_move = col_UP_move[y-1] + 1 
            if curr_move > col_UP_move[y]:
                col_UP_move[y] = curr_move
        
        # branie max (scalanie)
        for y in range(n): 
            MAX_col[y] = max(col_DOWN_move[y], col_UP_move[y])
        # przejscie w prawo
        if x > n-2: #nie da sie juz w prawo
            break
        for y in range(0,n):
            if not is_room(L[y] [x+1]) or MAX_col[y] == -1 :  #ten po prawej nie komnata lub nie bylismy
                # formatowanie (w 2D tab bylo by tu -1)
                MAX_col[y] = -1
                col_UP_move[y] = -1
                col_DOWN_move[y] = -1
            else:
                curr_move = MAX_col[y] + 1
                MAX_col[y] = curr_move
                col_UP_move[y] = curr_move
                col_DOWN_move[y] = curr_move
    return MAX_col[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
