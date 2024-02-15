from egzP5atesty import runtests 

def inwestor ( T ):
    # F(a,b) - min wartosc z przedzialu tablicy [a,b]
    # if a==b: -> ([3]) = nums[a]
    # min ( nums[b] , f(a,b-1) ) -> rozpocznij nowy lepszy podciag, doklej do starego
    # [a,b-1] = [1,2,3]
    # [a,b] = [1,2,3,100]
    n = len(T)
    DP = [[None for i in range(n)] for j in range(n)]
    for a in reversed(range(n)):
        for b in range(n):
            if a==b:
                DP[a][b] = T[a] 
            else:   
                DP[a][b] = min(T[b] , DP[a][b-1]) if b-1 > 0 else T[b]
            
    #calc max area
    max_area = -1
    for b in reversed(range(n)):
        for a in reversed(range(n)):
            max_area = max(max_area , DP[a][b] * (b-a+1) ) #min z tego przedzialu * dlugosc 
    
    return max_area

def inwestor2(T):
    stack = [-1,0]
    n = len(T)
    
    left = [-1 for _ in range(n)] # left[i] - idx najblizeszego mniejszego el po lewej stronie
    right = [n for _ in range(n)] #rigth[i] - -||- po prawej stronie
    
    for i in range(1,n):
        while stack[-1] != -1 and T[stack[-1]] > T[i]: #get greater from stack
            right[ stack.pop() ] = i #relax nums from stac with i
            
        if T[i] == T[i-1]: #same as real left neibour -> same left
            left[i] = left[i-1]
        else:
            left[i] = stack[-1] #from stack
        stack.append(i)
    
    #calc max area
    max_area = -1
    for i in range(n):
        max_area = max(max_area , T[i]*(right[i]-left[i]-1) ) #min z tego przedzialu * dlugosc 
    
    return max_area

def largestRectangleArea(heights: list[int]) -> int:
        stack = [] #to do (not visited fully)
        max_area = heights[0]
        # stack.append((0,heights[0])) #(idx of start of that height , height)
        n = len(heights)
        for i in range(0,n):
            start = i
            
            while len(stack) > 0 :
                last_idx , last_h = stack[-1]
                if last_h > heights[i] :
                    max_area = max(max_area , last_h*(i-last_idx))
                    start = last_idx
                    stack.pop()
                else: break
            stack.append((start,heights[i]))

        for i,h in stack: #satisfy all el in stack
            max_area = max(max_area , h*(n-i))
        return max_area

# runtests ( inwestor2, all_tests=True )
runtests(largestRectangleArea , all_tests=True)