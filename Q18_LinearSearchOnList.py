# Perform linear search for a given set of numbers in a list.

numbers=[]
flag=0
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range (limit):
    numbers.append(int(input()))
key=int(input("Enter the element to be searched: "))
print("THE LIST IS: ",numbers)
for x in numbers:
    if x==key:
        flag=1
        break
if flag==1:
    print(key,"IS PRESENT AT POSITION",numbers.index(key))
else:
    print(key,"IS NOT PRESENT")

# SHORTCUT
#-------------------------
# if key in numbers:
#     print(key,"IS PRESENT AT POSITION",numbers.index(key))
# else:
#     print(key,"IS NOT PRESENT")