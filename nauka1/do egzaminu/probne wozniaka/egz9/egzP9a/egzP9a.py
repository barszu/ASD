from egzP9atesty import runtests
from math import isqrt

def UPDATE(T,idx,val):
    T.set(idx,val+T.get(idx))

def GETSUM(T,a,b):
    res = 0
    for i in range(a,b+1):
        res += T.get(i)
    return res

def ASD(T, buffer_len, Q, n):
    part_len = isqrt(n)
    part_no = n// part_len if n % part_len == 0 else (n// part_len) + 1
    
    starts = [i*part_len for i in range(part_no)] #starts[i] -> real idx in T
    slices_sum = [0 for i in range(part_no)]
    for i in range(part_no-1):
        a = starts[i]
        b = starts[i+1]-1
        slices_sum[i] = GETSUM(T,a,b)
    slices_sum[-1] = GETSUM(T,starts[-1],n-1)
    
    global_sum = 0
    for (task_type,p,q) in Q:
        if task_type == 0: #add
            UPDATE(T,p,q)
            #update przedzialu
            idx = p//part_len
            slices_sum[idx] += q
        else: #getsum
            suma = 0
            ptr = p
            while ptr <= q:
                if ptr%part_len == 0 and ptr + part_len <= q :
                    #uzyj z cache
                    suma += slices_sum[ptr//part_len]
                    ptr = ptr+part_len
                else:
                    # recznie licz
                    suma += T.get(ptr)
                    ptr += 1
            global_sum += suma
    return global_sum

class Node:
    def __init__(self, start, end):
        #node'y (nie liscie) zawieraja w domysle wartosci swoich dzieci np [1,2,3] -> left:[1,2], right:3 
        self.start = start #poczatek przedzialu
        self.end = end #koniec przedzialu
        self.total = 0 #suma wartosci pod wezlem (lub jego jesli dziecko)
        self.left = None
        self.right = None
        
    def __repr__(self) -> str:
        return f"idx{self.start} - idx{self.end} sum={self.total}"

def build_segment_tree(nums, start, end): 
    if start > end: 
        print("ERROR: start={} end={}".format(start,end))
        return None #blad danych podanych
    root = Node(start, end)

    if start == end: #dla lisci - konkretne liczby (total = wartosc)
        root.total = nums[start]
        return root
    # dla wezlow
    mid = (start + end) // 2
    root.left = build_segment_tree(nums, start, mid) #rekurencyjne zejscie w dol z kawalkiem tablicy
    root.right = build_segment_tree(nums, mid + 1, end)
    root.total = root.left.total + root.right.total #suma spod wezlow
    return root

def update_segment_tree(node, index, val): #node -> root
    #zmien wartosc node pod idx na val
    if node.start == node.end: #jest dzieckiem
        node.total = val
        return

    mid = (node.start + node.end) // 2
    if index <= mid: update_segment_tree(node.left, index, val)
    else: update_segment_tree(node.right, index, val)

    node.total = node.left.total + node.right.total

def get_total(node, left, right): #node -> root
    if node.start == left and node.end == right: #nie zaglebiaj sie albo juz to dziecko
        return node.total

    mid = (node.start + node.end) // 2
    if right <= mid: #wejdz w lewo
        return get_total(node.left, left, right)
    elif left > mid: #wejdz w prawo
        return get_total(node.right, left, right)
    else: #(utnij) chodzenie
        return get_total(node.left, left, mid) + get_total(node.right, mid + 1, right)

def add_node(root, new_start, new_end, new_value):
    if new_end < root.start or new_start > root.end:
        return

    if root.start == root.end:
        root.total += new_value
        return

    mid = (root.start + root.end) // 2
    if new_start <= mid:
        add_node(root.left, new_start, min(mid, new_end), new_value)
    if new_end > mid:
        add_node(root.right, max(mid + 1, new_start), new_end, new_value)

    root.total = root.left.total + root.right.total
    
def remove_node(root, index):
    if root.start == root.end:
        root.total = 0
        return

    mid = (root.start + root.end) // 2
    if index <= mid: remove_node(root.left, index)
    else: remove_node(root.right, index)

    root.total = root.left.total + root.right.total

# from egzP9atesty import Array

def ASD_drzewa_przedzialowe(T, buffer_len, Q, n):
    T = T.get_my_tab_now()
    root = build_segment_tree(T,0,n-1)
    global_sum = 0
    for (task_type,p,q) in Q:
        if task_type == 0: #add
            T[p] += q
            update_segment_tree(root,p,T[p])
        else: #getsum
            global_sum += get_total(root,p,q)
    return global_sum



#Podpowiedź. Format zadania jest dość nietypowy (także ze względu na sposób działania testów),
#w takiej formie żadne zadanie raczej nie powinno się pojawić na egzaminie. Zadanie ma na celu
#sprawdzenie zrozumienia struktury #### Drzewa Przedziałowego ####

# runtests(ASD, all_tests = True)
runtests(ASD_drzewa_przedzialowe, all_tests = True)
