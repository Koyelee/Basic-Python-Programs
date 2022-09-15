# Count the frequency of each element in list wihout using count function.

numbers=[]
print("ENTER THE NUMBERS IN THE LIST. TYPE done OR DONE TO STOP INSERTING.")
ch='Not Done'
while ch!='done':
    data=input()
    if data=='done' or data=='DONE':
        ch='done'
    elif data.isnumeric()==True :
        numbers.append(int(data))
    else:
        print("Improper Input....!!")
numbers2=numbers.copy()
# Removing duplicate elements from the list
print("THE ORIGINAL LIST IS: ",numbers)
for x in numbers:
    j=0
    while j<len(numbers):
        if numbers.index(x)!=j and x==numbers[j]:
            numbers.pop(j)
            j-=1
        j+=1
print("FREQUENCY:")
for x in numbers:
    count=0
    for y in numbers2:
        if x==y:
            count+=1
    print("FREQUENCY OF",x,"IS",count)
