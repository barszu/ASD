from zad1testy import runtests
# Bartłomiej Szubiak
# Idea algorytmu: wiemy ze palindrom jest nieparzystej dlugosci czyli jego centrum 
# znajduje sie na srodkowym znaku. Iterujemy po kazdym el tablicy (stringa) zakladajac ze jest 
# on potencialnym centrum. Dla kazdego centrum idziemy w lewo i prawo (od centrum)
# sprawdzajac jakiej dlugosci jest palindrom (t.j sprawdzamy czy lewy el == prawy el)
# stad "najkrotszy" palindrom ma dlugosc 1 
# idac w lewo czy w prawo nigdy nie wyjdziemy poza tablice (str) ponieważ sprawdzamy 
# czy nie wychodza poza nią
# złożonosć obliczeniowa O(N^2)


def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    n = len(s)
    longest=1
    for i in range(0,n-1): #chodzimy po tablicy zakladamy ze i-ty el jest centrum polindromu(bo sa one nieparzystej dlugosci)
        cond=True
        krok=1
        dl=1
        while cond:
            l=i-krok
            p=i+krok
            if l<0 or p>=n or (s[l]!=s[p]): #porownania poza tablica , konczy sie palindrom
                if dl>longest: longest=dl
                break
            else: 
                dl += 2 #bo +1 z lewej i z prawej
                krok += 1  
    return longest


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
