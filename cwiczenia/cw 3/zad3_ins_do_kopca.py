class Heap:
    def __init__(self,n):
        self.T=[0]*n
        self.size=0
# kopiec binarny z 2 galeziami drzewo
    
def insert(H,x):
    # if H.size==0:
    #     H.T[0]=x
    #     H.size +=1
    #     return
    i=H.size
    p=parent(H.size)
    H.T[H.size]=x
    H.size +=1
    while p>=0:
        # heapify(H.T,p,H.size)
        # p=parent(p)
        if H.T[p]<H.T[i]:
            H.T[p],H.T[i]=H.T[i],H.T[p]
        else: break
        i=p
        p=parent(p)