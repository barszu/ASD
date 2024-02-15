class queue():
    def __init__(self,data_list=[]):
        self.data_list=data_list
        
    def lenth(self): #-> int {len of queue}
        return len(self.data_list)
        
    def is_empty(self): #->bool {is empty ?}
        return (self.lenth()==0)
    
    def pop(self): #-> first el in line 
        if self.is_empty(): return "kolejka jest juz pusta!"
        a = (self.data_list).pop(0)
        return a
    
    def add(self,el): #-> void {add el to queue}
        (self.data_list).append(el)
    
    def prt(self): #-> void {print all el in order firt to last}
        a=""
        for el in self.data_list:
            a += str(el)
            a += " "
        print(a)

class stack():
    def __init__(self,data_list=[]):
        self.data_list=data_list
        
    def lenth(self): #-> int {len of stack}
        return len(self.data_list)
        
    def is_empty(self): #->bool {is empty ?}
        return (self.lenth()==0)
    
    def pop(self): #-> last el in stack
        if self.is_empty(): return "stos juz jest pusty!"
        a = (self.data_list).pop(-1)
        return a
    
    def add(self,el): #-> void {add el to stack (on top)}
        (self.data_list).append(el)
    
    def prt(self): #{print all el in order firt to last}
        a=""
        for el in self.data_list:
            a += str(el)
            a += " "
        print(a)
    
    def spal(self):
        import time
        for i in range(self.lenth()):
            a=self.pop()
            print(f"{i+1})wlasnie spalil sie : {a} \nstan stosu to:")
            self.prt()
            time.sleep(2)
            print("\n")
            
