# Implement queue opeartion (enqueue,dequeue,display) using list and function.
# ENQUEUE OPERATION
def enqueue(queue,size,rear):
    if len(queue)==0:
        rear=-1
    if rear==size-1:
        print("QUEUE OVERFLOW...!!")
    else:
        data=int(input("Enter the data: "))
        queue.append(data)
        rear+=1
    print("len:",len(queue))
    return rear

# DEQUEUE OPERATION
def dequeue(queue):
    if len(queue)==0:
        print("EMPTY QUEUE...!!")
    else:
        print("THE DELETED ELEMENT IS:",queue.pop(0))

# DISPLAY
def display(queue):
    if len(queue)==0:
        print("EMPTY QUEUE...!!")
    else:
        print("THE CONTENTS OF THE QUEUE IS:\n")
        for x in queue:
            print(x,end=' ')

queue=[]
size=int(input("Enter the size of the queue: "))
rear=-1
while True:
    print("\n---------------------------------------------------------------\n** Menu **\n1) ENQUEUE\n2) DEQUEUE\n3) DISPLAY\n4) EXIT")
    choice=int(input("Enter the choice: "))
    if choice==1:
        rear=enqueue(queue,size,rear)
    elif choice==2:
        dequeue(queue)
    elif choice==3:
        display(queue)
    elif choice==4:
        exit(0)
    else:
        print("WRONG CHOICE....!!")
 