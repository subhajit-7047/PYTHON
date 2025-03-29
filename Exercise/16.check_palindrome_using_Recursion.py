def pal(text):
    if len(text) == 1:
        print("palindrome")
    else:
        if text[0] == text[-1]:
            pal(text[1:-1])
        else:
            print("not palindrome")

# Correct function call
User_input = input("Enter a string: ")#madam
pal(User_input)

# Output: palindrome
# Explanation:
# The function checks if the first and last characters are the same. If they are, it calls itself with the substring that excludes these two characters. This continues until the string is reduced to one character or becomes empty.

