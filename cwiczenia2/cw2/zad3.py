"""
Dana jest posortowana tablica A oraz liczba x, czy istnieja idx i , j takie ze A[i] + A[j] = x?
(po polsku: suma dwoch elementow z tablicy daje x)

# two pointer approach!!!
za malo -> bierze wiekszy kes listy (poszerza okno)
za duzo -> shrinkuje okno z lewej

#two pointer approach v2
start = 0 
end = len(A) - 1
if A[start] + A[end] < x: start += 1   #shrinkuj z lewej
if A[start] + A[end] > x: end -= 1     #shrinkuj z prawej
"""