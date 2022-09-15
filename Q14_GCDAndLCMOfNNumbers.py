# GCD and LCM of n numbers
def GCD(x,y):
    while x!=y:
      if x>y:
        x-=y
      else:
        y-=x
    return x

numbers=[]
n=int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(n):
  numbers.append(int(input()))
num=numbers.copy()
for i in range(1,n):
    numbers[i-1]=numbers[i]=GCD(numbers[i-1],numbers[i])
print("THE GCD OF THE GIVEN NUMBERS:",numbers[-1])
lcm=num[0]
for i in range(1,n):
  lcm=(lcm*num[i])//GCD(lcm,num[i])
print("THE LCM OF THE GIVEN NUMBERS:",lcm)