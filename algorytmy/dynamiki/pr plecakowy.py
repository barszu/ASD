"""
kazdy item ma swoja wage, cene
plecak max pomiesci B - maksymalna wage

Zadanie:
szukamy itemy ktorych laczna waga < B , laczna cena maxymalna
b - laczna waga (chwilowa) < B
f(i,b) = maxymalna suma cen przedmiotow ze zbioru {0,i}
f(i,b) = max( f(i-1,b) , f(i-1,b-waga(i)))
"""
#  i-ty NIE bierzemy / bierzemy (trzeba na niego miejsce miec)
#  kiedy b-waga(i) < 0 - nie ma miejsca na ten item - nie da go wziac
"""
# f(0,b) = cena(0) dla b - waga(0) >= 0
       # = 0 dla b - waga(0) < 0 (nie da sie wziac)
"""
class Item:
    def __init__(self,weight,price):
        self.w = weight 
        self.p = price
    def __repr__(self):
        return "|w: {}, p: {}|".format(self.w, self.p)

def find_path(item_tab,parent,last_point):
    taken_items=[] #tablica typu Item
    w,k = last_point
    while True:
        if parent[w][k] == None : break
        p_w , p_k = parent[w][k]
        if p_k == k : #element nie zostal wziety
            w,k = p_w , p_k #dalsza iteracja
        elif p_k < k : #element zostal wziety
            taken_items.append(item_tab[w])
            w,k = p_w , p_k #dalsza iteracja
        if p_w <0 or p_k <0 : break
    return taken_items

def knapsack(item_tab , B):
    n = len(item_tab)
    
    F = [[0 for b in range(B+1)] for i in range(n) ] #-> indeksacja F[i][b]
    parent = [[None for b in range(B+1)] for i in range(n) ] #tablica kordow pola rodzica
    
    for b in range(item_tab[0].w , B+1 ): #update f(0,b) , dla itema 0
        F[0][b] = item_tab[0].p
        parent[0][b] = (-1,-1) # tak jakby biore ten 1 el zawsze?
    for i in range(1,n): #update f(i,b) , update reszty el
        for b in range(B+1):
            F[i][b] = F[i-1][b] #nie bierzemy itema (idziemy w gore tablicy)
            parent[i][b] = (i-1 , b)
            if b - item_tab[i].w >= 0 : #jest git i mozna go wziac
                # zostaje z wyborem nie wziecia ,
                # bierzemy i-go przedmiotu ale zostawiamy na niego miejsce + wartosc jego
                f_val_as_taken = (F[i-1][b - item_tab[i].w] + item_tab[i].p)
                if f_val_as_taken >= F[i][b] : #albo > nwm?
                    F[i][b] = f_val_as_taken
                    parent[i][b] = (i-1 , b- item_tab[i].w)
    #najwieksza wartosc tych el
    return F[n-1][B] , find_path(item_tab,parent,(n-1 , B))#prawy dolny rog przeszlismy po wszystkich mozliwosciach

         


# mozna dodac tablice parent dla pol F[i][b] uwzglednijac zmiany (biore, nie biore)
def knapsack_orginal(W,P,B): #item dyskretnie zapisany (pod indeksem) w W,P (weight,price)
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n) ] #-> indeksacja F[i][b]
    for b in range(W[0] , B+1 ): #update f(0,b)
        F[0][b] = P[0]
    for i in range(1,n): #update f(i,b)
        for b in range(B+1):
            F[i][b] = F[i-1][b] #nie bierzemy itema (idziemy w gore tablicy)
            if b - W[i] > 0 : #jest git i mozna go wziac
                # zostaje z wyborem nie wziecia ,
                # bierzemy i-go przedmiotu ale zostawiamy na niego miejsce + wartosc jego
                F[i][b] = max(F[i][b] , F[i-1][b-W[i]] + P[i]) 
    return F[n-1][B] #prawy dolny rog przeszlismy po wszystkich mozliwosciach

item1 = Item(2, 10)
item2 = Item(3, 15)
item3 = Item(5, 30)
item4 = Item(1, 5)

item_tab = [item1, item2, item3, item4]
B = 8

result, taken_items = knapsack(item_tab, B)
print("Max value:", result)
print("Taken items:")
for item in taken_items:
    print(item)