# Check a number is Krishnamurty or not.
def factorialNumber(n):
  fact=1
  for i in range (1,n+1):
    fact*=i
  return(fact)

number=int(input("Enter a number: "))
temp=number
sum=0
while temp>0:
  sum+=factorialNumber(temp%10)
  temp//=10
if number==sum:
  print(number,"IS A KRISHNAMURTY NUMBER")
else:
  print(number,"IS NOT A KRISHNAMURTY NUMBER")