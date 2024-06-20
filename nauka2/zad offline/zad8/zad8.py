from zad8testy import runtests
"""
Bartlomiej Szubiak 415810

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


runtests(parking, all_tests=True)
