# Find the 2nd and 3rd maximum of n number of elements in a list.
numbers=[]
n=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range (n):
    numbers.append(int(input()))
print("THE LIST IS:",numbers)
secondmax=numbers[0]
firstmax=max(numbers)
# Finding Second Maximum Element
for x in numbers:
    if firstmax==secondmax and x<firstmax:
        secondmax=x
    elif x>secondmax and x<firstmax:
        secondmax=x
print("THE SECOND MAXIMUM ELEMENT IS:",secondmax)
thirdmax=secondmax
# Finding Third Maximum Element
for x in numbers:
    if secondmax==thirdmax and x<thirdmax:
        thirdmax=x
    elif x>thirdmax and x<secondmax:
        thirdmax=x
print("THE THIRD MAXIMUM ELEMENT IS:",thirdmax)
