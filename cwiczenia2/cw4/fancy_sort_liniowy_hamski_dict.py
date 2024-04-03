# len(A) = n , el ze zbioru B gdzie len(B) = log(n)
# sortnij to szybko

# counting sort na bucketach, buckety pojedyncze liczby
# O(n + log n )

def solve(A,B):
    cnt_dict = {b : 0 for b in B} # len = log(n)
    for a in A:
        cnt_dict[a] += 1
    cnt_dict = [(k,v) for k,v in cnt_dict.items() if v > 0]
    result = []
    for k,v in cnt_dict:
        result += [k]*v
    return result

# mozna pozbyc sie slownika sortujac B, wtedy binsearchujac el jego index to bedzie hasz ze slowika
# -> znalezienie hasha (indexu) to  O(log (log n))
# i wtedy dict[idx] = value , B[idx] = key

def binsearch(a,x,lo=0,hi=None): #binsearch right
    if hi == None: hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x == a[mid]: 
            return mid
        elif x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

class Num_cnt_dict:
    def __init__(self, keys , defaul_value = 0):
        # klucz czym kolwiek ale musi dzialac > < ==
        # default value jakiegolwiek
        self.keys_list = keys
        self.keys_list.sort()
        m = len(self.keys_list)
        self.values_list = [defaul_value for _ in range(m)]
    
    def __getitem__(self, key): #O(log m )
        idx = binsearch(self.keys_list, key)
        if (self.keys_list[idx] != key):
            raise ValueError("Key not in dict")
        return self.values_list[idx]
    
    def __setitem__(self, key, value): #O(log m)
        idx = binsearch(self.keys_list, key)
        if (self.keys_list[idx] != key):
            raise ValueError("Key not in dict")
        self.values_list[idx] = value
    
    def __repr__(self):
        return str(list(zip(self.keys_list, self.values_list , [i for i in range(len(self.keys_list))])))

l = [1,10,2,1000,3,50]
d = Num_cnt_dict(l)
print(d)
d[1] = 100
d[10] = 200
d[2] = 300
d[1000] = 400
d[3] = 500
d[50] = 600
print(d)