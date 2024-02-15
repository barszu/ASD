# T-posortowana tabvlica liczb
# x - liczba (x>0)
# sprawdz czy istnieje i , j takie ze T[j]-T[i] = x

def zad(tab,x):
    i =0
    j=i+1
    while(j<len(tab)):
        if (tab[j]-tab[i]==x):
            return True
        if (tab[j]-tab[i]<x):
            j += 1
        else:
            i += 1
    return False