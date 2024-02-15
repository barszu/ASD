"""
Problem imprezy w firmie
- na imprezie nie moze byc przelozony i jego pracownik
- szukamy zbioru ludzi w ktorym jest najwiekszy fun

f(v) = wartosc najlepszej imprezy w podrzewie zakorzenionym w v (od v w dol) (v idzie na impreze albo nie)
g(v) = -||- (v NIE idzie na impreze)
"""
"""
f(v) = max( v.val + E g(ui) , g(v)) 
                 |ui - dziecko v|
"""
#- v idzie na impreze (wiec bierzemy jego fun) + dla kazdego dziecka iprezowosc bez nich(tego dziecka) (funkcja g)
# albo najlepsza impreze na ktore v nie idzie czyli g(v)
"""
g(v) = E f(ui)
   |vi - dziecko v|
"""
# suma najlepszych imprez na ktorych sa ich dzieci
"""
Ogolnie:
- zbior wierzcholkow niezaleznych o max sumie (nie polaczonych wspolna krawedzia)
- obliczamy 2 funkcje naraz -1 - nieobliczona wartosc jeszcze

"""
class Node:
    def __init__(self,val):
        # tablica node'ow
        self.childs = [] #dzieci, pracownicy node'a
        self.val = val
        # funkcje obliczane naraz w trakcie (-1 nie obliczono)
        #wartosci tych funkcji
        self.f = -1 # max suma wartosci w podrzewie od node'a (z nodem lub bez)
        self.g = -1 # -||- (BEZ node'a)
    
def g(v:Node):
    if v.g > -1 : return v.g
    f_sum = 0 # E (po dzieciach) f(ui)
    for ui in v.childs :
        f_sum += f(ui)
    v.g = f_sum
    return v.g
        
def f(v:Node): #v - node
    # rekurencja ze spamietywaniem
    if v.f > -1 : return v.f
    g_sum = v.val #v.val + E (po dzieciach) g(ui)
    for ui in v.childs:
        g_sum += g(ui)
    v.f = max(g_sum , g(v))
    return v.f

#wywolanie f(boss) boos - root

        