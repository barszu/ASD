from zad1testy import runtests


def countingSort(T, k):
    C = [0] * k
    B = [0] * len(T)
    for i in range(len(T)):
        C[T[i][0]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(T) - 1, -1, -1):
        C[T[i][0]] -= 1
        B[C[T[i][0]]] = T[i]

    return B


def tanagram(x, y, t):
    n = len(x)
    A, B = [], []

    for i in range(n):
        A.append([ord(x[i]) - ord("a"), i])
        B.append([ord(y[i]) - ord("a"), i])

    A = countingSort(A, 26)
    B = countingSort(B, 26)

    for i in range(n):
        if abs(A[i][1] - B[i][1]) > t: return False

    return True


class IntDict:
    def __init__(self):
        self.dict = [0 for _ in range(ord('z') - ord('a') + 1)]

    def get(self, x: str):
        return self.dict[ord(x) - ord('a')]

    def set(self, x: str, val: int):
        self.dict[ord(x) - ord('a')] = val


def tanagram(x, y, t): #rozwla sie bo nie wiadomo czy jak zuzylem litere to czy mam ja usunac
    dict = IntDict()
    # stworz zbior z y[0:t] dla x[0]:
    for i in range(0, t + 1):
        dict.set(y[i], dict.get(y[i]) + 1)

    # przediteracja
    idx = 0
    letter = x[idx]
    if dict.get(letter) == 0: return False
    dict.set(letter, dict.get(letter) - 1)

    for idx in range(1, len(x)):  # okno [idx-t:idx+t]
        letter = x[idx]
        # usun stary element idx-t-1
        if idx - t - 1 >= 0:
            _letter = x[idx - t - 1]
            if dict.get(_letter) == 0: return False  # rozspojnienie seta
            dict.set(_letter, dict.get(_letter) - 1)

        # dodaj nowy element idx+t
        if idx + t < len(x):
            _letter = x[idx + t]
            dict.set(_letter, dict.get(_letter) + 1)

        if dict.get(letter) == 0: return False  # nie ma tego znaczka w y
        dict.set(letter, dict.get(letter) - 1) #zuzyto ta literke

    return True


runtests(tanagram)
