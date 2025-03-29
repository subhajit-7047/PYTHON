#T1=(1,2,3,[4,5]) is true tuple
"""
Yes, T1 = (1, 2, 3, [4, 5]) is a tuple. However, while it is considered a tuple in Python, it is not entirely immutable. Tuples are usually immutable, meaning their elements cannot be changed after creation"""

"""
Why this tuple is not fully immutable:
The tuple itself (T1) cannot have elements added or removed.

However, the presence of the list [4, 5] inside the tuple makes part of its contents mutable. Lists are inherently mutable, so you can modify the list within the tuple."""

T1 = (1, 2, 3, [4, 5])
T1[3].append(6)  # Modifying the list inside the tuple
print(T1)

# Output: (1, 2, 3, [4, 5, 6])
# The tuple itself remains unchanged, but the list inside it has been modified.
# This demonstrates(Exhibit) that while tuples are immutable, they can contain mutable objects like lists.


#-------------------------
# #tuple inside tuple
# T2=(1,2,3,(4,5))#tuple inside tuple
# T2[3][0]#4th element of tuple inside tuple
# #output:4


#-------------------------
# tuple inside list it is not immutable thats why we cannot change the value of tuple inside list
T=[1,2,3,(4,5)]#tuple inside list
T[3][0]=10
#TypeError: 'tuple' object does not support item assignment
# T[3][0]#4th element of tuple inside list

#--------------------------