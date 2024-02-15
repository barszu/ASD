def b_sort(list_):
    n = len(list_)
    i = 0
    while n > 1 :
        while i < n - 1 :
            a = list_[i]
            b = list_[i+1]
            if list_[i] > list_[i+1]: 
                list_[i] , list_[i+1] = list_[i+1] , list_[i]
            i += 1
        i = 0
        n -= 1
    return list_

print(b_sort([2,5,6,9,11,5,6,7,9]))