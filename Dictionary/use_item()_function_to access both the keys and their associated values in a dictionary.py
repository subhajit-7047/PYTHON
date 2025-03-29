"""We use .items() when we need to access both the keys and their associated values in a dictionary. Without .items(), a dictionary loop only iterates over the keys by default. Here's a comparison:
"""
# Without .items():
words = {"apple": "fruit", "carrot": "vegetable"}

for key in words:
    print(key)  # Only the keys are accessible

# Output:
# apple 
# carrot   """"" Only the keys are accessible"""""

#-------------------------------------

# With .items():

words = {"apple": "fruit", "carrot": "vegetable"}

for key, value in words.items():
    print(f"{key} is a {value}")

# Output:
# apple is a fruit
# carrot is a vegetable
#-------------------------------------