# Create a calculator using switch function such that for 1 is pressed for Addition, 2 is pressed for Subtraction, 3 is pressed for multiplication and 4 for division.
def switch(ch,a,b):
    return{
        1: a+b,
        2: a-b,
        3: a*b,
        4: a/b
    } .get(ch,"Wrong Choice!")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("1) Add\n2) Subtraction\n3) Multiplication\n4) Division")
ch=int(input("Enter the choice: "))
result=switch(ch,a,b)
print("THE RESULT IS: ",result)
