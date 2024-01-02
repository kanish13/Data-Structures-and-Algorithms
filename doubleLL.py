class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.nref=None
        self.pref=None

class DLL:
    def __init__(self) -> None:
        self.head=None
    def print_forward(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.nref
    def print_backward(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            print("Not Empty")
    def insert_beg(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            new=Node(data)
            new.nref=self.head
            self.head.pref=new
            self.head=new
    def insert_end(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            new=Node(data)
            new.pref=n
            n.nref=new
    def insert_after(self,data,x):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    new=Node(data)
                    new.nref=n.nref
                    new.pref=n
                    if n.nref is not None:
                        n.nref.pref=new
                    n.nref=new
                    return
                else:
                    n=n.nref
            print("Element Not Found")
    def insert_before(self,data,x):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            n=self.head
            while n.nref is not None:
                if n.nref.data==x:
                    new=Node(data)
                    new.nref=n.nref
                    new.pref=n
                    if n.nref is not None:
                        n.nref.pref=new
                    n.nref=new
                    
                    return
                else:
                    n=n.nref
            print("Element Not Found")
    def delete_beg(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.nref
    def delete_end(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n.nref.nref is not None:
                n=n.nref
            n.nref=None
    def delete_val(self,x):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n.nref is not None:
                if n.nref.data==x:
                    n.nref=n.nref.nref
                    return
                else:
                    n=n.nref
            print("Not Found")



a=DLL()
a.head=Node(1)
a2=Node(2)
a3=Node(3)
a.head.nref=a2
a2.nref=a3
a2.pref=a.head
a3.pref=a2
a.print_forward()
print("\n")
a.print_backward()
print("\n")
a.insert_beg(100)
a.print_forward()
print("\n")
a.insert_end(200)
a.print_forward()
print("\n")
a.insert_after(32,3)
a.print_forward()
print("\n")
a.insert_before(77,3)
a.print_forward()
a.delete_beg()
print("\n")
a.print_forward()
a.delete_end()
print("\n")
a.print_forward()
a.delete_val(77)
print("\n")
a.print_forward()