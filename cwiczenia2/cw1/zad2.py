# mamy posortowana tablice , chcemy znalezc x takie ze diff(arr[i] , arr[j]) = x

#mozna leciec oknem[i,j] i obserowac status tego diff -> O(n)
# jak za duzy to ukracac okno z lewej
# jak za maly to wydluzac okno z prawej

def find_idx(arr,x):
    n = len(arr)
    i = 0
    j = 0
    while j < n:
        if arr[j] - arr[i] == x:
            return (i,j)
        elif arr[j] - arr[i] < x:
            j += 1
        else:
            i += 1
    return None