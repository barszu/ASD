def bsort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i):
            if tab[j-1]>tab[j]:
                tab[j],tab[j-1]=tab[j-1],tab[j]