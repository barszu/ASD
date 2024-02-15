from zad7testy import runtests

def table_filling(L):
    n = len(L)
    # distances from (x, y) to (n-1, n-1) by only going to the right and upwards (count_upwards) or downwards (count_downwards)
    count_upwards = [[-1 for _ in range(n)] for _ in range(n)]
    count_downwards = [[-1 for _ in range(n)] for _ in range(n)]

    max_count = [[-1 for _ in range(n)] for _ in range(n)]

    count_upwards[0][0] = 0
    count_downwards[0][0] = 0
    max_count[0][0] = 0

    for y in range(n):
        # update moves downward
        for x in range(1, n):
            if L[x][y] != '#' and L[x-1][y] != '#' and count_downwards[x-1][y] != -1:
                count_downwards[x][y] = max(count_downwards[x-1][y] + 1, count_downwards[x][y])
        # update moves upward
        for x in range(n-2, -1, -1):
            if L[x][y] != '#' and L[x+1][y] != '#' and count_upwards[x+1][y] != -1:
                count_upwards[x][y] = max(count_upwards[x+1][y] + 1, count_upwards[x][y])
        
        # update main moves
        for x in range(n): max_count[x][y] = max(count_downwards[x][y], count_upwards[x][y])
        # make move to the right
        if y+1 < n:
            for x in range(n):
                if L[x][y+1] != '#' and max_count[x][y] != -1:
                    curr_move = max_count[x][y] + 1
                    max_count[x][y+1] = curr_move
                    count_upwards[x][y+1] = curr_move
                    count_downwards[x][y+1] = curr_move

    return max_count[n-1][n-1]

runtests( table_filling, all_tests = True )

def mallock_2d_tab(val,n):
    return [[val for _ in range(n)] for _ in range(n)]

def is_komnata(val): #poprostu aby traktowac '.' jako true
    return val == '.'

# DZIALAJACA Z TABLICA 2D
def maze_dzial(L):
    n = len(L)
    # distances from (x, y) to (n-1, n-1) by only going to the right and upwards (count_upwards) or downwards (count_downwards)
    count_upwards = mallock_2d_tab(-1,n) #tablica do chodzenia w GORE i w prawo
    count_downwards = mallock_2d_tab(-1,n) # do chodzenia w DOL i w prawo
    max_count = mallock_2d_tab(-1,n) #zbiorcza tablica z tych dwoch


    count_upwards[0] [0] = 0
    count_downwards[0] [0] = 0
    max_count[0] [0] = 0

    for x in range(n): #szerokosc
        # update moves downward
        for y in range(1, n): #wysokosc
            if not (is_komnata(L[y] [x]) and is_komnata(L[y-1] [x])) : continue #nie jest komnata wogole albo nie da sie pojsc w dol (uzyty de'Morgan)
            if count_downwards[y-1] [x] == -1: continue 
            #bylismy w tym na dole -> update bierzacego
            curr_move = count_downwards[y-1] [x] + 1 #calkowity koszt do tego pola +1 na przejscie
            if curr_move > count_downwards[y] [x]:
                count_downwards[y] [x] = curr_move

        # update moves upward
        # for y in reversed(range(0,n-1)): #-> [n-2,0]
        for y in range(n-2,-1,-1):
            if not (is_komnata(L[y] [x]) and is_komnata(L[y+1] [x])) : continue
            if count_upwards[y+1] [x] == -1: continue
            # #bylismy w tym na gorze -> update bierzacego
            curr_move = count_upwards[y+1] [x] + 1
            if curr_move > count_upwards[y] [x]:
                count_upwards[y] [x] = curr_move
        
        # update main moves
        for y in range(n): 
            max_count[y] [x] = max(count_downwards[y] [x], count_upwards[y] [x])
        # make move to the right
        if x+1 < n: # da sie jeszce w prawo
            for y in range(0,n):
                if not is_komnata(L[y] [x+1]): continue #ten po prawej nie komnata
                if not max_count[y] [x] == -1: #bylismy juz tu
                    curr_move = max_count[y] [x] + 1
                    max_count[y] [x+1] = curr_move
                    count_upwards[y] [x+1] = curr_move
                    count_downwards[y] [x+1] = curr_move

    return max_count[n-1] [n-1]