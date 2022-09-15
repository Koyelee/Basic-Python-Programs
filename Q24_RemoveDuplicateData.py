# Remove the duplicate data from the list and print the list.

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
print("THE ORIGINAL LIST IS: ",numbers)
for x in numbers:
    if numbers.count(x)>1:
        j=0
        while j<len(numbers):
            if numbers.index(x)!=j and x==numbers[j]:
                numbers.pop(j)
                j-=1
            j+=1
print("THE LIST AFTER REMOVING DUPLICATE ELEMENT IS: ",numbers)
