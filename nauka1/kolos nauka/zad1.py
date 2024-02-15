class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
def pop(prev,a):
    prev.next = a.next
    return a.val

def bucket_sort(head):
    a = head.next
    prev = head
    tab = [ Node(None) for _ in range(10)]
    ind = [tab[i] for i in range(10)]
    while a is not None: