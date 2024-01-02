class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class SLL:
    def __init__(self) -> None:
        self.head=None
    def print(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref
    def add_beg(self,data):
        new__node=Node(data)
        new__node.ref=self.head
        self.head=new__node
    def add_end(self,data):
        new__node=Node(data)
        if self.head is None:
            self.head=new__node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new__node
    def add_after(self,d,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("Node is not present")
        else:
            new_node=Node(d)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,d,x):
        if self.head is None:
            print("Empty")
            return 
        if self.head.ref.data==x:
            new=Node(d)
            new=self.head
            self.head=new.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("Node not found")
        else:
            new=Node(d)
            new.ref=n.ref
            n.ref=new

    def insert_empty(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            print("Not Empty")
    def delete_beg(self):
        if self.head is None:
            print("Linked is Empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("Empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_by_value(self,x):
        if self.head is None:
            print("Empty")
            return 
        if self.head.data==x:
            self.head=self.head.ref
            
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            n.ref=n.ref.ref
a=SLL()
a.head=Node(2)
a1=Node(3)
a2=Node(4)
a.head.ref=a1
a1.ref=a2
a.print()
print(a.head.ref)
print(a1.ref)
print(a2.ref)
a.add_beg(5)
a.print()
print("\n")
a.add_end(7)
a.print()
a.add_after(44,3)
print("\n")
a.print()
a.add_before(200,44)
print("\n")
a.print()
a.delete_beg()
print("\n")
a.print()
a.delete_end()
print("\n")
a.print()
a.delete_by_value(200)
print("\n")
a.print()