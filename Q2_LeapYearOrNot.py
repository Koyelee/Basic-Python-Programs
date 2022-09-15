# Check a Year is Leap year or Not
year=int(input("Enter a year:"))
if year%400==0:
  print(year,"IS A LEAP YEAR")
elif year%100==0:
  print(year,"IS NOT A LEAP YEAR")
elif year%4==0:
  print(year,"IS A LEAP YEAR")
else:
  print(year,"IS NOT A LEAP YEAR")