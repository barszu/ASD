"""
traveling salesperson problem - TSP
Zadanie:
Znajdz kolejnosc odwiedzania miast zaczac w s skonczyc s (szukamy cyklu)
i odwiedzic wszystkie miasta minimalizujac sume odleglosci miedzy kolejnymi miastami

f(S,t) - dlugosc najkrotszej trasy, ktora startuje w miescie 0 
         odwiedza wszystkie miasta ze zbioru S i konczymy w miescie t
(0 e S , t e S)

f(S,t) = min( f(S/{t} , r) + d(r,t) ,...) - r to miasto posrednie bezposrednio przed t
        r e S/{t}
        
f({0},0) = 0

Odczyt wyniku 
- start z miasta 0, odwiedzic wszystkie miasta skonczyc w miescie t i z niego pojechac do miasta 0
min ( f(0,t) + d(t,0) , ...) 
t e {1,...,n-1}

zlononosc O(2^n * n^2)

"""

#z GPT
import sys

def tsp(graph):
    n = len(graph)  # Liczba miast
    dp = [[-1] * n for _ in range(2**n)]  # Tablica pomocnicza dla programowania dynamicznego
    parent = [[-1] * n for _ in range(2**n)]  # Tablica przechowująca informację o poprzednim mieście w najkrótszej trasie
    
    # Funkcja pomocnicza do obliczenia odległości między dwoma miastami
    def dist(city1, city2):
        return graph[city1][city2]
    
    # Rekurencyjna funkcja rozwiązująca problem TSP
    def tsp_helper(mask, pos):
        if mask == (2**n) - 1:  # Wszystkie miasta zostały odwiedzone
            return dist(pos, 0)  # Wróć do miasta początkowego
        
        if dp[mask][pos] != -1:  # Sprawdź, czy wynik został już obliczony dla danego podproblemu
            return dp[mask][pos]
        
        ans = sys.maxsize  # Nieznacznie większa wartość niż maksymalna wartość inta
        next_city = -1
        
        for city in range(1, n):
            if not (mask & (1 << city)):  # Sprawdź, czy miasto jeszcze nie zostało odwiedzone
                new_mask = mask + (1 << city)
                new_dist = dist(pos, city) + tsp_helper(new_mask, city)
                
                if new_dist < ans:
                    ans = new_dist
                    next_city = city
        
        dp[mask][pos] = ans
        parent[mask][pos] = next_city
        
        return ans
    
    # Obliczanie najkrótszej trasy
    tsp_helper(1, 0)
    
    # Odtworzenie kolejności odwiedzanych miast
    path = []
    mask = 1
    pos = 0
    
    for _ in range(n - 1):
        next_city = parent[mask][pos]
        path.append(next_city)
        mask = mask + (1 << next_city)
        pos = next_city
    
    return path

# Przykładowy graf miast
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path = tsp(graph)

# Wyświetlenie wyniku
print("Kolejność odwiedzanych miast:")
print("0 ->", end=" ")

for city in path:
    print(city, "->", end=" ")

print("0")

"""
komiwojager - wersja listioniczna
f(i,j) = koszt sciezek z 0  do i oraz z 0 do j
    ktore odwiedzaja wszystkie miasta 0,i,..,j i zadnego nie powtarzaja
f(0,1) = d(0,1)
i < j-1
a)  f(i,j) = f(i,j-1) + d(j-1,j)
b)  f(j-1,j) = min ( f(i,j-1) + d(i,j) ,...)
             i < j-1
"""
def TSP_main(D):
    INF = float('inf')
    n = len(D)
    # D[i][j] = d(i,j)
    F = [ [INF for i in range(n)] for i in range(n)]
    F[0][1] = D[0][1]
    
    def tspf(i,j,F,D):
        if F[i][j] != INF : return F[i][j]
        if i==j-1:  #b)
            best = INF
            for k in range(j-1):
                best = min(best, tspf(k,j-1,F,D) + D[k][j])
            F[j-1][j] = best
        else: #a)
            F[i][j] = tspf(i,j-1,F,D) + D[j-1][j]
        return F[i][j]