from zad5ktesty import runtests
"""
On gra w to samo co i my !
-> f(a,b) => (max wartosc os co wykonuje teraz ruch , max wartosc os co wykonuje nast ruch)

if a==b: -> (T[a],0)
if a+1==b: -> (max(T[a],T[b]) , min(T[a],T[b]))

a) T[a] + f(a+1,b)[1] #jako ruch drugiego gracza tego przegrywajacego nast runde
b) -//- 
wez max z tych ^

"""

def garek ( T ): #niedziala, wybiera zawsze najwieksze z left,right
    n = len(T)
    dp = [[None for j in range(n)] for i in range(n)]
    
    def dfs(a,b):
        if not 0<=a<n or not 0<=b<n: return 0
        if dp[a][b] is not None: return dp[a][b]
        if a == b:
            dp[a][b] = T[a]
            return dp[a][b]
        if a + 1 == b:
            dp[a][b] = max(T[a],T[b])
            return dp[a][b]
        
        
        
        take_left = T[a] #-> g(a+1,b)
        if T[a+1] < T[b]: #wezmie b
            take_left += dfs(a+1,b-1) if a+1 <= b-1 else 0
        else: #wezmie a
            take_left += dfs(a+2,b) if a+2 <= b else 0
        
        take_right = T[b] #-> g(a,b-1)
        if T[a] < T[b-1]: #wezmie b-1
            take_right += dfs(a,b-2) if a <= b-2 else 0
        else: #wezmie a
            take_right += dfs(a+1,b-1) if a+1 <= b-1 else 0
        
        dp[a][b] = max(take_left,take_right)
        return dp[a][b]
    
    print(T)
    res = dfs(0,n-1)
    return res

def max_scoore(A):
    n = len(A)
    F = [[0] * n for _ in range(n)]
    
#     iters = 0
    
    # Recursive function to search for the greatest profit from i to j array part
    def play(i, j):
#         nonlocal iters
#         iters += 1
        
        # If a remaining part contains only one element, there is nothing to choose from
        # instead of the last possible value
        if i == j: return A[i]
        # If there are only 2 values remaining, we take the greater one
        if j - i == 1: return max(A[i], A[j])
        # In all other cases we choose max possible scoore considering all possible moves
        # (We remember that an opponent plays the way we get the least scoore, so he will
        # leave us with the worst possibility after his move)
        # Calculate if only there is no value cached
        if not F[i][j]:
            F[i][j] = max(A[i] + min(play(i + 2, j), play(i + 1, j - 1)),
                          A[j] + min(play(i, j - 2), play(i + 1, j - 1)))
        return F[i][j]
        
    res = play(0, n-1)
    
#     print('Iterations:', iters)
#     print(*F, sep='\n')
        
    return res

runtests ( max_scoore )
tab =  [50, 7, 44, 7, 44, 23, 10, 39, 6, 5, 28, 3, 8, 15, 36, 23, 8, 3, 42, 43]
# print(garek(tab))