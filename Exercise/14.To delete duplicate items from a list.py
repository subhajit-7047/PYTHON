L=[1,1,2,3,2,4,3,4]
unique_list=[]
for i in L:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

#---------------------
# Example list with duplicates
items = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates
unique_items = list(set(items))#The set data structure automatically removes duplicates because sets only allow unique elements.
# Convert back to list if needed

print(unique_items)  # Output might be [1, 2, 3, 4, 5] (order not preserved)

#------------------------
items = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates while preserving order
unique_items = list(dict.fromkeys(items))# The dict.fromkeys() method creates a dictionary with the items as keys, which removes duplicates, and then we convert it back to a list.
# This method preserves the order of the first occurrence of each item.
# Convert back to list if needed

print(unique_items)  # Output: [1, 2, 3, 4, 5]
