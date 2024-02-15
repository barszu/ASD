from zad2testy import runtests

#Bartłomiej Szubiak
# idea algorytmu sortujemy tablice ze sniegiem -> algorytm sortowania to cnt sort
# wybieramy el ktore oplaca sie brac zaczynamy od tych najwiekszych
# zawsze bierzemy ilosc sniegu z pola - tura (snieg topnienie)
# dlaczego to dziala?
# niezaleznie od dnia w ktorym zbieramy snieg ilosc tego co stopnialo jest stala i defakto zalezna od ilosci dni
# przez to oraz przez to ze mozemy zbierac z dwoch stron zawsze mozna wybrac taka trase ze zbierzemy 
# k maksymalnych wartosci bez rozjezdzania innych maksymalnych wartosci
# szacowana zlozonosc O( n+k+n) -> O(3n) -> O(n)

# dzialanie cnt sort: tworzymy tablice licznosci danych el
# i uzywajac jej nadpisujemy oryginalna tablice i tworzmy ja posortowana
# wybralem cnt sort ze wzgledu na liniowa zlozonosc plus ilosc sniegu jest liczba calkowita >0 wiec jest je latwo porownywac

def max_el(T,n):
    najwiekszy=0
    for i in range(n-1):
        if T[i]>najwiekszy : najwiekszy=T[i]
    return najwiekszy
    

def counting_sort(T): #el sa od 0 do +inf
    n=len(T)
    max_val = max_el(T,n)  # znajdujemy maksymalna wartosc w tablicy
    zliczenia = [0] * (max_val + 1)  # tworzymy liste zliczeń
    for num in T:
        zliczenia[num] += 1  # zwiekszamy licznik dla danego elementu
    
    i=0 
    for j in range(max_val): #j to nasz el
        cnt_el=zliczenia[j]
        if cnt_el==0: continue
        T[i:i+cnt_el]=[j]*cnt_el
        i=i+cnt_el
    j=max_val
    cnt_el=zliczenia[-1]
    T[i::]=[j]*cnt_el



def snow( S ):
    # tu prosze wpisac wlasna implementacje
    n=len(S)
    counting_sort(S)
    S=S[::-1]
    zebrany_snieg=0
    for i in range(n): #i oznacza ture (tyle sniegu z kazdego pola stopnialo przez tury)
        snieg=S[i]-i
        if (snieg>0) : #oplaca sie wziac
            zebrany_snieg += snieg
        else:
            break
    return zebrany_snieg


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
