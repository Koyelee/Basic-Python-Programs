# Check a number is Perfect or not.
number=int(input("Enter a number:"))
temp=number
new_number=0
for i in range (1,number):
    if number%i==0:
        new_number=new_number+i
if temp==new_number:
    print(temp,"IS A PERFECT NUMBER")
else:
    print(temp,"IS NOT A PERFECT NUMBER")
