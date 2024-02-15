def sort_sc(tab1 , tab2):
    #dziala tylko wtedy kiedy 2 ciagi sa rosnace
    if len(tab2) > len(tab1) : tab1 , tab2 = tab2 , tab1
    l1 , l2 = len(tab1) , len(tab2)
    sorted_tab = [None]*(l1+l2)
    x = 0
    y = 0
    i = 0
    przepisz_tab1 , przepisz_tab2 = False , False
    while przepisz_tab1 == False and przepisz_tab2 == False :
        a = tab1[x]
        b = tab2[y]
        if a <= b :
            sorted_tab[i] = a
            x += 1
        else:
            sorted_tab[i] = b
            y += 1
        
        if x > (l1-1) and y <= (l2-1) : przepisz_tab2 = True
        elif y > (l2-1) and x <= (l1-1) : przepisz_tab1 = True
        
        i += 1
    else:
        if przepisz_tab1: sorted_tab[i:] = tab1[x:]
        elif przepisz_tab2 : sorted_tab[i:] = tab2[y:]
    
    return sorted_tab
