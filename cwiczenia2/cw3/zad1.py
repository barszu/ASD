# zrob qsorta bez rekurencji




def swap(T,a,b):
    T[a],T[b]=T[b],T[a]

def partition(A,p,r):
    # bierzemy x(pivot) z samego konca
    # analizujemy tablice od lewa do prawa
    # szukamy miejsca medianowego chwilowego
    # x - pivot
    # j - aktualnie przetwarzany el
    # i - el tuz przed el > x (na lewo od niego sa <)
    x=A[r]
    i=p-1 #przed tablica bo nie przetworzylismy el >= x
    for j in range(p,r,1):
        if A[j]<=x:
            i += 1
            # swap(A[i],A[j])
            swap(A,i,j)
    # swap(A[i+1],A[r])
    swap(A,i+1,r)
    return i+1

def quicksort(A,p,r): #p,r zakres tablicy teraz sortowanej
    if p<r : #mamy prace do wykonania len>1
        q=partition(A,p,r) #partition rozdziela tablice tak jak wyzej opisano
        quicksort(A,p,q-1) #sortujemy lewa
        quicksort(A,q+1,r) #sortujemy prawa

def qs_bez_rek(A):
    stack = [(0, len(A)-1)]
    while stack:
        p ,r = stack.pop()
        if p<r : #mamy prace do wykonania len>1
            q=partition(A,p,r) #partition rozdziela tablice tak jak wyzej opisano
            #musi byc na odwrot bo stos oryginalny wejdzie do lewej strony i to wymuszamy
            stack.append((q+1,r)) #prawa strona
            stack.append((p,q-1)) #lewa strona

            # quicksort(A,p,q-1) #sortujemy lewa
            # quicksort(A,q+1,r) #sortujemy prawa


T=[6,10,20,15,0,0]

qs_bez_rek(T)
print(T)

import random

# Tworzenie kilku losowych tablic
array1 = [random.randint(0, 1000) for _ in range(10)]
array2 = [random.randint(0, 1000) for _ in range(10)]
array3 = [random.randint(0, 1000) for _ in range(10)]

# Sortowanie tablic za pomocą qs_bez_rek
qs_bez_rek(array1)
qs_bez_rek(array2)
qs_bez_rek(array3)

print(array1 == sorted(array1))
print(array2 == sorted(array2))
print(array3 == sorted(array3))
