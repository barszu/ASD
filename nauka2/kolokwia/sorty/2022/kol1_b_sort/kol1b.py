from kol1btesty import runtests

class letter_dict:

    data_len = ord('z') - ord('a') +2

    def get_pos(letter):
        return ord(letter) - ord('a')

    def __init__(self, S:str):
        self.data = [0 for _ in range(letter_dict.data_len)]

        for l in S:
            idx = letter_dict.get_pos(l)
            self.data[idx] += 1
    
    def getData(self): return self.data

    def compare(self,other):
        A = self.data
        B = other.data
        for i in range(letter_dict.data_len): #nie stabilne ale takie nie jest potrzebne
            comp = ord(A[i]) - ord(B[i])
            if comp != 0: return comp
        return 0





def radix_sort(Arr,lenth): #przechowuje obiekty tego typu
    n = len(Arr)
    for pos in reversed(range(lenth)):
        count_on_pos = [small_arr[pos] for small_arr in Arr]
        cnt_Arr = [[] for _ in range(max(count_on_pos)+1)] #cnt_Arr[number] -> [obj,obj]
        for small_arr in Arr:
            cnt_Arr[small_arr[pos]].append(small_arr)
        res = []
        for bucket_list in cnt_Arr:
            res.extend(bucket_list)
        Arr = res
    return Arr







def f(T):
    # tu prosze wpisac wlasna implementacje
    T = [letter_dict(s).getData() for s in T]
    # T.sort(key=lambda x: x.getData())
    # print([x.getData() for x in T])
    T = radix_sort(T,letter_dict.data_len)
    # for t in T:
    #     print(t)

    l = 0
    r = 0
    best_seq_len = 1
    for i,_ in enumerate(T):
        if T[i] == T[l]:
            r += 1
        else:
            best_seq_len = max(best_seq_len , r-l)
            l = r
            r += 1
    best_seq_len = max(best_seq_len , r-l)
    return best_seq_len

    return 0


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
