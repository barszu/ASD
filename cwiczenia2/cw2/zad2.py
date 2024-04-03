"""
zwroc liczbe par indeksow takich ze i<j i A[i] > A[j]
(po polsku ile jest sytuacji ze trzeba przestawic elementy)

-> naiwne n^2
-> n log n uzyc merge sort
licze inwersje jako suma inwersji z dzieci i z tego tez poziomu (merge sort)
czyli dla poziomu 1 po tym jak kawalki sie juz posortowaly, iwersjami sa (1,3) , (1,4)

        3  4  8  1  5

        l m   m+1  r
        3 4    1 5 8 
        i      j


"""
def merge(T , l , m , r):
    wynik = 0
    left_slice = T[l:m+1]
    right_slice = T[m+1:r+1]

    i , j =  l , m+1
    k = l #strikte do sortowania aby sledzic gdzie w T wrzucic liczbe (nie tak znaczace)
    while i < m+1 and j < r+1:
        if left_slice[i] > right_slice[j]:
            wynik += len(left_slice) - i
            T[k] = right_slice[j]
            j += 1
            k += 1
        else:
            T[k] = left_slice[i]
            i += 1
            k += 1
    return wynik



# def count_inversion(A:list[int]):
#     A_copy = [(a,i) for i,a in enumerate(A)]
#     A_copy.sort(key=lambda x: x[0])
#     #SUM for all (idx - i)  
#     print(A_copy)

# count_inversion([1,3,5,2,4,6]) # 3
# print([(a,i) for i,a in enumerate([1,3,5,2,4,6])])

