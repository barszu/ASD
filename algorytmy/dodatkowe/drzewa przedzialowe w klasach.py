# inttree.py
#
# implementacja drzewa przedzialowego -- wolno uzyc na kolokwium 3
# Algorytmy i Struktury Danych 2020
#
# Zlozonosci przy algorytmach sa takimi, jakie nalezy zalozyc przy
# analizie wlasnego kodu (faktyczna implementacja jest w niektorych przypadkach troche
# wolniejsza)

class Node:
    def __init__(self):
        self.cut    = None    # klucz tego wezla #mid
        self.left   = None    # span = [self.left, self.right]
        self.right  = None
        self.intervals = []   # przedzialy zgromadzone w tym wezle
        self.lchild = None    # lewe dziecko
        self.rchild = None    # prawe dziecko
        self.leaf   = False   # czy to lisc?
        
        
# zbuduj drzewo przedzialowe, ktore moze przechowywac
# przedzialy postaci [a,b], gdzie a,b to punkty z tablicy A
# tablica A musi byc posortowana rosnaco i bez powtorzen
#
# Zlozonosc: O(n), gdzie n to rozmiar A
def build(A):
    def tree_build_helper(A, i, j, left, right): # funkcja pomocnicza do budowania drzewa    
        X = Node()
        X.left  = left
        X.right = right
        if (j < i):
            # build leaf
            X.cut  = -1
            X.leaf = True
        else:
            # build internal node
            m = (i + j) // 2
            X.cut   = A[m]
            X.lchild = tree_build_helper(A, i, m - 1, left, A[m])
            X.rchild = tree_build_helper(A, m + 1, j, A[m], right)
        return X
    
    return tree_build_helper(A,0,len(A)-1,min(A)-1, max(A)+1)

# Wypisz zawartosc drzewa X
def tree_print(X, ind=""):
    if X.leaf:
        print(ind, "leaf-span: [%d, %d] --> " % (X.left, X.right), X.intervals);
    if not X.leaf:
        # cut - mid
        print(ind, "cut = %d," % X.cut, "span = [%d, %d], " % (X.left, X.right), "intervals =", X.intervals);
        tree_print(X.lchild, ind + "  ")
        tree_print(X.rchild, ind + "  ")

# funkcja pomocnicza wykonujaca operacje na zadanym przedziale
def tree_op( X, I, f):
    (a, b) = I
    if a <= X.left and b >= X.right:
        f(X,I)
        return
    if a < X.cut:
        tree_op(X.lchild, I, f)
    if b > X.cut:
        tree_op(X.rchild, I, f)

# Wstawia przedzial I do drzewa X
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_insert(X,I):
    def op_insert(X,I): X.intervals.append(I)# funkcja pomocnicza
    tree_op( X, I, op_insert )

# Usuwa przedzial I z drzewa X (jesli przedzialu nie ma, to nic nie robi)
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_remove(X,I):
    def op_remove( X, I ):# funkcja pomocnicza
        try:
            X.intervals.remove(I)
        except ValueError:
            None
    tree_op( X, I, op_remove )


# zwraca liste wszystkich przedzialow z drzewa X, ktore zawieraja punkt a
# UWAGA: niektore przedzialy moga wystepowac dwa razy
#
# Dziala w czasie O(logn + k), gdzie n to liczba punktow na bazie
# ktorych powstalo drzewo a k to liczba znalezionych przedzialow
def tree_intersect(X, a): #shallow
    R = X.intervals.copy()
    if X.leaf:
        return R
    if a <= X.cut:
        R += tree_intersect(X.lchild, a)
    if a >= X.cut:
        R += tree_intersect(X.rchild, a)
    return R

borders = [1,10,22,23,56,100,10000] #krance przedzialow
root = build(borders)
tree_insert(root,(10,22))
tree_insert(root,(1,56))
tree_print(root)
