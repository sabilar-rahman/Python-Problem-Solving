#stack implement

# create stack

def  create_stack():
    stack = []
    return stack

# create an empty stack
def empty_stack(stack):
    return len(stack) == 0

#Adding an element to the stack
def push(stack,item):
    stack.append(item)
    print("push Item:"+ item)

#Removing an element from the stack

def pop(stack):
    if(empty_stack(stack)):
        return "stack is empty"
    
    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))

print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))