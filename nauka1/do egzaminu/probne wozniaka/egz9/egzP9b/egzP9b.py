from egzP9btesty import runtests

def find_euler_cycle_non_rek(G):
    n = len(G)
    cycle = []
    stack = [0]
    
    while stack:
        u = stack[-1]
        if len(G[u]) > 0:
            v = G[u].pop()
            stack.append(v)
        else:
            cycle.append(u)
            stack.pop()
            
    return cycle[::-1]
    

def dyrektor( G:list, R:list ):
    #Tutaj proszę wpisać własną implementację 
    n = len(G)
    for u in range(n):
        for v in R[u]:
            G[u].remove(v)
    
    # cycle = find_euler_cycle_ls(G)
    cycle = find_euler_cycle_non_rek(G)

    return cycle
	
runtests(dyrektor, all_tests=True)
