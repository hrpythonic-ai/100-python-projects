#program to print all prime numbers in an interval
#for example you want to print from 2 to 50 
#then 2 is your lower limit and 50 is your upper limit
lower=int(input("Enter the number from where you want to start:"))
upper=int(input("Enter the number from where you want to end:"))
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
