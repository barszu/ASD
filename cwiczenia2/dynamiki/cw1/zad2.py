"""
zad 4
uluz ciag macierzy tak aby bylo najmniej mnozen
"""

"""
zad 5
mamy bufor o dlugosci n zostal podzielony na k spojnych podciagow
wartosc podciagu to suma wartosci w nim
wartosc podzialu to najgorsza wartosc z podciagu

znajdz podzial ktory maksymalizuje wartosc podzialu

f(a,b,c,..,k) = min( sum(0,a-1) sum(a,b-1), sum(b,c-1), sum(c,d-1), ...  ) #wartosc z podzialu

max = max( f(a,b,c,..,k) ) #wartosc podzialu <- bruteforce (n^k)
      dla wszystkich mozliwych podzialow



"""

"""
zad 6
coin change -> najmniejsza liczba monet ktora daje kwote

f(i) = min( f(i-1) , f(i-2) , f(i-5) ) + 1 (dla monet 1,2,5)

"""

