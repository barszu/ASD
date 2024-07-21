from egz1btesty import runtests
"""
Bartłomiej Szubiak 415810

Idea algorytmu jest bardzo prosta 
generalnie chcemy odrzucac ujemne liczby (jak tylko mozemy) bo zmniejszaja one sume (i szkodza, sa nie dobre), kazdą >= 0 chcemy bo zwieksza sume

biorac pod uwage kazdy przedzial T[i],...T[j], (kopjujemy elementy nie naruszamy struktury T)
sortujemy go aby miec najgorsze (najmniejsze liczby) po lewej stronie , a najlepsze (najwieksze) po prawej , (czyli definicja sortowania rosnaco)

i teraz agregujemy sume na tym posortowanym oknie i odrzucamy elementy ujemne jak tylko mozememy czyli kiedy usunelismy mniej niz jest limit k
(idziemy od najmniejszych ku najwiekszym | od lewa do prawa)

ta sume porownujemy z globalna i wyciagamy maximum

zlozonosc O(n^2 * (nlogn + n) ) = O(n^3 logn), nlogn bo sortujemy , n bo agregujemy sume, n^2 bo 2 petle
"""


# O(n^2 *(nlogn + n +n )) = O(n^3logn)



def kstrong( T, k):
  # tu prosze wpisac wlasna implementacje
  n = len(T)
  best_sum = -float("inf")
  for i in range(n):
    for j in range(n):
      window = T[i:j+1]
      window.sort()

      deleted_no = 0
      suma = 0
      for num in window: #sa posortowane to mozna tak robic
        if num < 0 and deleted_no < k : #nie chcemy najmniejszych ujemny i usuwamy je jak mozemy
          deleted_no += 1
          continue
        suma += num

      best_sum = max(suma, best_sum)


  return best_sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
