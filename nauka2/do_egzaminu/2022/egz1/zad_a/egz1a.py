from egz1atesty import runtests


def snow(S):  # O(nlogn)
    # tu prosze wpisac wlasna implementacje
    S.sort(reverse=True)
    j = 0
    suma = 0

    while (S[j] - j > 0):
        suma += (S[j] - j)
        j += 1

    return suma


def snow(S): #XD ?
    S.sort(reverse=True)

    @lru_cache(maxsize=None)
    def f(a, b, k):
        if a > b:
            return 0

        return max(
            max(0, S[a] - k) + f(a + 1, b, k + 1),
            max(0, S[b] - k) + f(a, b - 1, k + 1)
        )

    return f(0, len(S) - 1, 0)


from functools import lru_cache
def snow(S):

    @lru_cache(maxsize=None)
    def f(a, b, k):
        if a == b:
            if S[a] - k > 0:
                return S[a] - k
            else:
                return 0

        if a > b: raise ValueError("a > b")

        aggregation_list = [0]
        for i in range(1, b - a + 1):
            if S[a] - k > 0:  # jest sens to brac
                aggregation_list.append(S[a] - k + f(a + i, b, k + 1))

            if S[b] - k > 0:  # jest sens to brac
                aggregation_list.append(S[b] - k + f(a, b - i, k + 1))

        return max(aggregation_list)

    return f(0, len(S) - 1, 0)








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
