from zad3testy import runtests

def intersection(A:tuple,B:tuple): #intersection with None -> all interval
  if A is None:
    return B
  if B is None:
    return A
  # if A is None or B is None: return None
  if A>B: A , B = B , A
  x , y = A
  a , b = B
  if a > y : #krance twardo sie zaliczaja
    return None
  return (max(a,x),min(y,b))

def interval_len(A:tuple):
  if A is None: return -1
  a , b = A
  return b-a +1


def my_deep_copy(L:list) -> list:
  return [p for p in L]

# runtests( kintersect )

def kintersect2(A, k): #naiwny sposob 2 petle ze wrzucaniem do wora, sort po koncach (duze->male) -> ide od prawej do lewej
    interval = [(i, A[i][0], A[i][1]) for i in range(len(A))]
    interval.sort(key=lambda x: x[2], reverse=True)
    max_length = 0
    if k == 1:
        result = [0]
        for i in range(len(A)):
            if interval[i][2] - interval[i][1] > max_length:
                max_length = interval[i][2] - interval[i][1]
                result[0] = interval[i][0]
        return result
    result = []
    for i in range(len(A)):
        current = [interval[i][0]]
        for j in range(len(A)):
            if i != j and interval[j][1] <= interval[i][1] < interval[j][2]:
                current.append(interval[j][0])
                if len(current) == k:
                    actual_length = min(interval[j][2] - interval[i][1], interval[i][2] - interval[i][1])
                    if actual_length > max_length:
                        max_length = actual_length
                        result.clear()
                        result = [current[i] for i in range(k)]
                    break
    return result

# runtests( kintersect2 )

def kintersect3(A,K):
  n = len(A) #real len
  INF = float('inf')
  A = [ (krotki , real_idx) for real_idx , krotki in enumerate(A)]
  A.sort(key=lambda x: x[0][1] , reverse=True)
  #patrze sie od prawa do lewa
  DP = [[-1 for j in range(K+1)] for i in range(n)]
  
  def intersect(A:tuple,B:tuple):
    if A is None or B is None: return None
    if A>B: A , B = B , A
    x , y = A
    a , b = B
    if a > y : #krance twardo sie zaliczaja
      return None
    return (max(a,x),min(y,b))
    
  
  def dfs(i,k):
    if DP[i][k] != -1: return DP[i][k]
    if k==1:
      DP[i][k] = A[i][0] #A[i]
      return DP[i][k]
    if i < k-1:
      DP[i][k] = None
      return DP[i][k]
    
    max_inter_len = -1
    best_inter = None
    for j in range(0,i):
      intr = intersect(dfs(j,k-1) , A[i][0])
      if interval_len(intr) > max_inter_len :
        max_inter_len = interval_len(intr)
        best_inter = intr
    
    DP[i][k] = best_inter
    return DP[i][k]
  
  for i in (range(n)):
    dfs(i,K)
  
  max_inter_len = -1
  best_inter = None
  for i in range(n):
    intr = DP[i][K]
    if intr == -1: continue
    if interval_len(intr) > max_inter_len :
        max_inter_len = interval_len(intr)
        best_inter = intr
  
  res = []
  for (x,y),idx in A:
    if intersect((x,y),best_inter) == best_inter:
      res.append(idx)
      if len(res) == K: break
    
  return res

# A = [(0, 4), (1, 10), (6, 7), (2, 8)]
# k = 3 #-2
A = [(100, 100), (95, 105), (90, 110), (85, 115), (80, 120), (75, 125), (70, 130), (65, 135), (60, 140), (55, 145), (50, 150), (45, 155), (40, 160), (35, 165), (30, 170)]
k = 14 #-10

runtests( kintersect3 )
# print(kintersect3(A,k))