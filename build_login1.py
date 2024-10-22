credentials_list = [
     ("subhajit", "1234"),
    ("ankit", "7047"),
    ("souvik", "1299")
]

# Get user input
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

# Check if the username exists and the password matches
login_successful = False
for user, pwd in credentials_list:
    if user == username and pwd == password:
        login_successful = True
        break

if login_successful:
    print("Login successful!")
else:
    print("Please try again.")
