"""Dana jest tab A rozmiaru n 
Elementy z A naleza do zbioru B gdzie |B|=log(n)
Chcemy posortowac A jak najszybciej

odtwarzamy B utrzymujemy B w porzadku rosnacym -> O(log n)
kiedy nie znajdziemy A[i] w B to wstawiamy do B -> binary search O(n log log n)
wstawiamy -> O(log n * log n)
=> O(log n * log n)

A=[10,1,5,10^6,...]
B=[1,5,10,..,10^6]
A'[3,log n , 0 , 1 , ...] <- pozycja el A[i] w tablicy B

A' cnt sort
odtwarzamy posortowane A -> A[i]=B[A'[i]]

=> n log log n mamy zlozonosc (najwieksze)




"""