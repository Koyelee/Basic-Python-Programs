# Find GCD and LCM of two numbers.
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
multiplication=number1*number2
while number1!=number2:
    if number1>number2:
        number1-=number2
    else:
        number2-=number1
print("THE GCD OF THE TWO GIVEN NUMBERS IS:",number1)
print("THE LCM OF THE TWO GIVEN NUMBERS IS:",multiplication//number1)
