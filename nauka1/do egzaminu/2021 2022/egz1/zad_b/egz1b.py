from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

# def wideentall( T ):
#     # tu prosze wpisac wlasna implementacje
#     return None

def windeentall2(root):
    lvl = [] #lvl[i] -> ile jest node'ow na wysokosci i
    def DFS(node,l): #-> wysokosci
        #node.x = (l,r) #wysokosc podrzewa lewego , prawego
        if not node: return -1 #0
        if len(lvl) <= l: lvl.append(0)
        lvl[l] += 1
        left = 1 + DFS(node.left,l+1)
        right = 1+  DFS(node.right,l+1)
        node.x = (left,right)
        return max( left,right )

    DFS(root,0)
    max_dzieci = -1 #ile dzieci z tego poziomu (node'ow)
    max_poz = None #ktory poziom wybrany
    for i in range(len(lvl)-1 , -1 , -1): #wazniejsza jest szerokosc
        if lvl[i] > max_dzieci:
            max_dzieci = lvl[i]
            max_poz = i
    
    #przejdz po grafie i naprawiaj
    deleted = 0
    def DFS_repair(node,H):
        nonlocal deleted

        l , r = node.x
        if node.left:
            if (l < H) or (H==0 and l > 0): #zetnij
                deleted += 1
            else:# nie scinaj idz glebiej
                DFS_repair(node.left,H-1)
        if node.right:
            if (r < H) or (H==0 and r > 0): #zetnij
                deleted += 1
            else:# nie scinaj idz glebiej
                DFS_repair(node.right,H-1)
    
    DFS_repair(root,max_poz)
    return deleted
            
            
        
            


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( windeentall2, all_tests = True )