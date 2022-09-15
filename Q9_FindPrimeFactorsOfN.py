# Find prime factors of a number.
def checkPrime(n):
  count=0
  for i in range(1,n+1):
    if n%i==0:
      count+=1
  if count==2:
    return 1
  else:
    return 0


number=int(input("Enter a number: "))
print("THE PRIME FACTORS OF",number,"ARE: ")
for i in range (1,number+1):
  if number%i==0:
    check_result=checkPrime(i)
    if check_result==1:
      print(i)