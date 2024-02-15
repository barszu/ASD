from egzP8atesty import runtests 

"""
PROBLEM: Znajdz takie przedzialy ktorych suma wartosci jest najwieksza ale na siebie nie nachodza
SOLUTION O(n^2):
    -> dla kazdego przedzialu stworz liste nienachodzacych na siebie przedzialow (razem z nich)
    -> brute'forcowo znajdz tutaj maximum

SOLUTION O(nlogn):
    ->
"""

def reklamy ( Intervals, val, max_days ):
    #Tutaj proszę wpisać własną implementację 
    I = [(a,b,val[i]) for i,(a,b) in enumerate(Intervals)]
    I.sort()
    n = len(I)
    matching_list = [[] for i in range(n)] #lista gdzie i nie koliduje z j (wewnetrznie moga)
    for i in range(n):
        x , y , _ = I[i]
        for j in range(i+1,n):
            a , b , v = I[j]
            #no colision -> add both to adjecty list
            if not a<= y: #no colision
                matching_list[i].append(j)
                matching_list[j].append(i)
    
    global_max = 0
    for i in range(n):
        temp_max = I[i][2]
        max_from_another = 0
        for j in matching_list[i]:
            max_from_another = max(max_from_another , I[j][2])
        global_max = max( global_max , temp_max + max_from_another)
            
    return global_max


def binsearch(a,x,lo=0,hi=None): #binsearch right
    if hi == None: hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def reklamy2(Intervals, val, max_days):
    I = [(a,b,val[i]) for i,(a,b) in enumerate(Intervals)]
    I.sort()
    n = len(I)
    # idx dla tablicy sortowanej
    
    # max wartosc (znaleziona) ze wszystkich przedzialow znajdujacych sie na osi liczbowej 
    # na prawo od I[i].start 
    DP = [0 for i in range(n+1)] #DP[i] - max wartosc z [i:n]
    for i in range(n-1,-1,-1):
        DP[i] = max( DP[i+1] , I[i][2] ) #val[i-th interval]
        
    starts = [I[i][0] for i in range(len(I))] #domyslnie posortowana
    
    global_max = 0
    for i,(a,b,v1) in enumerate(I):
        temp_max = v1
        idx = binsearch(starts,b,lo=i)
        #znajduje najbliszy na prawo el -> dajac idx odpowiedniego przedzialu
        #weryfikuje czy to napewno ten na prawo (czy czasem nie wstrzelony)
        if idx < n and starts[idx] != b:
            temp_max += DP[idx]
            
        global_max = max(global_max , temp_max)
    return global_max
        
    

runtests ( reklamy2, all_tests=True )