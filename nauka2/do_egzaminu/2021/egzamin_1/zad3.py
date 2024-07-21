from zad3testy import runtests


def kintersect(A, k):
    """
    Function to find the k intersecting spans in a list of spans.

    Parameters:
    A (list): A list of tuples, where each tuple represents a span with a start and end point.
    k (int): The number of intersecting spans to find.

    Returns:
    list: A list of indices in A that represent the k intersecting spans with the longest length.
    """

    n = len(A)
    longest = 0
    res_spans = []

    if k == 1:
        # If k is 1, find the longest span
        for i in range(n):
            if A[i][1] - A[i][0] > longest:
                longest = A[i][1] - A[i][0]
                res_spans = [i]
    else:
        # If k is more than 1, find the k intersecting spans with the longest length
        for i in range(n):
            A[i] = A[i], i
        A.sort(key=lambda tup: tup[0][1], reverse=True)
        # sortowanie po koncach tak aby patrzec na przedzialy od konca

        for i in range(n):
            spans = [A[i][1]] #idx przedzialu i, reset przy kazdym elemencie
            for j in range(n):
                # jesli to ten sam przedzial lub przedzial j zaczyna sie pozniej niz i to kontynuuj
                if i == j or A[j][0][0] > A[i][0][0]: continue
                spans.append(A[j][1]) #dodaj przedzial j (nachodzi na i-ty)
                if len(spans) == k: break #mamy juz k przedzialow

            if len(spans) < k: continue #nie dozbieralismy k przedzialow

            length = min(A[i][0][1], A[j][0][1]) - A[i][0][0]
            if length > longest:
                longest = length
                res_spans = spans

    return res_spans


runtests(kintersect)
