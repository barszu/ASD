#algo znajdujacy jednoczesnie min i max uzywajac 3/2m porownań

def f(T):
    n=len(T)
    gus=T[-1]
    zus=T[-1]
    for i in range(1,n,2):
        if T[i]<T[i-1]:
            mi,ma = T[i],T[i-1]
        else:
            mi,ma = T[i-1],T[i]
            