from egz1btesty import runtests

"""
Bartłomiej Szubiak 415810

Pomysl polega na stworzeniu funkcji f(i,j), 
ktora odpowiada na pytanie jaka jest najwieksza suma podciagu 
jezeli jestesmy na i-tym elemencie i wycieliśmy co najwyzej j elementow. 

f(i,j) = max(
              f(i-1,j-1) #wyciecie elementu
              f(i-1, j) + T[i] #dodanie elementu do sumy
            )

f(0,j) = max(0, T[0]) # w zalezności od tego czy oplaca się zaczynac podciag na zerowym elemencie. (czy nie jest on ujemny)

Nie trzymam informacji o tym, gdzie rozpoczynal się podciag, bo jest ona zbedna 
- jezeli nie oplacaloby sie to, by brac pod uwagę jakies pierwsze kilka elementów
to wynik w danym polu tablicy cache'ujacej zostanie zdominowany przez inną sekwencję wyborów. 

Wynik to maksymalna wartosc funkcji f (w cache'u)


Zlozonosc: O(n*k). W przypadku, gdy wszystkie liczby są ujemne, zwracam sume 0.
"""

def kstrong( T, k):
  n = len(T)
  cache_array = [[0 for j in range(k+1)] for i in range(n)]
  for j in range(k+1):
    cache_array[0][j] = max(0, T[0])

  for i in range(1, n):
    cache_array[i][0] = max(cache_array[i-1][0] + T[i], T[i])
    for j in range(1, k+1):
      cache_array[i][j] = max(cache_array[i-1][j-1], cache_array[i-1][j] + T[i])


  maksimum = -float('inf')
  for j in range(k+1): #[0,k]
    for i in range(n): #[0, n-1]
      maksimum = max(maksimum, cache_array[i][j])

  return maksimum

runtests( kstrong, all_tests = True )
