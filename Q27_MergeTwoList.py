# Merge two list into one list in such a manner that new list contain 1st data from 1st list, 
# 2nd data from 2nd list, 3rd data from 1st list and so on. Note that the two lists may or may not have the
# same length.
numbers=[]
numbers1=[]
numbers2=[]
x=0
y=0
len1=int(input("Enter the size of the first list: "))
len2=int(input("Enter the size of the second list: "))
print("Enter the elements in the first list:")
for i in range(len1):
    numbers1.append(int(input()))
print("Enter the elements in the second list:")
for i in range(len2):
    numbers2.append(int(input()))
for i in range(2*min(len1,len2)):
    if i%2==0:
        data=numbers1[x]
        x+=1
    else:
        data=numbers2[y]
        y+=1
    numbers.append(data)
if x<len1-1:
    for i in range(x,len1):
        numbers.append(numbers1[i])
if y<len2-1:
    for i in range(y,len2):
        numbers.append(numbers2[i])
print("FIRST LIST:",numbers1)
print("SECOND LIST:",numbers2)
print("THE MERGED LIST:",numbers)
