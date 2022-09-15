# Split the data of a list into two list where one list contain odd number and another list contain even number
numbers=[]
oddNumbers=[]
evenNumbers=[]
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range (limit):
    n=int(input())
    numbers.append(n)
    if n%2==1:
        oddNumbers.append(n)
    else:
        evenNumbers.append(n)
print("THE ORIGINAL LIST IS:",numbers)
print("THE LIST CONTAINING ODD NUMBERS IS:",oddNumbers)
print("THE LIST CONTAINING EVEN NUMBERS IS:",evenNumbers)

