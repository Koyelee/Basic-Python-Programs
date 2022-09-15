# Implement circular queue opeartion (enqueue,dequeue,display) using list and function.
front=-1
rear=-1

# ENQUEUE OPERATION
def enqueue(cqueue,size):
    global rear,front
    if (rear+1)%size==front:
        print("QUEUE OVERFLOW...!!")
    else:
        data=int(input("Enter the data: "))
        if rear==front==-1:
            front=0
        rear=(rear+1)%size
        cqueue[rear]=data

# DEQUEUE OPERATION
def dequeue(cqueue):
    global rear,front
    if rear==front==-1:
        print("EMPTY QUEUE...!!")
    else:
        print("THE DELETED ELEMENT IS:",cqueue[front])
        if front==rear:
            front=rear=-1
        else:
            front=(front+1)%size

# DISPLAY
def display(cqueue,size):
    if rear==front==-1:
        print("EMPTY QUEUE...!!")
    else:
        print("THE CONTENTS OF THE QUEUE IS:\n")
        i=front
        while i!=rear:
            print(cqueue[i],end=' ')
            i=(i+1)%size
        print(cqueue[i],end=' ')

size=int(input("Enter the size of the queue: "))
cqueue=[0]*size
while True:
    print("\n---------------------------------------------------------------\n** Menu **\n1) ENQUEUE\n2) DEQUEUE\n3) DISPLAY\n4) EXIT")
    choice=int(input("Enter the choice: "))
    if choice==1:
        enqueue(cqueue,size)
    elif choice==2:
        dequeue(cqueue)
    elif choice==3:
        display(cqueue,size)
    elif choice==4:
        exit(0)
    else:
        print("WRONG CHOICE....!!")
