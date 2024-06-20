from zad9testy import runtests

"""
Bartlomiej Szubiak 415810

Generalnie zadanie sprowadza sie do znalezienia najdluzszej sciezki w grafie nieskierowanym.
Jesli pamietamy ile wynosi najdluzasza sciezka zaczynajaca sie od wierzcholka 'v' , 
a znajdujemy sie w wierzcholku 'u' probujac dolaczyc wierzcholek v do sciezki, problem sprowadzalby sie do pytania
ile wynosi najdlusza dlugosc sciezki z 'v' a to juz znamy,

F[u] = max([F[v] for v in sasiedzi(u)]) + 1
F[u] - dlugosc najdluzszej sciezki rozpoczynajacej sie w 'u'

Podejscie dziala tylko wtedy kiedy graf jest skierowany , acykliczny.

Sasiadem 'u' jest 'v' wtedy kiedy znajduje sie na lewo, prawo, gora lub dol od 'u' i M[v][u] > M[u][v]

zlozonosc: O(nm) gdzie n,m to wymiary macierzy M
"""


def trip(M):
    # tu prosze wpisac wlasna implementacje
    row_no = len(M)
    col_no = len(M[0])
    F = [[None for _ in range(col_no)] for _ in range(row_no)]

    def get_neighbours(node):
        row, col = node
        neighbours = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = row + dx
            new_col = col + dy
            if 0 <= new_row < row_no and 0 <= new_col < col_no:
                if M[new_row][new_col] > M[row][col]:
                    neighbours.append((new_row, new_col))
        return neighbours

    def dfs(node: (int, int)):
        row, col = node
        if F[row][col] is not None:  # already visited , cashed value
            return F[row][col]

        F[row][col] = 1 + max([dfs(neighbour) for neighbour in get_neighbours(node)], default=0)
        return F[row][col]

    maxy = 0
    for row in range(row_no):
        for col in range(col_no):
            maxy = max(maxy, dfs((row, col)))

    return maxy


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
