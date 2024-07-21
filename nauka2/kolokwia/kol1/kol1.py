from kol1testy import runtests
#Bartlomiej Szubiak 415810

# algorytm dla kazdego elementu z tablicy T przechodzi po wszystkich elementach na lewo od niego
# jesli znajdzie el ktory jest mniejszy od niego (od i-tego) to zwieksza range i-tego elementu o jeden
# (naturalnie j-ty element znajduje sie juz po lewej od niego i nie trzeba tego sprawdzac)

# algorytm ideowo jest prosty

# algorytm ma zlozonosc czasowa O(n^2) (dwie petle zagniezdzone po tablicy T)
# zlozonosc pamieciowa: O(1) (kilka zmiennych typu int)

def maxrank(T):
  n = len(T)
  global_max_rank = 0 #ogolna znaleziona najwieksza wartosc rangi
  for i in range(0,n): #[0,n-1]
    local_rank = 0 #dla i-tego
    for j in range(0,i): #[0,i-1] 
      if T[j] < T[i]:
        local_rank += 1
    global_max_rank = max(global_max_rank , local_rank)
  return global_max_rank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
