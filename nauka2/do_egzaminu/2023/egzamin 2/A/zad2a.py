# zlozonosc: O(n) gdzie n to liczba punktów

from egz2atesty import runtests


def dominance(P):
    max_x = max(P, key=lambda p: p[0])[0]
    max_y = max(P, key=lambda p: p[1])[1]

    Y_greater_eq = [0] * (max_y + 1)  # liczba punktow (x,y) ktorych y>=j   | x dowolne
    X_smaller_eq = [0] * (max_x + 1)  # liczba punktow (x,y) ktorych x<=i   | y dowolne
    X_equals = [0] * (max_x + 1)  # liczba punktow (x,y) ktorych x == i | y dowolne

    # same ze soba daja juz 1 (o ile wystepuja w P)
    for x, y in P:
        Y_greater_eq[y] += 1
        X_smaller_eq[x] += 1
        X_equals[x] += 1

    # akumulacja wartosci
    for x in range(1, max_x + 1): X_smaller_eq[x] += X_smaller_eq[x - 1]
    for y in range(max_y - 1, -1, -1): Y_greater_eq[y] += Y_greater_eq[y + 1]

    max_strength = []
    for x, y in P:
        max_strength.append(X_smaller_eq[x] - Y_greater_eq[y] - X_equals[x] + 1)
        # dla kazdego x (znajac ile jest punktow ktore maja 'x' <= x )
        # odfiltrowywuje punkty ktorych 'y' jest >= y
        # odfiltrowywuje punkty ktorych 'x' == x
        # -1 bo matematyka
    return max(max_strength)


runtests(dominance, all_tests=True)
