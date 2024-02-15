def map_stack_to_sum(stack: 'stack of plates'):
    # This function changes a stack in sucha way that 'i'th element from
    # a top has a value which is a sum o beauty of all the plates above
    # this element plus a beauty of an element itself (the current plate)
    S = stack[:]
    for i in range(len(S) - 2, -1, -1):
        S[i] += S[i + 1]
    return S

        
def beautiful_supper(stacks: 'stacks of plates', P: 'number of guests'):
    n = len(stacks)
    k = len(stacks[0])
    
    # If too many guests, return -1 as it's not possible to get enough plates
    if k * n < P: return -1
    
    # Prepare an array for memoization and stacks beauty sums array
    F = [[0] * (P + 1) for _ in range(n)]
    S = [map_stack_to_sum(s) for s in stacks]
        
    # Rewrite the first stack (as if we choose only from the first stack, we will
    # get a total beauty of sum of all plates taken from this stack only)
    for j in range(1, min(P, k) + 1):
        F[0][j] = S[0][k - j]
        
    # Fill the remaining values
    for i in range(1, n):
        for j in range(1, P + 1):
            F[i][j] = F[i - 1][j]
            
            for t in range(1, min(j, k) + 1):
                F[i][j] = max(F[i][j], F[i - 1][j - t] + S[i][k - t])
    
    return F[n - 1][P], F, S


def get_plates_counts(F, S: 'mapped plates'):  # O(n^2)
    n = len(S)
    k = len(S[0])
    counts = [0] * n
    
    i = n - 1
    j = len(F[0]) - 1
    while i > 0:
        if F[i][j] != F[i - 1][j]:
            for t in range(1, k + 1):
#                 print(i, j, k - t, j - t)
#                 print('Vals', F[i][j], S[i][k - t], F[i - 1][j - t])
                if F[i][j] - S[i][k - t] == F[i - 1][j - t]:
                    counts[i] = t
                    j -= t
                    break
        i -= 1
    counts[0] = j
    
    return counts