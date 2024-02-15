from egz2atesty import runtests

def coal(A,T):
  n = len(A)
  cap = [T] * n
  last_visited = None
  for w in A:
      for i,c in enumerate(cap):
          if c-w >= 0 : #laduj do i-tego magazynu
            cap[i] += -w
            last_visited = i
            break
  return last_visited

import heapq
def coal2(A,T):
  last_ins = None
  to_add = 1
  MinHeap = [(0,T)]
  bin = []
  for c in A:
    # zagldam w kopiec
    i , cap = MinHeap[0]
    if cap - c > 0: 
      MinHeap[0] = (i,cap-c)
      last_ins = i
    elif cap - c == 0:
      last_ins = i
      heapq.heappop(MinHeap)
      if len(MinHeap) == 0: #dodanie nowego magazynu bo potrzeba
        MinHeap.append((to_add,T))
        to_add += 1
    else: #nie wystarcza miejsca w tym magazynie
      # i , cap = MinHeap[0]
      while MinHeap and MinHeap[0][1] - c < 0 :
        bin.append(heapq.heappop(MinHeap))
      if len(MinHeap) == 0: #dodanie nowego magazynu bo potrzeba
          MinHeap.append((to_add,T))
          to_add += 1
			
      i , cap = MinHeap[0]
      MinHeap[0] = (i,cap-c)
      if cap-c == 0:
        heapq.heappop(MinHeap)
      last_ins = i
        #nie jestem pewnien
      if len(MinHeap) == 0:
        MinHeap = bin
      elif len(MinHeap) == 1:
        bin.append(MinHeap[0])
        MinHeap = bin
      else:
        MinHeap = bin + MinHeap
      bin = []
  return last_ins



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
