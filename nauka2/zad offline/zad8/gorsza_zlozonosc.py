from zad8testy import runtests
from functools import lru_cache


def parking(X, Y):
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


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
