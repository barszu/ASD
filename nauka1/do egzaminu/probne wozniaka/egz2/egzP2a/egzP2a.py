from egzP2atesty import runtests 
"""
solution:
 - rob QSelekta -> nie ma znaczenia poukladanie w wierszu aby tylko byly wieksze/mniejsze
 - wypopuj z listy do macierzy a pozniej przepisz do listy zeby bylo okej
"""

def qSelect(nums,k,track): #k th- largest el , k>= 1
    k = len(nums)-k
    
    def qsel_helper(l,r):
        pivot, ptr = nums[track[r]][1] , l #pivot right most el
        for i in range(l,r): #without pivot
            if nums[track[i]][1] <= pivot:
                nums[track[ptr]] , nums[track[i]] = nums[track[i]] , nums[track[ptr]] #swap
                ptr += 1
        nums[track[ptr]] , nums[track[r]] = nums[track[r]] , nums[track[ptr]]
        if ptr > k : return qsel_helper(l,ptr-1) #qs on left
        elif ptr < k: return qsel_helper(ptr + 1,r)
        else: return nums[track[ptr]] 
    
    return qsel_helper(0,len(nums)-1)

def zdjecie(T, m, k):
    #tutaj proszę wpisać własną implementację
    COLS = k+m-1
    track_idx = [[None for j in range(COLS)] for i in range(m) ]
    
    c = 0
    for j in range(COLS):
        for i in range(m): 
            if j > k+m-2-i: break
            track_idx[i][j] = c
            c += 1  
    
    track_idx = [track_idx[i][j] for i in range(m) for j in range(COLS) if track_idx[i][j] != None]
    
    q = k+m-1
    for i in range(m):
        qSelect(T,q,track_idx)
        q = q + q -1
    
    
    return None


runtests ( zdjecie, all_tests=False )