def eraseOverlapIntervals(intervals):
    def intersect(A,B): #are coliding?
        if not B>A: A,B = B,A
        return B[0]<A[1] #a < x colision
        
    INF = float('inf')
    intervals.append([INF,INF])
    intervals.sort(key=lambda x: x[1]) 
    #bo inaczej nie przewidujesz kolizji dobrze, nie musi kolidowac z j ale moze z k<j
    n = len(intervals)
    f = [1]*n
    for i in range(n):
        for j in range(i):
            if not intersect(intervals[i],intervals[j]):
                f[i] = max(f[i],f[j]+1)
    res = len(intervals)-f[-1]
    return res