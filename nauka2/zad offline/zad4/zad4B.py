from zad4testy import runtests
from collections import deque

def create_graph(L): #O(E)
  vertex_no = max([v for u,v,p in L]) + 1 # zawsze v > u
  G = [ [] for _ in range(vertex_no) ]
  for u,v,p in L:
    G[u].append((v,p))
    G[v].append((u,p))
  return G

def bfs(G,n,x,y,l,h):
  visited = [False] * n
  Q = deque()
  Q.append(x)

  while Q:
    u = Q.popleft() 
    if visited[u]: continue
    if u == y: return True
    for v,p in G[u]: 
      if l <= p <= h:
        Q.append(v)
    visited[u] = True
  return False

def get_lower_bound(G,x,t):
  #   x => x-2k |x+2k 
  # pobierz zakresy tylko z sasiadow i zmerguj to w unikalne zakresy -> mergowanie interwalow
  non_overlaping = []
  intervals = [( p - 2*t , p) for v,p in G[x]]
  intervals.sort()
  for l,r in intervals:
    if not non_overlaping:
      non_overlaping.append((l,r))
      continue
    last_l , last_r = non_overlaping[-1]
    if l <= last_r: #zaczyna sie wczesniej niz poprzedni sie konczy
      non_overlaping[-1] = (last_l, max(last_r,r)) #merge
    else:
      non_overlaping.append((l,r))

  res = [] #zdobadz wszystkie liczby z przedzialow
  for l,r in non_overlaping:
    num = l
    while num <= r:
      res.append(num)
      num += 1
  return res
  

def Flight(L,x,y,t): #O(kV+E)
  G = create_graph(L)
  n = len(G)

  for l in get_lower_bound(G,x,t):
    # czy w oknie mozliwego pulapu dotrzemy z x do y
    if bfs(G,n,x,y,l,l+2*t):
      return True
  
  return False

runtests( Flight, all_tests = True )

# my test
L = [(0,1,50),(1,2,50),(0,3,20),(3,4,10),(4,2,20),(2,5,10)]
t = 5
x = 0
y = 5
print(Flight(L,x,y,t)) #true
