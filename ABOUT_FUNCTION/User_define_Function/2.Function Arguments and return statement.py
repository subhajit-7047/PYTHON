###Function Arguments and return statement:->

"""There are four types of arguments that we can provide in a function:

1.Default Arguments
2.Keyword Arguments
3.Variable length Arguments
4.Required Arguments
"""

"""
1.Default arguments:->
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument."""

#1.Example:

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")
# Output:
# Hello, Amy Jhon Whatson (by default fname=Amy)

#2.Example:
def average(a=5,b=1):
    print("The average is",(a+b)/2)
average(2)
#The average is 1.5

#3.Example:
def average(a=5,b=1):
    print("The average is",(a+b)/2)
average(2)
average(b=5)
average(10,20)
#output:
# The average is 1.5 (by defauit it change the value a)
# The average is 5.0(by defauit it change the value b)
# The average is 15.0(by defauit it change the value both)


#--------------------------------------
"""
2.Keyword arguments:->
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter."""

#1.Example:

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")
# Output:
# Hello, Jade Peter Wesker

##2.Example:
def average(a=5,b=1):
    print("The average is",(a+b)/2)
average(b=4, a=4)
#The average is 4.0
#---------------------
"""
3.Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition."""

# Example 1: when number of arguments passed does not match to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Quill")
# Output:
# name("Peter", "Quill")\
# TypeError: name() missing 1 required positional argument: 'lname'

# Example 2: when number of arguments passed matches to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")
# Output:
# Hello, Peter Ego Quill

def average(a,b=2):
    print("The average is",(a+b)/2)
average(a=9)
#The average is 3.0
#---------------------------------
"""
4.Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments."""

# There are two ways to achieve this:

"""(4.i).Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple."""

# Example:

def sum(*r): #as tuple when one *
    sum=0
    for i in r:
        sum=sum+i
    print(sum)
sum(6,8)
#----------

def name(*name): #tuple format means for one *
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")
# Output:
# Hello, James Buchanan Barnes

"""
(4.(ii))Keyword Arbitrary Arguments:
While creating a function, pass a ** before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary."""

# Example:

def name(**name): #dictionary format means for two ** {key}: {value}
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")
# Output:
# Hello, James Buchanan Barnes
#-----------------------
"""
return Statement->
The return statement is used to return the value of the expression back to the calling function."""

#1.Example:

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))
# Output:
# Hello, James Buchanan Barnes

#2.Example:

def average(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum/len(num)

c=average(5,6,7,1)
print(c)

#4.75



#Example:3
def average(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum / len(num)

# Prompt the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, user_input.split()))

# Call the average function with the user's numbers
c = average(*numbers)
print("The average is:", c)


"""Explanation:
input() function: This takes a string of numbers entered by the user.

split() method: Splits the input string into a list of strings (based on spaces).

map(int, ...): Converts the list of strings into a list of integers.

*numbers: Unpacks the list of integers to pass as arguments to the average function.


    """

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)
# Output: Square: 9
#---------------------------------------------------------------