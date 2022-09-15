# Perform selection sort for a given set of numbers in a list without using sort function.

numbers=[]
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range(limit):
    numbers.append(int(input()))
print("THE UNSORTED LIST IS: ",numbers)
for i in range(limit-1):
    m=0
    for j in range(limit-i):
        if numbers[j]>numbers[m]:
            m=j
    if numbers[m]!=numbers[j]:
        temp=numbers[j]
        numbers[j]=numbers[m]
        numbers[m]=temp
print("THE SORTED LIST IN ASCENDING ORDER IS: ",numbers)
