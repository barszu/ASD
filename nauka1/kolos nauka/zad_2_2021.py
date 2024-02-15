class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def gowno_sort(p,k):
    T=[]
    while p is not None :
        T.append(p.val)
        p=p.next
    T.sort()

def zakres(T,n,i,k): #i-pivot
    T_slice=[]
    if i-k < 0 : #niepelno na lewa strone
        T_slice += T[:i] 
    else: T_slice += T[i-k,i] 
    
    # T_slice += T[i]
    if i+k > n-1 : #niepelno na prawa strone
        T_slice += T[i:] 
    else: T_slice += T[i:i+k+1]
    
    return T_slice 

def qs_obj(tab):
    n=len(tab)
    if n==0 : return []
    elif n==1 : return tab
    elif n==2 : 
        if tab[0].val < tab[1].val :
            return tab
        else: return tab[::-1]
    pivot=tab[0]
    lesser=[ i for i in tab if i.val<=pivot.val]
    greater=[ i for i in tab if i.val>pivot.val]
    return [ *qs_obj(lesser) , pivot , *qs_obj(greater) ]   

def merge(tab,obj_el,start_idx):
    for i in range(start_idx,len(tab)):
        if (tab[i].val > obj_el.val):
            tab.insert(i,obj_el)
            break
    return tab

def napraw_ll(T,n):
    g=Node()
    a=g
    for i in range(n):
        a.next=T[i]
        a=a.next
    return g.next
    
    

def sorty_sort(p,k):
    T=[] #tablica obiektow
    while p is not None:
        T.append(p)
        p=p.next
    
    n=len(T)
    if k>n: return "zle k"
    elif k==0: return p 
    
    T_ready = zakres(T,n,0,k)
    T_ready = qs_obj(T_ready)
    if len(T_ready)==n : return napraw_ll(T,n)  
    
    for pivot_inx in range(1,n):
        if pivot_inx> n-1+k :
            return napraw_ll(T,n)
        
        lasty_inx = pivot_inx+k
        start_inx = pivot_inx-k
        T_ready=merge(T_ready,T[lasty_inx],start_inx)
    
    return napraw_ll(T,n)

a=Node()
b=Node()
c=Node()
a.next=b
b.next=c
a.val=10
b.val=7
c.val=5
p=sorty_sort(a,1)
print(p.val , p.next.val)
         
    
    
     


    