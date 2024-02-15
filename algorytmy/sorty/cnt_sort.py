# dziala tylko dla liczb >= 0 bo tak wiaderka zliczen sa ustalone
def cnt_sort(A,k): #array , k=max_el+1 (ilosc zliczen liczb)
    n = len(A)
    C=[0]*k #tablica zliczen id=0 -> C[id=0] ile jest el "0" 
    B=[0]*n #tablica wynikowa
    for i in range(n):
        C[ A[i] ] += 1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
        #nadpisujemy tablice interpretacja:
        #T[id] ile jest el <= od id
        #-> na ktorym indeksie pojawia sie nowa liczba
    
    for i in range(n-1,-1,-1): #od tylu zeby zachowac stabilnosc sortowania
        B[ C[ A[i] ]-1 ] = A[i]
        # -> wez el -> zobacz ilosc el <= od niego ->
        # -> -1 od tej pozycji to jest ostatnia pozycja gdzie powininny sie znajdowac te el
        # -> wpisz na nowa pozycje ten el
        C[ A[i] ] -= 1
        # zmnijeszamy o 1 bo uzywam iterpretacji ze jest to miejsce gdzie nowy (koolejny) el powinien byc
    return B

    # O(n+k+n) => O(n+k)

T=[8,11,15,7,7,20,1,1,1,0,50]
print(cnt_sort(T,max(T)+1))