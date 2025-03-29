#lower()
name='SuBhajiT'
print(name.lower())#subhajit
#-----------------
#upper()
name="subhajit"
print(name.upper())#SUBHAJIT
#-----------------
#count()
name='subhajiisubhajit'
print(name.count('s')) #2
#------------------
#split()
name=input("Enter name:")
L=name.split(' ')# in bracket always give a space between comma like this ->(" ") and (' ')
print(L)
#output
#['subhajit', 'asha', 'swadesh']

# The split() method splits the given string at the specified instance and returns the separated strings as list items.

# Example:
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
# Output:
# ['Silver', 'Spoon']

text="welcome to my profile"
splited_text=text.split('o') #split this are where will be  'o'
print(splited_text)
#output
#['welc', 'me t', ' my pr', 'file']
#------------------
#rstrip()

a="subhajit!!!!!!!!!"
print(a)#subhajit!!!!!!!!!
print(a.rstrip("!"))#subhajit
b="!!subha"
print(b.rstrip('!')) #!!subha

#---------------------
#replace() #The replace() method replaces all occurences of a string with another string. Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

# Output:
#Silver Moon
a="subhajit"
print(a.replace("subhajit","swadesh"))
#swadesh
#---------------------
#capitalize() :
"""The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase."""

# Example:
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
# Output:
# Hello
# Hello world

college_name= "jIS College OF EnGineering"
print(college_name.capitalize())
# Jis college of engineering(only first is letter is capital)
#-----------------------
# center() :
# The center() method aligns the string to the center as per the parameters given by the user.

# Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50))
#            Welcome to the Console!!!
print(len(str1)) #25
print(len(str1.center(50)))#50
#-------------------------------
# endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

# Example :
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
# Output:
# True

# We can even also check for a value in-between the string by providing start and end index positions.


str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) #True
#---------------------------
# find() :
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.


str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
#10 (Return index)


# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.


str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))#because this text is not here
# Output:
# -1
#-------------------------
# index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.


str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# Output:
# 13

# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.


str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
# Output:
# ValueError: substring not found
#------------------------------
# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

# Example 1:
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# Output:
# True

# isalpha() :->

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.


str1 = "Welcome"
print(str1.isalpha())
# Output:
# True
#-------------------------------
# islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.

# Example:
str1 = "hello world"
print(str1.islower())
# Output:
# True
#-----------------------------
# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

# Example :
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
# Output:
# True

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
# Output:
# False (Because \n is not printable)
#------------------------
# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# Example:
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
# Output:
# True
# True

#-------------------------
# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# Example:
str1 = "World Health Organization" 
print(str1.istitle())
# Output:
# True
# Example:
str2 = "To kill a Mocking bird"
print(str2.istitle())
# Output:
# False
#-----------------------------
# isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.

# Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
# Output:
# True
#--------------------------
# startswith() :
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

# Example :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
# Output:
# True
#--------------------------
# swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

# Example:
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
# Output:
# pYTHON IS A iNTERPRETED lANGUAGE
#------------------------------
# title() :
# The title() method capitalizes each  letter of the word within the string.

# Example:
str1 ="He's name is Dan. Dan is an honest man."
print(str1.title())
# Output:
# He'S Name Is Dan.dan Is An Honest Man
#<|=======================================|>