# break statement:-> exits the loop entirely.
for i in range(1,11):
    if i==5:
        break
    print(i)
#ouput:
"""
1
2
3
4
"""
for i in range(12):
     if i==10:
        break
     print("5 *", i+1,"=", 5*(i+1))
    
print("Exit the loop.")

#output
"""
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
Exit the loop.
"""

#---------------

#continue statement:-> skips the current iteration and proceeds to the next one.

for i in range(1,11):
    if i==5:
        continue
    print(i)
#ouput:
"""
1
2
3
4 
6
7
8
9
10
"""
#----------------------
#pass statement:->
"""
In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.

Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. In such cases, we can use the pass statement.
"""

for i in range(5):
    pass

#-----------------------
