def interval_len(A:tuple):
  if A is None: return -1
  a , b = A
  return b-a +1

def intersect(A:tuple,B:tuple):
    if A is None or B is None: return None
    if A>B: A , B = B , A
    x , y = A
    a , b = B
    if a > y : #krance twardo sie zaliczaja
      return None
    return (max(a,x),min(y,b))

def kintersect3(A,K):
  n = len(A) #real len
  INF = float('inf')
  A = [ (krotki , real_idx) for real_idx , krotki in enumerate(A)]
  A.sort(key=lambda x: x[0][1] , reverse=True)
  #patrze sie od prawa do lewa
  DP = [[-1 for j in range(K+1)] for i in range(n)]
  
  def dfs(i,k): 
      #najdluzszy ptrzedzial z [0:i] bedac w i , i mam k do wybrania
      # i jest napewno brany
    if DP[i][k] != -1: return DP[i][k]
    if k==1: #kategorycznie musze go wziac
      DP[i][k] = A[i][0] #A[i]
      return DP[i][k]
    if i < k-1: #za malo ich bedzie
      DP[i][k] = None
      return DP[i][k]
    
    # znajdz najlepszy
    max_inter_len = -1
    best_inter = None
    for j in range(0,i): #szukaj z [0:i]
      intr = intersect(dfs(j,k-1) , A[i][0])
      if interval_len(intr) > max_inter_len :
        max_inter_len = interval_len(intr)
        best_inter = intr
    
    DP[i][k] = best_inter
    return DP[i][k]
  
  for i in (range(n)): 
    dfs(i,K)
    
  #znajdz najlepszy w DP
  max_inter_len = -1
  best_inter = None
  for i in range(n):
    intr = DP[i][K]
    if intr == -1: continue
    if interval_len(intr) > max_inter_len :
        max_inter_len = interval_len(intr)
        best_inter = intr
  #porownuj go ze wszystkimi i znajdz zbior tych co sie z nim przecinaja
  res = []
  for (x,y),idx in A:
    if intersect((x,y),best_inter) == best_inter:
      res.append(idx)
      if len(res) == K: break
    
  return res