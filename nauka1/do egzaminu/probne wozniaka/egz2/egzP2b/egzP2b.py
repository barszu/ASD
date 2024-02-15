from egzP2btesty import runtests
from math import log10

def kryptograf( D, Q ):    
    #tutaj proszę wpisać własną implementację
    res = 0
    for sufix in Q:
        commons = 0
        if len(sufix) == 0: commons = len(D)
        else:
            for word in D: #sprawdzenie z kazdym slowem
                if len(sufix) <= len(word): #jest sens sprawdzac
                    if sufix == word[len(word)-len(sufix):]: commons += 1
        res += log10(commons)
    return res

def reverse_in_tab(tab:[str]):
    for i,v in enumerate(tab):
        tab[i] = v[::-1]
    
import bisect
def kryptograf2(D,Q):
    # szukaj prefixow nie sufixow -> reverse wszystkiego
    reverse_in_tab(D)
    reverse_in_tab(Q)
    
    D.sort() #aby uzywac binsearch
    res = 0
    for prefix in Q:
        lo = bisect.bisect_left(D,prefix) #-> idx pierwszego wystąpienia elementu
        hi = bisect.bisect_right(D, prefix + "2") #idx wstawienia na pozycji za ostatnim wystąpieniem elementu.
        #aby byl zawsze wiekszy w porownianiu z tym samym
        res += log10(hi-lo) #z tyloma relacja slownikowa byla zachowana czyli mieli te same prefixy czyli prefix ten sam w tylu slowach sie pojawil
    return res
    
    
    
    
    
    
# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
# runtests(kryptograf, all_tests = 1)
runtests(kryptograf2, all_tests = 3)