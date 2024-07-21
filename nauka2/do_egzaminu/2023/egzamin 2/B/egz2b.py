# f(i, j) = minimalna suma odległości biurowców z pozycji X[0] do X[i]
# do przydzielonych im działek, przy założeniu że biurowiec 
# z pozycji X[i] ma przydzieloną działkę z pozycji Y [j].
from functools import lru_cache

from egz2btesty import runtests

def parking(X, Y):# O(nm^2)
    # tu prosze wpisac wlasna implementacje
    buildings_pos = X
    parkings_pos = Y

    INF = float('inf')

    def distance(building_idx, parking_idx):
        return abs(buildings_pos[building_idx] - parkings_pos[parking_idx])

    @lru_cache(maxsize=None)
    def f(i, d):
        if i == len(buildings_pos) - 1: #nie potrzeba juz dobierac parkingu
            return distance(i, d)

        others = [f(i + 1, new_d) for new_d in range(d + 1, len(parkings_pos))]

        if len(others) == 0 : # nie mozna dobrac juz parkingu!
            return INF

        return min(others) + distance(i, d)

    res = min([f(0, d) for d in range(len(parkings_pos))])
    return res


"""
Algorytm dziala w czasie O(n*m) gdzie n to liczba budynkow a m to liczba nadmiarowych parkingow -> liczba wszystkich parkingów

f(i, j) = min( 
            f(i - 1, j) + dist[i][j + i]      | i > 0 else dist[j + i][i]   #przypisuje j-ty nadmiarowy parking i-temu budynkowi
            f(i, j - 1) ;                     | j > 0 else INF              #probuje przypisac j-1 nadmiarowy parking i-temu budynkowi
            )


i - building index
j - excess parking index

f(i, j) - minimalna suma odległości od budynków 0..i do parkingów 0..j

funkcja create_dist tworzy tablice odległości między budynkami i parkingami tak aby latwo i szybko znajdowac te odleglosci
"""


def create_dist(building_pos, parking_pos):
    n = len(building_pos)
    m = len(parking_pos)
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dist[i][j] = abs(building_pos[i] - parking_pos[j])
    return dist
def parking(X, Y):
    building_pos = X
    parking_pos = Y
    dist = create_dist(building_pos, parking_pos)

    excess_parking_no = len(parking_pos) - len(building_pos) + 1
    building_no = len(building_pos)

    cache = [[0 for _ in range(excess_parking_no)] for _ in range(building_no)]

    for building_idx in range(building_no):
        for ex_parking_idx in range(excess_parking_no):

            cache[building_idx][ex_parking_idx] = dist[building_idx][ex_parking_idx + building_idx]

            cache[building_idx][ex_parking_idx] += cache[building_idx - 1][ex_parking_idx] if building_idx != 0 else 0
            if ex_parking_idx > 0:
                cache[building_idx][ex_parking_idx] = min(cache[building_idx][ex_parking_idx],
                                                          cache[building_idx][ex_parking_idx - 1])

    res = [cache[building_no - 1][o] for o in range(excess_parking_no)]
    return min(res, default=float('inf'))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True)