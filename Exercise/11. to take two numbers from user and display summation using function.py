#  to take two numbers from user and display summation using function:->

def sum(a,b):
    return a+b

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

result=sum(num1,num2)
print(f"The sum of {num1} and {num2} is: {result}")