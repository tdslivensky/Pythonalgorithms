e = '(){}[({})]' #true
f = '(({[{}]}))' #true
g = '({})[{[]}' #false

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def balanceCheck(s):
    
    if len(s)%2 != 0:
        return False
    
    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    
    stack = Stack()
    
    for p in s:
        if p in opening:
            stack.push(p)
        else:
            if stack.size() == 0:
                return False
            lastOpen = stack.pop() 
            
            if (lastOpen,p) not in matches:
                return False
            
    
    return stack.size() == 0        