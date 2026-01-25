#Program to Solve Quadratic Equation
#ax**2+b*x+c=0
import cmath
a=int(input("Enter number(a!=0): "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))
d=(b**2)-(4*a*c)  #d means discriminant formula
root1=(-b-cmath.sqrt(d))/(2*a)
print(root1)
root2=(-b+cmath.sqrt(d))/(2*a)
print(root2)
