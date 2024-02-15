from zad11ktesty import runtests

"""
jestem na i-tym el i decyduje na jaki poklad , p1 , p2 zapchania pokladow
mozna p2 = sum[0:i] - p1
f(i,p1,p2) = min( f(i+1 , p1+T[i] ,p2 ) , f(i+1,p1,p2+T[i]) )
if i == n: #wykorzystano juz wszystkie el
-> abs(p1-p2)

"""

def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację

    return 0

runtests ( kontenerowiec )
    