#Program to Convert Temprature
temp=float(input("Enter the temprature: "))
num=int(input("Enter the number: 1-Celsius to Fahrenheit \n 2-Celsius to kelvin \n 3-Fahrenheit to Celsius \n 4-Fahrenheit to kelvin \n 5-kelvin to Celsius \n 6-kelvin to Fahrenheit "))
if num==1:
  F = (temp * 9/5) + 32
  print(temp,"Celsius is:",F,"Fahrenheit")
elif num==2:
  K = temp + 273.15
  print(temp,"Celcius is:",K,"Kelvin")
elif num==3:
  C = (temp - 32) * 5/9
  print(temp,"Fahrenheit is:",C,"Celsius")
elif num==4:
  K = (temp - 32) * 5/9 + 273.15
  print(temp,"Fahrenheit is:",K,"Kelvin")
elif num==5:
  C = temp - 273.15
  print(temp,"Kelvin is:",C,"Celsius")
elif num==6:
  F = (temp - 273.15) * 9/5 + 32
  print(temp,"Kelvin is:",F,"Fahrenheit")
else:
  print("this is invalid input")
  
  
