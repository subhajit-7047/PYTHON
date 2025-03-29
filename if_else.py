#1.code using if
height=int(input("Enter yout height:"))

if height>3:
    print("buy token.")
    print("Now you can board the metro")
print("Bye")
#output -->
#Enter yout height:4
#buy token.
#Now you can board the metro
#Bye

#-----------------------------------------------

#2.code using if else:
height=int(input("Enter yout height:"))

if height>3:
    print("buy token.")
    print("Now you can board the metro")
else:
    print("No require token.")


#----------------------------------------------------
#3.code using if-elseif-else:

height=int(input("Enter your height:"))

if height>=3:
    print("can ride")
    age=int(input("enter your age:"))
    if age<=12:
        print("you pay 150 rs.")
    elif age<=18:
        print("you pay 200 rs.")
    else:
        print("you pay 500 rs.")
else:
    print("cannot ride.")
print("ok ")

#------------------------------------------------------------

#4.
##login system-->>


email=input("Enetr your email:")
password=input('Enter your pass:')

if email=="subha@gmail.com" and password=="1234":
    print("welcome.")
elif email!='subha@gmail.com' and password=="1234":
    print("your email is incorrect.")
    email=input("enter your email:")
    if email=="subha@gmail.com":
        print("email is correct and welcome")
    else:
        print("still incorrect your email:")
elif email=="subha@gmail.com" and password!="1234":
        print("your password incorrect;")
        password=input("enter your new password:")
        if password=="1234":
            print("password is correct and welcome")
        else:
            print("still wrong your password:")
else:
    print("password and email is incorrect.")
    

#----------------------------------


