# Factorial of a number using Recursion and without using Recursion.
def factorialUsingRecursion(number):
    if number==0 or number==1:
        return 1
    return number*factorialUsingRecursion(number-1)

def factorialWithoutRecursion(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact

number=int(input("Enter a number: "))
print("THE FACTORIAL OF THE NUMBER (USING RECURSION) IS:",factorialUsingRecursion(number))
print("THE FACTORIAL OF THE NUMBER (WITHOUT USING RECURSION) IS:",factorialWithoutRecursion(number))
