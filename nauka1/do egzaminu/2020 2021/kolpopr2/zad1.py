from zad1testy import runtests
"""
znajdz 1 prostokat ktorego wywalenie daje ( kiedy te inne sie beda przecinac) najwiekszy prostokat
"""
def ilo(A,B): #przeciecie z None to tak jak z R^2
    if not A or not B: return None #przeciecie ze zbiorem pustym
    x1_a, y1_a, x2_a, y2_a = A
    x1_b, y1_b, x2_b, y2_b = B

    # Sprawdzamy, czy prostokąty nachodzą na siebie
    if x1_a >= x2_b or x1_b >= x2_a or y1_a >= y2_b or y1_b >= y2_a:
        return None  # Brak przecięcia

    # Obliczamy współrzędne przecięcia
    x1_intersection = max(x1_a, x1_b)
    y1_intersection = max(y1_a, y1_b)
    x2_intersection = min(x2_a, x2_b)
    y2_intersection = min(y2_a, y2_b)

    return (x1_intersection, y1_intersection, x2_intersection, y2_intersection)

def pole(A):
    if not A: return 0
    x1, y1, x2, y2 = A
    width = abs(x2 - x1)  # Oblicz długość (szerokość) prostokąta
    height = abs(y2 - y1)  # Oblicz wysokość prostokąta
    area = width * height  # Oblicz pole prostokąta
    return area

def rect(D):
    # (x1,y1,x2,y2)
    n = len(D)
    pre = [None]*n #iloczyn [0:i-1]
    post = [None]*n #iloczyn [i+1:n-1]
    INF = float('inf')
    pre[0] = (-INF,-INF,INF,INF) # R^2
    post[n-1] = (-INF,-INF,INF,INF) # R^2
    
    for i in range(1,n):
        pre[i] = ilo(pre[i-1],D[i-1])
    for i in range(n-2,-1,-1):
        post[i] = ilo(post[i+1],D[i+1])
    
    max_pole_bez_niego = 0
    res = None
    for i in range(n):
        new_przeciecie = ilo(pre[i],post[i])
        if pole(new_przeciecie) > max_pole_bez_niego:
            max_pole_bez_niego = pole(new_przeciecie)
            res = i

    return res

    
runtests( rect )


