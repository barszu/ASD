def joinlist(*arg):
    str_ = ""
    for i in arg:
        str_ += str(i)
    return str_

def dz(a , b , N = 20 , asstr = False):
    w = [a//b]
    #0 el to int z dzielenia reszta czesc po przecinku
    a = (a%b) * 10
    for _ in range(N):
        w.append(a//b)
        a = (a%b) * 10
    if asstr :
        return (str(w[0]) + "," + joinlist(*w[1:]))
    return w

print(dz(99 , 7 , 100 ))