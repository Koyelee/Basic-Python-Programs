# Check a number is Armstrong or not.
number=int(input("Enter a number:"))
temp=temp2=number
count=0
sum=0
while number>0:
  count+=1
  number//=10
print(count)

while temp>0:
  sum+=pow(temp%10,count)
  temp//=10

if temp2==sum:
  print(temp2,"IS AN ARMSTRONG NUMBER")
else:
  print(temp2,"IS NOT AN ARMSTRONG NUMBER")