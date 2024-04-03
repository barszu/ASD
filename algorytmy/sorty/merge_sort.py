def merge(A,l,m,r):
    Left_Arr = A[l:m+1]
    Right_Arr = A[m+1:r+1]

    len_left_arr = len(Left_Arr)
    len_right_arr = len(Right_Arr)

    main_idx = l
    left_idx = right_idx = 0
    

    while left_idx < len_left_arr and right_idx < len_right_arr:
        if Left_Arr[left_idx] <= Right_Arr[right_idx]:
            A[main_idx] = Left_Arr[left_idx]
            left_idx += 1
            main_idx += 1
        else:
            A[main_idx] = Right_Arr[right_idx]
            right_idx += 1
            main_idx += 1
    
    while left_idx < len_left_arr:
        A[main_idx] = Left_Arr[left_idx]
        left_idx += 1
        main_idx += 1

    while right_idx < len_right_arr:
        A[main_idx] = Right_Arr[right_idx]
        right_idx += 1
        main_idx += 1

def mergeSort(A,l,r):
    if l < r:
        m = (l + r) // 2
        mergeSort(A,l,m)
        mergeSort(A,m+1,r)
        merge(A,l,m,r)




import random
A = [random.randint(1,20) for i in range(10)]
B = A.copy()

print(A)
mergeSort(A,0,len(A)-1)
# print(A == B)
print(A)
# print(B)