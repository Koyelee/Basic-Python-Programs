# Find the maximum, minimum between three numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
# Maximum Number
if num1>num2 and num1>num3 :
    max=num1
elif num2>num1 and num2>num3:
    max=num2
else:
    max=num3
print("THE MAXIMUM NUMBER BETWEEN",num1,",",num2,"AND",num3,"IS:",max)
#Minimum Number
if num1<num2 and num1<num3:
    min=num1
elif num2<num1 and num2<num3:
    min=num2
else:
    min=num3
print("THE MINIMUM NUMBER BETWEEN",num1,",",num2,"AND",num3,"IS:",min)