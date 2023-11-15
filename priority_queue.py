class pq:
    def __init__(self,k) -> None:
        self.k=k
        self.q=[]
    def enqueue(self,x):
        if len(self.q)<self.k:
            self.q.append(x)
        else:
            print("queue is full")
        self.q.sort()
    def dequeue(self):
        if len(self.q)!=0:
            self.q.pop(0)
        else:
            print("queue is empty")
    def display(self):
        print(self.q)

obj=pq(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.dequeue()
obj.display()