def check_palindrome(string):
    left = 0
    right = len(string) - 1
    
    # Loop until the two pointers meet
    while left < right:
        if string[left] != string[right]:
            return False  # Mismatch found, not a palindrome
        else:
            left += 1
            right -= 1
    
    return True  # If loop completes, it's a palindrome

# Taking input from the user
user_input = input("Enter a string: ")  # Example: madam

# Checking whether the input is a palindrome
if check_palindrome(user_input):
    print("Palindrome")
else:
    print("Not a palindrome")

