credentials_list = [("subhajit", "1234"), ("ankit", "7047"), ("souvik", "1299")]

# Get user input
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

#message = ""
for user, pwd in credentials_list:
    if user == username and pwd == password:
        message = "Login successful!"
        break

    else:
        message = "Login failed!"
        

print(message)