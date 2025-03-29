# basic-data-type======>>
#primitive data type:
#integer-->.
print(4)

#up to range-->> 1e308== That means 10^308 maximum value range
print(1e308)
#output
#1e+308

## when 1e309=10^309 it infinitive 
print(1e309)
#output
#inf



#float--> 
print(1.4)
#Range-->>
print(1.7e308)
#output
#1.7e+308
print(1.7e309)
#inf

#boolean-->>. 
print(True)
print(False)

#COMPLEX-->
print(4+5j)
a=complex(2,3)
print(a)
#(2+3j)

#string----->>>
print('kolkata')
print("kolkata")
print("""kolkata""")

# container-data-type======>>

#list ===>> create square bracket:

print(["subhajit","Rahul","suman"])
print([1,2,3,4,5])
list=[3,4.5,[-4,5],["apple","ball"]]
print(list)
#[3, 4.5, [-4, 5], ['apple', 'ball']]

#Tuple ===>> create small bracket:
print((1,2,3,4))

#sets =====>> create curly bracket:

print({1,2,3,4,4})

#Dictionary =====>> create  key value pair:
print({"name":"subhajit", "Age":19, "Gender":"male"})


##==============================>
# What is a variable?
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

# a = 1
# b = True
# c = "Harry"
# d = None
# These are four variables of different data types.

# What is a Data Type?
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

# a = 1
# print(type(a))
# b = "1"
# print(type(b))
# By default, python provides the following built-in data types:

# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i
# 2. Text data: str
# str: "Hello World!!!", "Python Programming"

# 3. Boolean data:
# Boolean data consists of values True or False.

# 4. Sequenced data: list, tuple
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

# Example:

# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)
# Output:

# [8, 2.3, [-4, 5], ['apple', 'banana']]
# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

# Example:

# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# print(tuple1)
# Output:

# (('parrot', 'sparrow'), ('Lion', 'Tiger'))
# 5. Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

# Example:

# dict1 = {"name":"Sakshi", "age":20, "canVote":True}
# print(dict1)
# Output:

# {'name': 'Sakshi', 'age': 20, 'canVote': True}