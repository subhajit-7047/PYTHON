"""class range(
    start: SupportsIndex,
    stop: SupportsIndex,
    step: SupportsIndex = ...,
    /
)"""
# Example: Print odd numbers from 0 to 10
for i in range(1, 10, 2):
    print(i)
# Output: 1 3 5 7 9

# Example: Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10
#--------------------------
list1=list(range(1,10))
print(list1)
# Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

list2=list(range(10,0,-1))
print(list2)
## Output:[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#----------------------------