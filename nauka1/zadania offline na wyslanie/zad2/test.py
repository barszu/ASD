def max_el(T,n):
    najwiekszy=0
    for i in range(n-1):
        if T[i]>najwiekszy : najwiekszy=T[i]
    return najwiekszy

def counting_sort(T): #el sa od 0 do +inf
    n=len(T)
    max_val = max_el(T,n)  # znajdujemy maksymalna wartosc w tablicy
    zliczenia = [0] * (max_val + 1)  # tworzymy liste zliczeń
    for num in T:
        zliczenia[num] += 1  # zwiekszamy licznik dla danego elementu
    
    i=0 
    for j in range(max_val): #j to nasz el
        cnt_el=zliczenia[j]
        if cnt_el==0: continue
        T[i:i+cnt_el]=[j]*cnt_el
        i=i+cnt_el
    j=max_val
    cnt_el=zliczenia[-1]
    T[i::]=[j]*cnt_el

T=[8, 8, 3, 8, 8, 3, 1, 8, 3, 4, 8, 4, 4, 8, 8, 5, 9, 1, 2, 9, 9, 9, 0]
A=[8, 8, 3, 8, 8, 3, 1, 8, 3, 4, 8, 4, 4, 8, 8, 5, 9, 1, 2, 9, 9, 9, 0]
counting_sort(T)
print(sorted(A))
print(T)