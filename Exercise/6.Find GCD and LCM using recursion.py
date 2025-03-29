# Finding GCD using recursion:
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))

# # Finding GCD using math module:
# import math

# # Finding the GCD of two numbers using math.gcd()
# num1 = 48
# num2 = 18

# gcd_result = math.gcd(num1, num2)

# print(f"The GCD of {num1} and {num2} is {gcd_result}")

#----------------------------------------------


# Finding LCM using recursion:


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage with user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))

