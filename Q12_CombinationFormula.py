# Find NcR where n,c and r are given as input.
def factorialNumber(n):
  fact=1
  for i in range (1,n+1):
    fact*=i
  return(fact)


n=int(input("Enter the value of n:"))
while True:
  r=int(input("Enter the value of r:"))
  if (r>=0 and r<=n):
    break
  print("Enter a valid value for r.......")
print("THE RESULT IS:",factorialNumber(n)//(factorialNumber(n-r)*factorialNumber(r)))