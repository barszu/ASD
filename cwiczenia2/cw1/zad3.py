# znajdz pozycje na ktora trzeba wstawic najmniejszego inta ktorego nie ma w tablicy -> binsearch (bo posortowane)
   
def binsearch(a,x,lo=0,hi=None):
    if hi == None: hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x == a[mid]: 
            return mid
        elif x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

arr = [1,20,30,70,100,2137]
print(binsearch(arr,21)) #1