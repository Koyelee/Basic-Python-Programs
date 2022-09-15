# Perform merge sort for a given set of numbers in a list without using sort function.

def merge(numbers,p,mid,q):
    left=numbers[p:mid+1]
    right=numbers[mid+1:q+1]
    i=j=0
    k=p
    while i<len(left) and j<len(right):
        if left[i]==right[j]:
            numbers[k]=left[i]
            k+=1
            numbers[k]=right[j]
            i+=1
            j+=1
        elif left[i]<right[j]:
            numbers[k]=left[i]
            i+=1
        else:
            numbers[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        numbers[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        numbers[k]=right[j]
        j+=1
        k+=1

def mergeSort(numbers,p,q):
    if p<q:
        mid=(p+q)//2
        mergeSort(numbers,p,mid)
        mergeSort(numbers,mid+1,q)
        merge(numbers,p,mid,q)
  
numbers=[]
limit=int(input("Enter the total number of elements:"))
print("Enter the elements:")
for i in range(limit):
    numbers.append(int(input()))
print("THE UNSORTED LIST IS: ",numbers)       
mergeSort(numbers,0,limit-1)
print("THE SORTED LIST IN ASCENDING ORDER IS: ",numbers)
