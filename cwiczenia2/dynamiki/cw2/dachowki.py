"""
mamy zbior liczb od x1 do xn

prubujemy polozyc na tym dachowki o szerokosci 1
ile najmniej dachowek mozna polozyc aby to przykrylo

"""

"""
Solution:

dobudowywujemy dachowki od lewej do prawej ile sie da tak aby przykryc wszystkie budynki
"""

def solution(A: [float]) -> int :
    A.sort()

    slabs_no: int = 0
    max_range: float = A[0] + 1
    for i in range(1, len(A)):
        if A[i] > max_range:
            max_range = A[i] + 1
            slabs_no += 1
    return slabs_no

