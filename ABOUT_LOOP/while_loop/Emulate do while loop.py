# Do-While loop in python

"""do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:"""

# Example
while True:  #infinite loop
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
# Output:->
"""
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1"""

# Explanation
"""This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path."""

#-----------------------------

i=int(input("Enter the number:")) #do means some content run fast in do{content} then execute while  loop.
print(i)

while i<20:
  i=int(input("Enter the number:"))
  print(i)
print("Done with the loop.")
#--------------------------------
i=0
while True:
	print(i)
	i=i+1
	if(i%5==0):   
	   break
   
#output:
"""
0
1
2
3
4
"""
#----------------------------------