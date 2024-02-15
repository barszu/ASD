from egzP6atesty import runtests 

"""
SOLUTION: QSeleck s-najwiekszego, str -> (len(str),letters_no,str_name)
"""
def cnt_letters(s:str) -> int:
    letters_cnt = 0
    for c in s:
        if c.isalpha(): letters_cnt +=1
    return letters_cnt

def qSelect(nums,k): #k th- largest el , k>= 1
    k = len(nums)-k
    
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
        

def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    # Data = [(len(word),cnt_letters(word),word) for word in H]
    # return qSelect(Data,s)[2]
    Data = [(len(word),cnt_letters(word),i) for i,word in enumerate(H)]
    return H[qSelect(Data,s)[2]]


runtests ( google, all_tests=True )