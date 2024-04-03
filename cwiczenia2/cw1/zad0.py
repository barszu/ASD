def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: #then swap
                arr[j], arr[j+1] = arr[j+1], arr[j]


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.isGuard = False

    def bubble_sort(self):
        if not self.isGuard: 
            raise ValueError("This is not a guard node!")
        prev = self
        curr = prev.next
        next = curr.next
        while curr:
            if curr.val > next.val: #swap
                prev.next = next
                next.next = curr
                curr.next = next.next

        prev = prev.next
        curr = curr.next
        next = next.next

#stabilne sortowanie - nie zmienia kolejnosci elementow o takiej samej "wartosci"
# wezmy liczby , niech cmp robi %10 zanim poronwuje i wteyd bedzie widac