def mask_gen(n , base = 2):
    # n - dlugosc masek
    # base - baza -> dla binarnej 2
    q = base**n
    maski = [[0 for _ in range(n)] for _q in range(q)]
    #num jest tez taki jak id maski w maskach
    for num in range ( 0 , q):
        id = n - 1
        a = num
        while a != 0 :
            maski[num][id] = a%base
            a //= base
            id -= 1
    return maski

print(mask_gen(3 , 2))