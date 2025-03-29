"""
Else with While Loop:

We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.
"""
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('I am Inside the else.')
#ouput:
"""
5
4
3
2
1
I am Inside the else.
"""