# Check a number is Palindrome or not.
number=int(input("Enter a number:"))
temp=number
reversed_number=0
while number>0 :
    reversed_number=reversed_number*10+number%10
    number=number//10
if temp==reversed_number:
    print(temp,"IS A PALINDROME NUMBER")
else:
    print(temp,"IS A NOT A PALINDROME NUMBER")

