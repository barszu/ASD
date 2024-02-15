text = str("""
class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def generate(self,T): #self jako start doklejania
        a = self
        for new_val in T:
            new_obj = Node(new_val)
            a.next = new_obj
            a = a.next
        return self
    
    def print_all(self,p=None):
        if p is not None : a=p
        else: a=self
        while True:
            print(a.val , end="->")
            a = a.next
            if a is None: 
                print("\n")
                return
""")
directory = input("nazwa folderu w programowanie wdi nr:")
od = int(input("od:"))
do = int(input("do:"))

for i in range(od,do+1):
    name = "./wdi {0}/zad {1}TODO.py".format(directory , i)
    fp = open(name, "x")
    fp.write(text)
    fp.close()

print("done")