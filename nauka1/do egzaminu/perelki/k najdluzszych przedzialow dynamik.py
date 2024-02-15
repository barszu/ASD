def interval_len(A:tuple):
  if A is None: return -1
  a , b = A
  return b-a +1

def znajdz_k_najdluszych_przedzialow(przedzialy, k):
    Data = [ (p,i) for i,p in enumerate(przedzialy)]
    Data.sort()
    przedzialy = [p for p,i in Data]
    
    n = len(przedzialy)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    SubCache = [[ [] for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            bez_i = dp[i - 1][j]
            z_i = dp[i - 1][j - 1] + interval_len(przedzialy[i-1]) #-1
           
            if z_i > bez_i:
                dp[i][j] = z_i
                SubCache[i][j] = SubCache[i-1][j-1] + [i-1]
            else:
                dp[i][j] = bez_i
                SubCache[i][j] = SubCache[i-1][j]

    res = []
    for i in SubCache[n][k]:
      res.append(Data[i][1])
    return res