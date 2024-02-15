from zad7testy import runtests
# Bartlomiej Szubiak
# Dzialanie algorytmu: (koszt przejscia - dlugosc drogi)
#  - uzywam tablice zawierajace informacje o najwiekszych kosztach przejscia przy ruchu w gore i w dol
#  ---> wartosc -1 oznacza ze nie bylismy na tym polu tz nie da sie tam wogole dostac ( np na chwile obecna) - nie znamy trasy do tego pola
#  - dodatkowo uzywam tablicy max-imow z tych 2 tablic bo iteresuja nas najwieksze koszty przejscia (0 wartosci dla pola startowego)
#  - przez to ze w szerokosci mozemy poruszac sie tylko w prawo nie potrzebuje tablicy 2D a tablice 
#   zawierajaca jedynie kolumne z tej tablicy 2D (jezeli przejde w prawo to juz poprzednich danych nie uzywam)
#  - iteruje od tylu wzgledem kierunku przejscia w pionie (tz np iteruje od rosnacych idx dla skoku w gore)
#  --> robie tak bo: wtedy dobrze dane sa wpisywane tz aby wygenerowac wartosc dla rodzica musze znac ja dla dziecka (krok: rodzic->dziecko)
#  - jesli bylem juz w tym polu wczesniej (dalo sie jakos do niego dostac z kosztem k) i nowy koszt k_new > k
#   to aktualizuje wartosc tego pola (traktuje ze mozna sie na nie dostac ta druga(obecna) trasa o koszcie k_new)
#  - scalam teraz wartosci na tych polach (biore najwieksze) dlatego ze ^
#  - teraz idac w prawo czyli do kolejnej kolumny przepisuje wartosci maksymalne "tworzac" nowe kolumny

# zlonosc: O(n^2) gdzie n to rozmiar tablicy - planszy

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
