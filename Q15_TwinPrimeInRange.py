# Find twin prime in a given range
def checkPrime(n):
  count=0
  for i in range(1,n+1):
    if n%i==0:
      count+=1
  if count==2:
    return 1
  else:
    return 0

limit=int(input("Enter the limit:"))
firstprime=[]
secondprime=[]
noPrime=1
for i in range(2,limit+1):
    if i+2<=limit:
        if checkPrime(i)==1 and checkPrime(i+2)==1:
            noPrime=0
            firstprime.append(i)
            secondprime.append(i+2)
if noPrime==1:
    print("NO TWIN-PRIME NUMBERS EXIST IN THE GIVEN RANGE.")
else:
     print("THE TWIN PRIME SETS ARE:")
     for i in range(len(firstprime)):
        print("(",firstprime[i],",",secondprime[i],")")
