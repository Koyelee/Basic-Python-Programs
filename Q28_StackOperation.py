# Implement stack opeartion (push,pop,display) using list and function.
# PUSH OPERATION
def push(stack,size):
    if len(stack)==size:
        print("STACK OVERFLOW...!!")
    else:
        data=int(input("Enter the data: "))
        stack.append(data)

# POP OPERATION
def pop(stack):
    if len(stack)==0:
        print("EMPTY STACK...!!")
    else:
        print("THE DELETED ELEMENT IS:",stack.pop())

# DISPLAY
def display(stack):
    if len(stack)==0:
        print("EMPTY STACK...!!")
    else:
        print("THE CONTENTS OF THE STACK IS:\n")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])

stack=[]
size=int(input("Enter the size of the stack: "))
while True:
    print("\n---------------------------------------------------------------\n** Menu **\n1) PUSH\n2) POP\n3) DISPLAY\n4) EXIT")
    choice=int(input("Enter the choice: "))
    if choice==1:
        push(stack,size)
    elif choice==2:
        pop(stack)
    elif choice==3:
        display(stack)
    elif choice==4:
        exit(0)
    else:
        print("WRONG CHOICE....!!")
 