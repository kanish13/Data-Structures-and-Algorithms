queue=[]

def size(queu):
    return len(queu)

def push(queu,n):
    queu.append(n)

def pop(queu):
    if size(queu)<1:
        return None
    queu.pop(0)

def display(queu):
    print(queu)

display(queue)

push(queue,1)
push(queue,2)
push(queue,3)
push(queue,4)
display(queue)
pop(queue)
pop(queue)
display(queue)
