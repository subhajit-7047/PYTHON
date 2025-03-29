"""Both for and while loops are used to execute a block of code repeatedly in Python, but they have different use cases and are suited to different situations:"""

"""
for Loop:-->
The for loop is used when you know in advance how many times you want to execute a statement or a block of statements. It is commonly used to iterate over a sequence (such as a list, tuple, or string) or any other iterable object.
"""
#Use cases for loop:=>

"""
Iterating over a list, tuple, string, or other iterable objects:
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#Iterating over a range of numbers:

for i in range(5):
    print(i)
# Iterating over dictionary items:


person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
#------------------------------------------------->    
"""
while Loop:
The while loop is used when you want to repeat a statement or a block of statements as long as a condition is true. It is more flexible than the for loop since it is not limited to iterating over a sequence or a range.
"""
# Use cases for while loop:

#Repeating a block of code while a condition is true:

count = 0
while count < 5:
    print(count)
    count += 1


# Creating an infinite loop (use with caution):

while True:
    # do something
    pass  # or break to exit the loop

#Using a loop for user input or other conditions:

user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to quit: ")

#--------------------------------------------------->

"""
Choosing Between for and while Loops
Use a for loop when you need to iterate over a specific sequence or range of values.

Use a while loop when the number of iterations is not known in advance and depends on a condition being true.

Example with Both Loops:
Here’s an example where both for and while loops could be used:
"""
# Using for loop:


for i in range(5):
    print(i)


#Using while loop:


i = 0
while i < 5:
    print(i)
    i += 1

"""
Both loops will produce the same output, but the choice of which loop to use depends on the specific context and requirements of your program.
"""