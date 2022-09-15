# Perform insertion sort for a given set of numbers in a list without using sort function.

numbers=[]
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range(limit):
    numbers.append(int(input()))
print("THE UNSORTED LIST IS: ",numbers)       
for i in range(1,limit):
    j=i
    c=0
    temp=numbers[j]
    while temp<numbers[j-1] and j>0:
        c=1
        numbers[j]=numbers[j-1]
        j-=1
    if c==1:
        numbers[j]=temp
print("THE SORTED LIST IN ASCENDING ORDER IS: ",numbers)
