"scalanie dwoch posortowaych list jednoskierunkowych do jednej"
def merge(L1, L2): #rekurencynie/funkcyjnie
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if L1.value < L2.value:
        L1.next = merge(L1.next, L2)
        return L1
    else:
        L2.next = merge(L1, L2.next)
        return L2
    
"""
algorytm sortowania list jednokierunkowych przez scalanie seri naturalnych

leetcode merge k sorted lists!
-> scalaj parowo te listy
"""

