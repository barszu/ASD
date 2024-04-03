from zad2testy import runtests

def partition(arr, l, r):
      
    x = arr[r]
    i = l
    for j in range(l, r):
          
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
  
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
  
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)
  
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
  
        # If position is more, recur 
        # for left subarray 
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
  
        # Else recur for right subarray 
        return kthSmallest(arr, index + 1, r, k - index + l - 1)


def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    suma=0
    for i in range(0,n-p):
        taby=T[i:i+p]
        # szukanie k el najwiekszego w malej tablicy
        # print(n-k)
        q=len(taby)-k+1
        suma += kthSmallest(taby,0,len(taby)-1,q)
    i=n-p
    taby=T[i::]
    q=len(taby)-k+1
    suma += kthSmallest(taby,0,len(taby)-1,q)
    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
