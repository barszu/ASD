"""
Org zadanie magiczny wojownik, komnaty
"""

def maxGoldInPath(C): # "Problemem najdłuższej ścieżki w DAG z wagami"
    n = len(C)
    #[G,[K0,W0],[K1,W1],[K2,W2]]
    # Initialize max_gold array
    max_gold = [float('-inf')] * n
    max_gold[0] = 0 #ilosc zlota ktora mozna wyniesc do pozycji i
    
    # Iterate through vertices in topological order
    for i in range(n):
        G = C[i][0]
        for k,v in C[i][1:]:
            if v == -1 or G-k > 10: continue #niepoprawny wierzcholek , w skrzynce zostaje za duzo
            travel = max_gold[i] + G-k
            if travel < 0 : continue #nie ma mowy o tym zeby tam przejsc
            max_gold[v] = max(max_gold[v], travel)

    
    return max_gold[n-1]  # Max gold at the last vertex