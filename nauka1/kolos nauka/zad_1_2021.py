def trs_2d_to_1d(arr_2d,N):
    T=[]
    for row in arr_2d:
        T += row
    return T   

def insert_greater(arr_2d,data,N,k):
    for i in range(0,N):
        for j in range(i+1,N):
            arr_2d[i] [j] = data[k]
            k+=1
    return k

def insert_lesser(arr_2d,data,N,k):
    for j in range(0,N-1):
        for i in range(1+j,N):
            arr_2d[i] [j] = data[k]
            k+=1
    return k

def insert_middle(arr_2d,data,N,k):
    for i in range(0,N):
        arr_2d[i] [i] = data[k]
        k+=1
    return k
        
 

def main(arr_2d):
    N=len(arr_2d)
    T=trs_2d_to_1d(arr_2d,N)
    T.sort()
    T=T[::-1]
    print(T)
    k=insert_greater(arr_2d,T,N,0)
    k=insert_middle(arr_2d,T,N,k)
    k=insert_lesser(arr_2d,T,N,k)
    return

T=[[2,3,5],
   [7,11,13],
   [17,19,23]]

main(T)
print(T)
    
    