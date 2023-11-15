stack=[]

def checkEmpty(stack):
    return len(stack)==0

def addItem(stack,item):
    stack.append(item)
    print(stack)

def removeItem(stack):
    if checkEmpty(stack)==False:
        stack.pop()
    
    print(stack)

addItem(stack,1)
addItem(stack,100)
addItem(stack,55)

removeItem(stack)
removeItem(stack)
removeItem(stack)