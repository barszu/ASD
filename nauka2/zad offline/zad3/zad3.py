"""
Bartlomiej Szubiak 415810
Algorytm polega na prostym przeszukaniu dla kazdego punktu po innych punktach sprawdzajac ile elementow on dominuje.
Zlozonosc obliczeniowa to O(n^2) gdzie n to ilosc punktow w zbiorze P.
"""

from zad3testy import runtests

def dominance(P):
  global_max = 0
  for i in range(len(P)):
    (x,y) = P[i]
    local_max = 0
    for j in range(len(P)):
      if (i == j): continue
      (x2,y2) = P[j]
      if y2 < y and x2 < x: #P[i] dominuje P[j]
        local_max += 1
    global_max = max(global_max, local_max)
  return global_max



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
