def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    n = len(s)
    longest=1
    for i in range(0,n-1): #chodzimy po tablicy zakladamy ze i-ty el jest centrum polidromu(bo sa one nieparzystej dlugosci)
        cond=True
        krok=1
        dl=1
        while cond:
            l=i-krok
            p=i+krok
            if l<0 or p>=n or (s[l]!=s[p]): #porownania poza tablica , konczy sie palidrom
                if dl>longest: longest=dl
                break
            else: 
                dl += 2 #bo +1 z lewej i z prawej
                krok += 1  
    return longest

print(ceasar("lmastsxhohgpvhqrjixrjbnzlsdptylygsuhvfqkxcgkvsobtyahvboidpvwdplpqfxcvfakawemgfqwdmnyurjfoyocqigcubxcuynfdwtclhaknrqctbjk"))