def binsearch(a,x,lo=0,hi=None): #binsearch right
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