# Find the 2nd and 3rd minimum of n number of elements in a list.
numbers=[]
n=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range (n):
    numbers.append(int(input()))
print("THE LIST IS:",numbers)
secondmin=numbers[0]
firstmin=min(numbers)
# Finding Second Minimum Element
for x in numbers:
    if firstmin==secondmin and x>firstmin:
        secondmin=x
    elif x<secondmin and x>firstmin:
        secondmin=x
print("THE SECOND MINIMUM ELEMENT IS:",secondmin)
# Finding Third Minimum Element
thirdmin=secondmin
for x in numbers:
    if secondmin==thirdmin and x>thirdmin:
        thirdmin=x
    elif x<thirdmin and x>secondmin:
        thirdmin=x
print("THE THIRD MINIMUM ELEMENT IS:",thirdmin)
