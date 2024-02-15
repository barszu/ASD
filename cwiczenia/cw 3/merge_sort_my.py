def merge(tab,part_1,part_2):
    tab1=tab[(part_1[0]):(part_1[1] +1)]
    tab2=tab[(part_2[0]):(part_2[1] +1)]
    p,q=0,0
    out_p=part_1[1]-part_1[0]+1
    out_q=part_2[1]-part_2[0]+1
    
    new_tab=[0]*(out_p + out_q)
    nic_nie_wyszlo_poza=True
    i=0
    while nic_nie_wyszlo_poza:
        if (p==out_p):
            # doklej wszytsko z tab2 do new_tab
            new_tab[i::]=tab2[q::]
            nic_nie_wyszlo_poza=False
            break
        elif (q==out_q):
            # doklej wszytsko z tab1 do new_tab
            new_tab[i::]=tab1[p::]
            nic_nie_wyszlo_poza=False
            break
        
        if(tab1[p]>=tab2[q]):
            # insert tab1[p]
            new_tab[i]=tab1[p]
            p += 1
        else:
            new_tab[i]=tab2[q]
            q += 1
        
        i += 1
    tab[part_1[0]:part_2[1]+1]=new_tab
    return (part_1[0],part_2[1])
                   

def my_sort(tab,start,end): #start- 1 el,  end - na ostatni el
    if (end-start+1 == 2):
        if tab[start]<tab[end]:
            tab[start],tab[end]=tab[end],tab[start] #swap
        return (start,end)
    elif (end-start+1==1):
        return(start,end)
    
    mid_point=((end-start)//2)+start
    
    left_side=my_sort(tab , start , mid_point)
    right_side=my_sort(tab , mid_point+1 , end)
    
    return merge(tab , left_side , right_side  )