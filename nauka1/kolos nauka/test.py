tab=[1,60,40,2,69,2137,21,21,21]
# for (idx,el) in enumerate(tab):
#     tab[idx]=(idx,el)
# print(tab)

def q_select(tab,k): #-> retuns el in k-position after sort  
    if len(tab)==0: return
    pivot=tab[0]
    if k==0: #pivot is our el on k-pos
        return pivot
    
    less=[i for i in tab[1:] if i<=pivot]
    great=[i for i in tab[1:] if i>pivot]
    #our pivot has to be on the len(less) position
    ll=len(less)-1
    # lg=len(great)-1
    
    if (ll+1==k): return pivot  
    elif ll >= k : #our el is in there because amount of el there are larger
        return q_select(less,k)
    else: #our el had to be there on new fixed position k-ll-2
        return q_select(great,k-ll-2)

print(q_select(tab,3))