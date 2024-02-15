"""
find/union - STRUKTURA DANYCH - las (rodzina) drzew rozlacznych
- pozwala efektywnie implementowac KRUSKALA

Idea:
find - daje indentyfikator zbioru w ktorym el jest
union - 2 zbiory skleja w 1

FIND 
- wedrujemy w gore drzewa do korzenia 
    i jego zwracamy jako identyfikator(reprezentant) zbioru
- kompresja sciezki przepinamy v do roota

rank = k - zawiera conajmniej 2^k el

UNION 
- dolaczamy korzen jednego drzewa do drugiego (szybkie skelejenie)
- z kazdym zbiorem laczymy "rank" 
    i drzewo o mniejszym rank dolaczamy do tego o wiekszej
    - jesli rank rowne to obojetne dolaczamy ale rank ROSNIE

Jezeli stosujemy laczenie wdl. rank oraz kompresje sciezki
-> zlonosc O(m log* m) m-ilosc operacji
log* - log(log(log(...))) <= 1

"""

class Node:
    def __init__(self,value):
        self.parent = self
        self.rank = 0 #2^k
        self.value = value

def find_set(x:Node): #idzie w gore korzenia i kiedy dojdzie 
    # przestawia parenty wszytkich el po ktorych przeszedl na roota
    if x.parent != x : #nie jestesmy jeszcze w rodzicu
        x.parent = find_set(x.parent) #kompresja sciezki
    return x.parent

def union(x:Node,y:Node):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank :
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank :
            y.rank += 1