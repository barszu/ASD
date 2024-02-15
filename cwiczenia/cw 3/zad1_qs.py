def quick_sort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        # quick_sort(A,p,q-1)
        # p=q+1
        if q-p<r-q :
            quick_sort(A,p,q-1)
            r=q+1
        else:
            quick_sort(A,q+1,r)
            r=q-1