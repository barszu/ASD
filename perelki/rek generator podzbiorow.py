def gen_podzb(tab):
    l = len(tab)
    global tab_podz
    tab_podz = []
    
    def engine(tab , l , i , temp_word = [] ):  # l const
        if i == l : #warunek zakonczenia
            tab_podz.append(temp_word)
            return False
        
        return engine(tab, l , i+1 , temp_word) or engine(tab, l , i+1 , temp_word + [tab[i]])
    
    engine(tab, l , 0 , [])
    return tab_podz