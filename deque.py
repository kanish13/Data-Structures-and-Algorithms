class dq:
    def __init__(self,k) -> None:
        self.k=k
        self.q=[None]*k
        self.front=self.rear=-1
    def fronten(self,x):
        if (self.front==0 and self.rear==self.k-1) or (self.front==self.rear+1):
            print("FULL")
        elif (self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=0
            self.q[self.front]=x
        elif self.front==0:
            self.front=self.k-1
            self.q[self.front]=x
        else:
            self.front=self.front-1
            self.q[self.front]=x
    def rearen(self,x):
        if (self.front==0 and self.rear==self.k-1) or (self.front==self.rear+1):
            print("FULL")
        elif (self.front==-1 and self.rear==-1):
            self.front=self.rear=0
            self.q[self.front]=x
        elif self.rear==self.k-1:
            self.rear=0
            self.q[self.rear]=x
        else:
            self.rear=self.rear+1
            self.q[self.rear]=x
    def frontde(self):
        if (self.front==-1 and self.rear==-1):
            print("EMPTY")
        elif self.front==self.rear:
            self.front=self.rear=-1
        elif self.front==self.k-1:
            self.front=0
        else:
            self.front=self.front+1
    def rearde(self):
        if (self.front==-1 and self.rear==-1):
            print("EMPTY")
        elif self.front==self.rear:
            self.front=self.rear=-1
        elif self.rear==0:
            self.rear=self.k-1
        else:
            self.rear=self.rear-1
    def display(self):
        i=self.front
        if (self.front==-1 and self.rear==-1):
            print("queue is empty")
        else:
            while (i!=self.rear):
                print(self.q[i])
                i=(i+1)%self.k
            print(self.q[self.rear])
obj=dq(5)
obj.fronten(1)
obj.fronten(2)
obj.fronten(3)
obj.display()



        
        

    
