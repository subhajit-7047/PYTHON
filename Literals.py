#Python Literals:
#----------------------
#Variable  কে জে মান(value) তা দিই সেটা কে আক্ষরিক(literals) বলে.
#Literals is a raw data given in variable.
#Literals are representations of fixed values in a program. They can be numbers, characters, or strings, etc. For example, 'Hello, World!', 12, 23.0, 'C', etc.

#Literals are often used to assign values to variables or constants. For example,
#site_name = 'programiz.com'
#--------------------------------------
#Types

#1.Numeric Literals
#2.String Literals
#3. Boolean Literals
#4.Special Literal 
#5.Collection Literals

#---------------------------------------------
#1.Numeric Literals(prrimitive data type)-->

#(i) Integer Literals
a = 0b1010  # Binary
b = 100     # Decimal
c = 0o310   # Octal
d = 0x12c   # Hex
print(a, b, c, d)
#output
#10 100 200 300
var_1=5
print(type(var_1))


# (ii)Float Literals
f1 = 10.5
f2 = 1.5e2 #1.5*10^2
f3 = 1.5e-3  #1.5*10^-3
print(f1, f2, f3)
#output
#10.5 150.0 0.0015

#(iii) Complex Literal
x = 3.14j
print(x, x.imag, x.real)
#output
#3.14j 3.14 0.0

#----------------------------
#2.String literals
string = 'This is Python'
strings = "This is Python"
char = "C"

print(string)
print(strings)
print(char)
#output
#This is Python
#This is Python
#c
  

#when multiple string value(literals)
multiline_str = """This is a multiline string with more than one line code."""
print(multiline_str)
#output
#This is a multiline string with more than one line code.

#Emoji(This is reperesnt uni code)--->>
unicode = u"\U0001f600\U0001F606\U0001F923"  #only u apply in frist in code,
print(unicode)
#output
#😀😆🤣


#raw _string
#In Python, a raw string is a string where backslashes (\) are treated as literal characters, rather than as escape characters. Normally, in regular strings, backslashes are used to introduce special character sequences like \n (newline), \t (tab), etc. 
#example:
normal_string = "Hello\nWorld"
raw_string = r"Hello\nWorld"

print(normal_string)  # Output: Hello (newline) World
print(raw_string)     # Output: Hello\nWorld

#As it is same 
file_path = r"C:\Users\TLU\Documents"
print(file_path)  # Output: C:\Users\TLU\Documents
#-----------------------------------------------

# 3. Boolean literals
#true = 1
#false=0

a = True + 4   # True == 1
b = False + 10 # False == 0

print("a:", a)  # Output: a: 5
print("b:", b)  # Output: b: 10

#-----------------------------------------------

#4. Special literals

a = None
print(a) # Output:None

# Variable Declaration
k = None