# Find the prime number within a range 1 to n.
def checkPrime(limit):
  count=0
  for i in range(1,limit+1):
    if limit%i==0:
      count+=1
  if count==2:
    return 1
  else:
    return 0

n=int(input("Enter the limit: "))
print("THE PRIME NUMBERS BETWEEN 1 AND",n,"IS")
for i in range (1,n+1):
  if checkPrime(i)==1:
      print(i)