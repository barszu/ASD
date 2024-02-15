class Node: #DZIALA
    # WSZYSTKIE OPERACJE NA IDX NIE NA LICZBACH!!!
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
    #nums[index] = val
    
    #zmien wartosc node pod idx na val
    # JAK CHCESZ ROBIJC += TO CACHE'UJ W TABLICY A POZNIEJ UPDATETUJ
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
    
def update_range(root, start, end, val):
    """
    Aktualizuje wartości węzłów o indeksach od 'start' do 'end' (włącznie) na 'val'.
    """
    if start > end:
        return

    # Jeśli przedział węzła jest całkowicie zawarty w [start, end], to aktualizujemy cały węzeł.
    if root.start >= start and root.end <= end:
        root.total = val * (root.end - root.start + 1)
        return

    # W przeciwnym razie idziemy rekurencyjnie w dół drzewa.
    mid = (root.start + root.end) // 2
    if start <= mid:
        update_range(root.left, start, min(mid, end), val)
    if end > mid:
        update_range(root.right, max(mid + 1, start), end, val)

    # Po zaktualizowaniu dzieci, aktualizujemy wartość tego węzła na sumę dzieci.
    root.total = root.left.total + root.right.total

def add_to_range(root, start, end, val): #tested
    """
    Dodaje 'val' do wartości węzłów o indeksach od 'start' do 'end' (włącznie).
    """
    if start > end:
        return

    # Jeśli przedział węzła jest całkowicie zawarty w [start, end], to dodajemy 'val' do całego węzła.
    if root.start >= start and root.end <= end:
        root.total += val * (root.end - root.start + 1)
        return

    # W przeciwnym razie idziemy rekurencyjnie w dół drzewa.
    mid = (root.start + root.end) // 2
    if start <= mid:
        add_to_range(root.left, start, min(mid, end), val)
    if end > mid:
        add_to_range(root.right, max(mid + 1, start), end, val)

    # Po zaktualizowaniu dzieci, aktualizujemy wartość tego węzła na sumę dzieci.
    root.total = root.left.total + root.right.total

# _______________________________________________________________

class SegmentTree: #NIEDZIALA?
    def __init__(self, arr): #[a,b)
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 1, 0, self.n - 1)

    def build_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node, start, mid)
            self.build_tree(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node, start, mid, left, right) + self.query(2 * node + 1, mid + 1, end, left, right)

    def query_range(self, left, right):
        return self.query(1, 0, self.n - 1, left, right)
    
    def update(self, node, start, end, idx, new_val):
        if start == end:
            self.tree[node] = new_val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, new_val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, new_val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update_value(self, idx, new_val): #nums not updated!, interial yes
        self.update(1, 0, self.n - 1, idx, new_val)
        
    def update_from_to(self, node, start, end, a, b, val): #start , end idx in num
        if a > end or b < start:
            return  # Przedział (a, b) nie przecina się z zakresem tego węzła
        if a <= start and b >= end:
            self.tree[node] += val  # Zwiększ wartość węzła o val
        else:
            mid = (start + end) // 2
            self.update_from_to(2 * node, start, mid, a, b, val)
            self.update_from_to(2 * node + 1, mid + 1, end, a, b, val)
    
    def update_interval(self, a, b, val): #a,b idx in nums
        self.update_from_to(1, 0, self.n - 1, a, b, val)  # Przekazujemy przedział (a, b) i wartość 1 do aktualizacji


nums = [1, 3, 5, 7, 9, 11]
root = build_segment_tree(nums, 0, len(nums) - 1)
# update_segment_tree(root, 2, 6) #nums[2] = 6
# update_range(root,1,1,10)
add_to_range(root,1,2,10)
result = get_total(root, 1, 4)
print(result)  # Wyświetli: 24

# ST = SegmentTree(nums)
# ST.update_interval(1,4,10)
# ST.update_value(2,6)

# print(ST.query_range(0,len(nums)),ST.tree)

