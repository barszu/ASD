def intlen(a):
    from math import log10
    return int(log10(a)+1)

def int_str(num):
    #potrzebny int len
    str_ = ""
    n = intlen(num) - 1
    symbols = [str(i) for i in range(10)]
    while n >= 0:
        p = 10**n
        str_ += symbols[num//p]
        num = num%p
        n -= 1
    return str_
