"""
podziel na k spojnych przedzialow o najmniejszej sumie
wywolanie f(n-1,k)

f(i,k) = min( max (sum[j+1,i] , f(j,k-1) ) , ... )
       j:[0,i-1]

odi-tego moge rozpoczac dzielenie
miejsce dzielenia to j -> nalezy juz do innej firmy

"""

def f(T,DP,SUM,i,k):
    if k<0 or i>len(T)-1:
        return float('inf')
    if DP[i][k]<float('inf'):
        return DP[i][k]
    res=float('inf')
    for j in range(0,i):
        res=min(res, max(SUM[i]-SUM[j], f(T,DP,SUM,j,k-1)))
    DP[i][k]=res
    return DP[i][k]

def autostrada( T,k ): #to litte change!
    n=len(T)
    SUM=[0 for _ in range(n)]
    SUM[0]=T[0]
    for i in range(1,n):
        SUM[i]=SUM[i-1]+T[i]
    DP=[[float('inf') for _ in range(k+1)] for _ in range(n)] #wynik dla i liczb, k przedziałów
    for i in range(n):
        DP[i][1]=SUM[i]
    for i in range(k+1):
        DP[0][i]=T[0]
    return f(T,DP,SUM,n-1,k)