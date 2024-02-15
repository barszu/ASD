# znajdujemy mediane-> pivot
# dzielimy tablice na el < od pivot , pivot , > od piwot
# lewa i prawa sortujemy rek

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

# partition Hoare'a

def quicksort(A,p,r): #p,r zakres tablicy teraz sortowanej
    if p<r : #mamy prace do wykonania len>1
        q=partition(A,p,r) #partition rozdziela tablice tak jak wyzej opisano
        quicksort(A,p,q-1) #sortujemy lewa
        quicksort(A,q+1,r) #sortujemy prawa

# lepszy pivot
# - losowy el tablicy
# - mediana z np 1 ostatniego i srodkowego el

# usuniecie rek ogonowej z qs
def qs_bez_rek(A,p,r):
    while p<r :
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        p = q+1


def qs(a):
    if len(a)==0 : return []
    piv = a[0]
    less = qs([i for i in a[1:] if i <= piv])
    grt = qs([i for i in a[1:] if i > piv])
    return [*less, piv, *grt]



T=[6,10,20,15,0,0]
# quicksort(T,0,len(T)-1)
T=qs(T)
print(T)