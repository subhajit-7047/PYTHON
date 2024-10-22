credentials_list = [
    ("subhajit", "1234"),
    ("ankit", "7047"),
    ("souvik", "1299")
]


# Get user input
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
#wrong code
# Check if the username exists and the password matches
# if username in credentials_list and credentials_list[username] == password:
#     print("Login successful!")
# else:
#     print("Please try again.")
#print(username in credentials_list)
#print(credentials_list[username])


print(username in credentials_list[0])