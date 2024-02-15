def select_buildings(T,p):
    cache = [[None for j in range(p+1)] for i in range(len(T))]
    Tab = [(h*(b-a) , a , b , w , i) for i , (h,a,b,w) in enumerate(T)] #(s,a,b,k,idx_real)
    Tab.sort(key = lambda x: x[1]) #po poczatkach
    INF = float('inf')
    good = []
    res = [None for i in range(p+1)]
    
    def dfs(i,cost,good): #-> s
        if i >= len(T) or cost > p : return 0
        if cache[i][cost]: return cache[i][cost]
        # take i-th -> check colision -> # poczatek dodawanego jest po lewej stronie od konca dobrego
        take = 0
        s , a , b , k , i = Tab[i]
        added = False

        if len(good) == 0 and k+cost <= p :
            good.append(Tab[i])
            added = True
            take = s + dfs(i+1,cost+k,good)
        elif len(good)>0 and k+cost <= p and not a < good[-1][2]:#no colision, sum_cost <= k
            good.append(Tab[i])
            added = True
            take = s + dfs(i+1,cost+k,good)
            
        not_take_good = good[:len(good)-1]
        not_take = dfs(i+1,cost,not_take_good)
        
        
        cache[i][cost] = max( not_take , take )
        if i == 0:
            if take > not_take:
                # good.append(Tab[i])
                res[i] = good.copy()
                # good.pop()
            else:
                res[i] = not_take_good.copy()
        return cache[i][cost]
    
    dfs(0,0,good)
    return res[0]

def knapsack(Data,tab,max_cap):
    # tab -> (val,mass)
    # f(i,S) = max( val[i] + f(i+1,S+mass[i]) , f(i+1,S) )
    def val(i): return Data[i][2]
    def mass(i): return Data[i][3]
    n = len(tab)
    DP = [[0 for j in range(max_cap+1)] for i in range(n)]
    taken = [[ [] for j in range(max_cap+1)] for i in range(n)] #co zostalo dokladnie wziete
    
    for i in range(n-1,-1,-1):
        for s in range(max_cap , -1 ,-1):      
            take = 0
            if s+mass(i) <= max_cap : #jest jeszcze miejsce
                take = val(i)
                if i+1 < n : #in bound
                    take += DP[i+1][s+mass(i)]
                
            not_take = DP[i+1][s] if i+1 < n else 0 
            
            DP[i][s] = max(take,not_take)
            if take >= not_take:
                taken[i][s] = [i] 
                if i+1 < n and s+mass(i) <= max_cap: #in bound
                    taken[i][s] += taken[i+1][s+mass(i)]
            else:
                taken[i][s] = []
                if i+1 < n :#in bound
                    taken[i][s] += taken[i+1][s]
  
    return DP[0][0] , taken[0][0]

def select_buildings2(T,p):
    I = [(a , b , h*(b-a) , w ,i) for i,(h,a,b,w) in enumerate(T)] # (start,end,value,cost,org_idx)
    I.sort()
    n = len(I)
    matching_list = [[i] for i in range(n)] #by sorted idx
    for i in range(n):
        x , y , *_  = I[i]
        for j in range(i+1,n):
            a , b , *__ = I[j]
            #no colision -> add both to adjecty list
            if not a<= y: #no colision
                matching_list[i].append(j)
                matching_list[j].append(i)
    
    # dla kazdej grupy nie kolidujacej wewnetrznie knapsack(val,mass)
    max_from_groups = -1
    best_buildings = [] #dla idx w posortowanej tablicy
    for group in matching_list:
        students , buildings = knapsack(I,group,p)
        if students > max_from_groups :
            max_from_groups = students 
            best_buildings = buildings.copy()
    
    res = [I[idx][4] for idx in best_buildings]
    res.sort()
    return res

data = [(2,1,5,3),(3,7,9,2),(2,8,11,1)]
p = 5

# data = [(1,1,8,100),(1,2,11,50),(1,9,11,2),(1,9,10,1),(1,10,11,1),(1,12,18,1000)]
# p = 160



print(select_buildings2(data , p))
        
        
        
        
        
        
        
        