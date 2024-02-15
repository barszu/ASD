from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None

#max_val
def go_right(node:Node) -> Node: #priorytet chodzenia do prawej krawedzi
  temp = node
  while temp:
    if not temp.right: return temp #last one
    temp = temp.right
  return None

#min_val
def go_left(node:Node) -> Node: #only go left -> for > side
  temp = node
  while temp:
    if not temp.left: return temp #last one
    temp = temp.left
  return None


def node_prev(node:Node) -> Node:
  if node.left: return go_right(node.left)
  #jezeli lewy nie istnieje
  parent = node.parent
  while parent: #pojscie w gore bo drzewo krzywe
    if node != parent.left: break
    node = parent
    parent = node.parent
  return parent

def node_next(node:Node) -> Node:
  if node.right: return go_left(node.right)
  #jezeli prawy nie istnieje
  parent = node.parent
  while parent: #pojscie w gore bo drzewo krzywe
    if node != parent.right: break
    node = parent
    parent = node.parent
  return parent



def sol(root, T):
    #sposob naiwny -> dla kazdego el z T patrzec czy bezposrednio na lewo od niego wartosc z besposrednio na prawo (w ulozeniu jako posortowana lista) 
    # da ten el jako srednio arytmetyczna
    # SOLUTION - to samo ale uzywam struktury drzewa BST
    res = 0
    INF = float('inf')
    for u in T:
      nei_left = node_prev(u) #real neibour of u.val
      nei_right = node_next(u)
      if (not nei_left) or (not nei_right): continue
      if (nei_left.key + nei_right.key) == 2*u.key: 
        res += u.key
        
    return res
    
runtests(sol, all_tests = True)