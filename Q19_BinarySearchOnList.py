# Perform binary search for a given set of numbers in a list.

def binarySearch(numbers,key,low,high):
    if low>high:
        return -1
    else:
        mid=(low+high)//2
        if key==numbers[mid]:
            return 1
        elif key>numbers[mid]:
            return binarySearch(numbers,key,mid+1,high)
        else:
            return binarySearch(numbers,key,low,mid-1)

numbers=[]
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range (limit):
    numbers.append(int(input()))
numbers2=numbers.copy()
numbers2.sort()
key=int(input("Enter the element to be searched: "))
print("THE LIST IS: ",numbers)
if binarySearch(numbers,key,0,len(numbers)-1)!=-1:
    print(key,"IS PRESENT AT POSITION",numbers.index(key))
else:
    print(key,"IS NOT PRESENT")
