"""
Mamy n zolnierzy porzadkujemy ich malejaco chcemy wiedziecjacy znajduja sie od p do q
"""
def qSelect(nums,k): #k th- largest el , k>= 1
    # k = len(nums)-k
    
    def qsel_helper(l,r):
        pivot, ptr = nums[r] , l #pivot right most el
        for i in range(l,r): #without pivot
            if nums[i] <= pivot:
                nums[ptr] , nums[i] = nums[i] , nums[ptr] #swap
                ptr += 1
        nums[ptr] , nums[r] = nums[r] , nums[ptr]
        if ptr > k : return qsel_helper(l,ptr-1) #qs on left
        elif ptr < k: return qsel_helper(ptr + 1,r)
        else: return nums[ptr] 
        
    return qsel_helper(0,len(nums)-1)


def selection(T,p,q): #p >= 0 , 
    #qs p+1 najwiekszego (of by one error)
    #qs q+1 najwiekszego
    a = len(T)-q-1
    b = len(T)-p-1
    qSelect(T,a)
    qSelect(T,b)
    res = T[a:b+1]
    res.sort(reverse=True)
    return res

T = [2,1,10,1000,2,-4,7,8,10,13,5,10,1,1,1,5,7]
# [-4, 1, 1, 1, 1, 2, 2, 5, 5, 7, 7, 8, 10, 10, 10, 13, 1000]
# [0,  1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 12, 13, 14, 15, 16]
print(selection(T,3,6))