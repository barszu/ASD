# zad 1
# zwraca pare min max dla n elem tablicy mamay 3/2 n porownan

def min_max(arr):
    i = 1
    max = arr[0]
    min = arr[0]
    while i < len(arr):
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        #w trakcie polowicznego sortu z bubble sort, sprawdzam czy el sa min lub max wiem bo juz te dwa swapnalem zeby bylo dobrze
        if arr[i] > max:
            max = arr[i]
        if arr[i+1] < min:
            min = arr[i+1]
