#Program to Check a year is a leap_year or not
year=int(input("Enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
  print(year,"is a leap year.")
else:
  print(year,"is not a leap year.")

#2nd method 
year=int(input("Enter year: "))
if (year%4==0 and year%100!=0) 
  print(year,"is a leap year.")
elif(year%400==0):
  print(year,"is a leap year.")    
else:
  print(year,"is not a leap year.")
