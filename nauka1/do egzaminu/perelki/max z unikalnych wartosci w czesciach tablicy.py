"""
f(a,b) - max zarobek z [a,b] czesci tablicy

f(a,b) = V[b] + f(a,b-1) -> b NONPICKED
            #dokladam drzewo kiedy jeszcze go nienapotkalem , 
            # oznaczam jako PICKED
       = - V[b] + f(a,b-1)  -> b PICKED
            #nie moge dolozyc, naprawiam okno cofajac decyzje o wzieciu drzewa -> bo nie moge miec 2
            # oznaczam jako OVERPICKED
       = f(a,b-1) -> b OVERPICKED
            #nie moge dolozyc bo za duzo, okno mam dobre, pomijam drzewo
"""

def ogrod2( S, V ):
    NONPICKED = 0
    PICKED = 1
    OVERPICKED = 2
    
    V = [None] + V #aby indeksy sie zgadzaly
    n = len(S)
    m = len(V)
    DP = [[0 for i in range(n)] for j in range(n)] 
    
    for a in range(n): #rozpoczynam przedział
        taken = [NONPICKED for i in range(m)] #znacznik co sie dzieje z danym typem drzewa
        for b in range(a,n): #rozszerzam przedział  
                     
            if taken[S[b]] == NONPICKED: #nie zostalo jeszcze wziete, biore je
                DP[a][b] = DP[a][b-1] + V[S[b]] # b-1 problem nie zalatwiany -> bierze od konca
                taken[S[b]] = PICKED
                
            elif taken[S[b]] == PICKED: #bylo wziete, cofam decyzje o wzieciu bo w oknie mam 2 takie same drzewa
                DP[a][b] = DP[a][b-1] - V[S[b]]
                taken[S[b]] = OVERPICKED
                
            elif taken[S[b]] == OVERPICKED: # #pomijam bo za duzo i tak ich jest w oknie
                DP[a][b] = DP[a][b-1]
            
    return max([max(row) for row in DP])