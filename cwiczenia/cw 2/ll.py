class Node:
    def __init__(self,val):
        self.next=None
        self.val=val

#wstawianie do posortowanej listy el
#wyciaganie max z nieposortowanej listy
#sortowanie przez wstawianie 

def extract_max(L):
    M=L
    while L.next != None:
        if L.next.val>M.next.val:
            M = L
        R = M.next
        M.next = R.next
        R.next = None
        return R

def insert(head,node):
    while head.next.val < node.val and head.next != None:
        head=head.next
    node.next=head.next
    head.next=Node

def insertion_sort(head):
    A = Node(None)
    while head.next:
        temp=head.next
        head.next=temp.next
    
        
        
    
        
    