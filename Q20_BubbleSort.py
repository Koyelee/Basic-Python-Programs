# Perform bubble sort for a given set of numbers in a list without using sort function.

numbers=[]
flag=0
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range(limit):
    numbers.append(int(input()))
print("THE UNSORTED LIST IS: ",numbers)
for i in range(limit-1):
    flag=0
    for j in range(limit-i-1):
       if numbers[j]>numbers[j+1]:
            temp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=temp
            flag=1
    if flag==0:
        break
print("THE SORTED LIST IN ASCENDING ORDER IS: ",numbers)