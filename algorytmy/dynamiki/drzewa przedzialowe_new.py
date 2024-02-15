class SegmentTree: 
    def __init__(self, arr): #[a,b)
        self.n = len(arr) #ilosc przedzialow nie wielkosc drzewa
        self.tree = [0] * (4 * self.n) #((self.n//2) * (self.n + 1)) #drzewo binarne w postaci tablicowej, defultowe wartosci przedzialow [i,i+1) = 0
        self.build_tree(arr, 1, 0, self.n - 1) #licze wzgl pozycji 1
        self.tree[0] = None # nie uzywam pozycji 0
    
    def __repr__(self) -> str: return str(self.tree)
    
    def get_my_tab_now(self) -> list:
        stack = [(1,0,self.n-1)] #(node,start,end)
        res = []
        while stack:
            node , start , end = stack.pop()
            if start == end: #lisc
                res.append(self.tree[node])
                continue
            # najpierw lewy pozniej prawy
            mid = (start+end) // 2
            stack.append((2*node+1,mid+1,end))
            stack.append((2*node,start,mid))
        return res
    
    def show_internal(self) -> None:
        i = 0
        lvl = 0
        while True:
            if i >= 2*self.n: break
            j = i + 2**lvl
            print(self.tree[i+1:j+1])
            i = j
            lvl += 1         

    def build_tree(self, arr, node, start, end): #start,end in bound, node - node_idx
        # przetwarzamy fragment tablicy [start:end]
        if start == end: #to jest juz lisc
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node, start, mid) #zejscie w lewo z lewa czescia tablicy, razem z midem
            self.build_tree(arr, 2 * node + 1, mid + 1, end) #zejscie w prawo z prawym kawalkiem (bez mida)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1] #dynamiczne oliczenie wartosci na podstawie dwoch
            # tutaj operacja suma, moze byc max np

    def query(self, node, start, end, left, right): #query_range helper
        # node zawiera zasieg idx [start,end] , szukamy {sumy} zasiegu [left,right]
        # left , right to orginalne idx z nums
        # start , end to idx z drzewa node'ow -> zasieg node'a
        if left > end or right < start: #no overlap [left,right] z [start,end]
            return 0
        if left <= start and right >= end: #szukany [left,right] calkowicie sie naklada i jest szerszy niz [start,end]
            return self.tree[node]
        mid = (start + end) // 2
        
        # prosta rekurencja, partial overlap
        from_left = self.query(2 * node, start, mid, left, right)
        from_right = self.query(2 * node + 1, mid + 1, end, left, right)
        
        return from_left + from_right #dzialanie suma

    def query_range(self, left, right):
        # left , right to orginalne idx z nums
        return self.query(1, 0, self.n - 1, left, right)
    
    def update(self, node, start, end, idx, new_val):
        if start == end: #to jest lisc i to ten dobry (napewno)
            self.tree[node] = new_val #wersja add jesli +=
            return
        mid = (start + end) // 2
        # zaglebiam sie tam gdzie jest potrzeba
        if idx <= mid: # idx e [start,mid]
            self.update(2 * node, start, mid, idx, new_val)
        else: # idx e [mid,end]
            self.update(2 * node + 1, mid + 1, end, idx, new_val)
            
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        # na nowo obliczam wartosci tu (dzialanie suma)

    def update_value(self, idx, new_val): #nums not updated!, interial yes
        self.update(1, 0, self.n - 1, idx, new_val)
    
    def update_shallow_from_to_add(self, node, start, end, a, b, val): #start , end idx in num
        # plytki update, nie schodzimy do najnizszych layeri ich naprawiac
        if a > end or b < start:
            return  # Przedział (a, b) nie przecina się z zakresem tego węzła
        if a <= start and b >= end:
            # [start,end] zawiera sie w [a,b]
            self.tree[node] += val  # Zwiększ wartość węzła o val (mozna i ustawiac)
            return
        
        mid = (start + end) // 2
        self.update_shallow_from_to_add(2 * node, start, mid, a, b, val)
        self.update_shallow_from_to_add(2 * node + 1, mid + 1, end, a, b, val)
            
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1] #dzialanie suma
        
    
    def update_interval_shallow_add(self, a, b, val): #a,b idx in nums
        self.update_shallow_from_to_add(1, 0, self.n - 1, a, b, val)  # Przekazujemy przedział (a, b) i wartość 1 do aktualizacji

    def update_deep_from_to_add(self, node, start, end, a, b, val):
        # gleboki update, schodzimy do najnizszych layeri ich naprawiac
        if a > end or b < start:
            return  # Przedział (a, b) nie przecina się z zakresem tego węzła
        
        if start == end: #to jest lisc i to ten dobry (napewno)
            self.tree[node] += val #wersja add jesli +=
            return
        
        mid = (start + end) // 2
        # zaglebiam sie tam gdzie jest potrzeba
        self.update_deep_from_to_add(2 * node, start, mid, a , b , val)
        self.update_deep_from_to_add(2 * node + 1, mid + 1, end, a , b, val)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        # na nowo obliczam wartosci tu (dzialanie suma)
    
    def update_interval_deep_add(self,a,b,val):
        self.update_deep_from_to_add(1,0,self.n-1,a,b,val)
    
vals = [1]*20
# real_boundaries = [-5,1,3,7,100,101,200]
Tree = SegmentTree(vals)
# Tree.query_range(0,len(vals)-1)
print(Tree.show_internal())
print(Tree.get_my_tab_now())
print("po zmianie:\n")
# Tree.update_interval_shallow_add(0,8,1000)
print(Tree.show_internal())
print(Tree.get_my_tab_now())

