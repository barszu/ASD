from zad7ktesty import runtests 

def knapsack(V,M,max_cap):
  # tab -> (val,mass)
  # f(i,S) = max( val[i] + f(i+1,S+mass[i]) , f(i+1,S) )
  n = len(V)
  DP = [[0 for j in range(max_cap+1)] for i in range(n)]
  
  for i in range(n-1,-1,-1):
    for s in range(max_cap , -1 ,-1):      
      take = 0
      val , mass = V[i] , M[i]
      if s+mass <= max_cap :
        take = val
        take += DP[i+1][s+mass] if i+1 < n else 0
        
      not_take = DP[i+1][s] if i+1 < n else 0 
      DP[i][s] = max(take,not_take)
  
  return DP[0][0]

def ogrodnik (T, D, Z, l):
    visited = [ [False for j in range(len(T[0]))] for i in range(len(T))]
    
    def look_for_tree(i): #rosnie w i
        if T[0][i] == 0: return 0
        water = 0
        stack = [(0,i)]#wiersz,kolumna w T
        while stack:
            #idx w lewo,prawo,dol
            i,j = stack.pop()
            visited[i][j] = True
            water += T[i][j]
            #go left
            if j-1 >= 0 and T[i][j-1] != 0 and not visited[i][j-1]:
                stack.append((i,j-1))
            #go right
            if j+1 < len(T[0]) and T[i][j+1] != 0 and not visited[i][j+1]:
                stack.append((i,j+1))
            #go down
            if i+1 < len(T) and T[i+1][j] != 0 and not visited[i+1][j]:
                stack.append((i+1,j))
                        
        return water
            
    Water_tab = [look_for_tree(idx) for idx in D]
    # i.val -> Z[i]
    # i.mass -> Water_tab    
    # max_mass -> l 
        
    return knapsack(Z,Water_tab,l)

runtests( ogrodnik, all_tests=True )
