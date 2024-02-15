from egzP6btesty import runtests 

def jump ( M ):
    #tutaj proszę wpisać własną implementację
    moves = {'LU':(-1,-2) , 'UL':(-2,-1) , 'UR':(-2,1), 'RU':(-1,2) ,
             'RD':(1,2) , 'DR':(2,1), 'DL':(2,-1) , 'LD':(1,-2)} #(+ROWS , +COLS)
    trigered = set()
    curr = (0,0)
    trigered.add(curr)
    for m in M:
        dx , dy = moves[m]
        x , y = curr
        
        curr = (x+dx,y+dy)
        if curr in trigered: #lever on
            trigered.remove(curr) #lever off
        else:
            trigered.add(curr)
    return len(trigered)
    
runtests(jump, all_tests = True)