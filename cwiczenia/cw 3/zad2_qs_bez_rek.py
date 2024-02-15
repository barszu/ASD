def QS_iter(A,start,end):
    S=stack
    S.push((start,end))
    while not S.is_empty():
        a,b = S.pop()
        if b>a:
            q=partition(A,a,b)
            S.push((a,q-1))
            S.push((q+1,b))
        