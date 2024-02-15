from zad1ktesty import runtests
# f(a) - ilosc jedynek od [0:a] , razem z a
# g(a) - ilosc zer od [0:a]

# f(a,b) = f(b)-f(a-1) , a-1 == -1 => 0
# g(a,b) = g(b) - g(a-1)

def roznica( S ):
    n = len(S)
    f = [0 for i in range(n+1)] #zeby -1 dzialalo
    g = [0 for i in range(n+1)]
    
    def calc_range(tab,x,y): return tab[y] - tab[x-1]

    for i in range(n):
        if S[i] == '1':
            f[i] = f[i-1] + 1
            g[i] = g[i-1]
        else:
            f[i] = f[i-1] 
            g[i] = g[i-1] + 1
    
    dp = [[-10 for j in range(n)] for i in range(n)]
    # dp(a,b) ciagi od (a,b) - roznica miedzy iloscia zer a jedynek
    for a in range(n):
        for b in range(a,n):
            ones_no = calc_range(f,a,b)
            zeros_no = calc_range(g,a,b)
            dp[a][b] = max(zeros_no-ones_no,-1)
            
    print(S)
    return max([max(row) for row in dp])

runtests ( roznica )
# test 3
string = "10001011111001010101"