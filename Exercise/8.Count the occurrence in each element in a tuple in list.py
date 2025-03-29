# # Count the occurrence in each element in a tuple in list
# # Example:
# # shop_sales = [('apple', 'banana', 'apple'), ('orange', 'apple', 'banana'), ('banana', 'banana', 'orange')]

# shop_sales = [('apple', 'banana', 'apple'), ('orange', 'apple', 'banana'), ('banana', 'banana', 'orange')]

# # Dictionary to store the count of each element
# element_count = {}

# # Iterate through each tuple in the list
# for sales in shop_sales:
#     for item in sales:
#         # Update the count for each element
#         if item in element_count:
#             element_count[item] += 1
#         else:
#             element_count[item] = 1

# # Print the result
# for item, count in element_count.items():
#     print(f"{item}: {count}")


shop_sales = [('apple', 'banana', 'apple'), ('orange', 'apple', 'banana'), ('banana', 'banana', 'orange')]

# Dictionary to store the count of each element
element_count = {}

# Iterate through each tuple in the list
for sales in shop_sales:
    for item in sales:
        # Update the count for each element
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

# Print the result
for item, count in element_count.items():
    print(f"{item}: {count}")

    # ---------------------------------

shop_sales = [('apple', 'banana', 'apple'), ('orange', 'apple', 'banana'), ('banana', 'banana', 'orange')]

# List to store unique items and their counts
items = []
counts = []

# Iterate through each tuple in the list
for sales in shop_sales:
    for item in sales:
        # Check if the item is already in the items list
        if item in items:
            # Find the index of the item and increment its count
            index = items.index(item)
            counts[index] += 1
        else:
            # Add the item to the items list and initialize its count
            items.append(item)
            counts.append(1)

# Print the result
for i in range(len(items)):
    print(f"{items[i]}: {counts[i]}")
