# Check a number is Prime or not.
count=0
number=int(input("Enter a number:"))
for i in range(1,number+1):
    if(number%i==0):
        count+=1
if count==2 :
    print(number,"IS A PRIME NUMBER")
else:
    print(number,"IS NOT A PRIME NUMBER")
