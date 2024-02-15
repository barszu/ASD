def najblizsze_min(T):
    stack = [-1,0]
    n = len(T)
    
    # dopisuje jakby z lewej -INF i z prawej (od tablicy) bo matma
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
    
    return left,right