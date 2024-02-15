from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def knapsack(tab,max_cap):
  # tab -> (val,mass)
  # f(i,S) = max( val[i] + f(i+1,S+mass[i]) , f(i+1,S) )
  n = len(tab)
  DP = [[0 for j in range(max_cap+1)] for i in range(n)]
  
  for i in range(n-1,-1,-1):
    for s in range(max_cap , -1 ,-1):      
      take = 0
      val , mass = tab[i]
      if s+tab[i][1] <= max_cap :
        take = val
        take += DP[i+1][s+mass] if i+1 < n else 0
        
      not_take = DP[i+1][s] if i+1 < n else 0 
      DP[i][s] = max(take,not_take)
  
  return DP[0][0]



def wybory(T:[Node]):
    #tutaj proszę wpisać własną implementację
    # knapsack take/not take -> jezeli tura wyborow sie skonczyla -> ll -> node , przejdz do kolejnego knapsacka
    res = 0
    for starting_node in T:
      fundusz = starting_node.fundusze
      #make list from ll
      tab = []
      node = starting_node
      while node:
        tab.append((node.wyborcy , node.koszt))
        node = node.next
        
      res += knapsack(tab,fundusz) 
    return res

runtests(wybory, all_tests = True)